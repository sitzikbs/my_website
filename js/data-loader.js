// Load and display data on homepage

document.addEventListener('DOMContentLoaded', async function() {
    await loadNews();
    await loadRecentPublications();
    await loadRecentBlogPosts();
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
    if (!container) return;
    
    try {
        const response = await fetch('data/publications.json');
        const publications = await response.json();
        
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
                        ${pub.links.paper ? `<a href="${pub.links.paper}" target="_blank">Paper</a>` : ''}
                        ${pub.links.code ? `<a href="${pub.links.code}" target="_blank">Code</a>` : ''}
                        ${pub.links.project ? `<a href="${pub.links.project}" target="_blank">Project</a>` : ''}
                    </div>
                ` : ''}
            </div>
        `).join('');
        
        container.innerHTML = pubsHTML;
    } catch (error) {
        console.log('Publications data not found');
        container.innerHTML = '<p>No publications available yet.</p>';
    }
}

async function loadRecentBlogPosts() {
    const container = document.getElementById('recent-blog-posts');
    if (!container) return;
    
    try {
        const response = await fetch('data/blog.json');
        const posts = await response.json();
        
        // Filter for Research category only
        const researchPosts = posts.filter(post => post.category === 'Research');
        
        if (researchPosts.length === 0) {
            container.innerHTML = '<p>No research blog posts available yet.</p>';
            return;
        }
        
        const recentPosts = researchPosts.slice(0, 3);
        const postsHTML = recentPosts.map(post => `
            <div class="blog-card">
                ${post.image ? `<img src="${post.image}" alt="${post.title}" class="blog-card-image">` : ''}
                <div class="blog-card-content">
                    <span class="blog-category">${post.category}</span>
                    <h3>${post.title}</h3>
                    <p class="blog-date">${post.date}</p>
                    <p class="blog-excerpt">${post.excerpt}</p>
                    <a href="blog/${post.slug}.html" class="read-more">Read more →</a>
                </div>
            </div>
        `).join('');
        
        container.innerHTML = postsHTML;
    } catch (error) {
        console.log('Blog data not found');
        container.innerHTML = '<p>No blog posts available yet.</p>';
    }
}
