/**
 * Security Utilities
 * Functions for sanitizing user input and preventing XSS attacks
 */

// HTML entities map for escaping
const HTML_ENTITIES = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#x27;',
    '/': '&#x2F;'
};

/**
 * Escapes HTML special characters to prevent XSS attacks
 * @param {string} str - The string to escape
 * @returns {string} - The escaped string
 */
function escapeHtml(str) {
    if (typeof str !== 'string') return '';
    return str.replace(/[&<>"'\/]/g, (char) => HTML_ENTITIES[char]);
}

/**
 * Sanitizes a URL to prevent javascript: and data: URIs
 * @param {string} url - The URL to sanitize
 * @returns {string} - The sanitized URL or empty string if invalid
 */
function sanitizeUrl(url) {
    if (typeof url !== 'string') return '';
    
    const trimmed = url.trim().toLowerCase();
    
    // Block dangerous protocols
    if (trimmed.startsWith('javascript:') || 
        trimmed.startsWith('data:') || 
        trimmed.startsWith('vbscript:') ||
        trimmed.startsWith('file:')) {
        console.warn('Blocked potentially dangerous URL:', url);
        return '';
    }
    
    // Allow http, https, mailto, and relative URLs
    if (trimmed.startsWith('http://') || 
        trimmed.startsWith('https://') || 
        trimmed.startsWith('mailto:') ||
        trimmed.startsWith('/') ||
        trimmed.startsWith('./') ||
        trimmed.startsWith('../')) {
        return url;
    }
    
    // For relative URLs without protocol
    if (!trimmed.includes(':')) {
        return url;
    }
    
    console.warn('Blocked unknown protocol in URL:', url);
    return '';
}

/**
 * Validates and sanitizes data from JSON responses
 * @param {Object} data - The data object to validate
 * @param {Array<string>} requiredFields - Required field names
 * @returns {boolean} - True if valid, false otherwise
 */
function validateData(data, requiredFields = []) {
    if (!data || typeof data !== 'object') return false;
    
    for (const field of requiredFields) {
        if (!(field in data)) {
            console.warn(`Missing required field: ${field}`);
            return false;
        }
    }
    
    return true;
}

/**
 * Safely fetches JSON data with timeout and validation
 * @param {string} url - The URL to fetch from
 * @param {number} timeout - Timeout in milliseconds (default: 10000)
 * @returns {Promise<Object>} - The fetched and parsed JSON data
 */
async function safeFetch(url, timeout = 10000) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);
    
    try {
        const response = await fetch(url, {
            signal: controller.signal,
            headers: {
                'Accept': 'application/json'
            }
        });
        
        clearTimeout(timeoutId);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        clearTimeout(timeoutId);
        if (error.name === 'AbortError') {
            throw new Error('Request timeout');
        }
        throw error;
    }
}

// Export utilities for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        escapeHtml,
        sanitizeUrl,
        validateData,
        safeFetch
    };
} else {
    window.SecurityUtils = {
        escapeHtml,
        sanitizeUrl,
        validateData,
        safeFetch
    };
}
