/**
 * Artifacts & Monuments Gallery Component - History of India
 * High-resolution lightbox inspector with Wikipedia citations and bookmarking.
 */

window.HistoryApp = window.HistoryApp || {};

window.HistoryApp.Gallery = (function() {
  let currentCategory = 'all';

  function init() {
    render();
    setupFilters();
  }

  function render() {
    const grid = document.getElementById('gallery-grid');
    if (!grid) return;

    const artifacts = window.HistoryData.artifacts || [];
    const filtered = currentCategory === 'all' 
      ? artifacts 
      : artifacts.filter(item => item.category === currentCategory);

    let html = '';
    filtered.forEach(item => {
      const isSaved = HistoryApp.Bookmarks.isBookmarked(item.id);
      html += `
        <div class="artifact-card" data-id="${item.id}" onclick="HistoryApp.Gallery.openLightbox('${item.id}')">
          <button class="artifact-bookmark-btn ${isSaved ? 'saved' : ''}" 
                  title="${isSaved ? 'Remove from collection' : 'Save to collection'}"
                  onclick="event.stopPropagation(); HistoryApp.Gallery.toggleBookmark('${item.id}', this)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="${isSaved ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
              <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
            </svg>
          </button>
          <div class="artifact-thumb-wrap">
            <img class="artifact-thumb" 
                 src="${item.image}" 
                 alt="${item.title}" 
                 loading="lazy"
                 onerror="this.onerror=null; this.src='images/ashoka_lion.jpg';">
            <div class="artifact-thumb-overlay"></div>
          </div>
          <div class="artifact-info">
            <div class="artifact-era-tag">${item.period}</div>
            <h4 class="artifact-title">${item.title}</h4>
            <p class="artifact-snippet">${item.description}</p>
            <div class="artifact-footer">
              <span>📍 ${item.location.split(',')[0]}</span>
              <span style="color: var(--text-gold);">Inspect Artifact ↗</span>
            </div>
          </div>
        </div>
      `;
    });

    grid.innerHTML = html;
  }

  function setupFilters() {
    const filterBtns = document.querySelectorAll('.gallery-filter-btn[data-category]');
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCategory = btn.getAttribute('data-category');
        render();
      });
    });
  }

  function openLightbox(artifactId) {
    const item = (window.HistoryData.artifacts || []).find(a => a.id === artifactId);
    if (!item) return;

    const modal = document.getElementById('global-modal');
    const modalContent = document.getElementById('modal-dynamic-content');
    if (!modal || !modalContent) return;

    const isSaved = HistoryApp.Bookmarks.isBookmarked(item.id);

    modalContent.innerHTML = `
      <div class="modal-card">
        <button class="modal-close-btn" onclick="HistoryApp.closeModal()">✕</button>
        <div class="modal-visual-side">
          <img src="${item.image}" alt="${item.title}" onerror="this.onerror=null; this.src='images/ashoka_lion.jpg';">
        </div>
        <div class="modal-info-side">
          <div class="flex-between" style="margin-bottom: 0.5rem;">
            <span class="badge badge-gold">${item.period}</span>
            <span class="badge" style="text-transform: capitalize;">${item.category}</span>
          </div>
          <h2 style="font-size: 1.8rem; margin-bottom: 0.8rem; line-height: 1.2;">${item.title}</h2>
          <p style="margin-bottom: 1.5rem; font-size: 0.95rem;">${item.description}</p>

          <div class="modal-provenance-list">
            <div class="modal-provenance-row">
              <span>Civilizational Era</span>
              <span>${item.eraName || item.era}</span>
            </div>
            <div class="modal-provenance-row">
              <span>Current Provenance</span>
              <span>${item.location}</span>
            </div>
            ${item.material ? `
              <div class="modal-provenance-row">
                <span>Material / Medium</span>
                <span>${item.material}</span>
              </div>
            ` : ''}
            ${item.dimensions ? `
              <div class="modal-provenance-row">
                <span>Dimensions</span>
                <span>${item.dimensions}</span>
              </div>
            ` : ''}
          </div>

          <div style="margin-top: auto; padding-top: 1.8rem; border-top: var(--border-subtle); display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap;">
            <a href="${item.wikipediaUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="font-size: 0.78rem;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 0.4rem;">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                <polyline points="15 3 21 3 21 9"></polyline>
                <line x1="21" y1="3" x2="9" y2="15"></line>
              </svg>
              View on Wikipedia
            </a>
            <button class="btn ${isSaved ? 'btn-gold' : 'btn-primary'}" onclick="HistoryApp.Gallery.toggleBookmark('${item.id}', this); HistoryApp.Gallery.render();">
              ${isSaved ? '★ In Your Collection' : '☆ Save to Collection'}
            </button>
          </div>
        </div>
      </div>
    `;

    modal.classList.add('active');
  }

  function toggleBookmark(artifactId, triggerEl) {
    const isNowSaved = HistoryApp.Bookmarks.toggle(artifactId);
    if (triggerEl) {
      if (isNowSaved) {
        triggerEl.classList.add('saved');
        triggerEl.innerHTML = `
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
          </svg>
        `;
      } else {
        triggerEl.classList.remove('saved');
        triggerEl.innerHTML = `
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
          </svg>
        `;
      }
    }
  }

  return {
    init: init,
    render: render,
    openLightbox: openLightbox,
    toggleBookmark: toggleBookmark
  };
})();
