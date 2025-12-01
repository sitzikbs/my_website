// Load and display publications

document.addEventListener('DOMContentLoaded', async function() {
    await loadPublications();
});

async function loadPublications() {
    const container = document.getElementById('publications-container');
    if (!container) return;
    
    try {
        const response = await fetch('data/publications.json');
        const publications = await response.json();
        
        if (publications.length === 0) {
            container.innerHTML = '<p>No publications available yet.</p>';
            return;
        }
        
        const pubsHTML = publications.map(pub => `
            <div class="publication-item">
                <h3>${pub.title}</h3>
                <p class="publication-authors">${pub.authors}</p>
                <p class="publication-venue">${pub.venue}</p>
                <p class="publication-year">${pub.year}</p>
                ${pub.abstract ? `<p style="margin-top: 1rem;">${pub.abstract}</p>` : ''}
                ${pub.links ? `
                    <div class="publication-links">
                        ${pub.links.paper ? `<a href="${pub.links.paper}" target="_blank">Paper</a>` : ''}
                        ${pub.links.code ? `<a href="${pub.links.code}" target="_blank">Code</a>` : ''}
                        ${pub.links.project ? `<a href="${pub.links.project}" target="_blank">Project</a>` : ''}
                        ${pub.links.video ? `<a href="${pub.links.video}" target="_blank">Video</a>` : ''}
                        ${pub.links.slides ? `<a href="${pub.links.slides}" target="_blank">Slides</a>` : ''}
                    </div>
                ` : ''}
            </div>
        `).join('');
        
        container.innerHTML = pubsHTML;
    } catch (error) {
        console.error('Error loading publications:', error);
        container.innerHTML = '<p>Error loading publications. Please check back later.</p>';
    }
}
