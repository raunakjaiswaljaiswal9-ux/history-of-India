/**
 * Main Application Coordinator - History of India
 * Coordinates Sony darkroom theme, navigation, localStorage bookmarks, and modals.
 */

window.HistoryApp = window.HistoryApp || {};

// ---------------------------------------------------------------------------
// Bookmarks Manager (100% Client-Side LocalStorage)
// ---------------------------------------------------------------------------
window.HistoryApp.Bookmarks = (function() {
  const STORAGE_KEY = 'india_history_bookmarks_v1';

  function getBookmarks() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      return stored ? JSON.parse(stored) : [];
    } catch (e) {
      return [];
    }
  }

  function isBookmarked(id) {
    return getBookmarks().includes(id);
  }

  function toggle(id) {
    let list = getBookmarks();
    let isNowSaved = false;
    if (list.includes(id)) {
      list = list.filter(item => item !== id);
      isNowSaved = false;
    } else {
      list.push(id);
      isNowSaved = true;
    }
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
    } catch (e) {}

    updateBadge();
    return isNowSaved;
  }

  function updateBadge() {
    const badge = document.getElementById('bookmarks-count-badge');
    const list = getBookmarks();
    if (badge) {
      badge.textContent = list.length;
      badge.style.display = list.length > 0 ? 'inline-flex' : 'none';
    }
  }

  function renderList() {
    const container = document.getElementById('bookmarks-items-list');
    if (!container) return;

    const list = getBookmarks();
    const artifacts = window.HistoryData.artifacts || [];
    const savedItems = artifacts.filter(a => list.includes(a.id));

    if (savedItems.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 3rem 1rem; color: var(--text-tertiary);">
          <div style="font-size: 2rem; margin-bottom: 0.8rem; opacity: 0.5;">✦</div>
          <p style="font-size: 0.95rem; margin-bottom: 0.4rem; color: var(--text-secondary);">Your collection is currently empty</p>
          <p style="font-size: 0.82rem;">Click the bookmark star on any historical artifact or monument to pin it here.</p>
        </div>
      `;
      return;
    }

    let html = '';
    savedItems.forEach(item => {
      html += `
        <div class="search-result-item" onclick="HistoryApp.closeDrawer(); HistoryApp.Gallery.openLightbox('${item.id}')">
          <div class="flex-between" style="margin-bottom: 0.35rem;">
            <span class="badge badge-gold" style="font-size: 0.65rem; padding: 0.2rem 0.5rem;">${item.period}</span>
            <button onclick="event.stopPropagation(); HistoryApp.Bookmarks.toggle('${item.id}'); HistoryApp.Bookmarks.renderList(); HistoryApp.Gallery.render();" 
                    style="color: var(--text-tertiary); font-size: 0.75rem;" title="Remove">✕</button>
          </div>
          <h4 style="font-size: 1.05rem; margin-bottom: 0.25rem;">${item.title}</h4>
          <p style="font-size: 0.82rem; color: var(--text-secondary);">${item.location}</p>
        </div>
      `;
    });

    container.innerHTML = html;
  }

  return {
    getBookmarks: getBookmarks,
    isBookmarked: isBookmarked,
    toggle: toggle,
    updateBadge: updateBadge,
    renderList: renderList
  };
})();

// ---------------------------------------------------------------------------
// Global App Controllers
// ---------------------------------------------------------------------------
window.HistoryApp.openModal = function() {
  const modal = document.getElementById('global-modal');
  if (modal) modal.classList.add('active');
};

window.HistoryApp.closeModal = function() {
  const modal = document.getElementById('global-modal');
  if (modal) modal.classList.remove('active');
};

window.HistoryApp.openDrawer = function(tabName) {
  const backdrop = document.getElementById('global-drawer-backdrop');
  const searchTab = document.getElementById('drawer-tab-search');
  const bookmarksTab = document.getElementById('drawer-tab-bookmarks');
  const searchSection = document.getElementById('drawer-section-search');
  const bookmarksSection = document.getElementById('drawer-section-bookmarks');

  if (!backdrop) return;

  backdrop.classList.add('active');

  if (tabName === 'bookmarks') {
    searchTab.classList.remove('active');
    bookmarksTab.classList.add('active');
    searchSection.style.display = 'none';
    bookmarksSection.style.display = 'block';
    HistoryApp.Bookmarks.renderList();
  } else {
    bookmarksTab.classList.remove('active');
    searchTab.classList.add('active');
    bookmarksSection.style.display = 'none';
    searchSection.style.display = 'block';
    const input = document.getElementById('global-search-input');
    if (input) setTimeout(() => input.focus(), 150);
  }
};

window.HistoryApp.closeDrawer = function() {
  const backdrop = document.getElementById('global-drawer-backdrop');
  if (backdrop) backdrop.classList.remove('active');
};

// ---------------------------------------------------------------------------
// Application Lifecycle Initialization
// ---------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  // 1. Initialize Sub-modules
  if (window.HistoryApp.Timeline) window.HistoryApp.Timeline.init();
  if (window.HistoryApp.Gallery) window.HistoryApp.Gallery.init();
  if (window.HistoryApp.Atlas) window.HistoryApp.Atlas.init();
  if (window.HistoryApp.Search) window.HistoryApp.Search.init();
  if (window.HistoryApp.Audio) window.HistoryApp.Audio.init();
  if (window.HistoryApp.Bookmarks) window.HistoryApp.Bookmarks.updateBadge();

  // 1b. Check Python Localhost Backend Connection
  checkLocalhostBackend();

  // 2. Setup Navbar Scroll Effect
  const navbar = document.getElementById('sony-navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('nav-scrolled');
    } else {
      navbar.classList.remove('nav-scrolled');
    }
  }, { passive: true });

  // 3. Render Hero Era Quick Pills
  const eraTrack = document.getElementById('hero-era-track');
  if (eraTrack && window.HistoryData.eras) {
    let pillsHtml = '';
    window.HistoryData.eras.forEach(era => {
      pillsHtml += `
        <button class="hero-era-pill" onclick="HistoryApp.Timeline.openEraModal('${era.id}')">
          <span class="era-pill-year">${era.period.split('–')[0].trim()}</span>
          <span class="era-pill-name">${era.title.split(' ')[0]} ${era.title.split(' ')[1] || ''}</span>
        </button>
      `;
    });
    eraTrack.innerHTML = pillsHtml;
  }

  // 4. Render Quotation Banner
  const quoteContainer = document.getElementById('quote-banner-content');
  if (quoteContainer && window.HistoryData.quotes) {
    const quotes = window.HistoryData.quotes;
    let quoteIndex = 0;

    function displayQuote(index) {
      const q = quotes[index];
      quoteContainer.innerHTML = `
        <div class="quote-symbol">“</div>
        <blockquote class="quote-text">${q.quote}</blockquote>
        <div class="quote-author">— ${q.author}</div>
        <div class="quote-context">${q.context}</div>
      `;
    }

    displayQuote(0);

    // Subtle automatic rotation every 10 seconds
    setInterval(() => {
      quoteIndex = (quoteIndex + 1) % quotes.length;
      displayQuote(quoteIndex);
    }, 10000);
  }

  // 5. Drawer Tab Switchers
  const searchTab = document.getElementById('drawer-tab-search');
  const bookmarksTab = document.getElementById('drawer-tab-bookmarks');
  if (searchTab && bookmarksTab) {
    searchTab.addEventListener('click', () => HistoryApp.openDrawer('search'));
    bookmarksTab.addEventListener('click', () => HistoryApp.openDrawer('bookmarks'));
  }

  // 6. Keyboard Escape & Overlay Clicks
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      HistoryApp.closeModal();
      HistoryApp.closeDrawer();
    }
  });

  const modalOverlay = document.getElementById('global-modal');
  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        HistoryApp.closeModal();
      }
    });
  }

  const drawerBackdrop = document.getElementById('global-drawer-backdrop');
  if (drawerBackdrop) {
    drawerBackdrop.addEventListener('click', (e) => {
      if (e.target === drawerBackdrop) {
        HistoryApp.closeDrawer();
      }
    });
  }
});

function checkLocalhostBackend() {
  const badge = document.getElementById('server-status-pill');
  if (!badge) return;

  fetch('/api/status')
    .then(res => res.json())
    .then(data => {
      if (data.status === 'online') {
        badge.innerHTML = `<span style="width: 7px; height: 7px; background: #4ade80; border-radius: 50%; box-shadow: 0 0 8px #4ade80; display: inline-block;"></span> Python Localhost :${data.port}`;
        badge.style.borderColor = 'rgba(74, 222, 128, 0.4)';
        badge.style.color = '#e2e8f0';
        badge.title = 'Python REST API Backend Connected';
      }
    })
    .catch(() => {
      badge.innerHTML = `<span style="width: 7px; height: 7px; background: #a1a1aa; border-radius: 50%; display: inline-block;"></span> Client Mode`;
      badge.title = 'Running standalone. Start server.py for full Python API features.';
    });
}

