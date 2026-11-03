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
 const label=panel.querySelector('[data-map-label]'),visit=panel.querySelector('[data-map-visit]');let pinned=null;
 function show(pair){for(const p of pairs){p.path.classList.toggle('is-map-active',p===pair);p.link.classList.toggle('is-map-active',p===pair);p.path.setAttribute('aria-pressed',String(p===pair));}label.textContent=pair?pair.path.dataset.city:'Explore a location';visit.hidden=!pair;if(pair)visit.href=pair.link.href;}
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
