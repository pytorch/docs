(function() {
  'use strict';

  var placeholder = document.getElementById('toc-placeholder');
  if (!placeholder) return;

  var tocSrc = placeholder.getAttribute('data-toc-src');
  if (!tocSrc) return;

  // The TOC file contains URLs relative to the version root.
  // Compute the prefix from this page to the version root so we can
  // resolve those URLs correctly. The _toc file lives at the root,
  // so the number of "../" segments in tocSrc tells us the depth.
  var depthPrefix = tocSrc.replace(/[^/]*$/, '');  // e.g. "../" or ""

  fetch(tocSrc)
    .then(function(response) {
      if (!response.ok) throw new Error('TOC fetch failed: ' + response.status);
      return response.text();
    })
    .then(function(html) {
      var container = document.createElement('div');
      container.innerHTML = html;

      // Rewrite root-relative hrefs to be relative to this page
      if (depthPrefix) {
        var links = container.querySelectorAll('a[href]');
        for (var i = 0; i < links.length; i++) {
          var href = links[i].getAttribute('href');
          if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('mailto:')) {
            links[i].setAttribute('href', depthPrefix + href);
          }
        }
      }

      markCurrentPage(container);
      placeholder.innerHTML = container.innerHTML;
      reinitScrollSpy();
    })
    .catch(function(err) {
      console.warn('TOC loader:', err.message);
    });

  function markCurrentPage(container) {
    var currentPath = window.location.pathname.replace(/\/+/g, '/');
    var links = container.querySelectorAll('a.reference');

    for (var i = 0; i < links.length; i++) {
      var link = links[i];
      var href = link.getAttribute('href');
      if (!href || href.startsWith('http://') || href.startsWith('https://')) continue;

      var resolved = new URL(href, window.location.href).pathname.replace(/\/+/g, '/');

      if (resolved === currentPath) {
        link.classList.add('current');
        link.setAttribute('href', '#');

        var li = link.closest('li');
        while (li) {
          li.classList.add('current');
          if (li.classList.contains('has-children')) {
            li.classList.add('active');
            var details = li.querySelector(':scope > details');
            if (details) details.setAttribute('open', 'open');
          }
          var parentUl = li.parentElement;
          li = parentUl ? parentUl.closest('li') : null;
        }

        var ul = link.closest('ul');
        if (ul) ul.classList.add('current');
        break;
      }
    }
  }

  function reinitScrollSpy() {
    if (typeof bootstrap !== 'undefined' && bootstrap.ScrollSpy) {
      var scrollElement = document.querySelector('[data-bs-spy="scroll"]');
      if (scrollElement) {
        var instance = bootstrap.ScrollSpy.getInstance(scrollElement);
        if (instance) instance.refresh();
      }
    }
  }
})();
