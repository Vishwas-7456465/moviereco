/**
 * Frontend JavaScript for Movie Recommendation System
 * Handles autocomplete search, loading spinner, and image fallback placeholders.
 */

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('movie-search');
    const suggestionsList = document.getElementById('suggestions');
    const searchForm = document.getElementById('search-form');
    const spinnerContainer = document.getElementById('spinner-container');
    const recommendBtn = document.getElementById('recommend-btn');

    // Return if elements are not found (e.g. on pages other than Home)
    if (!searchInput || !suggestionsList || !searchForm) return;

    let debounceTimeout;

    // Listen for input in the search box to fetch autocomplete suggestions
    searchInput.addEventListener('input', () => {
        const query = searchInput.value.trim();

        // Clear previous pending fetches
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
                        data.forEach(title => {
                            const li = document.createElement('li');
                            li.textContent = title;
                            
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
                .catch(err => {
                    console.error('Error fetching suggestions:', err);
                });
        }, 150); // 150ms debounce delay
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

    // Helper to show spinner and disable button
    function showSpinner() {
        if (spinnerContainer) spinnerContainer.style.display = 'flex';
        if (recommendBtn) {
            recommendBtn.disabled = true;
            recommendBtn.innerHTML = '<span class="spinner-small"></span> Working...';
            // Add styling for small spinner in button
            recommendBtn.style.opacity = '0.7';
        }
    }

    // Helper to programmatically submit form
    function submitForm() {
        showSpinner();
        searchForm.submit();
    }
});

/**
 * Global fallback function for movie posters when the URL fails to load.
 * Dynamically replaces the image tag with a styled placeholder containing the movie title.
 * @param {HTMLImageElement} img - The image element that failed to load
 * @param {string} title - The title of the movie to display on the placeholder
 */
function handlePosterError(img, title) {
    // Prevent infinite loop if placeholder image itself fails
    img.onerror = null; 

    // Create container element
    const container = document.createElement('div');
    container.className = 'poster-placeholder';

    // SVG icon for movie
    const iconSvg = `
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="placeholder-icon">
            <rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect>
            <line x1="7" y1="2" x2="7" y2="22"></line>
            <line x1="17" y1="2" x2="17" y2="22"></line>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <line x1="2" y1="7" x2="7" y2="7"></line>
            <line x1="2" y1="17" x2="7" y2="17"></line>
            <line x1="17" y1="17" x2="22" y2="17"></line>
            <line x1="17" y1="7" x2="22" y2="7"></line>
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
