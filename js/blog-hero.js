/**
 * Blog Hero Header - Dynamically loaded component
 * Centralizes hero header configuration in one place
 */

const BLOG_HERO_CONFIG = {
  authorName: 'Itzik Ben-Shabat',
  authorPortrait: '/assets/images/profile/Itzik_Ben_Shabat_portrait.jpg',
  podcastLogo: '/assets/images/icons/talking-papers-logo.webp',
  homeUrl: '/index.html'
};

/**
 * Get blog post metadata from the page
 */
function getBlogMetadata() {
  // Try to get from meta tags
  const titleEl = document.querySelector('h1');
  const dateEl = document.querySelector('time[datetime]');
  const categoryEl = document.querySelector('meta[property="article:section"]');
  
  return {
    title: titleEl?.textContent || document.title,
    date: dateEl?.getAttribute('datetime') || '',
    dateFormatted: dateEl?.textContent || '',
    category: categoryEl?.getAttribute('content') || ''
  };
}

/**
 * Check if this is a Talking Papers episode
 */
function isTalkingPapers() {
  // Check if "Talking Papers" appears in the title or content
  const title = document.title.toLowerCase();
  const h1 = document.querySelector('h1')?.textContent.toLowerCase() || '';
  
  return title.includes('talking papers') || h1.includes('talking papers');
}

/**
 * Create and inject the blog hero header
 */
function createBlogHero() {
  const metadata = getBlogMetadata();
  const isPodcast = isTalkingPapers();
  
  const avatarSrc = isPodcast ? BLOG_HERO_CONFIG.podcastLogo : BLOG_HERO_CONFIG.authorPortrait;
  const avatarAlt = isPodcast ? 'Talking Papers Podcast Logo' : BLOG_HERO_CONFIG.authorName;
  
  const heroHTML = `
    <div class="blog-hero">
      <div class="blog-hero-content">
        <img src="${avatarSrc}" alt="${avatarAlt}" class="blog-hero-avatar">
        <div class="blog-hero-byline">
          <a href="${BLOG_HERO_CONFIG.homeUrl}" class="blog-hero-author">${BLOG_HERO_CONFIG.authorName}</a>
          <time class="blog-hero-date" datetime="${metadata.date}">${metadata.dateFormatted}</time>
        </div>
        <h1 class="blog-hero-title">${metadata.title}</h1>
      </div>
    </div>
  `;
  
  // Find the article element and prepend the hero
  const article = document.querySelector('article.blog-post');
  if (article) {
    article.insertAdjacentHTML('afterbegin', heroHTML);
  }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', createBlogHero);
} else {
  createBlogHero();
}
