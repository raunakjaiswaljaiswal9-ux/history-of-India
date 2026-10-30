import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from report_lib import (
    add_heading_1, add_heading_2, add_heading_3, add_p, add_bullet, 
    set_cell_background, set_cell_margins
)

def build_p11(doc):
    # Page 11: Chapter 3: Introduction
    add_heading_1(doc, "3. INTRODUCTION")
    add_p(doc, 
          "The history of the Indian subcontinent represents an unbroken continuum of civilizational evolution spanning "
          "over five millennia. From the planned urban grids and advanced drainage systems of the Bronze Age Indus Valley "
          "Civilization (c. 2500 BCE) to the intellectual revelations of the Vedic corpus, the pan-Indian administrative "
          "unification under the Maurya Empire, the mathematical and cultural Golden Age of the Guptas, the architectural "
          "grandeur of the Cholas and Mughals, through the crucible of the colonial struggle to the birth of the world's "
          "largest modern democracy in 1947, Indian history is profound in scope and unmatched in cultural diversity.", space_after=6)
    
    add_p(doc, 
          "Despite this extraordinary richness, contemporary digital dissemination of Indian history is severely hampered "
          "by outdated interfaces, static encyclopedic entries, and fragmented archives. Educational institutions and learners "
          "rely heavily on text-dense textbooks or commercial video portals that offer passive consumption rather than active, "
          "inquiry-based exploration. Key historical dimensions—such as spatial geographic movement, chronological simultaneity "
          "across regions, tactile artifact examination, and authentic period acoustics—are entirely missing from existing platforms.", space_after=6)

    add_p(doc, 
          "To bridge this civilizational and technological divide, this project introduces \"History of India: An Interactive "
          "Digital Archive & Full-Stack Web Platform\". Engineered by Mr. Raunak Dilip Jaiswal, the platform synthesizes "
          "modern full-stack web engineering, digital humanities curation, interactive cartography, and procedural audio synthesis "
          "into an accessible, institutional-grade digital terminal. By presenting history as an interconnected visual, spatial, "
          "and chronological continuum, the platform transforms static history into a living, interactive digital museum.", space_after=4)

def build_p12(doc):
    # Page 12: Chapter 4: Objectives (Part 1)
    add_heading_1(doc, "4. OBJECTIVES")
    add_p(doc, 
          "The overarching aim of the 'History of India' platform is to engineer an autonomous, resilient, and engaging "
          "web-based digital museum that democratizes access to verified Indian civilizational history for students, researchers, "
          "and cultural enthusiasts worldwide. The platform eliminates dependence on bloated third-party frameworks by utilizing "
          "pure native web standards and Python backend services.", space_after=6)

    add_heading_2(doc, "Primary Objective")
    add_p(doc, 
          "To conceptualize, design, implement, and benchmark a full-stack interactive digital archive that seamlessly unifies "
          "chronological civilizational timelines, high-resolution museum artifact curation, interactive geographic cartography, "
          "pedagogical self-assessment quizzes, and procedural ambient audio synthesis within a unified, high-contrast darkroom "
          "aesthetic.", space_after=6)

    add_heading_2(doc, "Specific Technical & Curatorial Objectives")
    add_bullet(doc, "Design and implement a responsive, dual-layout chronological navigation system that allows users to toggle seamlessly between a horizontal scrolling era strip and a detailed vertical historical feed with milestone cards.", bold_prefix="1. Dual-Mode Chronological Timeline Engine: ")
    add_bullet(doc, "Curate and ingest 22 high-resolution museum artifacts representing each epoch, complete with archaeological provenance, excavation origins, curatorial summaries, and full-screen modal zoom inspection.", bold_prefix="2. Museum Artifact Curation & Lightbox Inspection: ")
    add_bullet(doc, "Engineer an interactive vector map of historical India displaying key civilizational focal points, dynastic capitals, and dynamic coordinate markers with detailed popover dossiers upon user interaction.", bold_prefix="3. Imperial Interactive Atlas & Geo-Mapping: ")

def build_p13(doc):
    # Page 13: Chapter 4: Objectives (Part 2)
    add_heading_2(doc, "Specific Technical & Curatorial Objectives (Continued)")
    add_bullet(doc, "Develop an interactive, randomized knowledge self-assessment engine featuring dynamic question shuffling, era-based categorization, instant score calculation, corrective explanations, and local result persistence.", bold_prefix="4. Pedagogical Knowledge Quiz Suite: ")
    add_bullet(doc, "Implement a real-time procedural audio synthesis engine utilizing the browser's native Web Audio API to generate an authentic, continuous Indian classical Tanpura drone (Pa-Sa-Sa-Sa tuning) with zero external audio assets.", bold_prefix="5. Ambient Web Audio Synthesizer: ")
    add_bullet(doc, "Deliver a sub-millisecond client-side multi-index search terminal capable of instant substring filtering across historical eras, dynasties, key rulers, major battles, and museum artifacts.", bold_prefix="6. Real-Time Multi-Index Search Terminal: ")
    add_bullet(doc, "Build an ultra-lightweight, zero-dependency Python WSGI/HTTP server capable of serving static assets, resolving proper MIME types, and handling REST API endpoints (/api/status, /api/quiz, /api/bookmarks) on localhost.", bold_prefix="7. Lightweight Zero-Dependency Backend Architecture: ")

    add_heading_2(doc, "Measurable Success Criteria")
    add_bullet(doc, "The entire web application must initialize and achieve Interactive status in under 1.2 seconds on standard broadband connections.", bold_prefix="Sub-Second Latency: ")
    add_bullet(doc, "Zero broken image links across all 22 high-resolution curated museum assets, verified via automated SHA-256 integrity checks.", bold_prefix="Curatorial Asset Integrity: ")
    add_bullet(doc, "Complete functionality across Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari across desktop, tablet, and mobile viewport sizes.", bold_prefix="Cross-Device Responsiveness: ")

def build_p14(doc):
    # Page 14: Chapter 5: Scope (Part 1 - Functional Scope)
    add_heading_1(doc, "5. SCOPE")
    add_p(doc, 
          "The scope of the 'History of India' project encompasses the architectural design, curatorial research, full-stack "
          "software engineering, and performance benchmarking of an end-to-end interactive digital archive. The functional, "
          "historical, technical, and boundary dimensions of the platform are demarcated as follows:", space_after=6)

    add_heading_2(doc, "1. Functional Scope")
    add_bullet(doc, "Provides bidirectional chronological navigation spanning six distinct epochs (Ancient, Classical, Medieval, Early Modern, Colonial, and Modern). Supports interactive card expansion, key event tagging, and visual ruler highlights.", bold_prefix="Chronological Navigation Module: ")
    add_bullet(doc, "Organizes 22 artifacts into categorical collections (Sculpture, Numismatics, Manuscripts, Architecture, Royal Regalia). Implements a responsive CSS Grid with tag-based filtering and instant modal lightbox inspection.", bold_prefix="Museum Artifact Curation & Lightbox: ")
    add_bullet(doc, "Renders an interactive SVG-based map of the Indian subcontinent with plotted historical coordinates for Mohenjo-daro, Pataliputra, Thanjavur, Delhi, Vijayanagara, and Kolkata with detailed historical dossiers.", bold_prefix="Imperial Interactive Atlas: ")
    add_bullet(doc, "Includes a bank of 10 comprehensive multi-choice historical questions evaluating student comprehension with real-time feedback, detailed explanations, and performance scoring.", bold_prefix="Knowledge Self-Assessment Engine: ")

def build_p15(doc):
    # Page 15: Chapter 5: Scope (Part 2 - Historical Coverage & User Scope)
    add_heading_2(doc, "2. Historical & Curatorial Coverage Scope")
    add_bullet(doc, "Indus Valley Civilization, Vedic Age, and Mahajanapadas (c. 2500 BCE - 322 BCE). Focuses on urban planning, Pashupati seals, and foundational philosophical texts.", bold_prefix="Ancient India: ")
    add_bullet(doc, "Maurya Empire and Gupta Golden Age (322 BCE - 550 CE). Highlights Ashoka's Edicts, Arthashastra statecraft, Aryabhata's mathematics, and classical Sanskrit literature.", bold_prefix="Classical & Golden Age: ")
    add_bullet(doc, "Delhi Sultanate, Chola Maritime Hegemony, and Vijayanagara Empire (550 CE - 1526 CE). Covers temple architecture, oceanic trade routes, and Indo-Islamic cultural fusion.", bold_prefix="Medieval Era: ")
    add_bullet(doc, "Mughal Empire and Maratha Confederacy (1526 CE - 1857 CE). Examines administrative consolidation, monumental architecture (Taj Mahal), and Maratha naval resistance.", bold_prefix="Early Modern Era: ")
    add_bullet(doc, "East India Company, British Raj, and the Freedom Struggle (1857 CE - 1947 CE). Traces civil resistance, 1857 uprising, and constitutional development under Mahatma Gandhi.", bold_prefix="Colonial Era & Freedom Movement: ")
    add_bullet(doc, "Post-Independence consolidation, Constitution of 1950, and technological emergence as the world's largest democracy (1947 - Present).", bold_prefix="Modern Republic of India: ")

    add_heading_2(doc, "3. Target User Scope")
    add_bullet(doc, "Secondary and collegiate students exploring Indian history for examinations and academic curricula.", bold_prefix="Academic Students: ")
    add_bullet(doc, "Historians, curators, and educators requiring quick reference to chronological timelines, artifacts, and geographical coordinate data.", bold_prefix="Educators & Researchers: ")

def build_p16(doc):
    # Page 16: Chapter 5: Scope (Part 3 - Technical Scope & Boundaries)
    add_heading_2(doc, "4. Technical & Architectural Scope")
    add_bullet(doc, "Pure Python 3.12 standard library HTTP server with custom request dispatching, REST API routing, dynamic file serving, and JSON persistence.", bold_prefix="Backend Infrastructure: ")
    add_bullet(doc, "Vanilla ES6+ JavaScript utilizing modular component architecture (State Bus, Timeline, Gallery, Lightbox, Atlas, Quiz, Audio, Search) with zero runtime dependencies.", bold_prefix="Frontend Architecture: ")
    add_bullet(doc, "Modern CSS3 utilizing Custom Properties, CSS Grid, Flexbox, and Glassmorphism inspired by Sony's premium darkroom user interfaces.", bold_prefix="Styling & Aesthetic Framework: ")
    add_bullet(doc, "Native W3C Web Audio API implementing real-time additive sound synthesis via OscillatorNodes and BiquadFilterNodes.", bold_prefix="Acoustic Synthesis Engine: ")

    add_heading_2(doc, "5. Curatorial Boundaries & System Constraints")
    add_bullet(doc, "All included artifacts and historical photographs are strictly sourced from public domain museum archives (National Museum New Delhi, British Museum, ASI) under CC0 or open educational licenses.", bold_prefix="Public Domain Heritage Integrity: ")
    add_bullet(doc, "The current release operates locally on localhost:8000 for academic evaluation, with modular architecture prepared for cloud deployment.", bold_prefix="Deployment Boundary: ")
    add_bullet(doc, "The initial release focuses on core pan-Indian civilizational epochs, leaving regional sub-dynasties for future community curation.", bold_prefix="Curatorial Granularity: ")

def build_p17(doc):
    # Page 17: Chapter 6: Methodology (Part 1)
    add_heading_1(doc, "6. METHODOLOGY")
    add_p(doc, 
          "The engineering of the 'History of India' platform followed an Iterative and Incremental Agile Methodology. "
          "Given the dual requirements of rigorous historical curatorial accuracy and cutting-edge interactive web performance, "
          "the Agile framework allowed continuous validation of data schemas, UI components, and real-time audio synthesis "
          "across structured sprint cycles.", space_after=6)

    add_heading_2(doc, "Agile Development Phases")
    add_bullet(doc, "Conducted comprehensive historical research across NCERT, ASI, and National Museum publications. Identified 6 chronological epochs, 14 major dynasties, and 22 iconic artifacts. Defined JSON data schemas for epochs, rulers, and artifacts.", bold_prefix="Phase 1: Curatorial Research & Data Modeling (Sprint 1): ")
    add_bullet(doc, "Constructed the pure Python 3.12 server using `http.server.HTTPServer` and `SimpleHTTPRequestHandler`. Implemented custom REST endpoints (`/api/status`, `/api/quiz`, `/api/bookmarks`) and robust MIME type mapping.", bold_prefix="Phase 2: Backend Architecture & REST Services (Sprint 2): ")
    add_bullet(doc, "Developed the responsive Sony Darkroom aesthetic using CSS custom properties. Built the dual-mode chronological timeline engine supporting horizontal wheel scrolling and vertical timeline view.", bold_prefix="Phase 3: Core UI Framework & Timeline Engine (Sprint 3): ")

def build_p18(doc):
    # Page 18: Chapter 6: Methodology (Part 2 - Sprint breakdown & Tech Roles)
    add_heading_2(doc, "Agile Development Phases (Continued)")
    add_bullet(doc, "Implemented the dynamic CSS Grid gallery with category filtering. Engineered the accessible modal lightbox with image zoom, high-res preloading, and detailed metadata tabs.", bold_prefix="Phase 4: Artifact Gallery & Lightbox System (Sprint 4): ")
    add_bullet(doc, "Engineered the interactive SVG Imperial Atlas with historical coordinates. Programmed the procedural Web Audio Tanpura synthesizer with real-time harmonic overtone control.", bold_prefix="Phase 5: Interactive Cartography & Web Audio DSP (Sprint 5): ")
    add_bullet(doc, "Constructed the randomized quiz engine, sub-millisecond search terminal, local bookmarking system, cross-browser automated testing, and comprehensive documentation.", bold_prefix="Phase 6: Gamification, Search & Quality Assurance (Sprint 6): ")

    add_heading_2(doc, "Technology Roles & Architectural Responsibilities")
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    hdr[0].width = Inches(1.5)
    hdr[1].width = Inches(1.5)
    hdr[2].width = Inches(3.6)
    for i, h in enumerate(["Technology", "Layer", "Architectural Role & Function"]):
        set_cell_background(hdr[i], "1E293B")
        set_cell_margins(hdr[i], top=50, bottom=50, left=80, right=80)
        p = hdr[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    roles1 = [
        ("Python 3.12", "Backend Core", "Serves HTTP traffic, handles REST API routing, and manages data persistence."),
        ("Vanilla ES6+ JS", "Frontend Logic", "Controls state bus, event delegation, dynamic DOM rendering, and user input."),
        ("Web Audio API", "Synthetic Audio", "Generates procedural Tanpura acoustic drone using real-time audio oscillators.")
    ]
    for tech, lay, rol in roles1:
        row = tbl.add_row().cells
        row[0].width = Inches(1.5)
        row[1].width = Inches(1.5)
        row[2].width = Inches(3.6)
        bg = "F8FAFC" if (len(tbl.rows) % 2 == 0) else "FFFFFF"
        for i, val in enumerate([tech, lay, rol]):
            set_cell_background(row[i], bg)
            set_cell_margins(row[i], top=35, bottom=35, left=70, right=70)
            p = row[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            r = p.add_run(val)
            r.font.name = 'Calibri'
            r.font.size = Pt(9.5)
            if i == 0:
                r.bold = True
            r.font.color.rgb = RGBColor(30, 41, 59)

def build_p19(doc):
    # Page 19: Chapter 6: Methodology (Part 3 - Tech roles continued & QA)
    add_heading_2(doc, "Technology Roles & Architectural Responsibilities (Continued)")
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    hdr[0].width = Inches(1.5)
    hdr[1].width = Inches(1.5)
    hdr[2].width = Inches(3.6)
    for i, h in enumerate(["Technology", "Layer", "Architectural Role & Function"]):
        set_cell_background(hdr[i], "1E293B")
        set_cell_margins(hdr[i], top=50, bottom=50, left=80, right=80)
        p = hdr[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    roles2 = [
        ("CSS3 & Grid", "Presentation", "Delivers Sony Darkroom theme, glassmorphic modals, and responsive layouts."),
        ("SVG Vector", "Cartography", "Renders high-definition historical territorial maps with dynamic pins."),
        ("JSON / SQLite", "Persistence", "Provides structured data catalogs and relational schemas for user data.")
    ]
    for tech, lay, rol in roles2:
        row = tbl.add_row().cells
        row[0].width = Inches(1.5)
        row[1].width = Inches(1.5)
        row[2].width = Inches(3.6)
        bg = "F8FAFC" if (len(tbl.rows) % 2 == 0) else "FFFFFF"
        for i, val in enumerate([tech, lay, rol]):
            set_cell_background(row[i], bg)
            set_cell_margins(row[i], top=35, bottom=35, left=70, right=70)
            p = row[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            r = p.add_run(val)
            r.font.name = 'Calibri'
            r.font.size = Pt(9.5)
            if i == 0:
                r.bold = True
            r.font.color.rgb = RGBColor(30, 41, 59)

    add_heading_2(doc, "Quality Assurance & Verification Strategy")
    add_bullet(doc, "Automated validation of all 22 downloaded museum image files, verifying dimensions, byte size, and HTTP 200 availability.", bold_prefix="Asset Integrity Testing: ")
    add_bullet(doc, "Verified audio synthesis latency, buffer starvation, and oscillator cleanup to guarantee zero memory leaks or audio clipping across sessions.", bold_prefix="Web Audio Latency & DSP Testing: ")
    add_bullet(doc, "Tested interactive controls and visual contrast across Google Chrome, Firefox, Safari, and Edge on 320px, 768px, 1024px, and 1920px viewports.", bold_prefix="Cross-Browser & Responsiveness Audit: ")

def build_p20(doc):
    # Page 20: Chapter 7: Requirement Specification (Part 1)
    add_heading_1(doc, "7. REQUIREMENT SPECIFICATION")
    add_p(doc, 
          "The Requirement Specification establishes the baseline computational environment, hardware configurations, "
          "software dependencies, functional requirements, and non-functional quality standards required for developing, "
          "deploying, and operating the 'History of India' web platform.", space_after=6)

    add_heading_2(doc, "Hardware Specifications")
    tbl_hw = doc.add_table(rows=1, cols=3)
    tbl_hw.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl_hw.rows[0].cells
    hdr[0].width = Inches(1.8)
    hdr[1].width = Inches(2.4)
    hdr[2].width = Inches(2.4)
    for i, h in enumerate(["Hardware Component", "Minimum Requirement", "Recommended Specification"]):
        set_cell_background(hdr[i], "1E293B")
        set_cell_margins(hdr[i], top=45, bottom=45, left=80, right=80)
        p = hdr[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    hw_specs = [
        ("Processor (CPU)", "Dual-Core 2.0 GHz (x86/ARM)", "Intel Core i5 / AMD Ryzen 5 / Apple M1+"),
        ("System Memory (RAM)", "4 GB DDR4", "8 GB / 16 GB High-Speed RAM"),
        ("Storage (Disk Space)", "500 MB Free Disk Space", "2 GB Free NVMe SSD Storage"),
        ("Display Resolution", "1024 x 768 (SVGA)", "1920 x 1080 (Full HD IPS Panel)"),
        ("Audio Output", "Basic Stereo Sound Card", "24-bit DAC / High-Definition Headphones"),
        ("Network Interface", "1 Mbps Broadband", "10 Mbps+ High-Speed Fiber Internet")
    ]
    for comp, min_s, rec_s in hw_specs:
        row = tbl_hw.add_row().cells
        row[0].width = Inches(1.8)
        row[1].width = Inches(2.4)
        row[2].width = Inches(2.4)
        bg = "F8FAFC" if (len(tbl_hw.rows) % 2 == 0) else "FFFFFF"
        for i, val in enumerate([comp, min_s, rec_s]):
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

    add_heading_2(doc, "Software Environment")
    add_bullet(doc, "Microsoft Windows 10/11 (x64), Ubuntu Linux 22.04 LTS, or macOS Sonoma 14+.", bold_prefix="Operating System: ")
    add_bullet(doc, "Python 3.10, 3.11, or 3.12 (Standard Library distribution, zero pip dependencies).", bold_prefix="Backend Runtime: ")
    add_bullet(doc, "Google Chrome 110+, Mozilla Firefox 115+, Microsoft Edge 110+, Apple Safari 16+.", bold_prefix="Web Browsers: ")

print("pages_11_to_20 loaded.")
