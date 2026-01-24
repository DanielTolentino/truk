// Theme Toggle - Dark Mode System
class ThemeToggle {
  constructor() {
    this.theme = localStorage.getItem('theme') || 
                 (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    this.init();
  }
  
  init() {
    this.applyTheme(this.theme);
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.addEventListener('click', () => this.toggleTheme());
      this.updateButton();
    }
  }
  
  applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    this.theme = theme;
    localStorage.setItem('theme', theme);
    this.updateButton();
  }
  
  toggleTheme() {
    this.applyTheme(this.theme === 'light' ? 'dark' : 'light');
  }
  
  updateButton() {
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.innerHTML = this.theme === 'dark' ? '☀️' : '🌙';
      button.title = this.theme === 'dark' ? 'Tema Claro' : 'Tema Escuro';
    }
  }
}

// Initialize
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new ThemeToggle());
} else {
  new ThemeToggle();
}
