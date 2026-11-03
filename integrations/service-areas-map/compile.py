"""Compile the single Elementor Custom Code deployment artifact. No runtime dependencies."""
from pathlib import Path
import json
import re
from shapely.geometry import LinearRing
HERE=Path(__file__).parent

def compact_context(markup):
    """Simplify only decorative land by <=0.45 SVG units; preserve every ring.

    Featured municipalities and Lake Michigan stay byte-identical. Shapely is
    already used by the project's Census geometry builder, never at runtime.
    Always compile from the unchanged source, avoiding cumulative simplification.
    """
    start=markup.index('<g class="gc-map-context"')
    end=markup.index('<g class="gc-map-water"',start)
    def simplify_path(match):
        rings=[]
        for ring in re.findall(r'M([^Z]+)Z',match[1]):
            points=[tuple(map(float,p.split(','))) for p in ring.split('L')]
            boundary=LinearRing(points)
            reduced=boundary.simplify(.45,preserve_topology=True)
            # Do not erase small islands/holes or change their winding.
            assert boundary.hausdorff_distance(reduced)<=.451
            coords=list(reduced.coords)[:-1]
            if len(coords)<3:
                rings.append('M'+ring+'Z')
                continue
            rings.append('M'+'L'.join(f'{x:g},{y:g}' for x,y in coords)+'Z')
        return 'd="'+''.join(rings)+'"'
    context=re.sub(r'(?<= )d="([^"]+)"',simplify_path,markup[start:end])
    return markup[:start]+context+markup[end:]

js=(HERE/'map.js').read_text(encoding='utf-8')
panel=compact_context((HERE/'map-panel.html').read_text(encoding='utf-8'))
js=js.replace('/* MAP_PANEL */null',json.dumps(panel))
js=js.replace('/* MAP_CSS */null',json.dumps((HERE/'map.css').read_text(encoding='utf-8')))
(HERE/'custom-code.html').write_text('<script>'+js+'</script>',encoding='utf-8')
