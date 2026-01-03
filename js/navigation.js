// Navigation component - dynamically loaded on all pages
function initNavigation() {
    const navContainer = document.getElementById('main-nav');
    if (!navContainer) return;

    // Determine which page is active based on current URL
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    
    const navHTML = `
        <nav class="navbar">
            <div class="container">
                <div class="nav-brand">
                    <a href="index.html">Itzik Ben-Shabat</a>
                </div>
                <button class="nav-toggle" aria-label="Toggle navigation">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <ul class="nav-menu">
                    <li><a href="index.html" class="${currentPage === 'index.html' || currentPage === '' ? 'active' : ''}">Home</a></li>
                    <li><a href="about.html" class="${currentPage === 'about.html' ? 'active' : ''}">About</a></li>
                    <li><a href="publications.html" class="${currentPage === 'publications.html' ? 'active' : ''}">Publications</a></li>
                    <li><a href="podcast.html" class="${currentPage === 'podcast.html' ? 'active' : ''}">Podcast</a></li>
                    <li><a href="blog.html" class="${currentPage === 'blog.html' ? 'active' : ''}">Blog</a></li>
                    <li><a href="code.html" class="${currentPage === 'code.html' ? 'active' : ''}">Code</a></li>
                    <li><a href="contact.html" class="${currentPage === 'contact.html' ? 'active' : ''}">Contact</a></li>
                </ul>
            </div>
        </nav>
    `;
    
    navContainer.innerHTML = navHTML;
    
    // Re-initialize mobile menu toggle after navigation is loaded
    initMobileMenu();
}

function initMobileMenu() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle && navMenu) {
        // Toggle menu on click
        navToggle.addEventListener('click', (event) => {
            event.stopPropagation();
            const isExpanded = navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
            
            // Update ARIA attributes for accessibility
            navToggle.setAttribute('aria-expanded', isExpanded);
        });
        
        // Close menu with Escape key
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' && navMenu.classList.contains('active')) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
                navToggle.focus(); // Return focus to toggle button
            }
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (navMenu.classList.contains('active')) {
                const isClickInsideNav = navToggle.contains(event.target) || navMenu.contains(event.target);
                if (!isClickInsideNav) {
                    navToggle.classList.remove('active');
                    navMenu.classList.remove('active');
                    navToggle.setAttribute('aria-expanded', 'false');
                }
            }
        });
        
        // Set initial aria-expanded state
        navToggle.setAttribute('aria-expanded', 'false');
    }
}

// Initialize navigation when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initNavigation);
} else {
    initNavigation();
}
