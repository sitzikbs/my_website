/**
 * Email Obfuscation
 * Protects email addresses from bot scrapers while keeping them accessible to users
 */

(function() {
    'use strict';
    
    /**
     * Decodes an obfuscated email address
     * @param {string} encoded - Base64 encoded email
     * @returns {string} - Decoded email address
     */
    function decodeEmail(encoded) {
        try {
            return atob(encoded);
        } catch (e) {
            console.error('Failed to decode email');
            return '';
        }
    }
    
    /**
     * Creates a clickable mailto link from obfuscated data
     * @param {HTMLElement} element - The element containing data attributes
     */
    function revealEmail(element) {
        const encodedEmail = element.getAttribute('data-email');
        if (!encodedEmail) return;
        
        const email = decodeEmail(encodedEmail);
        if (!email) return;
        
        // Validate email format
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            console.error('Invalid email format');
            return;
        }
        
        // Create mailto link
        const link = document.createElement('a');
        link.href = 'mailto:' + email;
        link.textContent = email;
        link.className = element.className;
        
        // Add aria-label for accessibility
        link.setAttribute('aria-label', 'Send email to ' + email);
        
        // Replace the placeholder
        element.parentNode.replaceChild(link, element);
    }
    
    /**
     * Reveals email as plain text (for non-link contexts)
     * @param {HTMLElement} element - The element containing data attributes
     */
    function revealEmailText(element) {
        const encodedEmail = element.getAttribute('data-email');
        if (!encodedEmail) return;
        
        const email = decodeEmail(encodedEmail);
        if (!email) return;
        
        // Validate email format
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            console.error('Invalid email format');
            return;
        }
        
        // Replace with plain text
        element.textContent = email;
    }
    
    /**
     * Initialize email obfuscation on page load
     */
    function init() {
        // Reveal email links
        const emailLinks = document.querySelectorAll('[data-email][data-reveal="link"]');
        emailLinks.forEach(revealEmail);
        
        // Reveal email text
        const emailTexts = document.querySelectorAll('[data-email][data-reveal="text"]');
        emailTexts.forEach(revealEmailText);
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Export for manual use if needed
    window.EmailObfuscation = {
        decodeEmail: decodeEmail,
        revealEmail: revealEmail,
        revealEmailText: revealEmailText
    };
})();
