// Load and display publications

document.addEventListener('DOMContentLoaded', async function() {
    await loadPublications();
    setupSearch();
});

let allPublications = [];

async function loadPublications() {
    const container = document.getElementById('publications-container');
    if (!container) return;
    
    try {
        const response = await fetch('data/publications.json');
        allPublications = await response.json();
        
        renderPublications(allPublications);
    } catch (error) {
        console.error('Error loading publications:', error);
        container.innerHTML = '<p>Error loading publications. Please check back later.</p>';
    }
}

function renderPublications(publications) {
    const container = document.getElementById('publications-container');
    if (!container) return;

    if (publications.length === 0) {
        container.innerHTML = '<p>No publications found.</p>';
        return;
    }

    // Sort by year (descending)
    publications.sort((a, b) => parseInt(b.year) - parseInt(a.year));

    // Group by year
    const pubsByYear = {};
    publications.forEach(pub => {
        if (!pubsByYear[pub.year]) {
            pubsByYear[pub.year] = [];
        }
        pubsByYear[pub.year].push(pub);
    });

    let html = '';
    const years = Object.keys(pubsByYear).sort((a, b) => b - a);

    years.forEach(year => {
        html += `<h2 class="year-heading" style="color: var(--primary-color); margin: 2rem 0 1rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">${year}</h2>`;
        
        html += pubsByYear[year].map((pub, index) => `
            <div class="publication-item" style="display: flex; gap: 20px; margin-bottom: 2rem; align-items: start;">
                ${pub.image ? `
                    <div class="publication-image" style="flex: 0 0 200px;">
                        <img src="${pub.image}" alt="${pub.title}" style="width: 100%; height: auto; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    </div>
                ` : ''}
                <div class="publication-content" style="flex: 1;">
                    <h3 style="margin-top: 0;">${pub.title}</h3>
                    <p class="publication-authors" style="font-style: italic; margin-bottom: 0.5rem;">${pub.authors}</p>
                    <p class="publication-venue" style="font-weight: bold; margin-bottom: 0.5rem;">${pub.venue}</p>
                    ${pub.abstract ? `<p class="publication-abstract" style="margin-top: 1rem;">${pub.abstract}</p>` : ''}
                    
                    <div class="publication-links" style="margin-top: 1rem;">
                        ${pub.links ? pub.links.map(link => 
                            `<a href="${link.url}" target="_blank" class="btn-link" style="display: inline-block; margin-right: 10px; padding: 4px 8px; background: var(--bg-light); border: 1px solid var(--border-color); border-radius: 4px; text-decoration: none; font-size: 0.9rem;">${link.name}</a>`
                        ).join('') : ''}
                        ${pub.bibtex ? `<button class="btn-bibtex" onclick="toggleBibtex(this)" style="background: none; border: 1px solid var(--border-color); padding: 0.4rem 0.8rem; border-radius: 4px; cursor: pointer; font-size: 0.85rem; color: var(--text-color);">BibTeX</button>` : ''}
                    </div>
                    
                    ${pub.bibtex ? `
                        <div class="bibtex-container" style="display: none; margin-top: 1rem; background: var(--bg-light); padding: 1rem; border-radius: 4px; overflow-x: auto;">
                            <pre style="margin: 0; font-size: 0.85rem;"><code>${pub.bibtex}</code></pre>
                        </div>
                    ` : ''}
                </div>
            </div>
        `).join('');
    });
    
    container.innerHTML = html;
}

function setupSearch() {
    const searchInput = document.getElementById('pub-filter');
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        
        const filtered = allPublications.filter(pub => 
            pub.title.toLowerCase().includes(searchTerm) || 
            pub.authors.toLowerCase().includes(searchTerm) ||
            pub.venue.toLowerCase().includes(searchTerm)
        );
        
        renderPublications(filtered);
    });
}

// Make toggle function global so it can be called from HTML
window.toggleBibtex = function(btn) {
    const container = btn.parentElement.nextElementSibling;
    if (container && container.classList.contains('bibtex-container')) {
        const isHidden = container.style.display === 'none';
        container.style.display = isHidden ? 'block' : 'none';
        btn.style.backgroundColor = isHidden ? 'var(--bg-light)' : 'transparent';
    }
};
