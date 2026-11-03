"""Build-time only: pip install pyshp shapely pyproj. No runtime dependencies.
Usage: python build.py CENSUS_ZIP VERIFIED_NATIVE_LINK_EXPORT.json
"""
import sys, json, zipfile, hashlib, html
from pathlib import Path
import shapefile
from shapely.geometry import shape, box
from shapely.ops import transform, unary_union
from pyproj import Transformer

HERE=Path(__file__).parent
archive=Path(sys.argv[1]); links=json.loads(Path(sys.argv[2]).read_text(encoding='utf-8-sig'))
z=zipfile.ZipFile(archive); stem='tl_2026_17_place'
r=shapefile.Reader(shp=z.open(stem+'.shp'),shx=z.open(stem+'.shx'),dbf=z.open(stem+'.dbf'))
project=Transformer.from_crs('EPSG:4269','EPSG:26916',always_xy=True).transform
records=[]
for sr in r.iterShapeRecords():
    d=sr.record.as_dict(); records.append((d,transform(project,shape(sr.shape.__geo_interface__))))
selected=[]
for link in links:
    match=[(d,g) for d,g in records if d['NAME'].lower()==link['name'].lower()]
    assert len(match)==1,link
    d,g=match[0]; assert link['status']=='publish'
    selected.append((d,g,link))
extent=unary_union([g for d,g,l in selected]).bounds
x0,y0,x1,y1=extent; pad=5500; x0-=pad;y0-=pad;x1+=pad;y1+=pad
W=640; H=580; scale=min(W/(x1-x0),H/(y1-y0))
# Extend the real geographic context to the entire map viewport, without stretching cities.
cx=(x0+x1)/2; cy=(y0+y1)/2
x0=cx-W/(2*scale); x1=cx+W/(2*scale)
y0=cy-H/(2*scale); y1=cy+H/(2*scale)
ox=0; oy=0
def point(x,y):return ((x-x0)*scale+ox,(y1-y)*scale+oy)
def path(g):
    out=[]
    polys=[g] if g.geom_type=='Polygon' else list(g.geoms) if g.geom_type=='MultiPolygon' else []
    for p in polys:
        for ring in [p.exterior,*p.interiors]:
            pts=[point(x,y) for x,y in ring.coords]
            out.append('M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z')
    return ''.join(out)
clip=box(x0,y0,x1,y1); ids={d['GEOID'] for d,g,l in selected}
background=[]
for d,g in records:
    if d['GEOID'] not in ids and g.intersects(clip):
        background.append('<path d="'+path(g.intersection(clip).simplify(90,preserve_topology=True))+'"/>')
# Official Lake Michigan water polygons; build-time inputs beside the PLACE archive.
waters=[]; water_candidates=[]; water_sources=[]
for county in ['17031','17097']:
    name=f'tl_2026_{county}_areawater'; water_file=archive.parent/(name+'.zip')
    wz=zipfile.ZipFile(water_file); wr=shapefile.Reader(shp=wz.open(name+'.shp'),shx=wz.open(name+'.shx'),dbf=wz.open(name+'.dbf'))
    for sr in wr.iterShapeRecords():
        record=sr.record.as_dict()
        if record.get('MTFCC')=='H2030':
            geometry=transform(project,shape(sr.shape.__geo_interface__))
            water_candidates.append(geometry)
            if record.get('FULLNAME')=='Lk Michigan': waters.append(geometry)
    water_sources.append({'url':'https://www2.census.gov/geo/tiger/TIGER2026/AREAWATER/'+name+'.zip','sha256':hashlib.sha256(water_file.read_bytes()).hexdigest()})
named_lake=unary_union(waters)
# Include adjoining official lake/pond water faces (some carry channel names).
lake=unary_union([g for g in water_candidates if g.intersects(named_lake)]).intersection(clip).simplify(45,preserve_topology=True)
assert lake.is_valid and not lake.is_empty
lx,ly=point(*lake.representative_point().coords[0])
water=f'<g class="gc-map-water" aria-label="Lake Michigan"><path d="{path(lake)}"/><text x="{min(lx,580):.1f}" y="{ly:.1f}" text-anchor="middle"><tspan x="{min(lx,580):.1f}">Lake</tspan><tspan x="{min(lx,580):.1f}" dy="1.2em">Michigan</tspan></text></g>'
chicago=next(d for d,g in records if d['GEOID']=='1714000')
cx,cy=point(*project(float(chicago['INTPTLON']),float(chicago['INTPTLAT'])))
assert 0<cx<W and 0<cy<H
landmark=f'<g class="gc-map-landmark" aria-label="Chicago geographic reference"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="4"/><text x="{cx-9:.1f}" y="{cy+4:.1f}" text-anchor="end">Chicago</text></g>'
features=[]; registry=[]
for d,g,l in selected:
    simplified=g.simplify(45,preserve_topology=True)
    assert simplified.is_valid
    delta=abs(simplified.area-g.area)/g.area
    assert delta<0.02,(d['NAME'],delta)
    x,y=point(*g.representative_point().coords[0])
    name=html.escape(d['NAME']); geoid=d['GEOID']
    features.append(f'<path class="gc-map-city" data-geoid="{geoid}" data-city="{name}" data-x="{x:.1f}" data-y="{y:.1f}" d="{path(simplified)}"><title>{name}</title></path>')
    registry.append({'name':d['NAME'],'geoid':geoid,'page_id':l['page_id'],'area_change_ratio':round(delta,6)})
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 580" aria-label="Featured Chicagoland municipalities" class="gc-map-svg"><g class="gc-map-context" aria-hidden="true">'+''.join(background)+water+'</g><g class="gc-map-features">'+''.join(features)+landmark+'</g><g class="gc-map-north" aria-hidden="true"><text x="600" y="28">N</text><path d="M600 38V67M594 46L600 38L606 46"/></g></svg>'
(HERE/'map.svg').write_text(svg,encoding='utf-8')
manifest={'source':'https://www2.census.gov/geo/tiger/TIGER2026/PLACE/tl_2026_17_place.zip','version':'TIGER/Line 2026','source_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'projection':'EPSG:26916 / NAD83 UTM16N','simplification_meters':45,'context_simplification_meters':90,'cities':registry,'water_sources':water_sources,'chicago_reference':{'geoid':'1714000','latitude':chicago['INTPTLAT'],'longitude':chicago['INTPTLON'],'type':'Census internal point, non-navigation landmark'}}
(HERE/'geography.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
css=(HERE/'map.css').read_text(encoding='utf-8');js=(HERE/'map.js').read_text(encoding='utf-8')
fragment='<style>'+css+'</style><div class="gc-map-fallback"><div class="gc-map-panel" data-gc-map-panel><div class="gc-map-canvas"><span class="gc-map-caption">Chicagoland</span>'+svg+'<div class="gc-map-selection" aria-live="polite" hidden><span data-map-label></span><a data-map-visit hidden>View city page <span aria-hidden="true">→</span></a></div></div><p class="gc-map-note">Featured locations shown for reference. Contact GCPRO to confirm service availability.</p><p class="gc-map-source">Municipal boundaries: US Census Bureau · TIGER/Line 2026</p></div></div><script>'+js+'</script>'
(HERE/'prototype-widget.html').write_text(fragment,encoding='utf-8')
print(json.dumps({'cities':registry,'svg_bytes':len(svg.encode()),'widget_bytes':len(fragment.encode())},indent=2))
