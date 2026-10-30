/**
 * Dynasties & Empires Atlas Component - History of India
 */

window.HistoryApp = window.HistoryApp || {};

window.HistoryApp.Atlas = (function() {
  let activeDynastyId = 'maurya';

  function init() {
    render();
  }

  function render() {
    const navContainer = document.getElementById('dynasty-nav');
    const displayContainer = document.getElementById('dynasty-display');
    if (!navContainer || !displayContainer) return;

    const dynasties = window.HistoryData.dynasties || [];
    const active = dynasties.find(d => d.id === activeDynastyId) || dynasties[0];

    // Render Navigation List
    let navHtml = '';
    dynasties.forEach(d => {
      const isActive = d.id === active.id;
      navHtml += `
        <button class="dynasty-nav-item ${isActive ? 'active' : ''}" onclick="HistoryApp.Atlas.selectDynasty('${d.id}')">
          <div class="dynasty-item-name">${d.name}</div>
          <div class="dynasty-item-period">${d.period}</div>
        </button>
      `;
    });
    navContainer.innerHTML = navHtml;

    // Render Detail Display
    displayContainer.innerHTML = `
      <div class="dynasty-display-card">
        <div class="dynasty-header-meta">
          <span class="badge badge-gold">${active.period}</span>
          <span class="badge">Emblem: ${active.emblem}</span>
        </div>
        <h2 style="font-size: 2.2rem; margin-bottom: 0.6rem;">${active.name}</h2>
        <p style="color: var(--text-gold); font-size: 1.05rem; margin-bottom: 1.5rem;">${active.region}</p>

        <div class="dynasty-stats-grid">
          <div class="dynasty-stat-box">
            <h5>Imperial Capital</h5>
            <p>${active.capital}</p>
          </div>
          <div class="dynasty-stat-box">
            <h5>Dynastic Founder</h5>
            <p>${active.founder}</p>
          </div>
          <div class="dynasty-stat-box">
            <h5>Greatest Sovereign</h5>
            <p>${active.greatestRuler}</p>
          </div>
        </div>

        <div style="margin-bottom: 2rem;">
          <h4 style="font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.14em; color: var(--text-tertiary); margin-bottom: 1rem;">Civilizational Footprint & Territory</h4>
          <div style="display: flex; align-items: baseline; gap: 1rem; margin-bottom: 0.8rem;">
            <span style="font-size: 2.4rem; font-family: var(--font-editorial); color: var(--text-primary);">${active.territoryKm2}</span>
            <span style="font-size: 0.85rem; color: var(--text-tertiary);">Peak Sovereign Domain</span>
          </div>
        </div>

        <div>
          <h4 style="font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.14em; color: var(--text-tertiary); margin-bottom: 1rem;">Monumental Achievements & Legacy</h4>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem;">
            ${active.keyAccomplishments.map(acc => `
              <li style="display: flex; align-items: flex-start; gap: 0.75rem; font-size: 0.95rem; color: var(--text-secondary);">
                <span style="color: var(--text-gold); font-size: 1.1rem; line-height: 1;">✦</span>
                <span>${acc}</span>
              </li>
            `).join('')}
          </ul>
        </div>

        <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: var(--border-subtle); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
          <div style="font-size: 0.82rem; color: var(--text-tertiary);">
            Associated Heritage Sites: <strong style="color: var(--text-primary);">${active.monuments.join(', ')}</strong>
          </div>
        </div>
      </div>
    `;
  }

  function selectDynasty(id) {
    activeDynastyId = id;
    render();
  }

  return {
    init: init,
    render: render,
    selectDynasty: selectDynasty
  };
})();
