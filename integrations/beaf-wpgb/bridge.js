/* Prototype owner: WP Grid Builder Grid 1 > JavaScript. Do not enqueue this mirror.
 * Existing BEAF runtime owns dragging and fullscreen; WPGB owns filtering/loading.
 */
(function ($) {
  'use strict';
  var root = document.querySelector('.wpgb-grid-1');
  if (!root || !wpgb.facets) return;
  var popupSeed;
  var status = document.createElement('p');
  status.className = 'gcpro-ba-status';
  status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite');
  root.before(status);
  function layout() {
    $(window).trigger('resize.twentytwenty');
    if (wpgb.grid) wpgb.grid.layout();
  }
  function accessibleSlider(el, suppliedTitle) {
    var handle = el.querySelector('.twentytwenty-handle');
    if (!handle || handle.dataset.gcproKeyboard) return;
    handle.dataset.gcproKeyboard = 'true';
    var vertical = el.getAttribute('bafg-orientation') === 'vertical';
    var title = suppliedTitle || el.closest('.ba-card').querySelector('.ba-card__title').textContent;
    handle.setAttribute('tabindex', '0');
    handle.setAttribute('role', 'slider');
    handle.setAttribute('aria-label', 'Before and after: ' + title);
    handle.setAttribute('aria-orientation', vertical ? 'vertical' : 'horizontal');
    handle.setAttribute('aria-valuemin', '0');
    handle.setAttribute('aria-valuemax', '100');
    function value() {
      var size = vertical ? el.clientHeight : el.clientWidth;
      return Math.max(0, Math.min(100, Math.round(parseFloat(handle.style[vertical ? 'top' : 'left']) / size * 100))) || 0;
    }
    function sync() {
      var percent = value();
      handle.setAttribute('aria-valuenow', String(percent));
      handle.setAttribute('aria-valuetext', percent + '% before image');
    }
    new MutationObserver(sync).observe(handle, {attributes: true, attributeFilter: ['style']});
    handle.addEventListener('keydown', function (event) {
      var keys = {ArrowLeft:-5, ArrowDown:-5, ArrowRight:5, ArrowUp:5, PageDown:-10, PageUp:10};
      if (!(event.key in keys) && event.key !== 'Home' && event.key !== 'End') return;
      event.preventDefault();
      var percent = event.key === 'Home' ? 0 : event.key === 'End' ? 100 : Math.max(0, Math.min(100, value() + keys[event.key]));
      var offset = $(el).offset();
      // Use the vendor's move handlers so its stored position survives resize.
      function move(type) {
        var nativeEvent = new Event(type, {cancelable:true});
        Object.assign(nativeEvent, {distX:0, distY:0, pageX:offset.left + el.clientWidth * percent / 100, pageY:offset.top + el.clientHeight * percent / 100});
        $(handle).triggerHandler($.Event(nativeEvent));
      }
      move('movestart'); move('move'); move('moveend');
      sync();
    });
    sync();
  }
  // A bookmarked filter can initially contain no fullscreen-enabled item, so
  // no vendor-bound button exists to clone. Reuse the same BEAF endpoint/runtime.
  function openNativePopup(button) {
    if (button.dataset.gcproLoading) return;
    button.dataset.gcproLoading = 'true';
    var title = button.closest('.ba-card').querySelector('.ba-card__title').textContent;
    $.ajax({url:bafg_ajax_url.ajax_url + '/inc/popup-load.php', type:'post', dataType:'json', data:{id:button.getAttribute('data-id')}}).done(function(response) {
      var modal = $('<section class="bafg_popup_preview" role="dialog" aria-modal="true"></section>').attr('aria-label', title);
      var content = $('<div class="bafg_popup_preview_content"></div>').appendTo(modal);
      var close = $('<button type="button" class="close" aria-label="Exit full screen">×</button>').appendTo(content);
      var wrap = $('<div id="bafg_popup_wrap"></div>').html(response.shortcode).appendTo(content);
      wrap.find('.popup_button').remove();
      modal.appendTo('body').show();
      wrap.find('.bafg-twentytwenty-container').each(function() {
        var el = $(this);
        el.twentytwenty({orientation:el.attr('bafg-orientation'), default_offset_pct:el.attr('bafg-default-offset'), before_label:el.attr('bafg-before-label'), after_label:el.attr('bafg-after-label'), no_overlay:el.attr('bafg-overlay') !== '1', move_slider_on_hover:!!el.attr('bafg-move-slider-on-hover'), click_to_move:!!el.attr('bafg-click-to-move')});
        el.find('.bafg-preloader').remove();
        accessibleSlider(this, title);
        el.find('img').on('load.gcproBA', layout);
      });
      modal.on('keydown.gcproBA', function(event) {
        if (event.key === 'Escape') {event.preventDefault(); close.trigger('click');}
        if (event.key === 'Tab') {
          var controls = modal.find('button,[tabindex="0"]');
          var first = controls[0], last = controls[controls.length - 1];
          if (event.shiftKey && document.activeElement === first) {event.preventDefault(); last.focus();}
          else if (!event.shiftKey && document.activeElement === last) {event.preventDefault(); first.focus();}
        }
      });
      close.on('click.gcproBA', function() {modal.remove(); button.focus();});
      close[0].focus(); layout();
    }).fail(function() {status.textContent = 'The full-screen comparison could not load. Please try again.';}).always(function() {delete button.dataset.gcproLoading;});
  }
  function enhance() {
    $(root).find('.bafg-twentytwenty-container').each(function () {
      var el = this, $el = $(el);
      if (!el.classList.contains('twentytwenty-container')) {
        $el.twentytwenty({orientation:$el.attr('bafg-orientation'), default_offset_pct:$el.attr('bafg-default-offset'), before_label:$el.attr('bafg-before-label'), after_label:$el.attr('bafg-after-label'), no_overlay:$el.attr('bafg-overlay') !== '1', move_slider_on_hover:!!$el.attr('bafg-move-slider-on-hover'), click_to_move:!!$el.attr('bafg-click-to-move')});
        $el.find('.bafg-preloader').remove();
      }
      accessibleSlider(el);
      $el.find('img').each(function () {
        if (!this.complete) $(this).one('load.gcproBA error.gcproBA', layout);
      });
    });
    $(root).find('.popup_button').each(function () {
      if (this.dataset.gcproPopup) return;
      var button = this;
      // Clone the existing vendor-bound button; preserve its own AJAX/fullscreen handler.
      if (popupSeed) {
        var clone = popupSeed.clone(true);
        Array.from(button.attributes).forEach(function (a) { clone.attr(a.name, a.value); });
        clone.html(button.innerHTML);
        $(button).replaceWith(clone);
        button = clone[0];
      }
      if (!popupSeed && !button.dataset.gcproInitial) $(button).on('click.gcproBA', function() {openNativePopup(this);});
      button.dataset.gcproPopup = 'true';
      button.setAttribute('role', 'button');
      button.setAttribute('tabindex', '0');
      button.setAttribute('aria-label', 'Full screen: ' + button.closest('.ba-card').querySelector('.ba-card__title').textContent);
      $(button).on('keydown.gcproBA', function (event) { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); $(this).trigger('click'); } });
    });
    layout();
    status.textContent = root.querySelectorAll('.ba-card').length + ' comparisons shown.';
  }
  function initial() {
    popupSeed = $(root).find('.popup_button').first().clone(true);
    // The original buttons already have the vendor listener; mark before enhancing.
    var seed = popupSeed;
    $(root).find('.popup_button').attr('data-gcpro-initial', 'true');
    popupSeed = null;
    enhance();
    popupSeed = seed.length ? seed : null;
  }
  if (document.readyState === 'complete') setTimeout(initial, 0);
  else $(window).one('load.gcproBA', function () { setTimeout(initial, 0); });
  wpgb.facets.on('appended', enhance);
})(jQuery);
