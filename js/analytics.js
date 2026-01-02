/**
 * Google Analytics 4 Configuration
 * Centralized analytics tracking for the website
 */

// GA4 Measurement ID
const GA4_MEASUREMENT_ID = 'G-0EC0BTHZ23';

// Initialize dataLayer FIRST (before any scripts)
window.dataLayer = window.dataLayer || [];

// Create gtag function
function gtag() {
  dataLayer.push(arguments);
}

// Set up initial config
gtag('js', new Date());
gtag('config', GA4_MEASUREMENT_ID, {
  anonymize_ip: true,
  cookie_flags: 'SameSite=None;Secure'
});
