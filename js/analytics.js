/**
 * Google Analytics 4 Configuration
 * Centralized analytics tracking for the website
 */

(function() {
  'use strict';
  
  // GA4 Measurement ID
  const GA4_MEASUREMENT_ID = 'G-0EC0BTHZ23';
  
  // Load Google Analytics script
  const script = document.createElement('script');
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${GA4_MEASUREMENT_ID}`;
  document.head.appendChild(script);
  
  // Initialize dataLayer FIRST
  window.dataLayer = window.dataLayer || [];
  
  // Create gtag function that references window.dataLayer
  window.gtag = function() {
    window.dataLayer.push(arguments);
  };
  
  // Configure GA4
  window.gtag('js', new Date());
  window.gtag('config', GA4_MEASUREMENT_ID, {
    anonymize_ip: true,
    cookie_flags: 'SameSite=None;Secure'
  });
})();
