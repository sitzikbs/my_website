// Load and display blog posts

document.addEventListener('DOMContentLoaded', async function() {
    await loadBlogPosts();
});

async function loadBlogPosts() {
    const container = document.getElementById('blog-container');
    if (!container) return;
    
    try {
        const response = await fetch('data/blog.json');
        const posts = await response.json();
        
        if (posts.length === 0) {
            container.innerHTML = '<p>No blog posts available yet.</p>';
            return;
        }
        
        const postsHTML = posts.map(post => `
            <div class="blog-card">
                ${post.image ? `<img src="${post.image}" alt="${post.title}" class="blog-card-image">` : ''}
                <div class="blog-card-content">
                    <h3>${post.title}</h3>
                    <p class="blog-date">${post.date}</p>
                    <p class="blog-excerpt">${post.excerpt}</p>
                    <a href="blog/${post.slug}.html" class="read-more">Read more →</a>
                </div>
            </div>
        `).join('');
        
        container.innerHTML = postsHTML;
    } catch (error) {
        console.error('Error loading blog posts:', error);
        container.innerHTML = '<p>No blog posts available yet.</p>';
    }
}
