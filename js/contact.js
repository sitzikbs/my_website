// Contact form handling

document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact-form');
    const formMessage = document.getElementById('form-message');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(contactForm);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                subject: formData.get('subject'),
                message: formData.get('message')
            };
            
            // Since this is a static site, we'll show a message
            // In a real implementation, you would send this to a backend service
            // or use a service like Formspree, Basin, or Netlify Forms
            
            showMessage('Thank you for your message! However, this is a demo contact form. ' +
                       'To make it functional, you need to integrate it with a form handling service.', 
                       'success');
            
            // Reset form
            contactForm.reset();
            
            // Here's how you could integrate with a service like Formspree:
            // fetch('https://formspree.io/f/YOUR_FORM_ID', {
            //     method: 'POST',
            //     body: formData,
            //     headers: {
            //         'Accept': 'application/json'
            //     }
            // }).then(response => {
            //     if (response.ok) {
            //         showMessage('Thank you for your message! I will get back to you soon.', 'success');
            //         contactForm.reset();
            //     } else {
            //         showMessage('Oops! There was a problem submitting your form.', 'error');
            //     }
            // }).catch(error => {
            //     showMessage('Oops! There was a problem submitting your form.', 'error');
            // });
        });
    }
    
    function showMessage(message, type) {
        formMessage.textContent = message;
        formMessage.className = 'form-message ' + type;
        
        // Hide message after 5 seconds
        setTimeout(() => {
            formMessage.className = 'form-message';
        }, 5000);
    }
});
