/* Existing Elementor modal/form only. No search persistence, tracking or second modal. */
(() => {
  'use strict';
  if (window.gcproCoverageReady) return;
  window.gcproCoverageReady = true;
  const rootNow = () => document.querySelector('.elementor-popup-modal [data-elementor-id="1801"]');
  let position = {x:scrollX,y:scrollY}, trigger = null, request = null, sequence = 0;
  const slots = root => ({input:root.querySelector('input'),form:root.querySelector('form'),error:root.querySelector('[data-error]'),result:root.querySelector('[data-result]'),actions:root.querySelector('[data-coverage-actions]'),config:root.querySelector('[data-gcpro-availability]')});
  const cancel = () => { sequence++; if(request) request.abort(); request=null; };
  function busy(root, value) {
    const {form} = slots(root); if(!form) return;
    form.setAttribute('aria-busy',String(value));
    const button = form.querySelector('[type="submit"]'); if(button) button.disabled=value;
  }
  function reset() {
    const root=rootNow(); if(!root) return;
    cancel(); const {input,form,error,result,actions}=slots(root);
    if(!input||!form||!error||!result||!actions) return;
    form.noValidate=true; form.reset(); input.maxLength=80;
    input.setAttribute('aria-describedby','gcpro-coverage-error'); input.removeAttribute('aria-invalid');
    error.textContent=''; result.textContent=''; actions.replaceChildren(); busy(root,false);
    const oldCall=root.querySelector('a[href="tel:+18476563322"]'); if(oldCall) oldCall.hidden=true;
    const modal=root.closest('.elementor-popup-modal');
    modal.setAttribute('role','dialog'); modal.setAttribute('aria-modal','true'); modal.setAttribute('aria-label','Check Service Availability'); modal.tabIndex=-1;
    const close=modal.querySelector('.dialog-close-button'); if(close) close.setAttribute('aria-label','Close service availability');
    modal.focus({preventScroll:true});
  }
  document.addEventListener('click',event=>{
    const a=event.target.closest('a');
    if(!a) return;
    // Native popup action identifies the trigger, independent of editable button copy.
    try {
      const action=decodeURIComponent(a.hash || '');
      const settings=action.match(/(?:[?&])settings=([^&]+)/);
      if(action.includes('action=popup:open') && settings && Number(JSON.parse(atob(settings[1])).id)===1801) {
        trigger=a;position={x:scrollX,y:scrollY};
      }
    } catch(_) { /* An unrelated or malformed link is not this popup's trigger. */ }
  },true);
  document.addEventListener('submit',async event=>{
    const root=event.target.closest('.elementor-popup-modal')?.querySelector('[data-elementor-id="1801"]');
    if(!root || !root.querySelector('[data-endpoint]')) return;
    event.preventDefault(); event.stopImmediatePropagation();
    cancel(); const token=sequence;
    const {input,error,result,actions,config}=slots(root);
    error.textContent=''; result.textContent=''; actions.replaceChildren();
    const value=input.value.trim().replace(/\s+/g,' ');
    if(value.length>80 || !(/^[0-9]{5}(?:-[0-9]{4})?$/.test(value)||/^[A-Za-z]+(?:[ .’'\-]+[A-Za-z]+)*$/.test(value))) {
      error.textContent='Enter a city name or a five-digit ZIP code.';input.setAttribute('aria-invalid','true');input.focus({preventScroll:true});return;
    }
    input.removeAttribute('aria-invalid'); busy(root,true); result.textContent='Checking…';
    request=new AbortController(); const controller=request; const timer=setTimeout(()=>controller.abort(),12000);
    try {
      const response=await fetch(config.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:value}),signal:request.signal,credentials:'omit',cache:'no-store'});
      const data=await response.json(); if(token!==sequence) return;
      if(!response.ok || typeof data.message!=='string' || !Array.isArray(data.actions)) throw Error('lookup');
      result.textContent=data.message;
      for(const action of data.actions) {
        if(typeof action.label!=='string'||typeof action.url!=='string') continue;
        const url=new URL(action.url,location.href);
        if(url.protocol!=='tel:' && (url.origin!==location.origin||!['http:','https:'].includes(url.protocol))) continue;
        if(url.protocol==='tel:' && action.url!=='tel:+18476563322') continue;
        const link=document.createElement('a');link.href=action.url;link.textContent=action.label;
        // Reuse the existing native action's generated classes; no duplicated button design.
        const existing=root.querySelector('a[href="tel:+18476563322"]');
        if(existing && (action.label==='Request Service'||url.protocol==='tel:')) link.className=existing.className; else link.className='gcpro-coverage-services-link';
        link.setAttribute('data-coverage-action','');actions.append(link);
      }
    } catch(errorCaught) {
      if(token===sequence) { result.textContent='We couldn’t check coverage right now. Please call us.'; const link=document.createElement('a');link.href='tel:+18476563322';link.textContent='Call Now'; const existing=root.querySelector('a[href="tel:+18476563322"]'); if(existing)link.className=existing.className;actions.append(link); }
    } finally { clearTimeout(timer); if(token===sequence) {busy(root,false);request=null;} }
  },true);
  document.addEventListener('keydown',event=>{
    if(event.key!=='Tab')return;
    const modal=event.target.closest('.elementor-popup-modal');if(!modal?.querySelector('[data-elementor-id="1801"] [data-endpoint]'))return;
    const focusable=[...modal.querySelectorAll('a[href],button,input,[tabindex="0"]')].filter(x=>!x.hidden&&!x.disabled&&x.getClientRects().length);
    const first=focusable[0],last=focusable[focusable.length-1];if(!first)return;
    if(event.shiftKey&&(document.activeElement===first||document.activeElement===modal)){event.preventDefault();last.focus();}
    else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}
  });
  if(window.jQuery) {
    window.jQuery(document).on('elementor/popup/show.gcproCoverage',(event,id)=>{if(+id===1801)reset();});
    window.jQuery(document).on('elementor/popup/hide.gcproCoverage',(event,id)=>{
      if(+id!==1801)return;cancel();const root=rootNow();if(root)busy(root,false);
      const restore=()=>{if(trigger?.isConnected)trigger.focus({preventScroll:true});window.scrollTo({left:position.x,top:position.y,behavior:'instant'});};
      requestAnimationFrame(restore);setTimeout(restore,340);
    });
  }
  reset();
})();
