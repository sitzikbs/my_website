/**
 * Google Analytics 4 Configuration
 * Centralized analytics tracking for the website
 */

(function() {
  'use strict';
  
  // GA4 Measurement ID
  const GA4_MEASUREMENT_ID = 'G-0EC0BTHZ23';
  
  // Initialize dataLayer and gtag function
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }
  
  // Configure GA4
  gtag('js', new Date());
  gtag('config', GA4_MEASUREMENT_ID, {
    anonymize_ip: true,
    cookie_flags: 'SameSite=None;Secure',
    allow_google_signals: false,
    allow_ad_personalization_signals: false
  });
  
  // Make gtag available globally
  window.gtag = gtag;
})();
