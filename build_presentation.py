#!/usr/bin/env python3
"""
History of India - Academic Project Presentation Generator
Generates a clean, professional, human-made 10-slide PowerPoint presentation (.pptx)
for Mr. Raunak Dilip Jaiswal (University of Mumbai / V.K. Krishna Menon College).
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_ASSETS = os.path.join(SCRIPT_DIR, "doc_assets")
DESKTOP_DIR = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
if not os.path.exists(DESKTOP_DIR):
    DESKTOP_DIR = os.path.join(os.path.expanduser("~"), "Desktop")

OUTPUT_PROJECT = os.path.join(SCRIPT_DIR, "History_of_India_Project_Presentation.pptx")
OUTPUT_DESKTOP = os.path.join(DESKTOP_DIR, "History_of_India_Project_Presentation.pptx")

# Color Palette (Classic Human Academic Theme - Navy & Heritage Gold)
COLOR_NAVY = RGBColor(24, 43, 73)        # #182B49 - Deep Academic Navy
COLOR_NAVY_LIGHT = RGBColor(38, 65, 107) # #26416B - Medium Navy
COLOR_GOLD = RGBColor(197, 145, 52)      # #C59134 - Indian Heritage Warm Gold
COLOR_GOLD_DARK = RGBColor(160, 115, 35) # #A07323
COLOR_BG_LIGHT = RGBColor(247, 249, 252) # #F7F9FC - Off-white canvas
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_CARD_BG = RGBColor(255, 255, 255)  # Clean white cards
COLOR_CARD_BORDER = RGBColor(218, 225, 235)
COLOR_TEXT_DARK = RGBColor(28, 37, 48)   # #1C2530 - Primary charcoal
COLOR_TEXT_MUTED = RGBColor(90, 104, 120)# Slate grey
COLOR_ACCENT_BG = RGBColor(238, 242, 248)

FONT_HEADING = "Arial"
FONT_BODY = "Calibri"

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide

    def add_header(slide, title_text, category_text):
        """Adds a clean standard human academic header banner."""
        # Top accent bar
        accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.1))
        accent.fill.solid()
        accent.fill.fore_color.rgb = COLOR_GOLD
        accent.line.fill.background()

        # Category tracker
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.5), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = FONT_BODY
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_GOLD_DARK

        # Main slide title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.5), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = FONT_HEADING
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_NAVY

        # Subtle bottom line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.25), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_CARD_BORDER
        line.line.fill.background()

    def add_footer(slide, current_slide, total_slides=10):
        """Adds a subtle academic footer with student details and slide count."""
        footer_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.015))
        footer_line.fill.solid()
        footer_line.fill.fore_color.rgb = COLOR_CARD_BORDER
        footer_line.line.fill.background()

        box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.35))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        
        # Left side info
        p.text = "History of India: Interactive Digital Archive  |  Raunak Dilip Jaiswal (V.K. Krishna Menon College, Mumbai)"
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = COLOR_TEXT_MUTED

        # Right side slide number box
        box_num = slide.shapes.add_textbox(Inches(11.0), Inches(7.05), Inches(1.533), Inches(0.35))
        tf_num = box_num.text_frame
        tf_num.word_wrap = True
        tf_num.margin_left = tf_num.margin_top = tf_num.margin_right = tf_num.margin_bottom = 0
        p_num = tf_num.paragraphs[0]
        p_num.alignment = PP_ALIGN.RIGHT
        p_num.text = f"Slide {current_slide} of {total_slides}"
        p_num.font.name = FONT_BODY
        p_num.font.size = Pt(9.5)
        p_num.font.color.rgb = COLOR_TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=COLOR_WHITE, border_color=COLOR_CARD_BORDER):
        """Creates a clean content card rectangle."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Clean Academic Navy & Gold)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    # Dark Navy Canvas
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_NAVY
    bg1.line.fill.background()

    # Gold Accent Top Bar
    bar_top = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.18))
    bar_top.fill.solid()
    bar_top.fill.fore_color.rgb = COLOR_GOLD
    bar_top.line.fill.background()

    # Decorative gold vertical divider
    bar_vert = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.6), Inches(0.08), Inches(4.3))
    bar_vert.fill.solid()
    bar_vert.fill.fore_color.rgb = COLOR_GOLD
    bar_vert.line.fill.background()

    # Title & Subtitle Frame
    title_box = s1.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.5), Inches(2.2))
    tf1 = title_box.text_frame
    tf1.word_wrap = True
    
    p_kicker = tf1.paragraphs[0]
    p_kicker.text = "BACHELOR OF SCIENCE (COMPUTER SCIENCE) • FINAL YEAR PROJECT"
    p_kicker.font.name = FONT_BODY
    p_kicker.font.size = Pt(11)
    p_kicker.font.bold = True
    p_kicker.font.color.rgb = COLOR_GOLD

    p_main = tf1.add_paragraph()
    p_main.text = "History of India"
    p_main.font.name = FONT_HEADING
    p_main.font.size = Pt(40)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_WHITE
    p_main.space_before = Pt(8)
    p_main.space_after = Pt(4)

    p_sub = tf1.add_paragraph()
    p_sub.text = "An Interactive Digital Archive & Educational Web Platform"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(18)
    p_sub.font.color.rgb = RGBColor(210, 225, 245)

    # Details Card (White / Semi-transparent card inside dark slide)
    card_meta = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(4.1), Inches(10.3), Inches(2.3))
    card_meta.fill.solid()
    card_meta.fill.fore_color.rgb = RGBColor(32, 55, 92)
    card_meta.line.color.rgb = RGBColor(55, 85, 135)

    tf_meta = card_meta.text_frame
    tf_meta.word_wrap = True
    tf_meta.margin_left = Inches(0.4)
    tf_meta.margin_top = Inches(0.25)
    tf_meta.margin_right = Inches(0.4)

    p_by = tf_meta.paragraphs[0]
    p_by.text = "PROJECT PRESENTATION & DEFENSE"
    p_by.font.name = FONT_BODY
    p_by.font.size = Pt(10)
    p_by.font.bold = True
    p_by.font.color.rgb = COLOR_GOLD

    p_cand = tf_meta.add_paragraph()
    p_cand.text = "Candidate: Mr. Raunak Dilip Jaiswal"
    p_cand.font.name = FONT_HEADING
    p_cand.font.size = Pt(14)
    p_cand.font.bold = True
    p_cand.font.color.rgb = COLOR_WHITE
    p_cand.space_before = Pt(4)

    p_inst = tf_meta.add_paragraph()
    p_inst.text = "College: V.K. Krishna Menon College of Commerce & Economics, Mumbai\nUniversity: University of Mumbai  |  Academic Year: 2026-2027"
    p_inst.font.name = FONT_BODY
    p_inst.font.size = Pt(12)
    p_inst.font.color.rgb = RGBColor(220, 230, 245)
    p_inst.space_before = Pt(4)

    # =========================================================================
    # SLIDE 2: PROJECT OVERVIEW & BACKGROUND
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Project Overview & Background", "Section 1 • Introduction")
    add_footer(s2, 2)

    # Left Column: The Problem & Context
    add_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    tb_left = s2.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(5.0), Inches(4.7))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

    p = tf_l.paragraphs[0]
    p.text = "Challenges in Traditional History Education"
    p.font.name = FONT_HEADING
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    points_l = [
        ("Textbook Disconnect: ", "Static printed materials and long walls of text fail to engage visual, modern digital learners."),
        ("Fragmented Digital Content: ", "Online historical information is scattered across unverified blogs, low-res scans, and non-interactive pages."),
        ("Lack of Temporal Flow: ", "Learners struggle to grasp concurrent civilizational developments across 5,000 years of Indian epochs."),
        ("Missing Multimedia Context: ", "Museum treasures, geographical imperial expansions, and indigenous classical art forms are rarely experienced together in a single platform.")
    ]
    for bold_prefix, text in points_l:
        p = tf_l.add_paragraph()
        p.space_before = Pt(10)
        p.level = 0
        r_bold = p.add_run()
        r_bold.text = "• " + bold_prefix
        r_bold.font.name = FONT_BODY
        r_bold.font.size = Pt(12)
        r_bold.font.bold = True
        r_bold.font.color.rgb = COLOR_NAVY_LIGHT
        
        r_text = p.add_run()
        r_text.text = text
        r_text.font.name = FONT_BODY
        r_text.font.size = Pt(12)
        r_text.font.color.rgb = COLOR_TEXT_DARK

    # Right Column: The Proposed Solution
    add_card(s2, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    tb_right = s2.shapes.add_textbox(Inches(7.1), Inches(1.7), Inches(5.1), Inches(4.7))
    tf_r = tb_right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

    p = tf_r.paragraphs[0]
    p.text = "The 'History of India' Web Solution"
    p.font.name = FONT_HEADING
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    points_r = [
        ("Unified Digital Humanities Portal: ", "A single responsive hub covering 6 major epochs from the Bronze Age Indus Valley to the Modern Republic."),
        ("Sony Darkroom Aesthetics: ", "Cinema-grade dark theme reducing eye fatigue while accentuating museum artifact colors and historical manuscripts."),
        ("Real-Time Web Audio Synthesis: ", "A procedural Tanpura acoustic drone synthesized directly in-browser using mathematical audio oscillators."),
        ("Zero Dependency Architecture: ", "Engineered in pure standard-library Python, native ES6+ JavaScript, and semantic HTML5—100% lightweight and robust.")
    ]
    for bold_prefix, text in points_r:
        p = tf_r.add_paragraph()
        p.space_before = Pt(10)
        p.level = 0
        r_bold = p.add_run()
        r_bold.text = "• " + bold_prefix
        r_bold.font.name = FONT_BODY
        r_bold.font.size = Pt(12)
        r_bold.font.bold = True
        r_bold.font.color.rgb = COLOR_GOLD_DARK
        
        r_text = p.add_run()
        r_text.text = text
        r_text.font.name = FONT_BODY
        r_text.font.size = Pt(12)
        r_text.font.color.rgb = COLOR_TEXT_DARK

    # =========================================================================
    # SLIDE 3: OBJECTIVES & GOALS
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Project Objectives & Scope", "Section 2 • Goals")
    add_footer(s3, 3)

    objectives = [
        ("01", "Dual-Mode Temporal Chronology", 
         "Deliver two synchronized perspectives on Indian history: a dynamic horizontal carousel for broad comparative epoch exploration, and a vertical scholarly feed for deep milestone reading."),
        ("02", "Curated Museum Lightbox Gallery", 
         "Digitize and organize 22 high-resolution, public-domain archaeological treasures with zoomable modal lightboxes, provenance notes, and verified historical metadata."),
        ("03", "Imperial Dynasties Atlas", 
         "Build an interactive visual map detailing peak territorial borders, sovereign capitals, pioneering rulers, and cultural landmarks of India's major ruling empires."),
        ("04", "In-Browser Procedural Soundscape", 
         "Leverage the W3C Web Audio API to procedurally generate an authentic Indian classical Tanpura drone (Sa-Pa tuning) with zero external MP3s and zero network latency."),
        ("05", "Interactive Assessment & Persistence", 
         "Provide a dynamic knowledge quiz with immediate feedback, paired with a persistent client-side bookmarking drawer stored across user sessions via localStorage.")
    ]

    card_w = Inches(11.733)
    card_h = Inches(0.92)
    start_y = Inches(1.5)

    for i, (num, title, desc) in enumerate(objectives):
        y_pos = start_y + Inches(i * 1.05)
        card = add_card(s3, Inches(0.8), y_pos, card_w, card_h)

        # Number Badge
        nb = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), y_pos + Inches(0.18), Inches(0.6), Inches(0.55))
        nb.fill.solid()
        nb.fill.fore_color.rgb = COLOR_NAVY
        nb.line.fill.background()
        tf_nb = nb.text_frame
        tf_nb.margin_left = tf_nb.margin_top = tf_nb.margin_right = tf_nb.margin_bottom = 0
        p_nb = tf_nb.paragraphs[0]
        p_nb.alignment = PP_ALIGN.CENTER
        p_nb.text = num
        p_nb.font.name = FONT_HEADING
        p_nb.font.size = Pt(13)
        p_nb.font.bold = True
        p_nb.font.color.rgb = COLOR_WHITE

        # Text box
        tb = s3.shapes.add_textbox(Inches(1.8), y_pos + Inches(0.12), Inches(10.5), Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.name = FONT_HEADING
        p_title.font.size = Pt(13)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_NAVY

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.name = FONT_BODY
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = COLOR_TEXT_DARK
        p_desc.space_before = Pt(2)

    # =========================================================================
    # SLIDE 4: TECHNOLOGY STACK
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Technology Stack & Engineering Architecture", "Section 3 • Technical Stack")
    add_footer(s4, 4)

    stacks = [
        ("Frontend Presentation", COLOR_NAVY, [
            ("Semantic HTML5: ", "Accessible landmark structure (<header>, <main>, <article>, <aside>) with full ARIA attributes."),
            ("Custom CSS3 Darkroom: ", "Engineered with CSS Custom Properties, glassmorphism backdrops, Flexbox, and CSS Grid."),
            ("Modular ES6+ JavaScript: ", "Native DOM scripting, event-delegation controllers, and zero heavy frameworks like React or Angular.")
        ]),
        ("Audio DSP & Synthesis", COLOR_GOLD_DARK, [
            ("W3C Web Audio API: ", "Client-side digital signal processing utilizing AudioContext, OscillatorNode, and GainNode."),
            ("Additive Synthesis: ", "Simulates resonant harmonics of acoustic Tanpura strings (fundamental C#3/D3 at 138-146 Hz)."),
            ("Zero Asset Bandwidth: ", "Pure algorithmic sound generation with no external audio files, saving memory and data.")
        ]),
        ("Backend & REST Services", COLOR_NAVY, [
            ("Python 3.12 HTTP Server: ", "Built with standard-library http.server, socket, and urllib.parse—zero pip runtime dependencies."),
            ("Custom RESTful Endpoints: ", "/api/status (health check), /api/quiz (randomized questions), and /api/bookmarks (sync)."),
            ("Graceful Port Negotiation: ", "Auto-detects open TCP ports (8000-8010) and launches default web browser automatically.")
        ]),
        ("Data, Storage & Hosting", COLOR_GOLD_DARK, [
            ("Client-Side Persistence: ", "HTML5 localStorage API retains bookmarked artifacts and quiz performance across browser reloads."),
            ("Source Version Control: ", "Managed via Git and GitHub CLI with clean branch structure and semantic commit history."),
            ("Global Cloud Deployment: ", "Hosted live worldwide on GitHub Pages with HTTPS encryption and global edge CDN distribution.")
        ])
    ]

    card_positions = [
        (Inches(0.8), Inches(1.5)),
        (Inches(6.8), Inches(1.5)),
        (Inches(0.8), Inches(4.2)),
        (Inches(6.8), Inches(4.2))
    ]

    for idx, (title, color, items) in enumerate(stacks):
        cx, cy = card_positions[idx]
        add_card(s4, cx, cy, Inches(5.733), Inches(2.55))

        # Title bar inside card
        tb = s4.shapes.add_textbox(cx + Inches(0.3), cy + Inches(0.2), Inches(5.1), Inches(0.35))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        # Content list
        tb_c = s4.shapes.add_textbox(cx + Inches(0.3), cy + Inches(0.65), Inches(5.1), Inches(1.75))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0

        for b_idx, (bold, text) in enumerate(items):
            p = tf_c.paragraphs[0] if b_idx == 0 else tf_c.add_paragraph()
            p.space_before = Pt(6)
            
            r_b = p.add_run()
            r_b.text = "• " + bold
            r_b.font.name = FONT_BODY
            r_b.font.size = Pt(10.5)
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_TEXT_DARK

            r_t = p.add_run()
            r_t.text = text
            r_t.font.name = FONT_BODY
            r_t.font.size = Pt(10.5)
            r_t.font.color.rgb = COLOR_TEXT_DARK

    # =========================================================================
    # SLIDE 5: SYSTEM DESIGN & ARCHITECTURE
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "System Design & Architecture", "Section 4 • System Design")
    add_footer(s5, 5)

    # Left Column: Architectural Diagram
    sys_diag_path = os.path.join(DOC_ASSETS, "system_design_diagram.png")
    if os.path.exists(sys_diag_path):
        # Card container for image
        add_card(s5, Inches(0.8), Inches(1.5), Inches(6.0), Inches(5.2))
        s5.shapes.add_picture(sys_diag_path, Inches(0.95), Inches(1.65), width=Inches(5.7))
    else:
        add_card(s5, Inches(0.8), Inches(1.5), Inches(6.0), Inches(5.2))

    # Right Column: Architecture Breakdown
    add_card(s5, Inches(7.1), Inches(1.5), Inches(5.433), Inches(5.2))
    tb_arch = s5.shapes.add_textbox(Inches(7.4), Inches(1.7), Inches(4.8), Inches(4.8))
    tf_a = tb_arch.text_frame
    tf_a.word_wrap = True
    tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0

    p_at = tf_a.paragraphs[0]
    p_at.text = "Multi-Tiered Architectural Model"
    p_at.font.name = FONT_HEADING
    p_at.font.size = Pt(15)
    p_at.font.bold = True
    p_at.font.color.rgb = COLOR_NAVY

    arch_layers = [
        ("Client Tier (Browser):", 
         "Executes responsive UI rendering, interactive state machines, filter transitions, and hardware-accelerated CSS animations. Processes user input with instant feedback."),
        ("Audio DSP Pipeline:", 
         "An independent audio graph initialized upon user gesture, connecting parametric oscillators, biquad low-pass filters, and exponential gain ramps."),
        ("Application & REST Tier:", 
         "A lightweight Python HTTP server acting as a reverse-proxy and JSON REST dispatcher, exposing endpoints for health checks, quiz datasets, and sync."),
        ("Data & Storage Tier:", 
         "Structured static datasets in JSON format combined with client localStorage for instantaneous access without database query overhead.")
    ]

    for title, desc in arch_layers:
        p = tf_a.add_paragraph()
        p.space_before = Pt(8)
        
        r_b = p.add_run()
        r_b.text = title + " "
        r_b.font.name = FONT_BODY
        r_b.font.size = Pt(11)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_GOLD_DARK

        r_t = p.add_run()
        r_t.text = desc
        r_t.font.name = FONT_BODY
        r_t.font.size = Pt(10.5)
        r_t.font.color.rgb = COLOR_TEXT_DARK

    # =========================================================================
    # SLIDE 6: KEY FEATURES - TIMELINE & MUSEUM GALLERY
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Core Features: Chronology & Artifact Gallery", "Section 5 • Key Features (Part 1)")
    add_footer(s6, 6)

    # Feature 1: Dual Timeline
    add_card(s6, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    ss_timeline = os.path.join(DOC_ASSETS, "ss2_horizontal_timeline.png")
    if os.path.exists(ss_timeline):
        s6.shapes.add_picture(ss_timeline, Inches(1.0), Inches(1.7), width=Inches(5.2))
    
    tb_f1 = s6.shapes.add_textbox(Inches(1.0), Inches(4.3), Inches(5.2), Inches(2.2))
    tf_f1 = tb_f1.text_frame
    tf_f1.word_wrap = True
    p1 = tf_f1.paragraphs[0]
    p1.text = "1. Dual-Mode Master Chronology"
    p1.font.name = FONT_HEADING
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_NAVY

    p1_desc = tf_f1.add_paragraph()
    p1_desc.text = "• Interactive Epoch Filtering: Seamlessly switch across 6 civilizational epochs.\n• Dual Perspective: Horizontal timeline for visual progression; vertical milestone feed for comprehensive scholarly reading.\n• Dynamic Milestone Cards: Displays historical significance, dating, and key architectural/cultural contributions."
    p1_desc.font.name = FONT_BODY
    p1_desc.font.size = Pt(10.5)
    p1_desc.font.color.rgb = COLOR_TEXT_DARK
    p1_desc.space_before = Pt(4)

    # Feature 2: Museum Gallery & Lightbox
    add_card(s6, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    ss_gallery = os.path.join(DOC_ASSETS, "ss4_artifact_gallery.png")
    if os.path.exists(ss_gallery):
        s6.shapes.add_picture(ss_gallery, Inches(7.05), Inches(1.7), width=Inches(5.2))

    tb_f2 = s6.shapes.add_textbox(Inches(7.05), Inches(4.3), Inches(5.2), Inches(2.2))
    tf_f2 = tb_f2.text_frame
    tf_f2.word_wrap = True
    p2 = tf_f2.paragraphs[0]
    p2.text = "2. Curated Museum Lightbox Gallery"
    p2.font.name = FONT_HEADING
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_NAVY

    p2_desc = tf_f2.add_paragraph()
    p2_desc.text = "• 22 Curated Public-Domain Treasures: Includes Dancing Girl, Ashoka Lion Capital, Ajanta murals, Brihadisvara Temple, and Koh-i-Noor.\n• High-Resolution Lightbox: Modal zoom, provenance notes, discovery location, and Wikipedia reference citations.\n• Instant Categorical Filtering: Filter by sculpture, architecture, coins, or painting."
    p2_desc.font.name = FONT_BODY
    p2_desc.font.size = Pt(10.5)
    p2_desc.font.color.rgb = COLOR_TEXT_DARK
    p2_desc.space_before = Pt(4)

    # =========================================================================
    # SLIDE 7: KEY FEATURES - DYNASTIES, AUDIO & QUIZ
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Core Features: Atlas, Audio DSP & Quiz Engine", "Section 5 • Key Features (Part 2)")
    add_footer(s7, 7)

    col_w = Inches(3.644)
    gap = Inches(0.4)

    feat_cols = [
        ("Imperial Dynasties Atlas", "ss6_imperial_atlas.png", [
            ("Territorial Cartography: ", "Visualizes peak territorial borders of Maurya, Gupta, Chola, Mughal, and Maratha empires."),
            ("Dynasty Fast Facts: ", "Quick reference for capital cities, prominent rulers, founding dates, and epoch achievements."),
            ("Comparative Analysis: ", "Enables students to understand geographical shifts across centuries of Indian governance.")
        ]),
        ("Tanpura Synthesizer", "ss9_audio_atmosphere.png", [
            ("Web Audio API DSP: ", "Algorithmic additive synthesis generating real acoustic Tanpura resonance in real-time."),
            ("Sa-Pa Drone Tuning: ", "Calibrated to meditative frequencies (fundamental C#3/D3 at 138-146 Hz)."),
            ("Zero Audio Assets: ", "No MP3/WAV files required—pure mathematical code running natively inside the browser.")
        ]),
        ("Knowledge Quiz & Bookmarks", "ss7_knowledge_quiz.png", [
            ("Trivia Engine: ", "Dynamic multiple-choice questions covering all eras with randomized options and scoring."),
            ("Instant Feedback: ", "Immediate answer validation with detailed historical explanations for educational reinforcement."),
            ("Persistent Bookmarks: ", "Users can save artifacts and timeline cards to a persistent drawer via localStorage.")
        ])
    ]

    for c_idx, (c_title, img_name, c_points) in enumerate(feat_cols):
        left_pos = Inches(0.8) + Inches(c_idx * 4.044)
        add_card(s7, left_pos, Inches(1.5), col_w, Inches(5.2))

        # Image preview
        img_path = os.path.join(DOC_ASSETS, img_name)
        if os.path.exists(img_path):
            s7.shapes.add_picture(img_path, left_pos + Inches(0.2), Inches(1.7), width=col_w - Inches(0.4))

        # Text Content
        tb = s7.shapes.add_textbox(left_pos + Inches(0.2), Inches(3.8), col_w - Inches(0.4), Inches(2.7))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_t = tf.paragraphs[0]
        p_t.text = c_title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(12.5)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY

        for b_bold, b_txt in c_points:
            p = tf.add_paragraph()
            p.space_before = Pt(6)
            
            r_b = p.add_run()
            r_b.text = "• " + b_bold
            r_b.font.name = FONT_BODY
            r_b.font.size = Pt(9.5)
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_GOLD_DARK

            r_t = p.add_run()
            r_t.text = b_txt
            r_t.font.name = FONT_BODY
            r_t.font.size = Pt(9.5)
            r_t.font.color.rgb = COLOR_TEXT_DARK

    # =========================================================================
    # SLIDE 8: TESTING & VERIFICATION RESULTS
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Testing, Quality Assurance & Verification", "Section 6 • Verification")
    add_footer(s8, 8)

    # 4 Cards Layout
    tests = [
        ("Automated Code Audit", "0 Errors / 0 Warnings", COLOR_NAVY, [
            "Executed custom Python test harness (audit_project.py).",
            "100% verified DOM element IDs across dynamic templates.",
            "All 22 museum image assets verified locally (zero missing files).",
            "Validated semantic HTML5 tags and CSS syntax consistency."
        ]),
        ("REST API & Server Tests", "100% Passing Endpoints", COLOR_GOLD_DARK, [
            "Tested HTTP server endpoints (/api/status, /api/quiz, /api/bookmarks).",
            "Confirmed valid Content-Type headers for .js, .css, .json, and .html.",
            "Graceful handling of malformed requests and unmapped URLs.",
            "Verified port conflict auto-resolution across TCP ports 8000-8010."
        ]),
        ("Cross-Browser Compatibility", "Chrome, Edge, Firefox, Safari", COLOR_NAVY, [
            "Tested responsive viewports: Desktop (1920x1080), Tablet, and Mobile.",
            "Web Audio API unlocked cleanly across modern user interaction policies.",
            "CSS glassmorphism and backdrop-filters verified on all modern engines.",
            "Touch-friendly timeline navigation and accessible keyboard controls."
        ]),
        ("Performance & Accessibility", "High Lighthouse Scores", COLOR_GOLD_DARK, [
            "Sub-100ms first paint achieved via zero external library overhead.",
            "Zero render-blocking third-party scripts (pure native ES6+).",
            "High contrast text adhering to WCAG 2.1 AA readability standards.",
            "Dual-run capability: runs completely offline or hosted on GitHub Pages."
        ])
    ]

    for idx, (t_title, t_badge, t_color, t_bullets) in enumerate(tests):
        cx, cy = card_positions[idx]
        add_card(s8, cx, cy, Inches(5.733), Inches(2.55))

        # Title & Badge
        tb = s8.shapes.add_textbox(cx + Inches(0.3), cy + Inches(0.18), Inches(5.1), Inches(0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = t_title + "  "
        r1.font.name = FONT_HEADING
        r1.font.size = Pt(13)
        r1.font.bold = True
        r1.font.color.rgb = t_color

        r2 = p.add_run()
        r2.text = f"[{t_badge}]"
        r2.font.name = FONT_BODY
        r2.font.size = Pt(10)
        r2.font.bold = True
        r2.font.color.rgb = COLOR_TEXT_MUTED

        # Bullets
        tb_b = s8.shapes.add_textbox(cx + Inches(0.3), cy + Inches(0.68), Inches(5.1), Inches(1.7))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0

        for b_idx, bullet in enumerate(t_bullets):
            p_b = tf_b.paragraphs[0] if b_idx == 0 else tf_b.add_paragraph()
            p_b.space_before = Pt(4)
            p_b.text = "• " + bullet
            p_b.font.name = FONT_BODY
            p_b.font.size = Pt(10.5)
            p_b.font.color.rgb = COLOR_TEXT_DARK

    # =========================================================================
    # SLIDE 9: FUTURE SCOPE & ENHANCEMENTS
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Future Scope & Potential Enhancements", "Section 7 • Future Roadmap")
    add_footer(s9, 9)

    future_cards = [
        ("3D WebGL Artifact Inspection", 
         "Integrate Three.js to provide 360-degree interactive 3D rotatable models of selected archaeological relics (e.g. Harappan seals, Chola bronzes, and temple spires)."),
        ("Regional Multilingual Localization", 
         "Expand language support to include Hindi, Marathi, Tamil, Bengali, and Sanskrit to broaden accessibility for schools and colleges across India."),
        ("Text-to-Speech Audio Tours", 
         "Incorporate Web Speech API or neural TTS narration to provide guided voiceover tours for each historical era, assisting visually impaired learners."),
        ("Dynamic Geo-Temporal Map Slider", 
         "Develop an animated timeline slider showing continuous empire territorial expansions and treaty changes across centuries on interactive vector maps.")
    ]

    for idx, (f_title, f_desc) in enumerate(future_cards):
        cx, cy = card_positions[idx]
        add_card(s9, cx, cy, Inches(5.733), Inches(2.55))

        # Icon number pill
        nb = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx + Inches(0.3), cy + Inches(0.25), Inches(0.55), Inches(0.45))
        nb.fill.solid()
        nb.fill.fore_color.rgb = COLOR_GOLD
        nb.line.fill.background()
        tf_nb = nb.text_frame
        tf_nb.margin_left = tf_nb.margin_top = tf_nb.margin_right = tf_nb.margin_bottom = 0
        p_nb = tf_nb.paragraphs[0]
        p_nb.alignment = PP_ALIGN.CENTER
        p_nb.text = f"0{idx+1}"
        p_nb.font.name = FONT_HEADING
        p_nb.font.size = Pt(12)
        p_nb.font.bold = True
        p_nb.font.color.rgb = COLOR_WHITE

        # Title
        tb_t = s9.shapes.add_textbox(cx + Inches(1.0), cy + Inches(0.25), Inches(4.4), Inches(0.45))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = f_title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY

        # Description
        tb_d = s9.shapes.add_textbox(cx + Inches(0.3), cy + Inches(0.85), Inches(5.1), Inches(1.5))
        tf_d = tb_d.text_frame
        tf_d.word_wrap = True
        tf_d.margin_left = tf_d.margin_top = tf_d.margin_right = tf_d.margin_bottom = 0
        p_d = tf_d.paragraphs[0]
        p_d.text = f_desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_DARK
        p_d.space_before = Pt(4)

    # =========================================================================
    # SLIDE 10: CONCLUSION & PROJECT SUMMARY
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Conclusion & Project Summary", "Section 8 • Conclusion & Q&A")
    add_footer(s10, 10)

    # Left Column: Summary of Achievements
    add_card(s10, Inches(0.8), Inches(1.5), Inches(6.0), Inches(5.2))
    tb_c_left = s10.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(5.4), Inches(4.7))
    tf_cl = tb_c_left.text_frame
    tf_cl.word_wrap = True
    tf_cl.margin_left = tf_cl.margin_top = tf_cl.margin_right = tf_cl.margin_bottom = 0

    p_ct = tf_cl.paragraphs[0]
    p_ct.text = "Key Project Achievements"
    p_ct.font.name = FONT_HEADING
    p_ct.font.size = Pt(15)
    p_ct.font.bold = True
    p_ct.font.color.rgb = COLOR_NAVY

    achievements = [
        ("Bridging Technology & Heritage: ", "Successfully synthesized modern full-stack web engineering with 5,000 years of Indian historical scholarship."),
        ("Zero-Dependency Reliability: ", "Proved that responsive, rich multimedia web apps can be constructed efficiently using standard libraries without heavy framework bloat."),
        ("Comprehensive Documentation: ", "Produced an exhaustive 68-page academic report adhering to University of Mumbai guidelines."),
        ("Global Accessibility: ", "Successfully published and hosted live worldwide on GitHub Pages with SSL encryption and public version control.")
    ]
    for b_bold, b_desc in achievements:
        p = tf_cl.add_paragraph()
        p.space_before = Pt(10)
        
        r_b = p.add_run()
        r_b.text = "✔ " + b_bold
        r_b.font.name = FONT_BODY
        r_b.font.size = Pt(11.5)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_GOLD_DARK

        r_t = p.add_run()
        r_t.text = b_desc
        r_t.font.name = FONT_BODY
        r_t.font.size = Pt(11)
        r_t.font.color.rgb = COLOR_TEXT_DARK

    # Right Column: Project Links & Student Information
    add_card(s10, Inches(7.2), Inches(1.5), Inches(5.333), Inches(5.2), bg_color=COLOR_NAVY)
    tb_c_right = s10.shapes.add_textbox(Inches(7.5), Inches(1.8), Inches(4.7), Inches(4.5))
    tf_cr = tb_c_right.text_frame
    tf_cr.word_wrap = True
    tf_cr.margin_left = tf_cr.margin_top = tf_cr.margin_right = tf_cr.margin_bottom = 0

    p_rt = tf_cr.paragraphs[0]
    p_rt.text = "Thank You!"
    p_rt.font.name = FONT_HEADING
    p_rt.font.size = Pt(28)
    p_rt.font.bold = True
    p_rt.font.color.rgb = COLOR_GOLD

    p_sub = tf_cr.add_paragraph()
    p_sub.text = "Questions & Answers are Welcome"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = RGBColor(210, 225, 245)
    p_sub.space_before = Pt(4)

    p_d = tf_cr.add_paragraph()
    p_d.space_before = Pt(20)
    p_d.text = "STUDENT & COLLEGE DETAILS"
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(10)
    p_d.font.bold = True
    p_d.font.color.rgb = COLOR_GOLD

    p_name = tf_cr.add_paragraph()
    p_name.text = "Mr. Raunak Dilip Jaiswal\nB.Sc. Computer Science (Final Year)\nV.K. Krishna Menon College of Commerce & Economics\nUniversity of Mumbai"
    p_name.font.name = FONT_BODY
    p_name.font.size = Pt(11.5)
    p_name.font.color.rgb = COLOR_WHITE
    p_name.space_before = Pt(4)

    p_links_t = tf_cr.add_paragraph()
    p_links_t.space_before = Pt(16)
    p_links_t.text = "ONLINE PROJECT LINKS"
    p_links_t.font.name = FONT_BODY
    p_links_t.font.size = Pt(10)
    p_links_t.font.bold = True
    p_links_t.font.color.rgb = COLOR_GOLD

    p_links = tf_cr.add_paragraph()
    p_links.text = "• Live Site: raunakjaiswaljaiswal9-ux.github.io/history-of-India\n• GitHub: github.com/raunakjaiswaljaiswal9-ux/history-of-India"
    p_links.font.name = FONT_BODY
    p_links.font.size = Pt(10.5)
    p_links.font.color.rgb = RGBColor(220, 235, 255)
    p_links.space_before = Pt(4)

    # Save presentations
    prs.save(OUTPUT_PROJECT)
    print(f"[+] Saved project presentation: {OUTPUT_PROJECT}")
    try:
        prs.save(OUTPUT_DESKTOP)
        print(f"[+] Saved desktop presentation: {OUTPUT_DESKTOP}")
    except Exception as e:
        print(f"[!] Note on desktop copy: {e}")

if __name__ == "__main__":
    create_deck()
