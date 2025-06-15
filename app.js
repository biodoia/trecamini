// JavaScript for Antico Casale Tre Camini - Sistema Domotico Integrato

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initTabSystem();
    initScrollAnimations();
    initScrollProgress();
    initSmoothScrolling();
    initCTAButton();
    initIntersectionObserver();
});

// Tab System for Features Section
function initTabSystem() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetTab = this.getAttribute('data-tab');
            
            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button and corresponding content
            this.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
            
            // Animate the tab content appearance
            const activeContent = document.getElementById(targetTab);
            activeContent.style.opacity = '0';
            activeContent.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                activeContent.style.opacity = '1';
                activeContent.style.transform = 'translateY(0)';
                activeContent.style.transition = 'all 0.4s ease-out';
            }, 50);
        });
    });
}

// Scroll Progress Indicator
function initScrollProgress() {
    // Create progress bar element
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    document.body.appendChild(progressBar);

    // Update progress on scroll
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset;
        const docHeight = document.body.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        progressBar.style.width = scrollPercent + '%';
    });
}

// Smooth Scrolling for Internal Links
function initSmoothScrolling() {
    // Add smooth scroll behavior to any internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// CTA Button Functionality
function initCTAButton() {
    const ctaButton = document.querySelector('.cta-button');
    
    if (ctaButton) {
        ctaButton.addEventListener('click', function() {
            // Create a more elaborate interaction
            this.style.transform = 'scale(0.95)';
            
            setTimeout(() => {
                this.style.transform = 'scale(1)';
                
                // Show contact modal or redirect to contact form
                showContactModal();
            }, 150);
        });
    }
}

// Contact Modal (simple implementation)
function showContactModal() {
    // Create modal overlay
    const modalOverlay = document.createElement('div');
    modalOverlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(45, 80, 22, 0.9);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10000;
        animation: fadeIn 0.3s ease-out;
    `;

    // Create modal content
    const modalContent = document.createElement('div');
    modalContent.style.cssText = `
        background: white;
        padding: 40px;
        border-radius: 16px;
        max-width: 500px;
        width: 90%;
        text-align: center;
        animation: slideInUp 0.4s ease-out;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    `;

    modalContent.innerHTML = `
        <h3 style="color: var(--color-restaurant-green); margin-bottom: 20px; font-family: 'Playfair Display', serif;">
            Richiedi Consultazione Gratuita
        </h3>
        <p style="margin-bottom: 30px; color: var(--color-text-secondary);">
            Saremo lieti di presentarti nel dettaglio come il nostro sistema domotico può trasformare 
            la gestione del tuo ristorante. La consultazione è completamente gratuita e senza impegno.
        </p>
        <div style="margin-bottom: 30px;">
            <p style="margin: 10px 0;"><strong>📧</strong> info@anticocaletrecamini.it</p>
            <p style="margin: 10px 0;"><strong>📞</strong> +39 045 123 4567</p>
            <p style="margin: 10px 0;"><strong>📍</strong> Lago di Garda, Verona</p>
        </div>
        <button id="closeModal" style="
            background: var(--color-restaurant-gold);
            color: var(--color-restaurant-green);
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        ">Chiudi</button>
    `;

    modalOverlay.appendChild(modalContent);
    document.body.appendChild(modalOverlay);

    // Add closing functionality
    document.getElementById('closeModal').addEventListener('click', function() {
        modalOverlay.style.animation = 'fadeOut 0.3s ease-out';
        setTimeout(() => {
            document.body.removeChild(modalOverlay);
        }, 300);
    });

    // Close on overlay click
    modalOverlay.addEventListener('click', function(e) {
        if (e.target === modalOverlay) {
            modalOverlay.style.animation = 'fadeOut 0.3s ease-out';
            setTimeout(() => {
                document.body.removeChild(modalOverlay);
            }, 300);
        }
    });
}

// Intersection Observer for Scroll Animations
function initIntersectionObserver() {
    // Create observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Add animation classes to elements and observe them
    const animatedElements = [
        '.investment-card',
        '.component-category',
        '.benefit-card',
        '.feature-card',
        '.comparison-row',
        '.chart-container'
    ];

    animatedElements.forEach(selector => {
        document.querySelectorAll(selector).forEach((element, index) => {
            element.classList.add('fade-in');
            element.style.transitionDelay = `${index * 0.1}s`;
            observer.observe(element);
        });
    });
}

// Scroll Animations (legacy support)
function initScrollAnimations() {
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function handleScrollAnimation() {
        const elements = document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right');
        
        elements.forEach(element => {
            if (isElementInViewport(element)) {
                element.classList.add('visible');
            }
        });
    }

    // Throttle scroll events for better performance
    let ticking = false;
    function scrollHandler() {
        if (!ticking) {
            requestAnimationFrame(function() {
                handleScrollAnimation();
                ticking = false;
            });
            ticking = true;
        }
    }

    window.addEventListener('scroll', scrollHandler);
    handleScrollAnimation(); // Initial check
}

// Add CSS animations dynamically
function addAnimationStyles() {
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; }
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .fade-in {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease-out;
        }
        
        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }
    `;
    document.head.appendChild(style);
}

// Initialize animation styles
addAnimationStyles();

// Enhanced card interactions
function initCardInteractions() {
    // Investment cards hover effects
    const investmentCards = document.querySelectorAll('.investment-card');
    investmentCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Benefit cards click interaction
    const benefitCards = document.querySelectorAll('.benefit-card');
    benefitCards.forEach(card => {
        card.addEventListener('click', function() {
            // Create a subtle pulse effect
            this.style.animation = 'pulse 0.6s ease-in-out';
            setTimeout(() => {
                this.style.animation = '';
            }, 600);
        });
    });

    // Feature cards expand on click
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('click', function() {
            const isExpanded = this.classList.contains('expanded');
            
            // Reset all cards
            featureCards.forEach(c => c.classList.remove('expanded'));
            
            if (!isExpanded) {
                this.classList.add('expanded');
                this.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    });
}

// Initialize card interactions when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(initCardInteractions, 100);
});

// Parallax effect for hero section
function initParallaxEffect() {
    const hero = document.querySelector('.hero');
    
    if (hero) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            hero.style.backgroundPositionY = rate + 'px';
        });
    }
}

// Add parallax effect
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(initParallaxEffect, 100);
});

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimized scroll handler
const optimizedScrollHandler = debounce(function() {
    // Handle scroll-based animations here
}, 16); // ~60fps

window.addEventListener('scroll', optimizedScrollHandler);

// Add loading state management
function initLoadingState() {
    // Hide loading elements when page is fully loaded
    window.addEventListener('load', function() {
        document.querySelectorAll('.loading').forEach(element => {
            element.classList.remove('loading');
        });
    });
}

// Initialize loading state
document.addEventListener('DOMContentLoaded', initLoadingState);

// Keyboard navigation support
function initKeyboardNavigation() {
    document.addEventListener('keydown', function(e) {
        // ESC key to close modal
        if (e.key === 'Escape') {
            const modal = document.querySelector('[style*="position: fixed"]');
            if (modal && modal.style.zIndex === '10000') {
                modal.click();
            }
        }
        
        // Tab navigation for feature tabs
        if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
            const activeTab = document.querySelector('.tab-button.active');
            if (activeTab) {
                const tabs = Array.from(document.querySelectorAll('.tab-button'));
                const currentIndex = tabs.indexOf(activeTab);
                let nextIndex;
                
                if (e.key === 'ArrowLeft') {
                    nextIndex = currentIndex > 0 ? currentIndex - 1 : tabs.length - 1;
                } else {
                    nextIndex = currentIndex < tabs.length - 1 ? currentIndex + 1 : 0;
                }
                
                tabs[nextIndex].click();
                tabs[nextIndex].focus();
            }
        }
    });
}

// Initialize keyboard navigation
document.addEventListener('DOMContentLoaded', initKeyboardNavigation);