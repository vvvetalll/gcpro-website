(()=>{'use strict';
if(location.hostname!=='vitaliiv1.sg-host.com'||window.GCPROServiceAreasMap)return;
window.GCPROServiceAreasMap={version:'1.0.0'};let instanceCount=0;
const panelMarkup=/* MAP_PANEL */null;
const css=/* MAP_CSS */null;
function init(root){
 if(root.dataset.mapReady)return;
 const template=document.createElement('template');template.innerHTML=panelMarkup;root.append(template.content);
 const scopeId='gc-map-touch-'+(++instanceCount);root.dataset.mapInstance=scopeId;
 const panel=root.querySelector('[data-gc-map-panel]'),section=root,columns=section?.querySelector('.city-link')?.parentElement?.parentElement;
 if(!panel||!columns)return;
 const container=columns.parentElement,links=[...columns.querySelectorAll('a.city-link')],paths=[...panel.querySelectorAll('[data-geoid]')];
 const normalize=s=>s.trim().toLowerCase();
 const pairs=paths.map(path=>({path,link:links.find(a=>normalize(a.textContent)===normalize(path.dataset.city))}));
 if(pairs.some(p=>!p.link)||pairs.length!==links.length)return;
 root.dataset.mapReady='true';container.classList.add('gc-map-layout');columns.classList.add('gc-map-links');container.firstElementChild.classList.add('gc-map-intro');columns.nextElementSibling.classList.add('gc-map-actions');container.insertBefore(panel,columns.nextElementSibling);
 const left=document.createElement('div');left.className='gc-map-left';const actions=container.querySelector('.gc-map-actions');container.insertBefore(left,columns);left.append(columns,actions);
 const svg=panel.querySelector('svg'),ns='http://www.w3.org/2000/svg',world=document.createElementNS(ns,'g');
 svg.prepend(world);world.append(svg.querySelector('.gc-map-context'),svg.querySelector('.gc-map-features'));
 const controls=document.createElement('div');controls.className='gc-map-zoom';controls.setAttribute('role','group');controls.setAttribute('aria-label','Map zoom controls');
 controls.innerHTML='<button type="button" data-zoom="out" aria-label="Zoom out">−</button><button type="button" data-zoom="in" aria-label="Zoom in">+</button><button type="button" data-zoom="reset">Reset</button>';
 svg.before(controls);svg.setAttribute('tabindex','0');svg.setAttribute('role','group');svg.setAttribute('aria-label','Featured municipalities map. When zoomed, drag to pan or use arrow keys.');
 let zoom=1,tx=0,ty=0,drag=null,suppressClick=false;
 function positionInfo(){}
 function renderZoom(){tx=Math.max(640*(1-zoom),Math.min(0,tx));ty=Math.max(580*(1-zoom),Math.min(0,ty));world.setAttribute('transform',`translate(${tx} ${ty}) scale(${zoom})`);svg.classList.toggle('is-zoomed',zoom>1);controls.querySelector('[data-zoom="out"]').disabled=zoom===1;controls.querySelector('[data-zoom="in"]').disabled=zoom===3;positionInfo();}
 controls.addEventListener('click',e=>{const action=e.target.closest('button')?.dataset.zoom;if(!action)return;touchSelected=null;hovered=null;update();const previous=zoom;zoom=action==='reset'?1:Math.max(1,Math.min(3,zoom+(action==='in'?.5:-.5)));tx=320-(320-tx)*zoom/previous;ty=290-(290-ty)*zoom/previous;renderZoom();});
 svg.addEventListener('pointerdown',e=>{suppressClick=false;if(zoom===1||e.button!==0)return;drag={id:e.pointerId,x:e.clientX,y:e.clientY,tx,ty};});
 svg.addEventListener('pointermove',e=>{if(!drag||drag.id!==e.pointerId)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(!suppressClick&&Math.hypot(dx,dy)<6)return;suppressClick=true;touchSelected=null;hovered=null;update();svg.setPointerCapture(e.pointerId);const r=svg.getBoundingClientRect(),scale=Math.min(r.width/640,r.height/580);tx=drag.tx+dx/scale;ty=drag.ty+dy/scale;renderZoom();});
 function endDrag(e){if(!drag||drag.id!==e.pointerId)return;if(svg.hasPointerCapture(e.pointerId))svg.releasePointerCapture(e.pointerId);drag=null;}
 svg.addEventListener('pointerup',endDrag);svg.addEventListener('pointercancel',endDrag);
 svg.addEventListener('click',e=>{if(suppressClick){e.preventDefault();e.stopImmediatePropagation();suppressClick=false;}},true);
 svg.addEventListener('keydown',e=>{if(zoom===1||!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key))return;e.preventDefault();tx+=e.key==='ArrowLeft'?40:e.key==='ArrowRight'?-40:0;ty+=e.key==='ArrowUp'?40:e.key==='ArrowDown'?-40:0;renderZoom();});
 svg.addEventListener('focusin',e=>{const p=e.target.closest('.gc-map-city');if(!p||zoom===1)return;const x=Number(p.dataset.x)*zoom+tx,y=Number(p.dataset.y)*zoom+ty;if(x<30||x>610||y<30||y>550){tx=320-Number(p.dataset.x)*zoom;ty=290-Number(p.dataset.y)*zoom;renderZoom();}});
 renderZoom();
 const label=panel.querySelector('[data-map-label]'),visit=panel.querySelector('[data-map-visit]'),info=label.parentElement;
 panel.querySelector('.gc-map-canvas').after(info);
 let hovered=null,focused=null,touchSelected=null,inputKind='keyboard',lastPointer='mouse';
 function update(){const pair=hovered||focused||touchSelected;for(const p of pairs){p.path.classList.toggle('is-map-active',p===pair);p.link.classList.toggle('is-map-active',p===pair);if(p===touchSelected)p.path.setAttribute('aria-describedby',scopeId);else p.path.removeAttribute('aria-describedby');}
  const touch=(inputKind!=='mouse'&&inputKind!=='keyboard')?touchSelected:null;info.hidden=!touch;visit.hidden=!touch;label.textContent=touch?touch.path.dataset.city:'';visit.firstChild.textContent=touch?.path.dataset.city==='Chicago'?'View service areas ':'View city page ';
  if(touch){visit.href=touch.link.href;info.dataset.x=touch.path.dataset.x;info.dataset.y=touch.path.dataset.y;positionInfo();}
 }
 label.id=scopeId;
 document.addEventListener('pointerdown',e=>{inputKind=e.pointerType||'mouse';if(inputKind==='mouse'||!e.target.closest('.gc-map-city,.gc-map-selection'))touchSelected=null;update();},true);
 document.addEventListener('keydown',()=>{inputKind='keyboard';touchSelected=null;hovered=null;update();},true);
 svg.addEventListener('pointerdown',e=>{lastPointer=e.pointerType||'mouse';});
 for(const p of pairs){
  if(!p.reference){p.link.dataset.geoid=p.path.dataset.geoid;p.path.setAttribute('tabindex','0');p.path.setAttribute('role','link');p.path.setAttribute('aria-label',p.path.dataset.city+(p.path.dataset.city==='Chicago'?' — view service areas':' — view city page'));p.path.querySelector('title')?.remove();p.path.removeAttribute('aria-pressed');}
  for(const node of [p.link,p.path]){
   node.addEventListener('pointerenter',e=>{if(e.pointerType==='touch'||e.pointerType==='pen')return;inputKind='mouse';touchSelected=null;hovered=p;update();});
   node.addEventListener('pointerleave',e=>{if(e.pointerType==='touch'||e.pointerType==='pen')return;if(hovered===p)hovered=null;update();});
   node.addEventListener('focus',()=>{if(inputKind==='keyboard'){focused=p;update();}});
   node.addEventListener('blur',()=>{if(focused===p)focused=null;update();});
  }
  if(p.reference)continue;
  p.path.addEventListener('click',e=>{const type=e.pointerType||lastPointer;if(type==='touch'||type==='pen'){inputKind=type;hovered=null;focused=null;if(touchSelected===p){window.location.assign(p.link.href);return;}touchSelected=p;update();}else window.location.assign(p.link.href);});
  p.path.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();window.location.assign(p.link.href);}if(e.key==='Escape'){touchSelected=null;hovered=null;focused=null;p.path.blur();update();}});
 }
 root.addEventListener('keydown',e=>{if(e.key==='Escape'){touchSelected=null;hovered=null;update();}});

}
const boot=()=>{const roots=[...document.querySelectorAll('.gc-service-areas-map')];if(!roots.length)return;if(!document.getElementById('gc-service-areas-map-style')){const style=document.createElement('style');style.id='gc-service-areas-map-style';style.textContent=css;document.head.append(style);}roots.forEach(init);};
let scheduled=false;const observe=()=>{boot();new MutationObserver(records=>{if(scheduled||!records.some(r=>[...r.addedNodes].some(n=>n.nodeType===1&&(n.matches?.('.gc-service-areas-map')||n.querySelector?.('.gc-service-areas-map')))))return;scheduled=true;queueMicrotask(()=>{scheduled=false;boot();});}).observe(document.body,{childList:true,subtree:true});};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',observe,{once:true});else observe();
})();
