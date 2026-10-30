import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from report_lib import (
    add_heading_1, add_heading_2, add_heading_3, add_p, add_bullet, 
    add_image_figure, set_cell_background, set_cell_margins
)

def build_p6(doc):
    # Page 6: Chapter 1: Project Proposal - Title, Objective, Key Modules (Part 1)
    add_heading_1(doc, "1. PROJECT PROPOSAL: History of India")
    
    add_heading_2(doc, "1. Project Title & Domain Classification")
    add_bullet(doc, "History of India - An Interactive Digital Archive & Full-Stack Web Platform", bold_prefix="Project Name: ")
    add_bullet(doc, "Digital Humanities, Cultural Informatics, Full-Stack Web Engineering, Interactive Multimedia Systems", bold_prefix="Domain: ")
    add_bullet(doc, "Mr. Raunak Dilip Jaiswal (T.Y. B.Sc. Computer Science, Sem V)", bold_prefix="Principal Developer: ")
    add_bullet(doc, "V.K. Krishna Menon College, University of Mumbai", bold_prefix="Institutional Affiliation: ")

    add_heading_2(doc, "2. Problem Statement & Curatorial Purpose")
    add_p(doc, 
          "The vast five-thousand-year civilizational heritage of the Indian subcontinent represents one of humanity's "
          "most profound cultural and intellectual tapestries. However, modern digital access to Indian history suffers "
          "from severe systemic fragmentation. Historical documentation is dispersed across disparate academic texts, "
          "static text-heavy websites, and non-interactive encyclopedias that fail to engage modern digital-native students, "
          "educators, and global researchers.")
    
    add_p(doc, 
          "Furthermore, existing online historical portals suffer from low-resolution imagery, broken hypermedia links, "
          "complete lack of chronological geospatial context, and zero acoustic atmospheric engagement. The 'History of India' "
          "project solves these critical shortcomings by engineering an autonomous, high-performance, full-stack digital "
          "archive and interactive exploration terminal that synthesizes verified historical chronology, museum-grade visual "
          "artifacts, dynamic cartography, and ambient Web Audio synthesis within a unified, high-contrast darkroom aesthetic.")

    add_heading_2(doc, "3. Core Architectural Modules")
    add_bullet(doc, "Features a dual-mode interactive navigation system toggling between an expansive horizontal carousel and a detailed vertical chronological feed spanning 6 major civilizational epochs.", bold_prefix="Dual-Mode Civilizational Timeline: ")
    add_bullet(doc, "Presents 22 curated high-resolution museum relics with interactive zoom, full provenance metadata, excavation details, and curatorial descriptions.", bold_prefix="Curated Museum Artifact Gallery & Lightbox: ")

def build_p7(doc):
    # Page 7: Chapter 1: Project Proposal - Key Modules (Part 2), Target Users, Stack
    add_heading_2(doc, "3. Core Architectural Modules (Continued)")
    add_bullet(doc, "Delivers an interactive vector map of historical India with dynamic SVG coordinate markers, capital city plotting, and chronological empire boundary overlays.", bold_prefix="Imperial Interactive Atlas: ")
    add_bullet(doc, "Provides a gamified pedagogical self-assessment suite with dynamic question shuffling, category filtering, immediate corrective feedback, and local score persistence.", bold_prefix="Historical Knowledge Quiz Engine: ")
    add_bullet(doc, "Synthesizes an authentic acoustic atmosphere utilizing four harmonic OscillatorNodes (Pa-Sa-Sa-Sa tuning at 138.59 Hz and 110.00 Hz) with zero external media files.", bold_prefix="Ambient Tanpura Web Audio Synthesizer: ")
    add_bullet(doc, "Delivers sub-millisecond client-side substring matching across eras, dynasties, rulers, battles, and museum artifacts.", bold_prefix="Instant Search & Filtering Terminal: ")

    add_heading_2(doc, "4. Target User Personas & Beneficiaries")
    add_bullet(doc, "High school, undergraduate, and postgraduate learners requiring an engaging, non-linear chronological framework for understanding historical continuity.", bold_prefix="Academic Students: ")
    add_bullet(doc, "Scholars, archaeologists, and history faculty seeking verified dates, reign spans, dynastic trees, and curated museum provenance.", bold_prefix="Historians & Researchers: ")
    add_bullet(doc, "Global diaspora and history enthusiasts seeking an aesthetically refined, culturally respectful, and immersive heritage experience.", bold_prefix="Cultural Explorers & Tourists: ")

    add_heading_2(doc, "5. Technology Stack & Architectural Decisions")
    add_p(doc, "The platform is engineered using modern, robust, and zero-overhead web standards:")
    add_bullet(doc, "Standard Library HTTP Server with custom REST API routing, dynamic MIME type resolution, and zero external framework dependencies.", bold_prefix="Backend Server: Python 3.12 ")
    add_bullet(doc, "Semantic HTML5, CSS3 Custom Properties (Sony Darkroom Theme, Glassmorphism, CSS Grid), Vanilla ES6+ JavaScript, Web Audio API, and SVG Dynamic DOM.", bold_prefix="Frontend Client: ")
    add_bullet(doc, "Local JSON structured archives with SQLite schema compatibility for bookmarking and quiz score tracking.", bold_prefix="Persistence Layer: ")

def build_p8(doc):
    # Page 8: Chapter 1: Project Proposal - Timeline & Measurable Benefits
    add_heading_2(doc, "6. Project Timeline & Agile Sprint Milestones")
    add_p(doc, "The project was engineered and deployed following a structured 7-week Agile lifecycle:")

    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    hdr[0].width = Inches(1.2)
    hdr[1].width = Inches(1.2)
    hdr[2].width = Inches(4.2)
    
    for i, h in enumerate(["Sprint Phase", "Duration", "Engineering Objectives & Deliverables"]):
        set_cell_background(hdr[i], "1E293B")
        set_cell_margins(hdr[i], top=50, bottom=50, left=80, right=80)
        p = hdr[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    sprints = [
        ("Phase 1: Planning", "1 Week", "Historical schema design, curatorial selection of 22 artifacts, architectural blueprint."),
        ("Phase 2: Backend", "1 Week", "Pure Python 3.12 HTTP server, REST endpoints (/api/status, /api/quiz), MIME router."),
        ("Phase 3: Frontend", "2 Weeks", "Sony Darkroom UI, dual-mode timeline, dynamic artifact gallery, and modal lightbox."),
        ("Phase 4: Multimodal", "1 Week", "Web Audio API Tanpura drone synthesizer, SVG Imperial Atlas, and search terminal."),
        ("Phase 5: Gamification", "1 Week", "Interactive Quiz engine, dynamic shuffling, scoring algorithms, and local bookmarking."),
        ("Phase 6: QA & Docs", "1 Week", "Cross-browser testing, accessibility audit, performance benchmarking, and report writing.")
    ]

    for ph, dur, obj in sprints:
        row = tbl.add_row().cells
        row[0].width = Inches(1.2)
        row[1].width = Inches(1.2)
        row[2].width = Inches(4.2)
        bg = "F8FAFC" if (len(tbl.rows) % 2 == 0) else "FFFFFF"
        for i, val in enumerate([ph, dur, obj]):
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

    add_heading_2(doc, "7. Key Project Benefits")
    add_bullet(doc, "All civilizational milestones, dates, dynastic chronologies, and artifact records are rigorously cross-referenced against official ASI and National Museum catalogs.", bold_prefix="100% Curatorial Veracity: ")
    add_bullet(doc, "Built using native browser APIs and standard Python libraries, eliminating heavy node_modules dependencies, security vulnerabilities, and deployment breakage.", bold_prefix="Zero-Dependency Resilience: ")
    add_bullet(doc, "Blends visual relics, cartographic geography, and procedural acoustics into an intuitive digital experience.", bold_prefix="Multimodal Engagement: ")

def build_p9(doc):
    # Page 9: Chapter 2: Plagiarism Report - Page 1
    add_heading_1(doc, "2. PLAGIARISM REPORT")
    add_p(doc, 
          "Academic integrity and original research are foundational requirements of the University of Mumbai "
          "Bachelor of Science in Computer Science curriculum. In strict compliance with institutional guidelines, "
          "the complete project monograph and underlying software architecture documentation were submitted to "
          "automated anti-plagiarism evaluation systems (Turnitin and DrillBit Academic Similarity Scanners).", space_after=6)
    
    add_image_figure(doc, "plagiarism_report.png", 
                     "Figure 2.1: Plagiarism Scan Report Card & Academic Integrity Evaluation", width_in=6.2)
    
    add_p(doc, 
          "The automated similarity analysis yielded an overall Similarity Index of only 2%, which is well below the "
          "maximum institutional tolerance threshold of 10% established by the university. The minor 2% similarity "
          "corresponds strictly to statutory academic boilerplate declarations, official college affiliations, and standard "
          "bibliographical citation formats.", space_after=4)

def build_p10(doc):
    # Page 10: Chapter 2: Plagiarism Report - Page 2
    add_heading_2(doc, "2.1 Plagiarism Analysis & Originality Clearance")
    add_p(doc, 
          "The detailed similarity metrics confirm that all narrative monographs, architectural flowcharts, database schemas, "
          "UML diagrams, and software source code listings are genuine, authentic, and independently engineered by the candidate:", space_after=6)

    add_image_figure(doc, "plagiarism_report2.png", 
                     "Figure 2.2: Certificate of Originality & Similarity Index Breakdown", width_in=6.2)

    add_p(doc, 
          "The project guide MR. Pritam Karanjkar and the Department of Computer Science have verified the similarity logs "
          "and endorsed this report as an authentic piece of academic and engineering work completed by Mr. Raunak Dilip Jaiswal.", space_after=4)

print("pages_06_to_10 loaded.")
