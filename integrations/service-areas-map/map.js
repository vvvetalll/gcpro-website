(()=>{'use strict';
if(location.hostname!=='vitaliiv1.sg-host.com'||window.GCPROServiceAreasMap)return;
window.GCPROServiceAreasMap={version:'1.1.0'};let instanceCount=0;
// Verified native routes identify geography, never the editable display label.
const destinations={
 '/service-area/':'1714000','/service-area/lombard/':'1744407',
 '/service-area/glenview/':'1729938','/service-area/northbrook/':'1753481',
 '/service-area/oak-brook/':'1754534','/service-area/carol-stream/':'1711332',
 '/service-area/downers-grove/':'1720591','/service-area/schaumburg/':'1768003',
 '/service-area/highland-park/':'1734722','/service-area/naperville/':'1751622',
 '/service-area/elmhurst/':'1723620'
};
const editor=new URLSearchParams(location.search).has('elementor-preview');
const diagnostic=(message,detail)=>{if(editor)console.warn('[GCPRO map] '+message,detail);};
const panelMarkup=/* MAP_PANEL */null;
const css=/* MAP_CSS */null;
function init(root){
 if(root.dataset.mapReady)return;
 const template=document.createElement('template');template.innerHTML=panelMarkup;
 const panel=template.content.querySelector('[data-gc-map-panel]'),columns=root.querySelector('.city-link')?.parentElement?.parentElement;
 if(!panel||!columns||!columns.nextElementSibling)return;
 const container=columns.parentElement,links=[...columns.querySelectorAll('a.city-link')],paths=[...panel.querySelectorAll('[data-geoid]')];
 const byGeoid=new Map();
 for(const link of links){const url=new URL(link.href,location.href),geoid=url.origin===location.origin?destinations[url.pathname.replace(/\/+$/,'')+'/']:null;
  if(geoid&&!byGeoid.has(geoid))byGeoid.set(geoid,link);else diagnostic('Unmatched or duplicate native city route',url.pathname);}
 const pairs=paths.map(path=>({path,link:byGeoid.get(path.dataset.geoid)})).filter(p=>p.link);
 if(!pairs.length){diagnostic('No verified city routes; native list retained');return;}
 for(const path of paths)if(!byGeoid.has(path.dataset.geoid)){path.style.pointerEvents='none';diagnostic('No native destination for municipality',path.dataset.geoid);}
 const scopeId='gc-map-touch-'+(++instanceCount);root.dataset.mapInstance=scopeId;
 root.dataset.mapReady='true';container.classList.add('gc-map-layout');columns.classList.add('gc-map-links');(container.querySelector(':scope > [data-id]')||container.firstElementChild).classList.add('gc-map-intro');columns.nextElementSibling.classList.add('gc-map-actions');container.insertBefore(panel,columns.nextElementSibling);
 const left=document.createElement('div');left.className='gc-map-left';const actions=container.querySelector('.gc-map-actions');container.insertBefore(left,columns);left.append(columns,actions);
 const svg=panel.querySelector('svg'),ns='http://www.w3.org/2000/svg',world=document.createElementNS(ns,'g');
 svg.prepend(world);world.append(svg.querySelector('.gc-map-context'),svg.querySelector('.gc-map-features'));
 const controls=document.createElement('div');controls.className='gc-map-zoom';controls.setAttribute('role','group');controls.setAttribute('aria-label','Map zoom controls');
 controls.innerHTML='<button type="button" data-zoom="out" aria-label="Zoom out">&#8722;</button><button type="button" data-zoom="in" aria-label="Zoom in">+</button><button type="button" data-zoom="reset">Reset</button>';
 svg.before(controls);svg.removeAttribute('tabindex');svg.setAttribute('role','img');svg.setAttribute('aria-label','Map of Chicago and ten suburban municipalities near Lake Michigan. Use the city links for navigation. Municipal boundaries do not establish service eligibility.');
 controls.setAttribute('aria-description','When zoomed, use arrow keys on these controls to pan the map.');
 for(const path of paths){path.removeAttribute('tabindex');path.removeAttribute('role');path.removeAttribute('aria-pressed');path.setAttribute('aria-hidden','true');path.querySelector('title')?.remove();}
 let zoom=1,tx=0,ty=0,drag=null,suppressClick=false;
 function renderZoom(){tx=Math.max(640*(1-zoom),Math.min(0,tx));ty=Math.max(580*(1-zoom),Math.min(0,ty));world.setAttribute('transform',`translate(${tx} ${ty}) scale(${zoom})`);svg.classList.toggle('is-zoomed',zoom>1);controls.querySelector('[data-zoom="out"]').disabled=zoom===1;controls.querySelector('[data-zoom="in"]').disabled=zoom===3;}
 controls.addEventListener('click',e=>{const action=e.target.closest('button')?.dataset.zoom;if(!action)return;touchSelected=null;hovered=null;update();const previous=zoom;zoom=action==='reset'?1:Math.max(1,Math.min(3,zoom+(action==='in'?.5:-.5)));tx=320-(320-tx)*zoom/previous;ty=290-(290-ty)*zoom/previous;renderZoom();});
 svg.addEventListener('pointerdown',e=>{suppressClick=false;if(zoom===1||e.button!==0)return;drag={id:e.pointerId,x:e.clientX,y:e.clientY,tx,ty};});
 svg.addEventListener('pointermove',e=>{if(!drag||drag.id!==e.pointerId)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(!suppressClick&&Math.hypot(dx,dy)<6)return;suppressClick=true;touchSelected=null;hovered=null;update();svg.setPointerCapture(e.pointerId);const r=svg.getBoundingClientRect(),scale=Math.min(r.width/640,r.height/580);tx=drag.tx+dx/scale;ty=drag.ty+dy/scale;renderZoom();});
 function endDrag(e){if(!drag||drag.id!==e.pointerId)return;if(svg.hasPointerCapture(e.pointerId))svg.releasePointerCapture(e.pointerId);drag=null;}
 svg.addEventListener('pointerup',endDrag);svg.addEventListener('pointercancel',endDrag);
 svg.addEventListener('click',e=>{if(suppressClick){e.preventDefault();e.stopImmediatePropagation();suppressClick=false;}},true);
 controls.addEventListener('keydown',e=>{if(zoom===1||!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key))return;e.preventDefault();tx+=e.key==='ArrowLeft'?40:e.key==='ArrowRight'?-40:0;ty+=e.key==='ArrowUp'?40:e.key==='ArrowDown'?-40:0;renderZoom();});
 renderZoom();
 const label=panel.querySelector('[data-map-label]'),visit=panel.querySelector('[data-map-visit]'),info=label.parentElement;
 panel.querySelector('.gc-map-canvas').after(info);
 let hovered=null,focused=null,touchSelected=null,inputKind='keyboard',lastPointer='mouse';
 function update(){const pair=hovered||focused||touchSelected;for(const p of pairs){p.path.classList.toggle('is-map-active',p===pair);p.link.classList.toggle('is-map-active',p===pair);}
  const touch=(inputKind!=='mouse'&&inputKind!=='keyboard')?touchSelected:null;info.hidden=!touch;visit.hidden=!touch;label.textContent=touch?touch.path.dataset.city:'';visit.firstChild.textContent=touch?.path.dataset.city==='Chicago'?'View service areas ':'View city page ';
  if(touch)visit.href=touch.link.href;
 }
 label.id=scopeId;
 document.addEventListener('pointerdown',e=>{inputKind=e.pointerType||'mouse';if(inputKind==='mouse'||!e.target.closest('.gc-map-city,.gc-map-selection'))touchSelected=null;update();},true);
 document.addEventListener('keydown',()=>{inputKind='keyboard';touchSelected=null;hovered=null;update();},true);
 svg.addEventListener('pointerdown',e=>{lastPointer=e.pointerType||'mouse';});
 for(const p of pairs){
  p.link.dataset.geoid=p.path.dataset.geoid;
  for(const node of [p.link,p.path]){
   node.addEventListener('pointerenter',e=>{if(e.pointerType==='touch'||e.pointerType==='pen')return;inputKind='mouse';touchSelected=null;hovered=p;update();});
   node.addEventListener('pointerleave',e=>{if(e.pointerType==='touch'||e.pointerType==='pen')return;if(hovered===p)hovered=null;update();});
  }
  p.link.addEventListener('focus',()=>{focused=p;hovered=null;update();if(zoom>1){const x=Number(p.path.dataset.x)*zoom+tx,y=Number(p.path.dataset.y)*zoom+ty;if(x<30||x>610||y<30||y>550){tx=320-Number(p.path.dataset.x)*zoom;ty=290-Number(p.path.dataset.y)*zoom;renderZoom();}}});
  p.link.addEventListener('blur',()=>{if(focused===p)focused=null;update();});
  p.path.addEventListener('click',e=>{const type=e.pointerType||lastPointer;if(type==='touch'||type==='pen'){inputKind=type;hovered=null;focused=null;if(touchSelected===p){window.location.assign(p.link.href);return;}touchSelected=p;update();}else window.location.assign(p.link.href);});
 }
 root.addEventListener('keydown',e=>{if(e.key==='Escape'){touchSelected=null;hovered=null;update();}});

}
const boot=()=>{const roots=[...document.querySelectorAll('.gc-service-areas-map')];if(!roots.length)return;if(!document.getElementById('gc-service-areas-map-style')){const style=document.createElement('style');style.id='gc-service-areas-map-style';style.textContent=css;document.head.append(style);}roots.forEach(init);};
// Published consumers render native1140 in the initial HTML. Elementor's editing
// canvas owns and replaces these nodes; keep its native editable tree intact.
// Use Preview Changes/the frontend to test the enhanced map.
const start=()=>{if(document.body.classList.contains('elementor-editor-active'))return;boot();};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
})();
