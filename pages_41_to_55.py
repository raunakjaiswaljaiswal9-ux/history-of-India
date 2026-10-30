import docx
from docx.shared import Inches, Pt, RGBColor
from report_lib import (
    add_heading_1, add_heading_2, add_heading_3, add_p, add_code_snippet
)

def build_p41(doc):
    # Page 41: 11.1 Backend Architecture - server.py
    add_heading_1(doc, "11. CODE IMPLEMENTATION")
    add_p(doc, 
          "This section presents the core source code implementation of the 'History of India' digital archive. "
          "The platform is engineered using standard Python 3.12 for localhost server services and native ES6+ JavaScript, "
          "HTML5, CSS3, and the Web Audio API for the client-side presentation and audio synthesis.", space_after=4)
    add_heading_2(doc, "11.1 Backend Architecture: server.py HTTP Server & MIME Router")
    add_p(doc, "Implements a custom HTTP server using Python's standard library with strict MIME type resolution:", space_after=4)
    
    code = """import os, sys, json, mimetypes
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class HistoryHTTPRequestHandler(SimpleHTTPRequestHandler):
    \"\"\"Custom Request Handler with REST API dispatching and MIME handling.\"\"\"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def guess_type(self, path):
        ctype, encoding = mimetypes.guess_type(path)
        if path.endswith('.js'): return 'application/javascript'
        if path.endswith('.css'): return 'text/css'
        if path.endswith('.json'): return 'application/json'
        if path.endswith('.svg'): return 'image/svg+xml'
        return ctype or 'application/octet-stream'

    def do_GET(self):
        if self.path.startswith('/api/'):
            return self.handle_api_get()
        return super().do_GET()"""
    add_code_snippet(doc, code, "server.py - HTTP Server & MIME Mapping")

def build_p42(doc):
    # Page 42: 11.2 Backend REST API Endpoints - server.py
    add_heading_2(doc, "11.2 Backend REST API Endpoints: Status, Quiz & Bookmarks")
    add_p(doc, "Handles client-side asynchronous REST API endpoints for server status and user data serialization:", space_after=4)

    code = """    def handle_api_get(self):
        if self.path == '/api/status':
            payload = {
                "status": "online",
                "platform": "History of India Digital Archive",
                "version": "1.0.0",
                "student": "Raunak Dilip Jaiswal",
                "institution": "V.K. Krishna Menon College",
                "engine": "Python 3.12 Standard Library",
                "endpoints": ["/api/status", "/api/quiz", "/api/bookmarks"]
            }
            self.send_json_response(payload)
        elif self.path == '/api/quiz':
            # Load and return quiz questions from persistent storage
            quiz_path = os.path.join(DIRECTORY, 'data', 'quiz.json')
            if os.path.exists(quiz_path):
                with open(quiz_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.send_json_response(data)
            else:
                self.send_json_response({"questions": [], "count": 0})
        else:
            self.send_error(404, "Endpoint Not Found")

    def send_json_response(self, data, code=200):
        body = json.dumps(data, indent=2).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)"""
    add_code_snippet(doc, code, "server.py - REST API Handlers & JSON Serializer")

def build_p43(doc):
    # Page 43: 11.3 Historical Eras Model - eras.js
    add_heading_2(doc, "11.3 Historical Eras Data Model: js/data/eras.js")
    add_p(doc, "Defines chronological civilizational epochs, time spans, summaries, and thematic accent palettes:", space_after=4)

    code = """export const ERAS_DATA = [
  {
    id: "ancient",
    title: "Ancient India & Indus Civilization",
    period: "c. 2500 BCE – 322 BCE",
    accentColor: "#d97706",
    summary: "From urban planning at Mohenjo-daro to the Vedic hymnody and Mahajanapadas.",
    dynasties: [
      { name: "Indus Valley Civilization", period: "c. 2500 – 1900 BCE", capital: "Mohenjo-daro / Harappa" },
      { name: "Vedic Period", period: "c. 1500 – 500 BCE", capital: "Saraswati-Ganga Plains" },
      { name: "Mahajanapadas", period: "c. 600 – 322 BCE", capital: "Magadha (Rajgir / Pataliputra)" }
    ],
    milestones: [
      { year: "2500 BCE", event: "Peak of Indus Valley urban sanitation & bronze metallurgy." },
      { year: "1500 BCE", event: "Composition of the Rigveda, world's oldest extant religious text." },
      { year: "563 BCE",  event: "Birth of Siddhartha Gautama (The Buddha) in Lumbini." }
    ]
  },
  {
    id: "classical",
    title: "Classical Empires & Golden Age",
    period: "322 BCE – 550 CE",
    accentColor: "#f59e0b",
    summary: "Ashoka's moral statecraft, the Gupta scientific renaissance, and Buddhist stupas.",
    dynasties: [
      { name: "Maurya Empire", period: "322 – 185 BCE", capital: "Pataliputra" },
      { name: "Gupta Empire",  period: "319 – 550 CE",   capital: "Pataliputra / Ujjain" }
    ]
  }
];"""
    add_code_snippet(doc, code, "js/data/eras.js - Chronological Epochs Schema")

def build_p44(doc):
    # Page 44: 11.4 Artifact Catalog - artifacts.js
    add_heading_2(doc, "11.4 Artifact Catalog & Metadata Engine: js/data/artifacts.js")
    add_p(doc, "Catalogs 22 curated museum treasures with high-resolution imagery, provenance, and coordinates:", space_after=4)

    code = """export const ARTIFACTS_DATA = [
  {
    id: "dancing-girl",
    title: "Dancing Girl of Mohenjo-daro",
    eraId: "ancient",
    category: "Sculpture",
    year: "c. 2300–1750 BCE",
    medium: "Bronze lost-wax casting (Cire perdue)",
    origin: "Mohenjo-daro, Indus Valley Civilization",
    currentLocation: "National Museum, New Delhi",
    dimensions: "10.5 cm x 5 cm x 2.5 cm",
    imageUrl: "images/dancing_girl.png",
    coordinates: { lat: 27.3292, lng: 68.1388 },
    description: "Iconic masterpiece of prehistoric bronze sculpture depicting a confident young woman standing in a naturalistic pose with bangles and necklace, demonstrating advanced metallurgical knowledge."
  },
  {
    id: "ashoka-lion-capital",
    title: "Lion Capital of Ashoka",
    eraId: "classical",
    category: "Sculpture",
    year: "c. 250 BCE",
    medium: "Polished Chunar sandstone",
    origin: "Sarnath, Uttar Pradesh",
    currentLocation: "Sarnath Museum (National Emblem of India)",
    imageUrl: "images/lion_capital.png",
    coordinates: { lat: 25.3811, lng: 83.0214 },
    description: "Carved out of a single block of sandstone, featuring four Asiatic lions standing back to back, mounted on an abacus with an elephant, a galloping horse, a zebu bull, and a lion, separated by Dharma Chakras."
  }
];"""
    add_code_snippet(doc, code, "js/data/artifacts.js - Museum Provenance Schema")

def build_p45(doc):
    # Page 45: 11.5 Main Controller - app.js
    add_heading_2(doc, "11.5 Platform Controller & State Bus: js/app.js")
    add_p(doc, "Bootstraps all component modules, manages global state bus, and coordinates view events:", space_after=4)

    code = """import { ERAS_DATA } from './data/eras.js';
import { ARTIFACTS_DATA } from './data/artifacts.js';
import { TimelineComponent } from './components/timeline.js';
import { GalleryComponent } from './components/gallery.js';
import { LightboxComponent } from './components/lightbox.js';
import { AtlasComponent } from './components/atlas.js';
import { AudioComponent } from './components/audio.js';
import { SearchComponent } from './components/search.js';
import { QuizComponent } from './components/quiz.js';

class HistoryApp {
  constructor() {
    this.state = {
      activeEra: 'ancient',
      viewMode: 'horizontal', // 'horizontal' or 'vertical'
      searchQuery: '',
      bookmarks: JSON.parse(localStorage.getItem('hoi_bookmarks') || '[]'),
      isAudioPlaying: false
    };
  }

  init() {
    console.log('[*] Initializing History of India Web Platform...');
    this.timeline = new TimelineComponent(this);
    this.gallery = new GalleryComponent(this);
    this.lightbox = new LightboxComponent(this);
    this.atlas = new AtlasComponent(this);
    this.audio = new AudioComponent(this);
    this.search = new SearchComponent(this);
    this.quiz = new QuizComponent(this);

    this.bindGlobalListeners();
    this.timeline.render(ERAS_DATA);
    this.gallery.render(ARTIFACTS_DATA);
    this.atlas.render(ARTIFACTS_DATA);
  }
}
document.addEventListener('DOMContentLoaded', () => new HistoryApp().init());"""
    add_code_snippet(doc, code, "js/app.js - Central State Bus & Controller")

def build_p46(doc):
    # Page 46: 11.6 Dual-Mode Timeline - timeline.js
    add_heading_2(doc, "11.6 Dual-Mode Timeline Engine: js/components/timeline.js")
    add_p(doc, "Renders horizontal carousel and vertical feed with mouse wheel translation and view toggling:", space_after=4)

    code = """export class TimelineComponent {
  constructor(app) {
    this.app = app;
    this.container = document.getElementById('timeline-container');
    this.modeToggleBtn = document.getElementById('timeline-mode-toggle');
  }

  render(eras) {
    if (this.app.state.viewMode === 'horizontal') {
      this.renderHorizontalCarousel(eras);
    } else {
      this.renderVerticalFeed(eras);
    }
    this.bindScrollEvents();
  }

  renderHorizontalCarousel(eras) {
    this.container.className = 'timeline-strip horizontal-view';
    this.container.innerHTML = eras.map(era => `
      <div class="era-card" data-era="${era.id}" style="--accent: ${era.accentColor}">
        <span class="era-period">${era.period}</span>
        <h3 class="era-title">${era.title}</h3>
        <p class="era-summary">${era.summary}</p>
        <div class="dynasties-chips">
          ${era.dynasties.map(d => `<span class="chip">${d.name}</span>`).join('')}
        </div>
      </div>
    `).join('');
  }

  bindScrollEvents() {
    this.container.addEventListener('wheel', (e) => {
      if (this.app.state.viewMode === 'horizontal' && e.deltaY !== 0) {
        e.preventDefault();
        this.container.scrollLeft += e.deltaY * 1.5;
      }
    }, { passive: false });
  }
}"""
    add_code_snippet(doc, code, "js/components/timeline.js - Dual-Mode Timeline")

def build_p47(doc):
    # Page 47: 11.7 Artifact Gallery - gallery.js
    add_heading_2(doc, "11.7 Artifact Gallery & Filter Engine: js/components/gallery.js")
    add_p(doc, "Manages dynamic CSS Grid rendering, category filtering, and artifact card click delegation:", space_after=4)

    code = """export class GalleryComponent {
  constructor(app) {
    this.app = app;
    this.grid = document.getElementById('artifact-grid');
    this.filterContainer = document.getElementById('gallery-filters');
    this.currentCategory = 'ALL';
  }

  render(artifacts) {
    this.renderFilterButtons();
    const filtered = this.currentCategory === 'ALL' 
      ? artifacts 
      : artifacts.filter(a => a.category === this.currentCategory);

    this.grid.innerHTML = filtered.map(item => `
      <article class="artifact-card" data-id="${item.id}" tabindex="0">
        <div class="card-image-box">
          <img src="${item.imageUrl}" alt="${item.title}" loading="lazy" />
          <span class="badge category-badge">${item.category}</span>
        </div>
        <div class="card-body">
          <span class="artifact-era">${item.year}</span>
          <h4 class="artifact-title">${item.title}</h4>
          <p class="artifact-origin"><i class="icon-pin"></i> ${item.origin}</p>
        </div>
      </article>
    `).join('');

    this.grid.querySelectorAll('.artifact-card').forEach(card => {
      card.addEventListener('click', () => {
        const id = card.dataset.id;
        const artifact = artifacts.find(a => a.id === id);
        this.app.lightbox.open(artifact);
      });
    });
  }
}"""
    add_code_snippet(doc, code, "js/components/gallery.js - Gallery Grid & Filters")

def build_p48(doc):
    # Page 48: 11.8 Modal Lightbox - lightbox.js
    add_heading_2(doc, "11.8 High-Resolution Lightbox System: js/components/lightbox.js")
    add_p(doc, "Provides accessible modal overlay, high-resolution image zoom, and metadata tabs:", space_after=4)

    code = """export class LightboxComponent {
  constructor(app) {
    this.app = app;
    this.modal = document.getElementById('lightbox-modal');
    this.imgEl = document.getElementById('lightbox-img');
    this.titleEl = document.getElementById('lightbox-title');
    this.metaEl = document.getElementById('lightbox-meta');
    this.closeBtn = document.getElementById('lightbox-close');
    this.isZoomed = false;

    this.closeBtn.addEventListener('click', () => this.close());
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.modal.classList.contains('active')) this.close();
    });
  }

  open(artifact) {
    this.imgEl.src = artifact.imageUrl;
    this.titleEl.textContent = artifact.title;
    this.metaEl.innerHTML = `
      <div class="meta-row"><strong>Period:</strong> <span>${artifact.year}</span></div>
      <div class="meta-row"><strong>Medium:</strong> <span>${artifact.medium}</span></div>
      <div class="meta-row"><strong>Excavation / Origin:</strong> <span>${artifact.origin}</span></div>
      <div class="meta-row"><strong>Current Provenance:</strong> <span>${artifact.currentLocation}</span></div>
      <p class="curatorial-notes">${artifact.description}</p>
    `;
    this.modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}"""
    add_code_snippet(doc, code, "js/components/lightbox.js - Lightbox Modal")

def build_p49(doc):
    # Page 49: 11.9 Imperial Atlas - atlas.js
    add_heading_2(doc, "11.9 Imperial Atlas & Geo-Mapping: js/components/atlas.js")
    add_p(doc, "Renders interactive vector map with plotted historical coordinates and popover dossiers:", space_after=4)

    code = """export class AtlasComponent {
  constructor(app) {
    this.app = app;
    this.svgContainer = document.getElementById('imperial-atlas-svg');
    this.tooltip = document.getElementById('map-tooltip');
  }

  render(artifacts) {
    // Project geographical latitude and longitude onto SVG canvas viewBox (800 x 900)
    const pinsHtml = artifacts.map(item => {
      const x = this.projectLongitude(item.coordinates.lng);
      const y = this.projectLatitude(item.coordinates.lat);
      return `
        <g class="map-pin" data-id="${item.id}" transform="translate(${x}, ${y})">
          <circle r="7" class="pin-pulse" />
          <circle r="4" class="pin-core" />
          <text x="10" y="4" class="pin-label">${item.title}</text>
        </g>
      `;
    }).join('');

    this.svgContainer.querySelector('.pins-layer').innerHTML = pinsHtml;
    this.bindHoverEvents(artifacts);
  }

  projectLongitude(lng) {
    // Calibrated projection for Indian Subcontinent: 68°E to 97°E -> SVG X (50 to 750)
    return 50 + ((lng - 68.0) / (97.0 - 68.0)) * 700;
  }

  projectLatitude(lat) {
    // Calibrated projection: 8°N to 37°N -> SVG Y (850 to 50)
    return 850 - ((lat - 8.0) / (37.0 - 8.0)) * 800;
  }
}"""
    add_code_snippet(doc, code, "js/components/atlas.js - Cartographic Projection")

def build_p50(doc):
    # Page 50: 11.10 Knowledge Quiz Engine - quiz.js
    add_heading_2(doc, "11.10 Historical Knowledge Quiz Engine: js/components/quiz.js")
    add_p(doc, "Implements dynamic question shuffling, option randomization, and score calculation:", space_after=4)

    code = """export class QuizComponent {
  constructor(app) {
    this.app = app;
    this.currentQuestionIdx = 0;
    this.score = 0;
    this.questions = [];
  }

  initQuiz(rawQuestions) {
    this.questions = this.shuffleArray([...rawQuestions]);
    this.currentQuestionIdx = 0;
    this.score = 0;
    this.renderQuestion();
  }

  shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  submitAnswer(selectedIdx) {
    const q = this.questions[this.currentQuestionIdx];
    const isCorrect = (selectedIdx === q.correctIndex);
    if (isCorrect) this.score += 10;

    this.showFeedbackModal(isCorrect, q.explanation);
    this.currentQuestionIdx++;
    if (this.currentQuestionIdx < this.questions.length) {
      setTimeout(() => this.renderQuestion(), 1500);
    } else {
      this.renderScoreSummary();
    }
  }
}"""
    add_code_snippet(doc, code, "js/components/quiz.js - Dynamic Quiz Engine")

def build_p51(doc):
    # Page 51: 11.11 Ambient Web Audio Synthesizer - audio.js
    add_heading_2(doc, "11.11 Ambient Web Audio Synthesizer: js/components/audio.js")
    add_p(doc, "Generates authentic Indian classical Tanpura drone using multi-oscillator additive synthesis:", space_after=4)

    code = """export class AudioComponent {
  constructor(app) {
    this.app = app;
    this.audioCtx = null;
    this.masterGain = null;
    this.oscillators = [];
    this.isPlaying = false;
    // Pa-Sa-Sa-Sa classical tuning frequencies (C# base at 138.59 Hz)
    this.tuning = [138.59, 110.00, 110.00, 55.00];
  }

  startDrone() {
    if (!this.audioCtx) {
      this.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }

    this.masterGain = this.audioCtx.createGain();
    this.masterGain.gain.setValueAtTime(0.2, this.audioCtx.currentTime);
    this.masterGain.connect(this.audioCtx.destination);

    this.tuning.forEach((freq, idx) => {
      const osc = this.audioCtx.createOscillator();
      const oscGain = this.audioCtx.createGain();
      
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(freq, this.audioCtx.currentTime);
      oscGain.gain.setValueAtTime(0.08, this.audioCtx.currentTime);

      osc.connect(oscGain);
      oscGain.connect(this.masterGain);
      osc.start();
      this.oscillators.push(osc);
    });
    this.isPlaying = true;
  }
}"""
    add_code_snippet(doc, code, "js/components/audio.js - Procedural Web Audio Synth")

def build_p52(doc):
    # Page 52: 11.12 Multi-Index Search Terminal - search.js
    add_heading_2(doc, "11.12 Real-Time Search Terminal: js/components/search.js")
    add_p(doc, "Implements debounced multi-field substring matching across eras, rulers, and artifacts:", space_after=4)

    code = """export class SearchComponent {
  constructor(app) {
    this.app = app;
    this.searchInput = document.getElementById('site-search-input');
    this.resultsOverlay = document.getElementById('search-results-overlay');
    this.debounceTimer = null;

    this.searchInput.addEventListener('input', (e) => {
      clearTimeout(this.debounceTimer);
      this.debounceTimer = setTimeout(() => this.executeSearch(e.target.value), 200);
    });
  }

  executeSearch(term) {
    const q = term.trim().toLowerCase();
    if (q.length < 2) {
      this.resultsOverlay.style.display = 'none';
      return;
    }

    const eraHits = this.app.erasData.filter(e => 
      e.title.toLowerCase().includes(q) || e.summary.toLowerCase().includes(q)
    );
    const artifactHits = this.app.artifactsData.filter(a =>
      a.title.toLowerCase().includes(q) || a.medium.toLowerCase().includes(q) || a.origin.toLowerCase().includes(q)
    );

    this.renderSearchResults(eraHits, artifactHits, q);
  }
}"""
    add_code_snippet(doc, code, "js/components/search.js - Debounced Search Engine")

def build_p53(doc):
    # Page 53: 11.13 Design System - style.css
    add_heading_2(doc, "11.13 Design System & Theme: css/style.css")
    add_p(doc, "Establishes Sony Darkroom color palette, typography hierarchy, and CSS Custom Properties:", space_after=4)

    code = """:root {
  /* Sony Darkroom Palette */
  --bg-primary: #0b0f19;
  --bg-surface: #111827;
  --bg-elevated: #1f2937;
  --border-subtle: #374151;
  --border-focus: #d97706;

  /* Typography Colors */
  --text-primary: #f9fafb;
  --text-secondary: #9ca3af;
  --text-muted: #6b7280;
  --text-accent: #f59e0b;

  /* Accent & Thematic Tones */
  --gold-glow: rgba(217, 119, 6, 0.25);
  --gold-hover: #b45309;

  /* Layout Spacing */
  --container-max-width: 1360px;
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --transition-smooth: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: 'Calibri', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}"""
    add_code_snippet(doc, code, "css/style.css - Sony Darkroom Custom Properties")

def build_p54(doc):
    # Page 54: 11.14 UI Components & Glassmorphism - components.css
    add_heading_2(doc, "11.14 UI Components & Glassmorphism: css/components.css")
    add_p(doc, "Styles glassmorphic modal overlays, interactive artifact cards, and animated buttons:", space_after=4)

    code = """.artifact-card {
  background: rgba(31, 41, 55, 0.7);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: var(--transition-smooth);
  cursor: pointer;
}

.artifact-card:hover {
  transform: translateY(-4px);
  border-color: var(--border-focus);
  box-shadow: 0 12px 24px -10px var(--gold-glow);
}

.lightbox-modal {
  position: fixed;
  inset: 0;
  background: rgba(11, 15, 25, 0.88);
  backdrop-filter: blur(16px);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
  z-index: 1000;
}

.lightbox-modal.active {
  opacity: 1;
  pointer-events: auto;
}"""
    add_code_snippet(doc, code, "css/components.css - Glassmorphic UI Components")

def build_p55(doc):
    # Page 55: 11.15 Client Entrypoint - index.html
    add_heading_2(doc, "11.15 Client Entrypoint: index.html Semantic Markup")
    add_p(doc, "Semantic HTML5 structural layout, viewport meta configuration, and script bootstrapping:", space_after=4)

    code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>History of India | Interactive Digital Archive</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body class="sony-darkroom-theme">
  <header class="app-header">
    <div class="header-container">
      <div class="brand-group">
        <span class="chakra-emblem"></span>
        <h1 class="brand-title">HISTORY OF INDIA</h1>
      </div>
      <div class="header-controls">
        <input type="search" id="site-search-input" placeholder="Search 5,000 years of history..." />
        <button id="audio-synth-toggle" class="btn btn-audio"><i class="icon-music"></i> Tanpura Drone</button>
        <button id="timeline-mode-toggle" class="btn btn-toggle"><i class="icon-layout"></i> Toggle View</button>
      </div>
    </div>
  </header>

  <main class="app-viewport">
    <section id="timeline-section" class="viewport-section"></section>
    <section id="gallery-section" class="viewport-section"></section>
    <section id="atlas-section" class="viewport-section"></section>
    <section id="quiz-section" class="viewport-section"></section>
  </main>

  <script type="module" src="js/app.js"></script>
</body>
</html>"""
    add_code_snippet(doc, code, "index.html - Semantic Client Entrypoint")

print("pages_41_to_55 loaded.")
