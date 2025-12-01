// Load and display blog posts

document.addEventListener('DOMContentLoaded', async function() {
    await loadBlogPosts();
    setupFilters();
});

let allPosts = [];

async function loadBlogPosts() {
    const container = document.getElementById('blog-container');
    if (!container) return;
    
    try {
        const response = await fetch('data/blog.json');
        allPosts = await response.json();
        
        renderPosts(allPosts);
    } catch (error) {
        console.error('Error loading blog posts:', error);
        container.innerHTML = '<p>No blog posts available yet.</p>';
    }
}

function renderPosts(posts) {
    const container = document.getElementById('blog-container');
    if (!container) return;

    if (posts.length === 0) {
        container.innerHTML = '<p>No blog posts found.</p>';
        return;
    }
    
    const postsHTML = posts.map(post => `
        <div class="blog-card">
            ${post.image ? `<img src="${post.image}" alt="${post.title}" class="blog-card-image">` : ''}
            <div class="blog-card-content">
                <span class="blog-category">${post.category || 'General'}</span>
                <h3>${post.title}</h3>
                <p class="blog-date">${post.date}</p>
                <p class="blog-excerpt">${post.excerpt}</p>
                <a href="blog/${post.slug}.html" class="read-more">Read more →</a>
            </div>
        </div>
    `).join('');
    
    container.innerHTML = postsHTML;
}

function setupFilters() {
    const buttons = document.querySelectorAll('.filter-btn');
    
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update active state
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Filter posts
            const filter = btn.getAttribute('data-filter');
            if (filter === 'all') {
                renderPosts(allPosts);
            } else {
                const filtered = allPosts.filter(post => post.category === filter);
                renderPosts(filtered);
            }
        });
    });
}
