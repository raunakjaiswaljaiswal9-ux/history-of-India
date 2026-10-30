import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from report_lib import (
    add_heading_1, add_heading_2, add_heading_3, add_p, add_bullet, 
    add_image_figure
)

def build_p31(doc):
    # Page 31: Chapter 10: System Design (Part 3 - Gallery & Atlas)
    add_heading_2(doc, "10.0.3 Museum Artifact Curation & Lightbox Architecture")
    add_p(doc, 
          "The artifact gallery (`gallery.js`) acts as a virtual exhibition wing. It organizes 22 iconic historical treasures "
          "into a responsive CSS Grid with tag-based filters (Sculptures, Numismatics, Architecture, Manuscripts, Regalia).", space_after=6)
    add_bullet(doc, "Displays high-resolution museum photography with lazy-loading, title, historical era badge, and estimated creation date.", bold_prefix="Exhibition Cards: ")
    add_bullet(doc, "Clicking any artifact instantiates the modal overlay (`lightbox.js`), locking the background document scroll and preloading high-res assets.", bold_prefix="Modal Lightbox Controller: ")
    add_bullet(doc, "Provides interactive image zoom, high-contrast detail inspection, complete provenance, excavation site, curatorial notes, and bookmarking toggle.", bold_prefix="Curatorial Inspection Suite: ")

    add_heading_2(doc, "10.0.4 Imperial Interactive Atlas & SVG Geo-Mapping")
    add_p(doc, 
          "The cartography module (`atlas.js`) renders a vector map of the Indian subcontinent utilizing inline Scalable "
          "Vector Graphics (SVG). This eliminates external mapping API licensing costs and enables pixel-perfect responsive scaling.", space_after=6)
    add_bullet(doc, "Plots key archaeological sites (Mohenjo-daro, Harappa, Lothal) and dynastic capitals (Pataliputra, Thanjavur, Delhi, Vijayanagara) using calibrated latitude/longitude projection coordinates.", bold_prefix="Dynamic Geocoded Markers: ")
    add_bullet(doc, "Hovering or tapping a pin highlights its location and presents an archaeological dossier detailing founding dynasty, period, key monuments, and historical significance.", bold_prefix="Interactive Territory Popovers: ")

def build_p32(doc):
    # Page 32: Chapter 10: System Design (Part 4 - Audio Synth & Quiz)
    add_heading_2(doc, "10.0.5 Ambient Tanpura Web Audio Synthesizer Engine")
    add_p(doc, 
          "The audio subsystem (`audio.js`) implements a real-time procedural synthesizer based on the W3C Web Audio API. "
          "Rather than loading heavy recorded MP3 files, the synthesizer models an Indian classical acoustic Tanpura in software:", space_after=6)
    add_bullet(doc, "Spawns four native `OscillatorNode` instances tuned to Pa-Sa-Sa-Sa (138.59 Hz, 110.00 Hz, 110.00 Hz, and 55.00 Hz).", bold_prefix="Multi-Oscillator Harmonic Tuning: ")
    add_bullet(doc, "Routes each oscillator through dedicated `GainNode` units with programmed exponential volume ramps (ADSR envelope) simulating rhythmic acoustic plucks.", bold_prefix="Envelope & Gain Staging: ")
    add_bullet(doc, "Applies a `BiquadFilterNode` lowpass filter (cutoff 2,400 Hz) to create a warm, non-fatiguing wooden resonance suitable for long study sessions.", bold_prefix="Acoustic Resonance Filtering: ")

    add_heading_2(doc, "10.0.6 Historical Knowledge Assessment Engine")
    add_p(doc, 
          "The educational quiz engine (`quiz.js`) reinforces user learning through dynamic self-assessment:", space_after=6)
    add_bullet(doc, "Applies the Fisher-Yates algorithmic shuffle to randomize question order and option choices upon each session initiation.", bold_prefix="Dynamic Question Shuffling: ")
    add_bullet(doc, "Computes immediate score feedback, reveals detailed historical explanations upon answer submission, and persists top scores in `localStorage`.", bold_prefix="Immediate Feedback & Scoring: ")

def build_p33(doc):
    # Page 33: Chapter 10: System Design (Part 5 - Search & Pipeline 1-3)
    add_heading_2(doc, "10.0.7 Real-Time Multi-Index Search Terminal")
    add_p(doc, 
          "The search terminal (`search.js`) implements an optimized client-side text filtering algorithm. As the user types into "
          "the search input, the engine debounces the keystrokes (200ms threshold) and scans a multi-field search index spanning "
          "era titles, descriptions, dynasty rulers, landmark battles, and artifact provenance.", space_after=6)
    add_p(doc, 
          "Matching results are highlighted in real-time, instantly scrolling the viewport to relevant timeline milestones or "
          "filtering the artifact gallery with zero page reloads and sub-millisecond execution times.", space_after=6)

    add_heading_2(doc, "10.0.8 Operational Data Processing Pipeline (Stages 1 - 3)")
    add_bullet(doc, "Client loads `index.html`. Python server serves semantic DOM, CSS stylesheets, and JavaScript component modules with strict MIME types.", bold_prefix="Stage 1 - Resource Loading & DOM Mount: ")
    add_bullet(doc, "`app.js` initializes the central State Bus, loads JSON datasets (`eras.js`, `artifacts.js`, `dynasties.js`), and constructs normalized memory indices.", bold_prefix="Stage 2 - Data Ingestion & State Initialization: ")
    add_bullet(doc, "The Timeline and Gallery components dynamically generate HTML cards, inject them into the DOM, and bind event delegation listeners.", bold_prefix="Stage 3 - DOM Synthesis & Component Rendering: ")

def build_p34(doc):
    # Page 34: Chapter 10: System Design (Part 6 - Pipeline 4-7)
    add_heading_2(doc, "10.0.9 Operational Data Processing Pipeline (Stages 4 - 7)")
    add_bullet(doc, "The Atlas component parses geographical coordinates for historical capitals and renders calibrated SVG pins on the map vector layer.", bold_prefix="Stage 4 - Geospatial Coordinate Projection: ")
    add_bullet(doc, "Upon first user interaction (audio gesture), `audio.js` awakens the browser's `AudioContext`, initializes oscillator gain nodes, and starts the continuous Tanpura drone loop.", bold_prefix="Stage 5 - Web Audio DSP Initialization: ")
    add_bullet(doc, "User interactions (scrolling, clicking artifacts, searching, taking quizzes) trigger internal custom events, updating component states reactively.", bold_prefix="Stage 6 - Event Loop & User Interaction: ")
    add_bullet(doc, "User bookmarks and completed quiz scores are serialized into JSON and stored in the browser's persistent `localStorage` and synchronized with the backend REST API.", bold_prefix="Stage 7 - Client-Side Persistence & REST Sync: ")

    add_heading_2(doc, "High-Level Architecture Summary")
    add_p(doc, 
          "The complete system architecture guarantees that computationally intensive visual rendering and audio synthesis "
          "occur directly within client hardware acceleration, while the Python backend maintains lightweight, zero-latency "
          "resource delivery. This decoupled architecture is illustrated in Figure 10.0 on the following page.", space_after=4)

def build_p35(doc):
    # Page 35: Chapter 10: System Design - Architecture Diagram
    add_heading_1(doc, "Figure 10.0: High-Level System Architecture Diagram")
    add_image_figure(doc, "system_design_diagram.png", 
                     "Figure 10.0: High-Level Decoupled Architecture & Multi-Tier Processing Pipeline", width_in=6.2)
    add_p(doc, 
          "Figure 10.0 illustrates the clean separation of concerns across the Client Presentation Layer, Component Logic "
          "Engine, Web Audio DSP Synthesis Tier, and the Python Backend Persistence Services. Each layer communicates through "
          "standardized interfaces and event buses, ensuring maximum modularity and zero runtime coupling.", space_after=4)

def build_p36(doc):
    # Page 36: 10.1 Entity-Relationship (ER) Diagram (Text)
    add_heading_1(doc, "10.1 Entity-Relationship (ER) Diagram")
    add_p(doc, 
          "The Entity-Relationship (ER) model formalizes the logical and physical data relationships governing the "
          "'History of India' digital archive. The data architecture is organized into five core normalized entities "
          "to eliminate data redundancy, enforce referential integrity, and enable high-speed client-side querying.", space_after=6)

    add_heading_2(doc, "Core Architectural Entities & Cardinalities")
    add_bullet(doc, "Represents primary civilizational epochs (Ancient, Classical, Medieval, Early Modern, Colonial, Modern). Holds attributes: era_id (PK), name, date_range, summary, accent_color.", bold_prefix="1. ERAS Entity: ")
    add_bullet(doc, "Captures ruling imperial powers within an era. Holds attributes: dynasty_id (PK), era_id (FK), name, capital, duration, famous_rulers. (One-to-Many relationship with ERAS: 1 Era contains N Dynasties).", bold_prefix="2. DYNASTIES Entity: ")
    add_bullet(doc, "Catalogs physical museum treasures and monuments. Attributes: artifact_id (PK), era_id (FK), title, year, medium, museum, location, image_url. (One-to-Many: 1 Era contains N Artifacts).", bold_prefix="3. ARTIFACTS Entity: ")
    add_bullet(doc, "Maintains pedagogical self-assessment queries. Attributes: question_id (PK), era_id (FK), question, options, correct_index, explanation. (One-to-Many: 1 Era contains N Questions).", bold_prefix="4. QUIZ_QUESTIONS Entity: ")
    add_bullet(doc, "Tracks user favorites. Attributes: bookmark_id (PK), artifact_id (FK), client_uuid, saved_timestamp.", bold_prefix="5. BOOKMARKS Entity: ")

def build_p37(doc):
    # Page 37: 10.1 Entity-Relationship (ER) Diagram (Figure)
    add_heading_2(doc, "Figure 10.1: Entity-Relationship (ER) Diagram")
    add_image_figure(doc, "er_diagram.png", 
                     "Figure 10.1: Entity-Relationship (ER) Diagram of the Relational Data Model", width_in=6.2)
    add_p(doc, 
          "Figure 10.1 delineates the primary and foreign key linkages connecting `ERAS`, `DYNASTIES`, `ARTIFACTS`, "
          "`QUIZ_QUESTIONS`, and `BOOKMARKS`. Foreign key constraints guarantee referential integrity across all queries.", space_after=4)

def build_p38(doc):
    # Page 38: 10.2 Class Diagram & Object Architecture
    add_heading_1(doc, "10.2 Class Diagram & Object Architecture")
    add_p(doc, 
          "The Unified Modeling Language (UML) Class Diagram illustrates the object-oriented component architecture of the "
          "platform. Engineered using modular JavaScript ES6 classes, the design cleanly separates state management, DOM rendering, "
          "and audio signal processing into distinct collaborating classes:", space_after=6)
    
    add_image_figure(doc, "class_diagram.png", 
                     "Figure 10.2: UML Class Diagram detailing Object-Oriented Component Architecture", width_in=6.0)
    add_p(doc, 
          "As shown in Figure 10.2, `HistoryApp` acts as the central orchestrator, delegating responsibilities to `TimelineEngine`, "
          "`GalleryEngine`, `LightboxController`, `AtlasEngine`, `QuizEngine`, `AudioSynthesizer`, and `SearchEngine`.", space_after=4)

def build_p39(doc):
    # Page 39: 10.3 Activity Diagram & Operational Workflow
    add_heading_1(doc, "10.3 Activity Diagram & Operational Workflow")
    add_p(doc, 
          "The UML Activity Diagram delineates the step-by-step operational lifecycle and concurrent data transformations "
          "across four architectural swimlanes: Presentation Tier, Controller Tier, Audio Synthesizer, and Data Service:", space_after=6)
    
    add_image_figure(doc, "activity_diagram.png", 
                     "Figure 10.3: UML Activity Diagram illustrating Concurrent Execution Swimlanes & Event Workflows", width_in=6.0)
    add_p(doc, 
          "As mapped in Figure 10.3, the system initiates concurrently: while the DOM renders visual cards, the Web Audio engine "
          "prepares audio nodes in a suspended state until first user gesture, ensuring compliance with browser autoplay policies.", space_after=4)

def build_p40(doc):
    # Page 40: 10.4 Use Case Diagram & Actor Interactions
    add_heading_1(doc, "10.4 Use Case Diagram & Actor Interactions")
    add_p(doc, 
          "The UML Use Case Diagram defines the functional boundaries of the platform, specifying interactions between "
          "human actors (Student, Researcher, Quiz Taker, Curator) and external system components (Web Audio Engine, REST Service):", space_after=6)
    
    add_image_figure(doc, "use_case_diagram.png", 
                     "Figure 10.4: UML Use Case Diagram defining Functional Capabilities & Actor Interactions", width_in=6.0)
    add_p(doc, 
          "Figure 10.4 details the primary use cases: navigating civilizational timelines, inspecting artifacts in the lightbox modal, "
          "exploring historical cartography, taking interactive quizzes, engaging ambient Tanpura audio, and searching multi-field indices.", space_after=4)

print("pages_31_to_40 loaded.")
