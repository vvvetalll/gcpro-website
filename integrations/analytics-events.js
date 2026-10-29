/* Sole GTM event bridge. Never reads form values or raw coverage input. */
(function () {
  'use strict';
  if (window.gcproAnalyticsReady || location.hostname !== 'vitaliiv1.sg-host.com') return;
  window.gcproAnalyticsReady = true;
  var names = ['page_view','generate_lead','contact_submit','click_to_call','request_service_click','email_click','directions_click','coverage_search','coverage_area_click','portfolio_filter','portfolio_reset','portfolio_load_more','project_open'];
  function send(name, values) {
    if (names.indexOf(name) < 0) return;
    var path=location.pathname;
    var project=path.indexOf('/portfolio/')===0 && path.replace(/\/$/,'')!=='/portfolio';
    var data = {event:'gcpro_event',gcpro_event_name:name,gcpro_cta_location:'',gcpro_form_type:'',gcpro_result_status:'',gcpro_filter_dimension:'',gcpro_filter_value:'',gcpro_project_id:'',gcpro_city:'',gcpro_service:'',gcpro_page_location:location.origin+(project?'/portfolio/project/':path),gcpro_page_referrer:'',gcpro_page_title:project?'Project details':path};
    try {data.gcpro_page_referrer=document.referrer?new URL(document.referrer).origin:'';}catch(ignore){}
    Object.keys(values || {}).forEach(function (key) { if (Object.prototype.hasOwnProperty.call(data,key)) data[key]=values[key]; });
    window.dataLayer = window.dataLayer || []; window.dataLayer.push(data);
  }
  function placement(node) {
    if (node.closest('.elementor-popup-modal')) return 'popup';
    if (node.closest('header,[data-elementor-type="header"]')) return 'header';
    if (node.closest('footer,[data-elementor-type="footer"]')) return 'footer';
    if (node.closest('.gcpro-cta-origin')) return 'hero';
    var main=document.querySelector('main');
    if (main) {
      var panels=main.querySelectorAll('.gcpro-cta-section-test');
      if(panels.length && panels[panels.length-1].contains(node)) return 'final';
    }
    return 'mid_page';
  }
  document.addEventListener('click', function (event) {
    var link=event.target.closest('a[href]'); if(!link) return;
    var url;try {url=new URL(link.href,location.href);}catch(ignore){return;}
    var context={gcpro_cta_location:placement(link)};
    if(url.protocol==='tel:') send('click_to_call',context);
    else if(url.protocol==='mailto:') send('email_click',context);
    else if(url.hostname==='www.google.com' && url.pathname.indexOf('/maps/dir')===0) send('directions_click',context);
    else if(url.origin===location.origin && url.pathname.replace(/\/$/,'')==='/service-request') send('request_service_click',context);
    else if(link.matches('[data-coverage-action]') && url.origin===location.origin && url.pathname.indexOf('/service-area/')===0) send('coverage_area_click',context);
    else if(link.closest('.elementor-loop-container') && url.origin===location.origin && url.pathname.indexOf('/portfolio/')===0) {
      var card=link.closest('.e-loop-item');
      var id=card && card.className.match(/(?:^|\s)e-loop-item-(\d+)(?:\s|$)/);
      if(id) context.gcpro_project_id=id[1];
      var city=card && card.className.match(/(?:^|\s)project_area-([a-z-]+)(?:\s|$)/);
      if(city) context.gcpro_city=city[1];
      send('project_open',context);
    }
  },true);
  function watchForm(form) {
    if(form.getAttribute('data-gcpro-analytics-watched')) return;
    var type={'GCPRO | Request Service':'request_service','GCPRO | Contact Us':'contact'}[form.getAttribute('aria-label')];
    if(!type) return; // Apply and unknown forms are intentionally excluded.
    form.setAttribute('data-gcpro-analytics-watched','true');
    var successful=form.classList.contains('form-state-success');
    new MutationObserver(function () {
      var now=form.classList.contains('form-state-success');
      if(now && !successful) send(type==='request_service'?'generate_lead':'contact_submit',{gcpro_form_type:type,gcpro_cta_location:'mid_page'});
      successful=now;
    }).observe(form,{attributes:true,attributeFilter:['class']});
  }
  function scan() {
    document.querySelectorAll('form[data-element_type="e-form"]').forEach(watchForm);
    document.querySelectorAll('[data-gcpro-availability]').forEach(function (root) {
      var result=root.querySelector('[data-result]'); if(!result || result.getAttribute('data-gcpro-analytics-watched')) return;
      result.setAttribute('data-gcpro-analytics-watched','true');
      new MutationObserver(function (records) {
        records.forEach(function(record){
          if(record.attributeName!=='data-status') return;
          var status=result.getAttribute('data-status');
          if(['served','requires_call','not_served','unresolved','error'].indexOf(status)>=0) send('coverage_search',{gcpro_result_status:status,gcpro_cta_location:'popup'});
        });
      }).observe(result,{attributes:true,attributeFilter:['data-status']});
    });
  }
  scan();new MutationObserver(scan).observe(document.body,{childList:true,subtree:true});
  send('page_view',{});
  // Native WPGB field attributes identify controls; no label-text matching.
  document.addEventListener('change',function(event){
    var control=event.target.closest('select.wpgb-select'); if(!control) return;
    var dimension={gcpro_projects_service:'service',gcpro_projects_location:'location',gcpro_projects_property_type:'sector'}[control.name];
    if(!dimension) return;
    var value=control.value;
    if(value && !/^[a-z-]{1,50}$/.test(value)) return;
    send('portfolio_filter',{gcpro_filter_dimension:dimension,gcpro_filter_value:value||'all'});
  });
  document.addEventListener('click',function(event){
    if(event.target.closest('.wpgb-reset')) send('portfolio_reset',{});
    if(event.target.closest('.wpgb-load-more')) send('portfolio_load_more',{});
  });
})();
