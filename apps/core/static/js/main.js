// Dark Mode Toggle
document.addEventListener('DOMContentLoaded', () => {
    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    // Create theme toggle button if not exists
    if (!document.querySelector('.theme-toggle')) {
        const themeToggle = document.createElement('button');
        themeToggle.className = 'theme-toggle';
        themeToggle.setAttribute('aria-label', 'Toggle dark mode');
        themeToggle.innerHTML = currentTheme === 'dark' ? '☀️' : '🌙';
        document.body.appendChild(themeToggle);
        
        themeToggle.addEventListener('click', () => {
            const theme = document.documentElement.getAttribute('data-theme');
            const newTheme = theme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            themeToggle.innerHTML = newTheme === 'dark' ? '☀️' : '🌙';
            
            // Animate the transition
            document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
        });
    }
});

// Dropdown Menu
document.addEventListener('DOMContentLoaded', () => {
    const dropdowns = document.querySelectorAll('.dropdown');
    
    dropdowns.forEach(dropdown => {
        const button = dropdown.querySelector('.user-menu');
        const menu = dropdown.querySelector('.dropdown-menu');
        
        if (button && menu) {
            button.addEventListener('click', (e) => {
                e.stopPropagation();
                dropdown.classList.toggle('active');
                const isExpanded = dropdown.classList.contains('active');
                button.setAttribute('aria-expanded', isExpanded);
            });
            
            // Close dropdown when clicking outside
            document.addEventListener('click', (e) => {
                if (!dropdown.contains(e.target)) {
                    dropdown.classList.remove('active');
                    button.setAttribute('aria-expanded', 'false');
                }
            });
            
            // Close dropdown on Escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && dropdown.classList.contains('active')) {
                    dropdown.classList.remove('active');
                    button.setAttribute('aria-expanded', 'false');
                    button.focus();
                }
            });
        }
    });
});

// Form Validation with Visual Feedback
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        
        inputs.forEach(input => {
            // Add real-time validation
            input.addEventListener('blur', () => {
                validateField(input);
            });
            
            input.addEventListener('input', () => {
                if (input.classList.contains('invalid')) {
                    validateField(input);
                }
            });
        });
        
        form.addEventListener('submit', (e) => {
            let isValid = true;
            
            inputs.forEach(input => {
                if (!validateField(input)) {
                    isValid = false;
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                const firstInvalid = form.querySelector('.invalid');
                if (firstInvalid) {
                    firstInvalid.focus();
                    firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        });
    });
});

function validateField(field) {
    const value = field.value.trim();
    const isRequired = field.hasAttribute('required');
    let isValid = true;
    
    // Remove previous error
    removeFieldError(field);
    
    // Required field validation
    if (isRequired && !value) {
        showFieldError(field, 'Este campo é obrigatório');
        isValid = false;
    }
    
    // Email validation
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            showFieldError(field, 'Email inválido');
            isValid = false;
        }
    }
    
    // Number validation
    if (field.type === 'number' && value) {
        const min = field.getAttribute('min');
        const max = field.getAttribute('max');
        const numValue = parseFloat(value);
        
        if (min && numValue < parseFloat(min)) {
            showFieldError(field, `Valor mínimo: ${min}`);
            isValid = false;
        }
        
        if (max && numValue > parseFloat(max)) {
            showFieldError(field, `Valor máximo: ${max}`);
            isValid = false;
        }
    }
    
    return isValid;
}

function showFieldError(field, message) {
    field.classList.add('invalid');
    field.style.borderColor = 'var(--color-error)';
    
    const error = document.createElement('span');
    error.className = 'field-error';
    error.textContent = message;
    error.style.color = 'var(--color-error)';
    error.style.fontSize = 'var(--font-size-sm)';
    error.style.marginTop = 'var(--spacing-1)';
    error.style.display = 'block';
    
    field.parentElement.appendChild(error);
}

function removeFieldError(field) {
    field.classList.remove('invalid');
    field.style.borderColor = '';
    
    const error = field.parentElement.querySelector('.field-error');
    if (error) {
        error.remove();
    }
}

// Smooth scroll for anchor links
document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    
                    // Update focus for accessibility
                    target.setAttribute('tabindex', '-1');
                    target.focus();
                }
            }
        });
    });
});

// Auto-hide alerts after 5 seconds
document.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'all 0.3s ease-out';
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-20px)';
            
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });
});

// Add loading state to buttons on form submit
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', () => {
            const submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.style.opacity = '0.6';
                submitBtn.style.cursor = 'not-allowed';
                
                const originalText = submitBtn.textContent;
                submitBtn.textContent = 'Carregando...';
                
                // Reset after 10 seconds as fallback
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.style.opacity = '';
                    submitBtn.style.cursor = '';
                    submitBtn.textContent = originalText;
                }, 10000);
            }
        });
    });
});

// Animate cards on scroll
const observeCards = () => {
    const cards = document.querySelectorAll('.card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    entry.target.style.transition = 'all 0.5s ease-out';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    cards.forEach(card => observer.observe(card));
};

document.addEventListener('DOMContentLoaded', observeCards);

// Table row click to navigate
document.addEventListener('DOMContentLoaded', () => {
    const tableRows = document.querySelectorAll('.table tbody tr[data-href]');
    
    tableRows.forEach(row => {
        row.style.cursor = 'pointer';
        
        row.addEventListener('click', (e) => {
            // Don't navigate if clicking on a button or link
            if (e.target.tagName !== 'BUTTON' && e.target.tagName !== 'A') {
                const href = row.getAttribute('data-href');
                if (href) {
                    window.location.href = href;
                }
            }
        });
        
        row.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const href = row.getAttribute('data-href');
                if (href) {
                    window.location.href = href;
                }
            }
        });
    });
});

// Copy to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copiado para a área de transferência!', 'success');
    }).catch(() => {
        showToast('Erro ao copiar', 'error');
    });
}

// Toast notifications
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type}`;
    toast.textContent = message;
    toast.style.position = 'fixed';
    toast.style.top = '20px';
    toast.style.right = '20px';
    toast.style.zIndex = '9999';
    toast.style.minWidth = '250px';
    toast.style.animation = 'slideDown 0.3s ease-out';
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.transition = 'all 0.3s ease-out';
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(400px)';
        
        setTimeout(() => {
            toast.remove();
        }, 300);
    }, 3000);
}

// Export functions for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        validateField,
        showFieldError,
        removeFieldError,
        copyToClipboard,
        showToast
    };
}
