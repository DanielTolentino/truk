// Acessibilidade - Dropdown Menu
document.addEventListener('DOMContentLoaded', function() {
    const dropdownButton = document.querySelector('.user-menu');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    
    if (dropdownButton && dropdownMenu) {
        // Toggle dropdown com click
        dropdownButton.addEventListener('click', function(e) {
            e.preventDefault();
            const isExpanded = dropdownButton.getAttribute('aria-expanded') === 'true';
            dropdownButton.setAttribute('aria-expanded', !isExpanded);
            dropdownMenu.style.display = !isExpanded ? 'block' : 'none';
        });
        
        // Toggle dropdown com Enter ou Space
        dropdownButton.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const isExpanded = dropdownButton.getAttribute('aria-expanded') === 'true';
                dropdownButton.setAttribute('aria-expanded', !isExpanded);
                dropdownMenu.style.display = !isExpanded ? 'block' : 'none';
                
                // Foca no primeiro item do menu quando abre
                if (!isExpanded) {
                    const firstMenuItem = dropdownMenu.querySelector('a');
                    if (firstMenuItem) {
                        setTimeout(() => firstMenuItem.focus(), 100);
                    }
                }
            }
            
            // Escape fecha o dropdown
            if (e.key === 'Escape') {
                dropdownButton.setAttribute('aria-expanded', 'false');
                dropdownMenu.style.display = 'none';
                dropdownButton.focus();
            }
        });
        
        // Navegação com setas dentro do menu
        const menuItems = dropdownMenu.querySelectorAll('a');
        menuItems.forEach((item, index) => {
            item.addEventListener('keydown', function(e) {
                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    const nextItem = menuItems[index + 1] || menuItems[0];
                    nextItem.focus();
                }
                
                if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    const prevItem = menuItems[index - 1] || menuItems[menuItems.length - 1];
                    prevItem.focus();
                }
                
                if (e.key === 'Escape') {
                    dropdownButton.setAttribute('aria-expanded', 'false');
                    dropdownMenu.style.display = 'none';
                    dropdownButton.focus();
                }
            });
        });
        
        // Fecha dropdown ao clicar fora
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.dropdown')) {
                dropdownButton.setAttribute('aria-expanded', 'false');
                dropdownMenu.style.display = 'none';
            }
        });
    }
});
