(()=>{'use strict';
const host=document.currentScript.closest('.elementor');if(host)host.classList.add('gc-map-prototype');
function init(root){
 if(root.dataset.mapReady)return;
 const panel=root.querySelector('[data-gc-map-panel]'),section=root.querySelector('section'),columns=section?.querySelector('.city-link')?.parentElement?.parentElement;
 if(!panel||!columns)return;
 const container=columns.parentElement,links=[...columns.querySelectorAll('a.city-link')],paths=[...panel.querySelectorAll('[data-geoid]')];
 const normalize=s=>s.trim().toLowerCase();
 const pairs=paths.map(path=>({path,link:links.find(a=>normalize(a.textContent)===normalize(path.dataset.city))}));
 if(pairs.some(p=>!p.link)||pairs.length!==links.length)return;
 root.dataset.mapReady='true';container.classList.add('gc-map-layout');columns.classList.add('gc-map-links');container.firstElementChild.classList.add('gc-map-intro');columns.nextElementSibling.classList.add('gc-map-actions');container.insertBefore(panel,columns.nextElementSibling);
 const svg=panel.querySelector('svg'),ns='http://www.w3.org/2000/svg',world=document.createElementNS(ns,'g');
 svg.prepend(world);world.append(svg.querySelector('.gc-map-context'),svg.querySelector('.gc-map-features'));
 const controls=document.createElement('div');controls.className='gc-map-zoom';controls.setAttribute('role','group');controls.setAttribute('aria-label','Map zoom controls');
 controls.innerHTML='<button type="button" data-zoom="out" aria-label="Zoom out">−</button><button type="button" data-zoom="in" aria-label="Zoom in">+</button><button type="button" data-zoom="reset">Reset</button>';
 svg.before(controls);svg.setAttribute('tabindex','0');svg.setAttribute('role','group');svg.setAttribute('aria-label','Featured municipalities map. When zoomed, drag to pan or use arrow keys.');
 let zoom=1,tx=0,ty=0,drag=null,suppressClick=false;
 function positionInfo(){const info=panel.querySelector('.gc-map-selection');if(info.hidden)return;const x=Number(info.dataset.x)*zoom+tx,y=Number(info.dataset.y)*zoom+ty;info.style.left=x>320?'12px':'auto';info.style.right=x>320?'auto':'12px';info.style.top=y>340?'68px':'auto';info.style.bottom=y>340?'auto':'12px';}
 function renderZoom(){tx=Math.max(640*(1-zoom),Math.min(0,tx));ty=Math.max(580*(1-zoom),Math.min(0,ty));world.setAttribute('transform',`translate(${tx} ${ty}) scale(${zoom})`);svg.classList.toggle('is-zoomed',zoom>1);controls.querySelector('[data-zoom="out"]').disabled=zoom===1;controls.querySelector('[data-zoom="in"]').disabled=zoom===3;positionInfo();}
 controls.addEventListener('click',e=>{const action=e.target.closest('button')?.dataset.zoom;if(!action)return;const previous=zoom;zoom=action==='reset'?1:Math.max(1,Math.min(3,zoom+(action==='in'?.5:-.5)));tx=320-(320-tx)*zoom/previous;ty=290-(290-ty)*zoom/previous;renderZoom();});
 svg.addEventListener('pointerdown',e=>{if(zoom===1||e.button!==0)return;suppressClick=false;drag={id:e.pointerId,x:e.clientX,y:e.clientY,tx,ty};});
 svg.addEventListener('pointermove',e=>{if(!drag||drag.id!==e.pointerId)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(!suppressClick&&Math.hypot(dx,dy)<6)return;suppressClick=true;svg.setPointerCapture(e.pointerId);const r=svg.getBoundingClientRect(),scale=Math.min(r.width/640,r.height/580);tx=drag.tx+dx/scale;ty=drag.ty+dy/scale;renderZoom();});
 function endDrag(e){if(!drag||drag.id!==e.pointerId)return;if(svg.hasPointerCapture(e.pointerId))svg.releasePointerCapture(e.pointerId);drag=null;}
 svg.addEventListener('pointerup',endDrag);svg.addEventListener('pointercancel',endDrag);
 svg.addEventListener('click',e=>{if(suppressClick){e.preventDefault();e.stopImmediatePropagation();suppressClick=false;}},true);
 svg.addEventListener('keydown',e=>{if(zoom===1||!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key))return;e.preventDefault();tx+=e.key==='ArrowLeft'?40:e.key==='ArrowRight'?-40:0;ty+=e.key==='ArrowUp'?40:e.key==='ArrowDown'?-40:0;renderZoom();});
 svg.addEventListener('focusin',e=>{const p=e.target.closest('.gc-map-city');if(!p||zoom===1)return;const x=Number(p.dataset.x)*zoom+tx,y=Number(p.dataset.y)*zoom+ty;if(x<30||x>610||y<30||y>550){tx=320-Number(p.dataset.x)*zoom;ty=290-Number(p.dataset.y)*zoom;renderZoom();}});
 renderZoom();
 const label=panel.querySelector('[data-map-label]'),visit=panel.querySelector('[data-map-visit]');let pinned=null;
 function show(pair){for(const p of pairs){p.path.classList.toggle('is-map-active',p===pair);p.link.classList.toggle('is-map-active',p===pair);p.path.setAttribute('aria-pressed',String(p===pair));}label.textContent=pair?pair.path.dataset.city:'';label.parentElement.hidden=!pair;visit.hidden=!pair;if(pair){visit.href=pair.link.href;label.parentElement.dataset.x=pair.path.dataset.x;label.parentElement.dataset.y=pair.path.dataset.y;positionInfo();}}
 function restore(){const active=pairs.find(p=>p.link===document.activeElement||p.path===document.activeElement);show(active||pinned);}
 for(const p of pairs){
  p.link.dataset.geoid=p.path.dataset.geoid;p.path.setAttribute('tabindex','0');p.path.setAttribute('role','button');p.path.setAttribute('aria-label','Select '+p.path.dataset.city);p.path.setAttribute('aria-pressed','false');
  for(const node of [p.link,p.path]){node.addEventListener('pointerenter',e=>{if(e.pointerType!=='touch')show(p)});node.addEventListener('pointerleave',restore);node.addEventListener('focus',()=>show(p));node.addEventListener('blur',()=>queueMicrotask(restore));}
  p.path.addEventListener('click',()=>{pinned=p;show(p)});
  p.path.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pinned=p;show(p);visit.focus();}if(e.key==='Escape'){pinned=null;p.path.blur();show(null);}});
 }
 panel.addEventListener('pointerleave',restore);root.addEventListener('keydown',e=>{if(e.key==='Escape'){pinned=null;show(null);}});
}
const boot=()=>document.querySelectorAll('.gc-map-prototype').forEach(init);
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();
})();
