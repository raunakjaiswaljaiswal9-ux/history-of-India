/**
 * Instant Client-Side Search Engine - History of India
 * Zero-dependency indexing across eras, artifacts, rulers, and events.
 */

window.HistoryApp = window.HistoryApp || {};

window.HistoryApp.Search = (function() {
  let searchInput;
  let resultsContainer;

  function init() {
    searchInput = document.getElementById('global-search-input');
    resultsContainer = document.getElementById('search-results-list');

    if (searchInput) {
      searchInput.addEventListener('input', handleSearch);
    }
  }

  function handleSearch(e) {
    const query = (e.target.value || '').trim().toLowerCase();
    if (!resultsContainer) return;

    if (query.length < 2) {
      resultsContainer.innerHTML = `
        <div style="text-align: center; padding: 3rem 1rem; color: var(--text-tertiary);">
          <p style="font-size: 0.9rem;">Type at least 2 characters to search across 5,000 years of history...</p>
        </div>
      `;
      return;
    }

    const eras = window.HistoryData.eras || [];
    const artifacts = window.HistoryData.artifacts || [];
    const dynasties = window.HistoryData.dynasties || [];

    const matches = [];

    // Search Eras
    eras.forEach(era => {
      const matchScore = (
        (era.title.toLowerCase().includes(query) ? 3 : 0) +
        (era.overview.toLowerCase().includes(query) ? 1 : 0) +
        (era.capital.toLowerCase().includes(query) ? 2 : 0) +
        (era.prominentFigures && era.prominentFigures.some(f => f.toLowerCase().includes(query)) ? 2 : 0)
      );

      if (matchScore > 0) {
        matches.push({
          type: 'Era / Epoch',
          title: era.title,
          subtitle: era.period,
          description: era.overview.slice(0, 130) + '...',
          action: () => {
            HistoryApp.closeDrawer();
            HistoryApp.Timeline.openEraModal(era.id);
          }
        });
      }
    });

    // Search Artifacts
    artifacts.forEach(item => {
      const matchScore = (
        (item.title.toLowerCase().includes(query) ? 3 : 0) +
        (item.description.toLowerCase().includes(query) ? 1 : 0) +
        (item.location.toLowerCase().includes(query) ? 2 : 0) +
        (item.material && item.material.toLowerCase().includes(query) ? 2 : 0)
      );

      if (matchScore > 0) {
        matches.push({
          type: 'Artifact / Monument',
          title: item.title,
          subtitle: `${item.period} · ${item.location.split(',')[0]}`,
          description: item.description.slice(0, 130) + '...',
          action: () => {
            HistoryApp.closeDrawer();
            HistoryApp.Gallery.openLightbox(item.id);
          }
        });
      }
    });

    // Search Dynasties
    dynasties.forEach(dynasty => {
      const matchScore = (
        (dynasty.name.toLowerCase().includes(query) ? 3 : 0) +
        (dynasty.greatestRuler.toLowerCase().includes(query) ? 3 : 0) +
        (dynasty.capital.toLowerCase().includes(query) ? 2 : 0) +
        (dynasty.keyAccomplishments.some(a => a.toLowerCase().includes(query)) ? 1 : 0)
      );

      if (matchScore > 0) {
        matches.push({
          type: 'Imperial Dynasty',
          title: dynasty.name,
          subtitle: `${dynasty.period} · Sovereign: ${dynasty.greatestRuler}`,
          description: `Capital: ${dynasty.capital} · Peak Territory: ${dynasty.territoryKm2}`,
          action: () => {
            HistoryApp.closeDrawer();
            HistoryApp.Atlas.selectDynasty(dynasty.id);
            document.getElementById('dynasties').scrollIntoView({ behavior: 'smooth' });
          }
        });
      }
    });

    renderResults(matches, query);
  }

  function renderResults(matches, query) {
    if (matches.length === 0) {
      resultsContainer.innerHTML = `
        <div style="text-align: center; padding: 3rem 1rem; color: var(--text-tertiary);">
          <p style="font-size: 1rem; margin-bottom: 0.5rem; color: var(--text-secondary);">No historical records matched "${query}"</p>
          <p style="font-size: 0.85rem;">Try searching for "Ashoka", "Harappa", "Taj Mahal", "Bronze", or "1947"</p>
        </div>
      `;
      return;
    }

    let html = `
      <div style="font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-tertiary); margin-bottom: 1rem;">
        Found ${matches.length} Historical Record${matches.length > 1 ? 's' : ''}
      </div>
    `;

    matches.forEach((m, idx) => {
      html += `
        <div class="search-result-item" id="search-result-${idx}">
          <div class="flex-between" style="margin-bottom: 0.4rem;">
            <span class="badge badge-gold" style="font-size: 0.65rem; padding: 0.2rem 0.55rem;">${m.type}</span>
            <span style="font-size: 0.72rem; color: var(--text-gold); font-family: var(--font-mono);">${m.subtitle}</span>
          </div>
          <h4 style="font-size: 1.05rem; margin-bottom: 0.35rem; color: #ffffff;">${highlightText(m.title, query)}</h4>
          <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">${highlightText(m.description, query)}</p>
        </div>
      `;
    });

    resultsContainer.innerHTML = html;

    // Attach click events
    matches.forEach((m, idx) => {
      const el = document.getElementById(`search-result-${idx}`);
      if (el) {
        el.addEventListener('click', m.action);
      }
    });
  }

  function highlightText(text, query) {
    if (!text || !query) return text;
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<span style="color: var(--text-gold); font-weight: 600; text-decoration: underline;">$1</span>');
  }

  return {
    init: init
  };
})();
