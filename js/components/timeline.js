/**
 * Timeline Component - History of India
 * Supports Sony-style Horizontal Scrubber & Vertical Chronicle Modes
 */

window.HistoryApp = window.HistoryApp || {};

window.HistoryApp.Timeline = (function() {
  let currentFilter = 'all';
  let currentViewMode = 'horizontal'; // 'horizontal' or 'vertical'
  let isDragging = false;
  let startX, scrollLeft;

  function init() {
    render();
    setupControls();
  }

  function getFilteredEras() {
    const eras = window.HistoryData.eras || [];
    if (currentFilter === 'all') return eras;
    return eras.filter(era => era.category === currentFilter);
  }

  function render() {
    const container = document.getElementById('timeline-viewport');
    if (!container) return;

    const filtered = getFilteredEras();

    if (currentViewMode === 'horizontal') {
      renderHorizontalView(container, filtered);
    } else {
      renderVerticalView(container, filtered);
    }
  }

  function renderHorizontalView(container, eras) {
    let html = `
      <div class="horizontal-timeline-wrap">
        <div class="horizontal-track" id="horizontal-track">
    `;

    eras.forEach(era => {
      html += `
        <div class="timeline-era-card" data-era-id="${era.id}">
          <div class="era-card-image-wrap">
            <span class="badge badge-gold era-card-tag">${era.period}</span>
            <img class="era-card-image" 
                 src="${era.image}" 
                 alt="${era.title}" 
                 loading="lazy"
                 onerror="this.onerror=null; this.src='images/ashoka_lion.jpg';">
            <div class="era-card-overlay"></div>
          </div>
          <div class="era-card-body">
            <div class="era-card-period">${era.subtitle}</div>
            <h3 class="era-card-title">${era.title}</h3>
            <p class="era-card-desc">${era.overview}</p>
            <div class="era-card-meta">
              <span class="era-card-capital">Epicenter: <strong>${era.capital}</strong></span>
              <button class="btn btn-outline" style="padding: 0.35rem 0.75rem; font-size: 0.72rem;" onclick="HistoryApp.Timeline.openEraModal('${era.id}')">Explore Era →</button>
            </div>
          </div>
        </div>
      `;
    });

    html += `
        </div>
      </div>
    `;

    container.innerHTML = html;
    setupDragScroll();
  }

  function renderVerticalView(container, eras) {
    let html = `
      <div class="vertical-timeline-wrap">
    `;

    eras.forEach(era => {
      html += `
        <div class="vertical-era-node" data-era-id="${era.id}">
          <div class="vertical-era-marker"></div>
          <div class="vertical-era-card">
            <div class="flex-between" style="margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
              <span class="badge badge-gold">${era.period}</span>
              <span style="font-size: 0.75rem; color: var(--text-tertiary); text-transform: uppercase;">Epicenter: ${era.capital}</span>
            </div>
            <h3 style="margin-bottom: 0.4rem;">${era.title}</h3>
            <p style="color: var(--text-gold); font-size: 0.88rem; margin-bottom: 1rem;">${era.subtitle}</p>
            <p style="margin-bottom: 1.25rem;">${era.overview}</p>

            <div class="milestones-list">
              <h5 style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.14em; color: var(--text-tertiary);">Key Civilizational Turning Points</h5>
              ${era.keyEvents.map(ev => `
                <div class="milestone-item">
                  <div class="milestone-year">${ev.year}</div>
                  <div class="milestone-text">
                    <strong>${ev.title}</strong>
                    ${ev.desc}
                  </div>
                </div>
              `).join('')}
            </div>

            <div style="margin-top: 1.5rem; text-align: right;">
              <button class="btn btn-outline" style="font-size: 0.75rem; padding: 0.45rem 1rem;" onclick="HistoryApp.Timeline.openEraModal('${era.id}')">View Full Era Archive & Artifacts →</button>
            </div>
          </div>
        </div>
      `;
    });

    html += `
      </div>
    `;

    container.innerHTML = html;
  }

  function setupDragScroll() {
    const track = document.getElementById('horizontal-track');
    if (!track) return;

    track.addEventListener('mousedown', (e) => {
      isDragging = true;
      startX = e.pageX - track.offsetLeft;
      scrollLeft = track.scrollLeft;
    });

    track.addEventListener('mouseleave', () => {
      isDragging = false;
    });

    track.addEventListener('mouseup', () => {
      isDragging = false;
    });

    track.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      e.preventDefault();
      const x = e.pageX - track.offsetLeft;
      const walk = (x - startX) * 1.8;
      track.scrollLeft = scrollLeft - walk;
    });

    // Optional horizontal wheel scrolling
    track.addEventListener('wheel', (e) => {
      if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
        track.scrollLeft += e.deltaY;
      }
    }, { passive: true });
  }

  function setupControls() {
    // Filter Buttons
    const filterBtns = document.querySelectorAll('.filter-btn[data-filter]');
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.getAttribute('data-filter');
        render();
      });
    });

    // View Switcher (Horizontal vs Vertical)
    const viewBtns = document.querySelectorAll('.view-btn[data-view]');
    viewBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        viewBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentViewMode = btn.getAttribute('data-view');
        render();
      });
    });
  }

  function openEraModal(eraId) {
    const era = (window.HistoryData.eras || []).find(e => e.id === eraId);
    if (!era) return;

    const modal = document.getElementById('global-modal');
    const modalContent = document.getElementById('modal-dynamic-content');
    if (!modal || !modalContent) return;

    modalContent.innerHTML = `
      <div class="modal-card">
        <button class="modal-close-btn" onclick="HistoryApp.closeModal()">✕</button>
        <div class="modal-visual-side">
          <img src="${era.banner || era.image}" alt="${era.title}" onerror="this.onerror=null; this.src='images/ashoka_lion.jpg';">
        </div>
        <div class="modal-info-side">
          <span class="badge badge-gold" style="align-self: flex-start; margin-bottom: 0.8rem;">${era.period}</span>
          <h2 style="font-size: 1.8rem; margin-bottom: 0.4rem;">${era.title}</h2>
          <p style="color: var(--text-gold); font-size: 0.95rem; margin-bottom: 1.2rem;">${era.subtitle}</p>
          <p style="margin-bottom: 1.5rem;">${era.overview}</p>

          <div class="modal-provenance-list">
            <div class="modal-provenance-row">
              <span>Geographic Span</span>
              <span>${era.geography || era.capital}</span>
            </div>
            ${era.stats ? Object.entries(era.stats).map(([k, v]) => `
              <div class="modal-provenance-row">
                <span>${k.replace(/([A-Z])/g, ' $1')}</span>
                <span>${v}</span>
              </div>
            `).join('') : ''}
          </div>

          <div style="margin-top: auto; padding-top: 1.5rem; border-top: var(--border-subtle); display: flex; gap: 1rem;">
            <button class="btn btn-primary" onclick="HistoryApp.closeModal(); document.getElementById('gallery').scrollIntoView({behavior: 'smooth'})">Browse Era Artifacts</button>
          </div>
        </div>
      </div>
    `;

    modal.classList.add('active');
  }

  function scrollToEra(eraId) {
    const card = document.querySelector(`[data-era-id="${eraId}"]`);
    if (card) {
      card.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'center' });
      card.style.outline = '2px solid var(--text-accent)';
      setTimeout(() => { card.style.outline = 'none'; }, 2000);
    }
  }

  return {
    init: init,
    render: render,
    openEraModal: openEraModal,
    scrollToEra: scrollToEra
  };
})();
