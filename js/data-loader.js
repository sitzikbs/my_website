// Load and display data on homepage

document.addEventListener('DOMContentLoaded', async function() {
    await loadNews();
    await loadRecentBlogPosts();
    await loadRecentPodcastEpisodes();
    await loadRecentPublications();
});

async function loadNews() {
    const newsContainer = document.getElementById('news-list');
    if (!newsContainer) return;
    
    try {
        const response = await fetch('data/news.json');
        const news = await response.json();
        
        if (news.length === 0) {
            newsContainer.innerHTML = '<li>No recent news available.</li>';
            return;
        }
        
        const newsHTML = news.slice(0, 5).map(item => `
            <li>
                <span class="news-date">${item.date}</span>
                <span>${item.content}</span>
            </li>
        `).join('');
        
        newsContainer.innerHTML = newsHTML;
    } catch (error) {
        console.log('News data not found, using default');
        newsContainer.innerHTML = `
            <li>
                <span class="news-date">Nov 2024</span>
                <span>Website launched with new design</span>
            </li>
        `;
    }
}

async function loadRecentPublications() {
    const container = document.getElementById('recent-publications');
    if (!container) {
        console.error('Publications container not found!');
        return;
    }
    
    console.log('Loading publications...');
    
    try {
        const response = await fetch('data/publications.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const publications = await response.json();
        
        console.log('Publications loaded:', publications.length);
        
        if (publications.length === 0) {
            container.innerHTML = '<p>No publications available yet.</p>';
            return;
        }
        
        const recentPubs = publications.slice(0, 3);
        const pubsHTML = recentPubs.map(pub => `
            <div class="publication-item">
                <h3>${pub.title}</h3>
                <p class="publication-authors">${pub.authors}</p>
                <p class="publication-venue">${pub.venue}</p>
                <p class="publication-year">${pub.year}</p>
                ${pub.links ? `
                    <div class="publication-links">
                        ${pub.links.map(link => `<a href="${link.url}" target="_blank">${link.name}</a>`).join('')}
                    </div>
                ` : ''}
            </div>
        `).join('');
        
        container.innerHTML = pubsHTML;
        console.log('Publications rendered successfully');
    } catch (error) {
        console.error('Publications data error:', error);
        container.innerHTML = '<p>No publications available yet.</p>';
    }
}

async function loadRecentBlogPosts() {
    const container = document.getElementById('recent-blog-posts');
    if (!container) {
        console.error('Blog posts container not found!');
        return;
    }
    
    console.log('Loading blog posts...');
    
    try {
        const response = await fetch('data/blog-index.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        const posts = data.posts || [];
        
        console.log('Blog posts loaded:', posts.length);
        
        // Filter for Research category only, or take all if none
        let recentPosts = posts.filter(post => post.categories && post.categories.includes('Research'));
        if (recentPosts.length === 0) {
            recentPosts = posts;
        }
        
        console.log('Filtered posts:', recentPosts.length);
        
        if (recentPosts.length === 0) {
            container.innerHTML = '<p>No blog posts available yet.</p>';
            return;
        }
        
        recentPosts = recentPosts.slice(0, 3);
        const postsHTML = recentPosts.map(post => `
            <a href="${post.content.replace(/^\//, '')}" class="blog-card">
                ${post.image ? `<img src="${post.image}" alt="${post.title}" class="blog-card-image">` : ''}
                <div class="blog-card-content">
                    <span class="blog-category">${(post.categories && post.categories.length > 0) ? post.categories[0] : 'General'}</span>
                    <h3>${post.title}</h3>
                    <p class="blog-date">${post.date}</p>
                    <p class="blog-excerpt">${post.excerpt || ''}</p>
                    <span class="read-more">Read more →</span>
                </div>
            </a>
        `).join('');
        
        container.innerHTML = postsHTML;
        console.log('Blog posts rendered successfully');
    } catch (error) {
        console.error('Blog data error:', error);
        container.innerHTML = '<p>No blog posts available yet.</p>';
    }
}

async function loadRecentPodcastEpisodes() {
    const container = document.getElementById('recent-podcast-episodes');
    if (!container) {
        console.error('Podcast episodes container not found!');
        return;
    }
    
    console.log('Loading podcast episodes...');
    
    try {
        const response = await fetch('data/blog-index.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        const posts = data.posts || [];
        
        console.log('Podcast data loaded, filtering for podcast episodes');
        
        // Filter for Talking Papers Podcast category only
        let podcastEpisodes = posts.filter(post => 
            post.categories && post.categories.includes('Talking Papers Podcast')
        );
        
        console.log('Filtered podcast episodes:', podcastEpisodes.length);
        
        if (podcastEpisodes.length === 0) {
            container.innerHTML = '<p>No podcast episodes available yet.</p>';
            return;
        }
        
        podcastEpisodes = podcastEpisodes.slice(0, 3);
        const episodesHTML = podcastEpisodes.map(post => `
            <a href="${post.content.replace(/^\//, '')}" class="blog-card">
                ${post.image ? `<img src="${post.image}" alt="${post.title}" class="blog-card-image">` : ''}
                <div class="blog-card-content">
                    <span class="blog-category">Podcast</span>
                    <h3>${post.title}</h3>
                    <p class="blog-date">${post.date}</p>
                    <p class="blog-excerpt">${post.excerpt || ''}</p>
                    <span class="read-more">Listen now →</span>
                </div>
            </a>
        `).join('');
        
        container.innerHTML = episodesHTML;
        console.log('Podcast episodes rendered successfully');
    } catch (error) {
        console.error('Podcast data error:', error);
        container.innerHTML = '<p>No podcast episodes available yet.</p>';
    }
}
