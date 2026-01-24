/**
 * Accessibility Enhancements
 * Keyboard navigation, ARIA live regions, reduced motion support
 */

(function() {
  'use strict';

  // Keyboard navigation detection
  function handleFirstTab(e) {
    if (e.key === 'Tab') {
      document.body.classList.add('user-is-tabbing');
      window.removeEventListener('keydown', handleFirstTab);
      window.addEventListener('mousedown', handleMouseDownOnce);
    }
  }

  function handleMouseDownOnce() {
    document.body.classList.remove('user-is-tabbing');
    window.removeEventListener('mousedown', handleMouseDownOnce);
    window.addEventListener('keydown', handleFirstTab);
  }

  window.addEventListener('keydown', handleFirstTab);

  // ARIA live region for announcements
  const ariaLiveRegion = document.createElement('div');
  ariaLiveRegion.className = 'aria-live-region';
  ariaLiveRegion.setAttribute('aria-live', 'polite');
  ariaLiveRegion.setAttribute('aria-atomic', 'true');
  ariaLiveRegion.setAttribute('role', 'status');
  document.body.appendChild(ariaLiveRegion);

  window.announceToScreenReader = function(message, priority = 'polite') {
    ariaLiveRegion.setAttribute('aria-live', priority);
    ariaLiveRegion.textContent = message;
    setTimeout(() => { ariaLiveRegion.textContent = ''; }, 1000);
  };

  // Reduced motion support
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  
  function handleReducedMotionChange() {
    if (prefersReducedMotion.matches) {
      document.documentElement.classList.add('reduce-motion');
    } else {
      document.documentElement.classList.remove('reduce-motion');
    }
  }

  prefersReducedMotion.addEventListener('change', handleReducedMotionChange);
  handleReducedMotionChange();

  // Touch device detection
  if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
    document.documentElement.classList.add('touch-device');
  }

  // Escape key handler
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      const openModals = document.querySelectorAll('.modal.show');
      openModals.forEach(modal => {
        const closeBtn = modal.querySelector('.modal-close');
        if (closeBtn) closeBtn.click();
      });
    }
  });

  console.log('✅ Accessibility enhancements loaded');
})();
