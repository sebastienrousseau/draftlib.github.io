/*!
 * Apex behaviour: a navigation disclosure and a theme toggle.
 *
 * Both controls are present and usable in the markup before this file
 * runs; this only upgrades them.
 */
(function () {
  'use strict';

  function ready(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn, { once: true });
    } else {
      fn();
    }
  }

  ready(function () {
    var root = document.documentElement;

    /* ---------------- navigation disclosure ---------------- */
    var navToggle = document.getElementById('navToggle');
    var navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
      var setNav = function (open) {
        navToggle.setAttribute('aria-expanded', String(open));
        navMenu.setAttribute('data-open', String(open));
      };

      setNav(false);

      navToggle.addEventListener('click', function () {
        setNav(navToggle.getAttribute('aria-expanded') !== 'true');
      });

      /* Escape closes the menu and returns focus to the control that
         opened it, so keyboard users are never stranded inside it. */
      navMenu.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
          setNav(false);
          navToggle.focus();
        }
      });

      document.addEventListener('click', function (event) {
        if (
          navToggle.getAttribute('aria-expanded') === 'true' &&
          !navMenu.contains(event.target) &&
          !navToggle.contains(event.target)
        ) {
          setNav(false);
        }
      });

      /* Re-opening the desktop layout must not leave the menu in the
         collapsed state the small-screen rules depend on. */
      var wide = window.matchMedia('(min-width: 48rem)');
      var syncWidth = function (mq) {
        if (mq.matches) {
          setNav(false);
        }
      };
      if (typeof wide.addEventListener === 'function') {
        wide.addEventListener('change', syncWidth);
      }
    }

    /* ---------------- search trigger, into the header ---------------- */

    /* The generator appends its search trigger near the end of the body and
       fixes it to the viewport, so it renders at the top right of the header
       while sitting last in the document. Visually it is the fifth thing on the
       page; by keyboard it was tab stop 374 of 400, which means reaching the
       search on a 2,861-page site required tabbing through an entire page
       first. WCAG 2.4.3 asks focus order to preserve meaning and operability,
       and no automated checker can see this one — focus order is not decidable
       from markup alone, so axe passes it.

       Moving the node keeps its listeners, and the generator's script binds by
       id afterwards, so it finds the trigger wherever it now lives. Nothing
       moves on screen either: the trigger is out of flow in both places. */
    var searchTrigger = document.getElementById('ssg-search-btn');
    var themeToggleForSearch = document.getElementById('themeToggle');

    if (searchTrigger && themeToggleForSearch && themeToggleForSearch.parentNode) {
      themeToggleForSearch.parentNode.insertBefore(
        searchTrigger, themeToggleForSearch.nextSibling);
    }

    /* ---------------- search shortcut hint ---------------- */

    /* The generator ships the trigger labelled `<kbd>K</kbd>`, and its own
       handler opens the overlay on Cmd+K or Ctrl+K. Pressing K on its own does
       nothing, so the badge names a shortcut that does not exist — and the badge
       is the only place the shortcut is advertised.

       Corrected here rather than in the markup because there is no one right
       static answer: Cmd on a Mac, Ctrl everywhere else. It also cannot be got
       wrong in a way that matters, because a visitor without scripting has no
       search overlay for the shortcut to open.

       The trigger is positioned by the generator's stylesheet, which fixes it to
       the viewport, so the badge growing a character moves nothing on the page. */
    var shortcutHint = document.querySelector('#ssg-search-btn kbd');

    if (shortcutHint) {
      var platform = (navigator.userAgentData && navigator.userAgentData.platform) ||
        navigator.platform || '';
      var apple = /mac|iphone|ipad|ipod/i.test(platform);
      shortcutHint.textContent = apple ? '\u2318K' : 'Ctrl K';
    }

    /* ---------------- theme toggle ---------------- */
    var themeToggle = document.getElementById('themeToggle');

    if (themeToggle) {
      var prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

      var currentTheme = function () {
        return (
          root.getAttribute('data-theme') ||
          (prefersDark.matches ? 'dark' : 'light')
        );
      };

      /* The visible icon is chosen by CSS from [data-theme]; the only
         state this needs to publish is `aria-pressed`. */
      var syncPressed = function () {
        themeToggle.setAttribute(
          'aria-pressed',
          String(currentTheme() === 'dark')
        );
      };

      syncPressed();

      themeToggle.addEventListener('click', function () {
        var next = currentTheme() === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        try {
          localStorage.setItem('theme', next);
        } catch (e) {
          /* Storage unavailable: the choice applies for this page only. */
        }
        syncPressed();
      });

      /* Track the OS while the visitor has not made an explicit choice. */
      if (typeof prefersDark.addEventListener === 'function') {
        prefersDark.addEventListener('change', function () {
          if (!root.hasAttribute('data-theme')) {
            syncPressed();
          }
        });
      }
    }
  });
})();
