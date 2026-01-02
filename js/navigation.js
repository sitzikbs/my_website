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
        navToggle.addEventListener('click', (event) => {
            event.stopPropagation();
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (navMenu.classList.contains('active')) {
                const isClickInsideNav = navToggle.contains(event.target) || navMenu.contains(event.target);
                if (!isClickInsideNav) {
                    navToggle.classList.remove('active');
                    navMenu.classList.remove('active');
                }
            }
        });
    }
}

// Initialize navigation when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initNavigation);
} else {
    initNavigation();
}
