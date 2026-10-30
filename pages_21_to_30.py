import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from report_lib import (
    add_heading_1, add_heading_2, add_heading_3, add_p, add_bullet, 
    add_image_figure, set_cell_background, set_cell_margins
)

def build_p21(doc):
    # Page 21: Chapter 7: Req Spec (Part 2 - Stack table & FR 1-3)
    add_heading_2(doc, "Technology Stack & Architecture Matrix")
    tbl_tech = doc.add_table(rows=1, cols=3)
    tbl_tech.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl_tech.rows[0].cells
    hdr[0].width = Inches(1.5)
    hdr[1].width = Inches(2.0)
    hdr[2].width = Inches(3.1)
    for i, h in enumerate(["Layer / Category", "Tool / Standard", "Operational Purpose"]):
        set_cell_background(hdr[i], "1E293B")
        set_cell_margins(hdr[i], top=45, bottom=45, left=80, right=80)
        p = hdr[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    stack = [
        ("Web Server", "Python 3.12 (http.server)", "Localhost WSGI HTTP server and REST dispatcher"),
        ("REST API", "Custom JSON Endpoints", "Handles /api/status, /api/quiz, /api/bookmarks"),
        ("Frontend UI", "HTML5 & CSS3 Variables", "Sony Darkroom high-contrast responsive interface"),
        ("Client Scripting", "Vanilla JavaScript ES6+", "Component state management, DOM events, and caching"),
        ("Audio DSP", "W3C Web Audio API", "Real-time procedural Tanpura synthesizer (OscillatorNodes)"),
        ("Vector Cartography", "Inline Scalable Vector Graphics", "Interactive geographic map of India with dynamic pins")
    ]
    for lay, tl, pur in stack:
        row = tbl_tech.add_row().cells
        row[0].width = Inches(1.5)
        row[1].width = Inches(2.0)
        row[2].width = Inches(3.1)
        bg = "F8FAFC" if (len(tbl_tech.rows) % 2 == 0) else "FFFFFF"
        for i, val in enumerate([lay, tl, pur]):
            set_cell_background(row[i], bg)
            set_cell_margins(row[i], top=30, bottom=30, left=70, right=70)
            p = row[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            r = p.add_run(val)
            r.font.name = 'Calibri'
            r.font.size = Pt(9)
            if i == 0:
                r.bold = True
            r.font.color.rgb = RGBColor(30, 41, 59)

    add_heading_2(doc, "Functional Requirements (FR-1 to FR-3)")
    add_bullet(doc, "The system must ingest structured JSON representations of six major civilizational epochs and dynamically render chronological headers and metadata.", bold_prefix="FR-1: Chronological Epoch Ingestion: ")
    add_bullet(doc, "The system must support smooth horizontal carousel panning across epochs with mouse wheel event redirection and visual scroll indicators.", bold_prefix="FR-2: Horizontal Timeline Scroller: ")
    add_bullet(doc, "The platform must provide a toggle mechanism enabling users to switch between a horizontal timeline strip and a detailed vertical chronological feed.", bold_prefix="FR-3: Dual-Mode Layout Switching: ")

def build_p22(doc):
    # Page 22: Chapter 7: Req Spec (Part 3 - FR 4-8)
    add_heading_2(doc, "Functional Requirements (FR-4 to FR-8 Continued)")
    add_bullet(doc, "The gallery must display curated museum relics with responsive CSS Grid thumbnails, category filter chips (Sculpture, Coins, Architecture, Regalia), and animated hover elevations.", bold_prefix="FR-4: Museum Artifact Gallery: ")
    add_bullet(doc, "Clicking an artifact must trigger a full-screen, accessible modal lightbox displaying high-resolution imagery, zoom controls, historical excavation origins, museum provenance, and close controls.", bold_prefix="FR-5: High-Resolution Lightbox Modal: ")
    add_bullet(doc, "The platform must render an interactive vector atlas of historical India, dynamically plotting geocoded capital cities and archaeological sites with clickable popover dossiers.", bold_prefix="FR-6: Imperial Interactive Atlas: ")
    add_bullet(doc, "The system must feature a randomized historical knowledge assessment engine that presents 10 multiple-choice questions, computes instant scores, provides corrective feedback, and tracks scores.", bold_prefix="FR-7: Knowledge Assessment Quiz Engine: ")
    add_bullet(doc, "The system must feature a real-time, debounced search terminal capable of sub-millisecond filtering across eras, dynasties, rulers, battles, and artifacts simultaneously.", bold_prefix="FR-8: Multi-Index Search Terminal: ")
    add_bullet(doc, "The platform must incorporate a procedural Web Audio synthesizer allowing users to play, pause, and adjust volume for an authentic Indian classical Tanpura drone.", bold_prefix="FR-9: Ambient Audio Synthesis: ")
    add_bullet(doc, "Users must be able to bookmark favorite artifacts and review bookmarked items in a persistent sidebar drawer stored via client-side localStorage.", bold_prefix="FR-10: Persistent Bookmarking Engine: ")

def build_p23(doc):
    # Page 23: Chapter 7: Req Spec (Part 4 - Non-Functional Requirements)
    add_heading_2(doc, "Non-Functional Requirements (NFR-1 to NFR-6)")
    add_bullet(doc, "The initial webpage, styles, scripts, and initial high-resolution assets must achieve full Time-to-Interactive (TTI) within 1.2 seconds under standard broadband conditions.", bold_prefix="NFR-1: Performance & Low Latency: ")
    add_bullet(doc, "The interface must strictly adhere to Sony Darkroom design standards, featuring a high-contrast dark palette (#0f172a, #1e293b), gold accenting (#d97706), and legible typography (Calibri/System Sans) meeting WCAG AA standards.", bold_prefix="NFR-2: Usability & Visual Contrast: ")
    add_bullet(doc, "The procedural audio synthesis engine must run without stutter, audio dropouts, or audible buffer underflows, maintaining zero thread contention with the UI main thread.", bold_prefix="NFR-3: Acoustic Fidelity & Real-Time DSP: ")
    add_bullet(doc, "All 22 museum artifact images and static web assets must be stored locally with absolute paths, guaranteeing 100% offline availability without external CDN dependency.", bold_prefix="NFR-4: Local Availability & Reliability: ")
    add_bullet(doc, "The codebase must be structured into decoupled ES6 modules (app, timeline, gallery, lightbox, atlas, quiz, audio, search) with comprehensive inline JSDoc comments.", bold_prefix="NFR-5: Maintainability & Code Modularity: ")
    add_bullet(doc, "The platform must seamlessly adapt across desktop (1920x1080), laptop (1366x768), tablet (768x1024), and smartphone (375x667) screen viewports.", bold_prefix="NFR-6: Cross-Platform Responsiveness: ")

def build_p24(doc):
    # Page 24: Chapter 8: Feasibility Study (Part 1 - Technical & Economic)
    add_heading_1(doc, "8. FEASIBILITY STUDY")
    add_p(doc, 
          "A comprehensive feasibility study was conducted prior to software development to rigorously assess whether "
          "the 'History of India' digital archive is technically viable, economically cost-effective, operationally practical, "
          "schedule-compliant, and legally sound.", space_after=6)

    add_heading_2(doc, "1. Technical Feasibility")
    add_p(doc, 
          "The platform leverages native, standardized web capabilities that are universally supported across all modern "
          "operating systems and web browsers. By utilizing Python 3.12's standard `http.server` library for localhost "
          "hosting, external runtime dependencies such as Node.js, heavy package managers, and third-party web frameworks "
          "are eliminated. Furthermore, the procedural sound synthesis relies on the W3C Web Audio API, which is natively "
          "compiled in browser engines (Blink, Gecko, WebKit). Therefore, the system is 100% technically feasible.", space_after=6)

    add_heading_2(doc, "2. Economic Feasibility")
    add_p(doc, "A comparative financial analysis demonstrates the tremendous cost-efficiency of the open-source architecture:")

    tbl_cost = doc.add_table(rows=1, cols=3)
    tbl_cost.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl_cost.rows[0].cells
    hdr[0].width = Inches(2.2)
    hdr[1].width = Inches(2.2)
    hdr[2].width = Inches(2.2)
    for i, h in enumerate(["Component / Resource", "Commercial Museum System", "History of India Platform"]):
        set_cell_background(hdr[i], "1E293B")
        set_cell_margins(hdr[i], top=45, bottom=45, left=80, right=80)
        p = hdr[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.name = 'Calibri'
        r.font.size = Pt(9.5)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    costs = [
        ("Web & App Server", "Proprietary Server ($1,200/yr)", "₹0 (Python Standard Library)"),
        ("Database Licensing", "Oracle / SQL Server ($2,500/yr)", "₹0 (Native JSON & SQLite)"),
        ("Audio Sample Licenses", "Commercial Soundfx ($450/yr)", "₹0 (Procedural Web Audio DSP)"),
        ("Museum CMS Software", "Contentdm / PastPerfect ($3,000/yr)", "₹0 (Custom Vanilla JS Engine)"),
        ("Cartography Maps API", "Google Maps Platform ($800/yr)", "₹0 (Inline Scalable Vector SVG)"),
        ("Total Annual Cost", "$7,950 (~₹6,60,000 INR)", "₹0 (100% Free & Open-Source)")
    ]
    for comp, com_c, our_c in costs:
        row = tbl_cost.add_row().cells
        row[0].width = Inches(2.2)
        row[1].width = Inches(2.2)
        row[2].width = Inches(2.2)
        bg = "F8FAFC" if (len(tbl_cost.rows) % 2 == 0) else "FFFFFF"
        for i, val in enumerate([comp, com_c, our_c]):
            set_cell_background(row[i], bg)
            set_cell_margins(row[i], top=30, bottom=30, left=70, right=70)
            p = row[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            r = p.add_run(val)
            r.font.name = 'Calibri'
            r.font.size = Pt(9)
            if i == 0 or "Total" in val:
                r.bold = True
            r.font.color.rgb = RGBColor(30, 41, 59)

def build_p25(doc):
    # Page 25: Chapter 8: Feasibility Study (Part 2 - Operational Feasibility)
    add_heading_2(doc, "3. Operational Feasibility")
    add_p(doc, 
          "Operational feasibility examines whether the target user base—consisting of secondary school students, "
          "undergraduate scholars, history teachers, and academic researchers—can seamlessly adopt and interact with the platform "
          "without requiring specialized technical training.", space_after=6)
    
    add_p(doc, 
          "The user experience is designed around intuitive physical museum interaction patterns. The dual-mode timeline allows "
          "linear navigation by dragging or mouse-scrolling. The artifact gallery behaves like a virtual exhibition hall, where "
          "clicking an artifact reveals high-definition visual details, provenance tags, and curatorial notes. The interactive "
          "atlas displays geographically accurate territory pins that reveal historical dossiers upon hover or click.", space_after=6)

    add_heading_3(doc, "User Workflow & Adoption Matrix")
    add_bullet(doc, "Instantly explore civilizational milestones, review artifact details, and test retention via the gamified quiz suite.", bold_prefix="Student Persona: ")
    add_bullet(doc, "Utilize the interactive map and timeline during classroom lectures to project dynamic chronological changes onto smartboards.", bold_prefix="Educator Persona: ")
    add_bullet(doc, "Access verified museum provenance, excavation dates, and dynastic chronologies with zero paywalls or subscription barriers.", bold_prefix="Academic Researcher: ")
    add_bullet(doc, "Verdict: Highly Operationally Feasible. The platform requires zero client software installation, launching instantly inside any web browser.", bold_prefix="Operational Evaluation Verdict: ")

def build_p26(doc):
    # Page 26: Chapter 8: Feasibility Study (Part 3 - Schedule & Legal)
    add_heading_2(doc, "4. Schedule Feasibility")
    add_p(doc, 
          "The development plan was structured across a rigorous 7-week timeline, perfectly aligned with the academic "
          "calendar of the University of Mumbai final year project submission requirements:", space_after=6)
    add_bullet(doc, "Curatorial research, historical data schema, artifact asset selection.", bold_prefix="Week 1: ")
    add_bullet(doc, "Pure Python 3.12 server development, REST endpoints, MIME routing.", bold_prefix="Week 2: ")
    add_bullet(doc, "Sony Darkroom UI architecture, dual-mode timeline component.", bold_prefix="Weeks 3-4: ")
    add_bullet(doc, "Interactive museum gallery, high-res lightbox, zoom controller.", bold_prefix="Week 5: ")
    add_bullet(doc, "SVG Imperial Atlas, procedural Web Audio Tanpura synthesizer, Quiz suite.", bold_prefix="Week 6: ")
    add_bullet(doc, "Cross-browser testing, accessibility audit, performance tuning, and project report.", bold_prefix="Week 7: ")
    add_bullet(doc, "Verdict: Schedule Feasible. All development milestones were achieved on schedule without project slippage.", bold_prefix="Schedule Evaluation Verdict: ")

    add_heading_2(doc, "5. Legal & Copyright Feasibility")
    add_bullet(doc, "All 22 historical artifacts, sculptures, and architectural photographs are in the Public Domain (CC0 / Wikimedia Commons / ASI Open Archives).", bold_prefix="Public Domain Artwork: ")
    add_bullet(doc, "All software libraries, tools, and runtimes (Python, Vanilla JS, HTML5, CSS3) are completely free, open-source, and free of proprietary licensing restrictions.", bold_prefix="Open-Source Software: ")
    add_bullet(doc, "The procedural Tanpura drone is generated algorithmically via mathematical sine wave synthesis, eliminating all copyright claims related to recorded music.", bold_prefix="Procedural Audio Synthesis: ")

def build_p27(doc):
    # Page 27: Chapter 9: Gantt Chart & Project Timeline (Narrative)
    add_heading_1(doc, "9. GANTT CHART & PROJECT TIMELINE")
    add_p(doc, 
          "The development lifecycle of the 'History of India' digital archive followed an Agile sprint schedule "
          "spanning seven weeks. The engineering workflow prioritized foundational historical data modeling and server-side "
          "stability during early sprints, followed by iterative front-end interactive component development, and culminating in "
          "real-time Web Audio synthesis and comprehensive quality assurance.", space_after=6)

    add_heading_2(doc, "Sprint Milestones & Lifecycle Breakdown")
    add_bullet(doc, "Drafting historical data structures (`eras.js`, `artifacts.js`), establishing JSON schemas, selecting 22 museum-grade artifacts, and finalizing architectural specifications.", bold_prefix="Sprint 1 (Milestone M1): ")
    add_bullet(doc, "Engineering the standalone Python 3.12 HTTP server, implementing custom request routing, establishing REST API handlers (`/api/status`, `/api/quiz`, `/api/bookmarks`), and MIME resolution.", bold_prefix="Sprint 2 (Milestone M2): ")
    add_bullet(doc, "Building the Sony Darkroom visual design system, glassmorphic layout, and dual-mode chronological timeline supporting horizontal and vertical views.", bold_prefix="Sprint 3 (Milestone M3): ")
    add_bullet(doc, "Implementing the dynamic CSS Grid gallery with category filtering, accessible modal lightbox, and high-resolution image inspection.", bold_prefix="Sprint 4 (Milestone M4): ")
    add_bullet(doc, "Developing the interactive SVG Imperial Atlas, real-time procedural Web Audio Tanpura synthesizer, and instant multi-index search terminal.", bold_prefix="Sprint 5 (Milestone M5): ")
    add_bullet(doc, "Building the randomized quiz self-assessment engine, scoring system, cross-browser validation, accessibility audit, and academic documentation.", bold_prefix="Sprint 6 (Milestone M6): ")

def build_p28(doc):
    # Page 28: Chapter 9: Gantt Chart Diagram & Milestone Analysis
    add_heading_2(doc, "Figure 9.1: Project Development Lifecycle Gantt Chart")
    add_image_figure(doc, "gantt_chart.png", 
                     "Figure 9.1: Seven-Week Agile Sprint Lifecycle & Engineering Milestones", width_in=6.2)
    add_p(doc, 
          "As depicted in Figure 9.1, each milestone proceeded with clean, overlapping agile phases, enabling continuous "
          "integration and immediate validation of client-side components with the Python backend server. The schedule allowed "
          "ample buffer time in Week 7 for rigorous testing and cross-browser benchmarking.", space_after=4)

def build_p29(doc):
    # Page 29: Chapter 10: System Design (Part 1 - Architecture Overview)
    add_heading_1(doc, "10. SYSTEM DESIGN")
    add_p(doc, 
          "The system design defines the overarching software architecture, structural modules, operational workflows, "
          "and data flows of the 'History of India' digital archive. The platform is architected around a Decoupled "
          "Multi-Tier Architecture consisting of four primary tiers: Client Presentation Tier, Application Processing Tier, "
          "Synthetic Media Engine, and Data Persistence Tier.", space_after=6)

    add_heading_2(doc, "10.0 Decoupled Multi-Tier Architectural Model")
    add_bullet(doc, "Delivers an accessible, responsive web interface adhering to the Sony Darkroom design language. Renders interactive timeline carousels, artifact exhibition grids, lightbox modal overlays, and imperial vector cartography.", bold_prefix="1. Client Presentation Tier: ")
    add_bullet(doc, "Manages client-side component orchestration, user event dispatching, debounced search filtering, quiz state management, and asynchronous REST communication with the backend.", bold_prefix="2. Application Processing Tier: ")
    add_bullet(doc, "Generates real-time acoustic atmospheres using the W3C Web Audio API. Computes mathematical frequency oscillations and harmonic overtones for authentic classical Tanpura drone synthesis without audio streaming overhead.", bold_prefix="3. Synthetic Media Engine: ")
    add_bullet(doc, "Maintains structured JSON datasets of civilizational eras, dynasties, and curated museum relics. Provides local browser storage for client bookmarks and quiz scores, with optional SQLite relational persistence.", bold_prefix="4. Data Persistence Tier: ")

def build_p30(doc):
    # Page 30: Chapter 10: System Design (Part 2 - Timeline & Presentation)
    add_heading_2(doc, "10.0.1 Client Presentation Layer & Interactive Canvas")
    add_p(doc, 
          "The presentation layer is engineered using semantic HTML5 and modern CSS3 Custom Properties. It adheres to a "
          "carefully calibrated 'Sony Darkroom' aesthetic characterized by deep slate backgrounds (`#0f172a`), obsidian card "
          "containers (`#1e293b`), crisp typography, and warm amber accents (`#d97706`). CSS Grid and Flexbox layouts ensure "
          "fluid responsiveness across ultra-wide monitors, standard laptops, tablets, and smartphones.", space_after=6)

    add_heading_2(doc, "10.0.2 Dual-Mode Chronological Timeline Engine")
    add_p(doc, 
          "The timeline module (`timeline.js`) provides two distinct visual representations of Indian civilizational history:")
    add_bullet(doc, "Presents epochs along an elongated chronological axis. The component intercepts vertical mouse wheel events and smoothly translates them into horizontal scroll offsets (`scrollLeft += deltaY`), allowing intuitive desktop navigation.", bold_prefix="Horizontal Era Carousel: ")
    add_bullet(doc, "Renders an expansive vertical stream where civilizational milestones, royal successions, cultural breakthroughs, and territorial expansions appear as alternating milestone cards linked by an illuminated central spine.", bold_prefix="Vertical Historical Feed: ")
    add_bullet(doc, "An accessible toggle button in the navigation header allows users to switch between horizontal and vertical views instantly without re-rendering or reloading data.", bold_prefix="Seamless Viewport Toggle: ")

print("pages_21_to_30 loaded.")
