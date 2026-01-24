// Sidebar Toggle
class Sidebar {
  constructor() {
    this.sidebar = document.querySelector('.sidebar');
    this.toggleBtn = document.getElementById('sidebar-toggle');
    this.init();
  }
  
  init() {
    if (this.toggleBtn) {
      this.toggleBtn.addEventListener('click', () => this.toggle());
    }
    
    // Auto-collapse on mobile
    if (window.innerWidth < 1024) {
      this.sidebar?.classList.add('collapsed');
    }
  }
  
  toggle() {
    this.sidebar?.classList.toggle('collapsed');
  }
}

// Initialize
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new Sidebar());
} else {
  new Sidebar();
}
