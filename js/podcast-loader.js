// Load and display podcast episodes

document.addEventListener('DOMContentLoaded', async function() {
    await loadPodcastEpisodes();
});

async function loadPodcastEpisodes() {
    const container = document.getElementById('podcast-container');
    if (!container) return;
    
    try {
        const response = await fetch('data/blog-index.json');
        const data = await response.json();
        
        // Filter for Talking Papers Podcast category
        const podcastEpisodes = (data.posts || []).filter(post => 
            post.categories && post.categories.includes('Talking Papers Podcast')
        );
        
        renderPodcastEpisodes(podcastEpisodes);
    } catch (error) {
        console.error('Error loading podcast episodes:', error);
        container.innerHTML = '<p>No podcast episodes available yet.</p>';
    }
}

function renderPodcastEpisodes(episodes) {
    const container = document.getElementById('podcast-container');
    if (!container) return;

    if (episodes.length === 0) {
        container.innerHTML = '<p>No podcast episodes found.</p>';
        return;
    }
    
    const episodesHTML = episodes.map(episode => `
        <a href="${episode.content.replace(/^\//, '')}" class="blog-card">
            ${episode.image ? `<img src="${episode.image}" alt="${episode.title}" class="blog-card-image">` : ''}
            <div class="blog-card-content">
                <span class="blog-category"><i class="fas fa-microphone"></i> Podcast</span>
                <h3>${episode.title}</h3>
                <p class="blog-date">${episode.date}</p>
                <p class="blog-excerpt">${episode.excerpt || ''}</p>
                <span class="read-more">Listen →</span>
            </div>
        </a>
    `).join('');
    
    container.innerHTML = episodesHTML;
}
