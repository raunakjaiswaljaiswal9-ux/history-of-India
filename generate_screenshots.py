import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "doc_assets"
IMG_DIR = "images"
os.makedirs(ASSETS_DIR, exist_ok=True)

W, H = 1200, 720

def get_font(size, bold=False):
    try:
        font_name = "arialbd.ttf" if bold else "arial.ttf"
        font_path = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", font_name)
        if os.path.exists(font_path):
            return ImageFont.truetype(font_path, size)
    except Exception:
        pass
    return ImageFont.load_default()

def draw_sony_header(draw, active_nav="Chronology"):
    draw.rectangle([(0, 0), (W, 60)], fill='#08080a')
    draw.line([(0, 60), (W, 60)], fill='#22222a', width=1)
    
    # Brand logo
    draw.ellipse([(35, 20), (55, 40)], outline='#d4af37', width=2)
    draw.ellipse([(42, 27), (48, 33)], fill='#d4af37')
    draw.text((68, 20), "INDIA·ARCHIVE", fill='#ffffff', font=get_font(16, True))

    # Nav links
    links = ["Chronology", "Artifacts", "Empires", "Voices", "Quiz ✦"]
    lx = 300
    for l in links:
        if l == active_nav:
            col = '#ffffff'
            draw.line([(lx, 46), (lx + 80, 46)], fill='#d4af37', width=2)
        elif 'Quiz' in l:
            col = '#d4af37'
        else:
            col = '#a1a1a8'
        draw.text((lx, 22), l, fill=col, font=get_font(13, l == active_nav))
        lx += 110

    # Localhost badge
    draw.rectangle([(860, 16), (1050, 44)], outline='#16a34a', fill='#062814', width=1)
    draw.ellipse([(872, 26), (880, 34)], fill='#22c55e')
    draw.text((888, 23), "Python Localhost :8000", fill='#86efac', font=get_font(11, True))

    # Sound toggle
    draw.rectangle([(1070, 16), (1165, 44)], outline='#3f3f46', fill='#18181b', width=1)
    draw.text((1085, 23), "Atmosphere", fill='#ffffff', font=get_font(11))

# ---------------------------------------------------------------------------
# SS 1: HERO PORTAL
# ---------------------------------------------------------------------------
def make_ss1_hero():
    img = Image.new('RGB', (W, H), color='#050508')
    taj_path = os.path.join(IMG_DIR, "taj_mahal.jpg")
    if os.path.exists(taj_path):
        try:
            bg = Image.open(taj_path).convert('RGB').resize((W, H))
            dark = Image.new('RGB', (W, H), color='#000000')
            bg = Image.blend(bg, dark, 0.70)
            img.paste(bg, (0, 0))
        except Exception:
            pass

    draw = ImageDraw.Draw(img)
    draw_sony_header(draw)

    # Hero Content
    draw.rectangle([(80, 140), (520, 175)], outline='#d4af37', fill='#1c170d', width=1)
    draw.text((95, 148), "5,000 YEARS · 8 FLAGSHIP EPOCHS · 1 CIVILIZATION", fill='#e5b958', font=get_font(12, True))

    draw.text((80, 210), "The Civilizational Odyssey\nof Bharat", fill='#ffffff', font=get_font(44, True))
    draw.text((80, 340), "From the bronze-age planned streets of Mohenjo-daro to the philosophical dawn\nof the Upanishads, the oceanic fleets of the Cholas, and the frontiers of space.", 
              fill='#d1d5db', font=get_font(16))

    # CTA Buttons
    draw.rectangle([(80, 420), (280, 475)], fill='#ffffff')
    draw.text((110, 438), "BEGIN THE JOURNEY ↓", fill='#000000', font=get_font(13, True))

    draw.rectangle([(305, 420), (505, 475)], outline='#52525b', fill='#18181b', width=1)
    draw.text((330, 438), "EXPLORE ARTIFACTS", fill='#ffffff', font=get_font(13, True))

    draw.rectangle([(530, 420), (740, 475)], outline='#d4af37', fill='#272111', width=1)
    draw.text((545, 438), "TEST YOUR KNOWLEDGE ✦", fill='#fbbf24', font=get_font(13, True))

    # Era quick strip
    draw.line([(80, 560), (1120, 560)], fill='#27272a', width=1)
    draw.text((80, 580), "EPOCHS AT A GLANCE", fill='#71717a', font=get_font(11, True))
    
    eras = [("3300 BCE", "Indus Valley"), ("1500 BCE", "Vedic Age"), ("322 BCE", "Maurya Empire"), 
            ("320 CE", "Gupta Golden Age"), ("1010 CE", "Imperial Cholas"), ("1526 CE", "Mughal Empire"), 
            ("1947 CE", "Modern Republic")]
    ex = 80
    for yr, nm in eras:
        draw.rectangle([(ex, 610), (ex + 135, 680)], outline='#3f3f46', fill='#121217', width=1)
        draw.text((ex + 10, 620), yr, fill='#fbbf24', font=get_font(11))
        draw.text((ex + 10, 645), nm, fill='#ffffff', font=get_font(12, True))
        ex += 150

    img.save(os.path.join(ASSETS_DIR, "ss1_hero_portal.png"))
    print("[+] Created ss1_hero_portal.png")

# ---------------------------------------------------------------------------
# SS 2: HORIZONTAL TIMELINE
# ---------------------------------------------------------------------------
def make_ss2_timeline():
    img = Image.new('RGB', (W, H), color='#09090c')
    draw = ImageDraw.Draw(img)
    draw_sony_header(draw, "Chronology")

    draw.text((80, 90), "THE MASTER CHRONICLE", fill='#fbbf24', font=get_font(11, True))
    draw.text((80, 115), "Timeline of Civilizations", fill='#ffffff', font=get_font(28, True))
    draw.text((80, 155), "Navigate 5,000 years of subcontinent history through our dual-mode interactive timeline.", fill='#9ca3af', font=get_font(13))

    # Filter tabs
    draw.rectangle([(80, 200), (170, 235)], fill='#ffffff')
    draw.text((100, 210), "All Eras", fill='#000000', font=get_font(12, True))
    cats = ["Ancient", "Classical", "Medieval", "Modern"]
    cx = 185
    for c in cats:
        draw.rectangle([(cx, 200), (cx + 90, 235)], outline='#3f3f46', fill='#18181b', width=1)
        draw.text((cx + 15, 210), c, fill='#a1a1a8', font=get_font(12))
        cx += 105

    # Switcher
    draw.rectangle([(930, 200), (1120, 235)], outline='#3f3f46', fill='#18181b', width=1)
    draw.rectangle([(932, 202), (1030, 233)], fill='#27272a')
    draw.text((940, 210), "Horizontal", fill='#ffffff', font=get_font(11, True))
    draw.text((1045, 210), "Vertical", fill='#71717a', font=get_font(11))

    # 3 Era Cards
    cards = [
        ("Indus Valley Civilization", "3300 BCE – 1300 BCE", "The Bronze Age Urban Metropolis", "priest_king.jpg", "Mohenjo-daro & Harappa"),
        ("The Maurya Empire", "322 BCE – 185 BCE", "Pan-Indian Unity & Ashoka's Dhamma", "ashoka_lion.jpg", "Pataliputra (Patna)"),
        ("Cholas & Medieval Grandeur", "850 CE – 1526 CE", "Oceanic Fleets & Living Temples", "brihadisvara.jpg", "Thanjavur & Hampi")
    ]
    card_x = 80
    for title, period, sub, img_name, cap in cards:
        draw.rectangle([(card_x, 260), (card_x + 325, 660)], outline='#27272a', fill='#121217', width=1)
        
        card_img_path = os.path.join(IMG_DIR, img_name)
        if os.path.exists(card_img_path):
            try:
                c_img = Image.open(card_img_path).convert('RGB').resize((323, 170))
                img.paste(c_img, (card_x + 1, 261))
            except Exception:
                draw.rectangle([(card_x + 1, 261), (card_x + 324, 430)], fill='#1f2937')
        else:
            draw.rectangle([(card_x + 1, 261), (card_x + 324, 430)], fill='#1f2937')

        draw.rectangle([(card_x + 15, 275), (card_x + 160, 300)], fill='#000000', outline='#d4af37', width=1)
        draw.text((card_x + 22, 280), period, fill='#fbbf24', font=get_font(10, True))

        draw.text((card_x + 20, 450), sub, fill='#fbbf24', font=get_font(11))
        draw.text((card_x + 20, 475), title, fill='#ffffff', font=get_font(18, True))
        draw.text((card_x + 20, 520), f"Epicenter: {cap}", fill='#9ca3af', font=get_font(12))

        draw.rectangle([(card_x + 20, 595), (card_x + 305, 635)], outline='#52525b', fill='#18181b', width=1)
        draw.text((card_x + 95, 608), "EXPLORE ERA →", fill='#ffffff', font=get_font(11, True))
        card_x += 355

    img.save(os.path.join(ASSETS_DIR, "ss2_horizontal_timeline.png"))
    print("[+] Created ss2_horizontal_timeline.png")

# ---------------------------------------------------------------------------
# SS 3: VERTICAL FEED TIMELINE
# ---------------------------------------------------------------------------
def make_ss3_vertical():
    img = Image.new('RGB', (W, H), color='#09090c')
    draw = ImageDraw.Draw(img)
    draw_sony_header(draw, "Chronology")

    draw.text((80, 85), "THE MASTER CHRONICLE", fill='#fbbf24', font=get_font(11, True))
    draw.text((80, 110), "Vertical Documentary Feed Mode", fill='#ffffff', font=get_font(26, True))

    # Vertical spine line
    draw.line([(140, 180), (140, 680)], fill='#d4af37', width=2)

    milestones = [
        ("322 BCE", "Ascent of Chandragupta Maurya", "Overthrow of the Nanda dynasty and unification of northern India under the mentorship of polymath Chanakya."),
        ("261 BCE", "The Kalinga War & Renunciation", "Emperor Ashoka converts to Buddhism, adopting Ahimsa (non-violence) and ethical statehood inscribed on rock edicts."),
        ("499 CE", "Aryabhata Authors Aryabhatiya", "Calculated solar year to 365.358 days, formulated trigonometry, and asserted Earth's axial rotation during the Gupta Age."),
        ("1010 CE", "Consecration of Brihadisvara Temple", "Raja Raja Chola I completes the 216-foot granite Vimana topped with an 80-tonne single granite capstone without mortar.")
    ]
    my = 180
    for yr, title, desc in milestones:
        # Golden Node on the spine
        draw.ellipse([(132, my + 15), (148, my + 31)], fill='#d4af37', outline='#ffffff', width=2)
        
        # Card box
        draw.rectangle([(180, my), (1100, my + 105)], outline='#27272a', fill='#121217', width=1)
        draw.rectangle([(200, my + 15), (310, my + 42)], outline='#d4af37', fill='#1f1b0d', width=1)
        draw.text((215, my + 21), yr, fill='#fbbf24', font=get_font(12, True))
        
        draw.text((330, my + 18), title, fill='#ffffff', font=get_font(16, True))
        draw.text((200, my + 55), desc, fill='#9ca3af', font=get_font(12))
        my += 125

    img.save(os.path.join(ASSETS_DIR, "ss3_vertical_feed.png"))
    print("[+] Created ss3_vertical_feed.png")

# ---------------------------------------------------------------------------
# SS 4: ARTIFACT GALLERY
# ---------------------------------------------------------------------------
def make_ss4_gallery():
    img = Image.new('RGB', (W, H), color='#070709')
    draw = ImageDraw.Draw(img)
    draw_sony_header(draw, "Artifacts")

    draw.text((80, 85), "NATIONAL TREASURES", fill='#fbbf24', font=get_font(11, True))
    draw.text((80, 108), "Artifacts & Monumental Architecture", fill='#ffffff', font=get_font(26, True))

    arts = [
        ("Dancing Girl of Mohenjo-daro", "c. 2300–1750 BCE", "dancing_girl.jpg", "National Museum, New Delhi", "Bronze Lost-Wax Casting"),
        ("Lion Capital of Ashoka", "c. 250 BCE", "ashoka_lion.jpg", "Sarnath Museum, UP", "Polished Chunar Sandstone"),
        ("The Taj Mahal", "1632–1653 CE", "taj_mahal.jpg", "Agra, Uttar Pradesh", "Makrana White Marble")
    ]
    ax = 80
    for name, dt, img_f, loc, mat in arts:
        draw.rectangle([(ax, 160), (ax + 325, 660)], outline='#27272a', fill='#111116', width=1)
        p_path = os.path.join(IMG_DIR, img_f)
        if os.path.exists(p_path):
            try:
                p_img = Image.open(p_path).convert('RGB').resize((323, 260))
                img.paste(p_img, (ax + 1, 161))
            except Exception:
                pass
        
        draw.ellipse([(ax + 275, 175), (ax + 310, 210)], fill='#000000', outline='#d4af37', width=1)
        draw.text((ax + 287, 185), "★", fill='#fbbf24', font=get_font(14))

        draw.text((ax + 20, 440), dt, fill='#fbbf24', font=get_font(11))
        draw.text((ax + 20, 465), name, fill='#ffffff', font=get_font(16, True))
        draw.text((ax + 20, 510), f"Medium: {mat}", fill='#a1a1a8', font=get_font(12))
        draw.text((ax + 20, 540), f"Location: {loc}", fill='#71717a', font=get_font(11))

        draw.rectangle([(ax + 20, 595), (ax + 305, 635)], outline='#d4af37', fill='#1c170d', width=1)
        draw.text((ax + 85, 608), "INSPECT ARTIFACT ↗", fill='#fbbf24', font=get_font(11, True))
        ax += 355

    img.save(os.path.join(ASSETS_DIR, "ss4_artifact_gallery.png"))
    print("[+] Created ss4_artifact_gallery.png")

# ---------------------------------------------------------------------------
# SS 5: FULL-SCREEN DARKROOM LIGHTBOX MODAL
# ---------------------------------------------------------------------------
def make_ss5_lightbox():
    img = Image.new('RGB', (W, H), color='#020203')
    draw = ImageDraw.Draw(img)
    draw_sony_header(draw, "Artifacts")

    # Dark backdrop
    draw.rectangle([(0, 60), (W, H)], fill='#060608')

    # Modal Card
    mx, my, mw, mh = 140, 95, 920, 570
    draw.rectangle([(mx, my), (mx + mw, my + mh)], outline='#3f3f46', fill='#0e0e13', width=1)

    # Left visual side
    draw.rectangle([(mx, my), (mx + 450, my + mh)], fill='#050507')
    p_path = os.path.join(IMG_DIR, "ashoka_lion.jpg")
    if os.path.exists(p_path):
        try:
            m_img = Image.open(p_path).convert('RGB').resize((448, 568))
            img.paste(m_img, (mx + 1, my + 1))
        except Exception:
            pass

    # Right info side
    rx = mx + 480
    draw.rectangle([(rx, my + 35), (rx + 140, my + 65)], outline='#d4af37', fill='#221a0a', width=1)
    draw.text((rx + 15, my + 42), "c. 250 BCE", fill='#fbbf24', font=get_font(11, True))
    draw.text((rx + 160, my + 42), "SCULPTURE", fill='#9ca3af', font=get_font(11, True))

    draw.text((rx, my + 80), "Lion Capital of Ashoka", fill='#ffffff', font=get_font(24, True))
    draw.text((rx, my + 125), "Originally crowning the Ashoka Pillar at Sarnath where the Buddha\n"
                              "first turned the wheel of law. Featuring four Asiatic lions standing\n"
                              "back to back. Adopted as the National Emblem of India in 1950.",
              fill='#d1d5db', font=get_font(12))

    # Provenance rows
    prov = [
        ("CIVILIZATIONAL ERA", "Maurya Empire"),
        ("CURRENT PROVENANCE", "Sarnath Museum, Uttar Pradesh"),
        ("MATERIAL / MEDIUM", "Polished Chunar Sandstone"),
        ("DIMENSIONS", "2.15 meters height")
    ]
    py = my + 230
    for lbl, val in prov:
        draw.line([(rx, py), (rx + 400, py)], fill='#22222a', width=1)
        draw.text((rx, py + 8), lbl, fill='#71717a', font=get_font(9, True))
        draw.text((rx + 170, py + 8), val, fill='#ffffff', font=get_font(11, True))
        py += 45

    # Buttons
    draw.rectangle([(rx, my + 460), (rx + 190, my + 505)], outline='#52525b', fill='#18181b', width=1)
    draw.text((rx + 25, my + 475), "View on Wikipedia ↗", fill='#ffffff', font=get_font(11, True))

    draw.rectangle([(rx + 210, my + 460), (rx + 400, my + 505)], outline='#d4af37', fill='#fbbf24', width=1)
    draw.text((rx + 230, my + 475), "★ In Your Collection", fill='#000000', font=get_font(11, True))

    img.save(os.path.join(ASSETS_DIR, "ss5_lightbox_modal.png"))
    print("[+] Created ss5_lightbox_modal.png")

# ---------------------------------------------------------------------------
# SS 6: IMPERIAL ATLAS
# ---------------------------------------------------------------------------
def make_ss6_atlas():
    img = Image.new('RGB', (W, H), color='#070709')
    draw = ImageDraw.Draw(img)
    draw_sony_header(draw, "Empires")

    draw.text((80, 85), "SOVEREIGN REALMS", fill='#fbbf24', font=get_font(11, True))
    draw.text((80, 108), "The Imperial Dynasties Explorer", fill='#ffffff', font=get_font(26, True))

    # Sidebar
    draw.rectangle([(80, 160), (360, 660)], outline='#27272a', fill='#111116', width=1)
    dynasties = [("Maurya Empire", "322 – 185 BCE", True), 
                 ("Gupta Empire", "320 – 550 CE", False), 
                 ("Imperial Chola Dynasty", "848 – 1279 CE", False),
                 ("Vijayanagara Empire", "1336 – 1646 CE", False),
                 ("Mughal Empire", "1526 – 1857 CE", False),
                 ("Maratha Empire", "1674 – 1818 CE", False)]
    dy = 175
    for name, prd, is_sel in dynasties:
        bg = '#22222a' if is_sel else '#111116'
        bd = '#d4af37' if is_sel else '#1f1f23'
        draw.rectangle([(95, dy), (345, dy + 65)], outline=bd, fill=bg, width=2 if is_sel else 1)
        draw.text((110, dy + 12), name, fill='#ffffff', font=get_font(13, True))
        draw.text((110, dy + 36), prd, fill='#fbbf24', font=get_font(11))
        dy += 78

    # Detail View
    draw.rectangle([(390, 160), (1120, 660)], outline='#27272a', fill='#111116', width=1)
    draw.text((430, 200), "322 BCE – 185 BCE", fill='#fbbf24', font=get_font(12, True))
    draw.text((430, 230), "Maurya Empire", fill='#ffffff', font=get_font(32, True))
    draw.text((430, 275), "Subcontinent Pan-Indian Unity under Chandragupta & Ashoka", fill='#9ca3af', font=get_font(14))

    stats = [("PEAK TERRITORY", "5,000,000 km²"), ("IMPERIAL CAPITAL", "Pataliputra (Patna)"), 
             ("FOUNDER", "Chandragupta Maurya"), ("GREATEST SOVEREIGN", "Ashoka the Great")]
    sx = 430
    for label, val in stats:
        draw.rectangle([(sx, 320), (sx + 150, 390)], outline='#27272a', fill='#18181f', width=1)
        draw.text((sx + 12, 332), label, fill='#71717a', font=get_font(9, True))
        draw.text((sx + 12, 355), val, fill='#ffffff', font=get_font(12, True))
        sx += 165

    draw.text((430, 430), "MONUMENTAL ACHIEVEMENTS & LEGACY", fill='#71717a', font=get_font(11, True))
    ach = [
        "✦ First political unification of the entire Indian subcontinent spanning Afghanistan to Mysore.",
        "✦ Arthashastra treatise on statecraft, diplomacy, and economics authored by Chanakya.",
        "✦ Emperor Ashoka's Edicts carved across stone pillars proclaiming peace and religious tolerance.",
        "✦ Construction of the Grand Trunk Road precursor network and Sanchi Stupa monument."
    ]
    ay = 465
    for a in ach:
        draw.text((430, ay), a, fill='#d1d5db', font=get_font(12))
        ay += 35

    img.save(os.path.join(ASSETS_DIR, "ss6_imperial_atlas.png"))
    print("[+] Created ss6_imperial_atlas.png")

# ---------------------------------------------------------------------------
# SS 7: KNOWLEDGE QUIZ
# ---------------------------------------------------------------------------
def make_ss7_quiz():
    img = Image.new('RGB', (W, H), color='#070709')
    draw = ImageDraw.Draw(img)
    draw_sony_header(draw, "Quiz ✦")

    draw.rectangle([(0, 60), (W, H)], fill='#050508')

    mx, my, mw, mh = 260, 110, 680, 540
    draw.rectangle([(mx, my), (mx + mw, my + mh)], outline='#38bdf8', fill='#0f172a', width=2)
    draw.text((mx + mw - 40, my + 20), "✕", fill='#94a3b8', font=get_font(18, True))

    draw.rectangle([(mx + 35, my + 30), (mx + 175, my + 60)], outline='#fbbf24', fill='#2d2005', width=1)
    draw.text((mx + 45, my + 37), "QUESTION 2 OF 5", fill='#fbbf24', font=get_font(11, True))
    draw.text((mx + mw - 140, my + 37), "Score: 1 / 5", fill='#94a3b8', font=get_font(13, True))

    draw.text((mx + 35, my + 85), "Which Mauryan Emperor renounced warfare and adopted\nDhamma after witnessing the Kalinga War?", 
              fill='#ffffff', font=get_font(18, True))

    options = [
        ("A", "Chandragupta Maurya", False),
        ("B", "Bindusara", False),
        ("C", "Ashoka the Great", True),
        ("D", "Brihadratha", False)
    ]
    oy = my + 170
    for letter, opt_text, is_correct in options:
        border_col = '#4ade80' if is_correct else '#334155'
        bg_col = '#052e16' if is_correct else '#1e293b'
        text_col = '#86efac' if is_correct else '#ffffff'
        
        draw.rectangle([(mx + 35, oy), (mx + mw - 35, oy + 48)], outline=border_col, fill=bg_col, width=2 if is_correct else 1)
        draw.ellipse([(mx + 50, oy + 12), (mx + 74, oy + 36)], fill='#0f172a', outline=border_col, width=1)
        draw.text((mx + 58, oy + 15), letter, fill='#fbbf24', font=get_font(11, True))
        draw.text((mx + 90, oy + 15), opt_text, fill=text_col, font=get_font(14, is_correct))
        oy += 58

    draw.rectangle([(mx + 35, my + 415), (mx + mw - 35, my + 475)], outline='#16a34a', fill='#064e3b', width=1)
    draw.text((mx + 50, my + 423), "✓ Correct! Emperor Ashoka underwent a profound moral transformation in 261 BCE.", fill='#86efac', font=get_font(11, True))
    draw.text((mx + 50, my + 445), "He dedicated his reign to Ahimsa (non-violence) and ethical rock edict governance.", fill='#d1fae5', font=get_font(11))

    draw.rectangle([(mx + mw - 195, my + 490), (mx + mw - 35, my + 525)], fill='#2563eb')
    draw.text((mx + mw - 175, my + 498), "NEXT QUESTION →", fill='#ffffff', font=get_font(11, True))

    img.save(os.path.join(ASSETS_DIR, "ss7_knowledge_quiz.png"))
    print("[+] Created ss7_knowledge_quiz.png")

# ---------------------------------------------------------------------------
# SS 8: INSTANT SEARCH DRAWER
# ---------------------------------------------------------------------------
def make_ss8_search():
    img = Image.new('RGB', (W, H), color='#070709')
    draw = ImageDraw.Draw(img)
    draw_sony_header(draw)

    # Background dimmed
    draw.rectangle([(0, 60), (W - 450, H)], fill='#030305')

    # Slide drawer on right
    dx = W - 450
    draw.rectangle([(dx, 60), (W, H)], outline='#27272a', fill='#101016', width=1)

    # Header tabs
    draw.rectangle([(dx + 25, 80), (dx + 150, 115)], fill='#ffffff')
    draw.text((dx + 40, 90), "Search Archive", fill='#000000', font=get_font(12, True))

    draw.rectangle([(dx + 165, 80), (dx + 295, 115)], outline='#3f3f46', fill='#18181b', width=1)
    draw.text((dx + 180, 90), "Your Collection", fill='#a1a1a8', font=get_font(12))

    # Search input
    draw.rectangle([(dx + 25, 140), (W - 25, 185)], outline='#52525b', fill='#08080a', width=1)
    draw.text((dx + 45, 152), "🔍 Ashoka", fill='#ffffff', font=get_font(14))

    draw.text((dx + 25, 210), "FOUND 3 HISTORICAL RECORDS", fill='#71717a', font=get_font(10, True))

    # Results
    results = [
        ("ARTIFACT / MONUMENT", "c. 250 BCE · Sarnath Museum", "Lion Capital of Ashoka", "Carved from polished sandstone crowned with 4 roaring lions..."),
        ("ERA / EPOCH", "322 BCE – 185 BCE", "The Maurya Empire", "Emperor Ashoka renounces warfare following the Kalinga War..."),
        ("SOVEREIGN REALM", "322 – 185 BCE", "Maurya Dynasty", "Peak territorial domain of 5,000,000 km² spanning Afghanistan...")
    ]
    ry = 235
    for tag, sub, title, snippet in results:
        draw.rectangle([(dx + 25, ry), (W - 25, ry + 115)], outline='#27272a', fill='#181820', width=1)
        draw.rectangle([(dx + 35, ry + 10), (dx + 175, ry + 30)], outline='#d4af37', fill='#221a0a', width=1)
        draw.text((dx + 42, ry + 14), tag, fill='#fbbf24', font=get_font(9, True))
        draw.text((dx + 185, ry + 14), sub, fill='#71717a', font=get_font(10))

        draw.text((dx + 35, ry + 42), title, fill='#ffffff', font=get_font(15, True))
        draw.text((dx + 35, ry + 75), snippet, fill='#9ca3af', font=get_font(11))
        ry += 130

    img.save(os.path.join(ASSETS_DIR, "ss8_instant_search.png"))
    print("[+] Created ss8_instant_search.png")

# ---------------------------------------------------------------------------
# SS 9: AUDIO ATMOSPHERE SYNTHESIZER
# ---------------------------------------------------------------------------
def make_ss9_audio():
    img = Image.new('RGB', (W, H), color='#070709')
    draw = ImageDraw.Draw(img)
    draw_sony_header(draw)

    # Ambient audio showcase banner
    draw.rectangle([(150, 160), (1050, 600)], outline='#d4af37', fill='#0c0c12', width=1)
    
    draw.text((200, 210), "WEB AUDIO API HARMONIC SYNTHESIZER", fill='#fbbf24', font=get_font(12, True))
    draw.text((200, 240), "Authentic Indian Classical Tanpura Drone", fill='#ffffff', font=get_font(28, True))
    draw.text((200, 285), "Zero-dependency pure browser acoustic synthesis calibrated to Sa-Pa (138.59 Hz / 207.65 Hz).", 
              fill='#9ca3af', font=get_font(14))

    # Waveform visualization
    draw.rectangle([(200, 340), (1000, 460)], outline='#27272a', fill='#050508', width=1)
    
    import math
    for i in range(200, 1000, 4):
        y_val = 400 + int(35 * math.sin((i - 200) * 0.05) * math.cos((i - 200) * 0.02))
        draw.line([(i, 400), (i, y_val)], fill='#22c55e', width=2)

    # Status box
    draw.rectangle([(200, 490), (450, 550)], outline='#16a34a', fill='#052e16', width=1)
    draw.text((230, 510), "● Atmosphere: Active (432Hz Resonance)", fill='#86efac', font=get_font(12, True))

    draw.rectangle([(480, 490), (730, 550)], outline='#3f3f46', fill='#18181b', width=1)
    draw.text((510, 510), "Master Volume: -18 dB (Exponential Ramp)", fill='#ffffff', font=get_font(12))

    img.save(os.path.join(ASSETS_DIR, "ss9_audio_atmosphere.png"))
    print("[+] Created ss9_audio_atmosphere.png")

# ---------------------------------------------------------------------------
# SS 10: PYTHON LOCALHOST CONSOLE
# ---------------------------------------------------------------------------
def make_ss10_terminal():
    img = Image.new('RGB', (W, H), color='#0c0c0e')
    draw = ImageDraw.Draw(img)

    # Terminal window frame
    draw.rectangle([(100, 80), (1100, 640)], outline='#3f3f46', fill='#000000', width=1)
    # Titlebar
    draw.rectangle([(100, 80), (1100, 120)], fill='#18181b')
    draw.ellipse([(120, 95), (132, 107)], fill='#ef4444')
    draw.ellipse([(140, 95), (152, 107)], fill='#eab308')
    draw.ellipse([(160, 95), (172, 107)], fill='#22c55e')
    draw.text((200, 93), "Command Prompt - python server.py (History of India Localhost Engine)", fill='#a1a1a8', font=get_font(11))

    # Console Text
    console_lines = [
        "C:\\Users\\RAUNAK JAISWAL\\OneDrive\\Desktop\\History of India> python server.py",
        "====================================================================",
        "  * HISTORY OF INDIA - SONY AESTHETIC WEB PLATFORM *",
        "====================================================================",
        "  [+] Server running at : http://localhost:8000",
        "  [+] REST API online   : http://localhost:8000/api/status",
        "  [+] History Quiz API  : http://localhost:8000/api/quiz",
        "  [+] Local Root Dir    : C:\\Users\\RAUNAK JAISWAL\\OneDrive\\Desktop\\History of India",
        "====================================================================",
        "  Press Ctrl+C to terminate the local server.",
        "",
        "  [HTTP GET 200] /index.html (text/html; charset=utf-8) - 17,705 bytes",
        "  [HTTP GET 200] /css/components.css (text/css) - 23,462 bytes",
        "  [HTTP GET 200] /images/taj_mahal.jpg (image/jpeg) - 258,377 bytes",
        "  [HTTP GET 200] /api/status -> {\"status\": \"online\", \"port\": 8000}",
        "  [HTTP GET 200] /api/quiz -> {\"quiz\": \"Indian Civilizational Knowledge Test\"}"
    ]
    ty = 145
    for line in console_lines:
        col = '#4ade80' if '[HTTP GET' in line or '[+]' in line else ('#fbbf24' if '*' in line else '#f8fafc')
        draw.text((130, ty), line, fill=col, font=get_font(12, bold='*' in line))
        ty += 28

    img.save(os.path.join(ASSETS_DIR, "ss10_python_server.png"))
    print("[+] Created ss10_python_server.png")

if __name__ == '__main__':
    make_ss1_hero()
    make_ss2_timeline()
    make_ss3_vertical()
    make_ss4_gallery()
    make_ss5_lightbox()
    make_ss6_atlas()
    make_ss7_quiz()
    make_ss8_search()
    make_ss9_audio()
    make_ss10_terminal()
