/**
 * Frontend JavaScript for Movie Recommendation System
 * Handles autocomplete search, loading spinner, and image fallback placeholders.
 * Now upgraded with Cineverse Fluid Motion and Scroll Animations.
 */

document.addEventListener('DOMContentLoaded', () => {
    /* =========================================
       1. AUTOCOMPLETE & SEARCH LOGIC
       ========================================= */
    const searchInput = document.getElementById('movie-search');
    const suggestionsList = document.getElementById('suggestions');
    const searchForm = document.getElementById('search-form');
    const spinnerContainer = document.getElementById('spinner-container');
    const recommendBtn = document.getElementById('recommend-btn');

    if (searchInput && suggestionsList && searchForm) {
        let debounceTimeout;

        // Listen for input in the search box to fetch autocomplete suggestions
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.trim();
            clearTimeout(debounceTimeout);

            if (query.length < 2) {
                suggestionsList.innerHTML = '';
                suggestionsList.style.display = 'none';
                return;
            }

            // Debounce to avoid hitting the backend on every fast keystroke
            debounceTimeout = setTimeout(() => {
                fetch(`/api/suggest?q=${encodeURIComponent(query)}`)
                    .then(response => response.json())
                    .then(data => {
                        suggestionsList.innerHTML = '';
                        
                        if (data.length > 0) {
                            data.forEach((title, index) => {
                                const li = document.createElement('li');
                                li.textContent = title;
                                // Add slight stagger delay for suggestions
                                li.style.animationDelay = `${index * 30}ms`;
                                li.classList.add('animate-fade-up');
                                
                                // Handle click on a suggestion
                                li.addEventListener('click', () => {
                                    searchInput.value = title;
                                    suggestionsList.innerHTML = '';
                                    suggestionsList.style.display = 'none';
                                    submitForm();
                                });
                                suggestionsList.appendChild(li);
                            });
                            suggestionsList.style.display = 'block';
                        } else {
                            suggestionsList.style.display = 'none';
                        }
                    })
                    .catch(err => console.error('Error fetching suggestions:', err));
            }, 150);
        });

        // Close suggestion list when clicking outside
        document.addEventListener('click', (e) => {
            if (e.target !== searchInput && e.target !== suggestionsList) {
                suggestionsList.style.display = 'none';
            }
        });

        // Handle form submission and show loading spinner
        searchForm.addEventListener('submit', (e) => {
            const query = searchInput.value.trim();
            if (!query) {
                e.preventDefault();
                return;
            }
            showSpinner();
        });

        function showSpinner() {
            if (spinnerContainer) spinnerContainer.style.display = 'flex';
            if (recommendBtn) {
                recommendBtn.disabled = true;
                recommendBtn.innerHTML = '<span class="spinner" style="width: 20px; height: 20px; border-width: 2px;"></span> &nbsp; Scanning...';
                recommendBtn.style.opacity = '0.8';
            }
        }

        function submitForm() {
            showSpinner();
            searchForm.submit();
        }
    }

    /* =========================================
       2. SCROLL ANIMATIONS (INTERSECTION OBSERVER)
       ========================================= */
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Select elements to animate on scroll
    const animatedElements = document.querySelectorAll('.movie-card, .selected-movie-card, .about-card, .section-title, .tech-card');
    animatedElements.forEach((el, index) => {
        // Add a slight stagger to cards in a grid
        if (el.classList.contains('movie-card')) {
            el.style.animationDelay = `${(index % 10) * 80}ms`;
        }
        observer.observe(el);
        // Hide initially so animation is visible when scrolling down
        el.style.opacity = '0'; 
    });

    /* =========================================
       3. FLUID CURSOR GLOW EFFECT
       ========================================= */
    // Apply liquid glow to cards
    const liquidElements = document.querySelectorAll('.movie-card, .selected-movie-card, .search-box');
    
    liquidElements.forEach(el => {
        el.classList.add('liquid-glow');
        
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            // Calculate cursor position relative to the element
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Update CSS variables for the glow position
            el.style.setProperty('--x', `${x}px`);
            el.style.setProperty('--y', `${y}px`);
        });
    });

    /* =========================================
       4. NAVBAR SCROLL EFFECT
       ========================================= */
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }, { passive: true });
    }
});

/* =========================================
   5. POSTER FALLBACK LOGIC
   ========================================= */
/**
 * Global fallback function for movie posters when the URL fails to load.
 * Dynamically replaces the image tag with a styled placeholder containing the movie title.
 */
function handlePosterError(img, title) {
    // Prevent infinite loop if placeholder image itself fails
    img.onerror = null; 

    // Create container element
    const container = document.createElement('div');
    container.className = 'poster-placeholder';

    // Cinematic SVG icon for movie fallback
    const iconSvg = `
        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="placeholder-icon">
            <rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect>
            <line x1="7" y1="2" x2="7" y2="22"></line>
            <line x1="17" y1="2" x2="17" y2="22"></line>
            <line x1="2" y1="12" x2="22" y2="12"></line>
        </svg>
    `;

    container.innerHTML = `
        ${iconSvg}
        <div class="placeholder-title">${escapeHtml(title)}</div>
    `;

    // Replace the img tag with the container in the DOM
    const wrapper = img.parentElement;
    if (wrapper) {
        wrapper.innerHTML = '';
        wrapper.appendChild(container);
    }
}

// Simple HTML escaping helper for security
function escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}
