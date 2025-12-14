/**
 * Google Analytics 4 Configuration
 * Centralized analytics tracking for the website
 */

(function() {
  'use strict';
  
  // GA4 Measurement ID (from original WordPress site using MonsterInsights)
  const GA4_MEASUREMENT_ID = 'G-EJRL17R9NE';
  
  // Load Google Analytics script
  const script = document.createElement('script');
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${GA4_MEASUREMENT_ID}`;
  document.head.appendChild(script);
  
  // Initialize dataLayer and gtag function
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }
  
  // Configure GA4
  gtag('js', new Date());
  gtag('config', GA4_MEASUREMENT_ID, {
    anonymize_ip: true,
    cookie_flags: 'SameSite=None;Secure'
  });
  
  // Make gtag available globally
  window.gtag = gtag;
})();
