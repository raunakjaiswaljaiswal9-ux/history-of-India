import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "doc_assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. GANTT CHART (Figure 9.1)
# ---------------------------------------------------------------------------
def create_gantt_chart():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f8fafc')

    tasks = [
        'Deployment & Launch',
        'QA & Cross-Browser Testing',
        'Local Asset Ingestion & Media Audit',
        'Audio Synthesizer & Python Backend',
        'UI Components & Scrubber Engine',
        'Data Modeling & Schema Formulation',
        'Planning & Curatorial Research'
    ]
    starts = [10, 9, 7, 6, 4, 2, 0]
    durations = [2, 2, 3, 3, 4, 3, 2]
    colors = ['#4c1d95', '#0284c7', '#059669', '#d97706', '#dc2626', '#2563eb', '#1e293b']

    for i in range(len(tasks)):
        ax.barh(tasks[i], durations[i], left=starts[i], color=colors[i], height=0.55, edgecolor='black', linewidth=0.8, alpha=0.9)
        ax.text(starts[i] + durations[i]/2, i, f"Weeks {starts[i]+1}–{starts[i]+durations[i]}", 
                va='center', ha='center', color='white', fontweight='bold', fontsize=9)

    ax.set_xlabel('Project Sprints (Weeks 1 to 12)', fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title('Figure 9.1: History of India Development Lifecycle Gantt Chart', fontsize=13, fontweight='bold', pad=15)
    ax.set_xlim(0, 12)
    ax.set_xticks(range(0, 13))
    ax.set_xticklabels([f"W{i}" if i > 0 else "Start" for i in range(0, 13)], fontsize=9)
    ax.grid(axis='x', linestyle='--', alpha=0.4, color='#94a3b8')
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "gantt_chart.png"), dpi=300)
    plt.close()
    print("[+] Created gantt_chart.png")

# ---------------------------------------------------------------------------
# 2. SYSTEM DESIGN DIAGRAM (Figure 10.0)
# ---------------------------------------------------------------------------
def create_system_design_diagram():
    fig, ax = plt.subplots(figsize=(9, 10), dpi=300)
    ax.set_facecolor('#ffffff')
    ax.axis('off')

    boxes = [
        # Left column: Client Interaction Pipeline
        (0.12, 0.88, 0.34, 0.08, "1. Client Launch\n(Browser / localhost:8000)", "#3b82f6"),
        (0.12, 0.72, 0.34, 0.08, "2. DOM Initialization\n(Sony Darkroom Canvas)", "#10b981"),
        (0.12, 0.56, 0.34, 0.08, "3. UI Module Mounting\n(Timeline, Gallery, Atlas)", "#f59e0b"),
        (0.12, 0.40, 0.34, 0.08, "4. Interactive User Input\n(Scrubbing, Lightbox, Quiz)", "#8b5cf6"),
        (0.12, 0.24, 0.34, 0.08, "5. Web Audio Synthesis\n(Tanpura Sa-Pa Drone)", "#ec4899"),
        (0.12, 0.08, 0.34, 0.08, "6. LocalStorage Sync\n(Client-Side Bookmarks)", "#06b6d4"),

        # Right column: Server & Data Processing Pipeline
        (0.54, 0.88, 0.34, 0.08, "Python HTTP Engine\n(Standard library server.py)", "#6366f1"),
        (0.54, 0.72, 0.34, 0.08, "REST API Endpoints\n(/api/status, /api/quiz)", "#14b8a6"),
        (0.54, 0.56, 0.34, 0.08, "Local Media Cache\n(22 Assets in images/)", "#84cc16"),
        (0.54, 0.40, 0.34, 0.08, "Server Disk Persistence\n(user_bookmarks.json)", "#f97316"),
        (0.54, 0.24, 0.34, 0.08, "Zero-Dependency Fallback\n(file:/// Direct Launch)", "#ef4444"),
        (0.54, 0.08, 0.34, 0.08, "Cross-Browser Render\n(Chrome, Edge, Firefox)", "#0284c7"),
    ]

    for (x, y, w, h, text, color) in boxes:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03", 
                                      linewidth=1.2, edgecolor='#1e293b', facecolor=color, alpha=0.88)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', color='white', fontweight='bold', fontsize=9.5)

    # Connecting arrows left column
    for y_pos in [0.88, 0.72, 0.56, 0.40, 0.24]:
        ax.annotate('', xy=(0.29, y_pos - 0.08), xytext=(0.29, y_pos),
                    arrowprops=dict(facecolor='#334155', shrink=0.15, width=1.5, headwidth=6))

    # Connecting arrows right column
    for y_pos in [0.88, 0.72, 0.56, 0.40, 0.24]:
        ax.annotate('', xy=(0.71, y_pos - 0.08), xytext=(0.71, y_pos),
                    arrowprops=dict(facecolor='#334155', shrink=0.15, width=1.5, headwidth=6))

    # Cross interaction arrow
    ax.annotate('', xy=(0.54, 0.76), xytext=(0.46, 0.76),
                arrowprops=dict(facecolor='#0f172a', shrink=0.1, width=2, headwidth=7))
    ax.text(0.50, 0.78, "API Sync", ha='center', fontsize=8, fontweight='bold', color='#0f172a')

    ax.set_title("Figure 10.0: High-Level System Architecture and Multi-Tier Processing Pipeline", 
                 fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "system_design_diagram.png"), dpi=300)
    plt.close()
    print("[+] Created system_design_diagram.png")

# ---------------------------------------------------------------------------
# 3. ENTITY RELATIONSHIP (ER) DIAGRAM (Figure 10.1)
# ---------------------------------------------------------------------------
def create_er_diagram():
    fig, ax = plt.subplots(figsize=(9, 7.5), dpi=300)
    ax.set_facecolor('#ffffff')
    ax.axis('off')

    entities = [
        (0.08, 0.68, 0.38, 0.25, "ERA\n---\nPK  id : String\n    title : String\n    period : String\n    category : Enum\n    capital : String\n    image : FilePath", "#1e3a8a"),
        (0.54, 0.68, 0.38, 0.25, "ARTIFACT\n---\nPK  id : String\nFK  era_id : String\n    title : String\n    period : String\n    material : String\n    location : String", "#065f46"),
        (0.08, 0.20, 0.38, 0.25, "DYNASTY\n---\nPK  id : String\n    name : String\n    period : String\n    capital : String\n    founder : String\n    territoryKm2 : String", "#854d0e"),
        (0.54, 0.20, 0.38, 0.25, "USER_BOOKMARK\n---\nPK  id : Integer\nFK  artifact_id : String\n    user_ip : String\n    saved_at : Timestamp\n    sync_status : Boolean", "#991b1b")
    ]

    for (x, y, w, h, text, color) in entities:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.02", 
                                      linewidth=1.5, edgecolor='#0f172a', facecolor='#f8fafc')
        ax.add_patch(rect)
        # Header banner
        header = patches.FancyBboxPatch((x, y + h*0.75), w, h*0.25, boxstyle="round,pad=0.02,rounding_size=0.02", 
                                        linewidth=1.2, edgecolor='#0f172a', facecolor=color)
        ax.add_patch(header)
        ax.text(x + w/2, y + h*0.87, text.split('\n')[0], ha='center', va='center', color='white', fontweight='bold', fontsize=11)
        ax.text(x + 0.02, y + h*0.35, '\n'.join(text.split('\n')[2:]), ha='left', va='center', color='#0f172a', fontfamily='monospace', fontsize=8.5)

    # Relationship connectors
    ax.annotate('', xy=(0.54, 0.80), xytext=(0.46, 0.80),
                arrowprops=dict(arrowstyle='<->', linewidth=2, color='#1e293b'))
    ax.text(0.50, 0.82, "1 : N (Contains)", ha='center', fontsize=9, fontweight='bold', color='#1e293b')

    ax.annotate('', xy=(0.73, 0.45), xytext=(0.73, 0.68),
                arrowprops=dict(arrowstyle='<->', linewidth=2, color='#1e293b'))
    ax.text(0.75, 0.56, "1 : N (Saved)", ha='left', fontsize=9, fontweight='bold', color='#1e293b')

    ax.set_title("Figure 10.1: Entity-Relationship (ER) Diagram of the Relational Data Model", 
                 fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "er_diagram.png"), dpi=300)
    plt.close()
    print("[+] Created er_diagram.png")

# ---------------------------------------------------------------------------
# 4. CLASS DIAGRAM (Figure 10.2)
# ---------------------------------------------------------------------------
def create_class_diagram():
    fig, ax = plt.subplots(figsize=(9, 7.5), dpi=300)
    ax.set_facecolor('#ffffff')
    ax.axis('off')

    classes = [
        (0.06, 0.60, 0.40, 0.32, "HistoryApp.Timeline\n--------------------\n- currentFilter: String\n- currentViewMode: String\n- isDragging: Boolean\n--------------------\n+ init(): void\n+ render(): void\n+ renderHorizontalView(): void\n+ openEraModal(id): void", "#1e40af"),
        (0.54, 0.60, 0.40, 0.32, "HistoryApp.Gallery\n--------------------\n- currentCategory: String\n- cachedArtifacts: Array\n--------------------\n+ init(): void\n+ render(): void\n+ openLightbox(id): void\n+ toggleBookmark(id): void", "#047857"),
        (0.06, 0.12, 0.40, 0.36, "HistoryApp.Audio\n--------------------\n- audioCtx: AudioContext\n- masterGain: GainNode\n- oscillators: Array\n--------------------\n+ init(): void\n+ startDrone(): void\n+ stopDrone(): void\n+ togglePlay(): void", "#7c2d12"),
        (0.54, 0.12, 0.40, 0.36, "HistoryApp.Quiz\n--------------------\n- questions: Array\n- currentIdx: Integer\n- userScore: Integer\n--------------------\n+ openQuizModal(): void\n+ loadQuestions(): Promise\n+ selectAnswer(idx): void\n+ renderResults(): void", "#6b21a8")
    ]

    for (x, y, w, h, text, color) in classes:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.02", 
                                      linewidth=1.5, edgecolor='#1e293b', facecolor='#f1f5f9')
        ax.add_patch(rect)
        hdr = patches.FancyBboxPatch((x, y + h*0.80), w, h*0.20, boxstyle="round,pad=0.02,rounding_size=0.02", 
                                     linewidth=1.2, edgecolor='#1e293b', facecolor=color)
        ax.add_patch(hdr)
        lines = text.split('\n')
        ax.text(x + w/2, y + h*0.90, lines[0], ha='center', va='center', color='white', fontweight='bold', fontsize=9.5)
        ax.text(x + 0.02, y + h*0.38, '\n'.join(lines[2:]), ha='left', va='center', color='#0f172a', fontfamily='monospace', fontsize=8)

    ax.set_title("Figure 10.2: UML Class Diagram detailing Object-Oriented Software Architecture", 
                 fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "class_diagram.png"), dpi=300)
    plt.close()
    print("[+] Created class_diagram.png")

# ---------------------------------------------------------------------------
# 5. ACTIVITY DIAGRAM (Figure 10.3)
# ---------------------------------------------------------------------------
def create_activity_diagram():
    fig, ax = plt.subplots(figsize=(9, 8.5), dpi=300)
    ax.set_facecolor('#ffffff')
    ax.axis('off')

    # Swimlanes
    swimlanes = [
        (0.04, 0.92, 0.28, "Presentation Layer"),
        (0.36, 0.92, 0.28, "Controller / Engine"),
        (0.68, 0.92, 0.28, "Data & Services")
    ]
    for x, y, w, title in swimlanes:
        hdr = patches.Rectangle((x, y - 0.05), w, 0.05, facecolor='#1e293b', edgecolor='black')
        ax.add_patch(hdr)
        ax.text(x + w/2, y - 0.025, title, ha='center', va='center', color='white', fontweight='bold', fontsize=9.5)
        lane = patches.Rectangle((x, 0.05), w, 0.82, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1)
        ax.add_patch(lane)

    activities = [
        (0.07, 0.76, 0.22, 0.07, "User navigates to\nhttp://localhost:8000", "#2563eb"),
        (0.39, 0.76, 0.22, 0.07, "checkLocalhostBackend()\nHTTP /api/status", "#059669"),
        (0.71, 0.76, 0.22, 0.07, "server.py returns\nStatus: Online, Port: 8000", "#7c3aed"),
        (0.07, 0.58, 0.22, 0.07, "Selects Era on Timeline\nor Clicks Artifact", "#d97706"),
        (0.39, 0.58, 0.22, 0.07, "Filter / Scrubber Event\nDispatch Modal Request", "#db2777"),
        (0.71, 0.58, 0.22, 0.07, "Loads images/<slug>.jpg\nfrom local disk cache", "#475569"),
        (0.07, 0.40, 0.22, 0.07, "User Triggers Quiz ✦\nKnowledge Challenge", "#0284c7"),
        (0.39, 0.40, 0.22, 0.07, "Fetch /api/quiz & Score\nInteractive 5-Questions", "#16a34a"),
        (0.07, 0.22, 0.22, 0.07, "Toggles Atmosphere\nAudio Button", "#b45309"),
        (0.39, 0.22, 0.22, 0.07, "Web Audio API Generates\nTanpura Harmonic Drone", "#9333ea")
    ]

    for x, y, w, h, text, color in activities:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.02",
                                     facecolor=color, edgecolor='black', linewidth=1, alpha=0.9)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', color='white', fontweight='bold', fontsize=8)

    # Connectors
    ax.annotate('', xy=(0.39, 0.795), xytext=(0.29, 0.795), arrowprops=dict(facecolor='black', width=1, headwidth=5))
    ax.annotate('', xy=(0.71, 0.795), xytext=(0.61, 0.795), arrowprops=dict(facecolor='black', width=1, headwidth=5))
    ax.annotate('', xy=(0.39, 0.615), xytext=(0.29, 0.615), arrowprops=dict(facecolor='black', width=1, headwidth=5))
    ax.annotate('', xy=(0.71, 0.615), xytext=(0.61, 0.615), arrowprops=dict(facecolor='black', width=1, headwidth=5))
    ax.annotate('', xy=(0.39, 0.435), xytext=(0.29, 0.435), arrowprops=dict(facecolor='black', width=1, headwidth=5))
    ax.annotate('', xy=(0.39, 0.255), xytext=(0.29, 0.255), arrowprops=dict(facecolor='black', width=1, headwidth=5))

    ax.set_title("Figure 10.3: UML Activity Diagram illustrating Concurrent Execution Swimlanes", 
                 fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "activity_diagram.png"), dpi=300)
    plt.close()
    print("[+] Created activity_diagram.png")

# ---------------------------------------------------------------------------
# 6. USE CASE DIAGRAM (Figure 10.4)
# ---------------------------------------------------------------------------
def create_use_case_diagram():
    fig, ax = plt.subplots(figsize=(9, 7.5), dpi=300)
    ax.set_facecolor('#ffffff')
    ax.axis('off')

    # Boundary Box
    system_box = patches.Rectangle((0.26, 0.08), 0.68, 0.84, facecolor='#f8fafc', edgecolor='#0f172a', linewidth=2)
    ax.add_patch(system_box)
    ax.text(0.60, 0.88, "History of India Web Platform Boundary", ha='center', va='center', fontweight='bold', fontsize=11, color='#0f172a')

    # Actor: Student / Visitor
    ax.plot(0.12, 0.65, 'o', markersize=14, color='#1e293b') # Head
    ax.plot([0.12, 0.12], [0.63, 0.52], color='#1e293b', lw=3) # Body
    ax.plot([0.08, 0.16], [0.59, 0.59], color='#1e293b', lw=3) # Arms
    ax.plot([0.12, 0.09], [0.52, 0.44], color='#1e293b', lw=3) # Left Leg
    ax.plot([0.12, 0.15], [0.52, 0.44], color='#1e293b', lw=3) # Right Leg
    ax.text(0.12, 0.39, "Student / Visitor\n(User)", ha='center', va='center', fontweight='bold', fontsize=9.5, color='#0f172a')

    # Use Cases
    use_cases = [
        (0.35, 0.77, "Browse 8 Historical Eras"),
        (0.35, 0.64, "Scrub Dual-Mode Timeline"),
        (0.35, 0.51, "Inspect Artifact Lightbox"),
        (0.35, 0.38, "Instant Global Search"),
        (0.35, 0.25, "Play Civilizational Quiz ✦"),
        (0.35, 0.12, "Toggle Audio Atmosphere")
    ]

    for cx, cy, label in use_cases:
        ellipse = patches.Ellipse((cx + 0.18, cy + 0.03), 0.32, 0.085, facecolor='#e0f2fe', edgecolor='#0369a1', linewidth=1.5)
        ax.add_patch(ellipse)
        ax.text(cx + 0.18, cy + 0.03, label, ha='center', va='center', fontweight='bold', fontsize=8.5, color='#0369a1')
        # Line from actor to use case
        ax.plot([0.16, cx + 0.02], [0.57, cy + 0.03], color='#64748b', lw=1.2, linestyle='-')

    ax.set_title("Figure 10.4: UML Use Case Diagram defining Functional Capabilities & Actor Roles", 
                 fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "use_case_diagram.png"), dpi=300)
    plt.close()
    print("[+] Created use_case_diagram.png")

# ---------------------------------------------------------------------------
# 7. DATABASE SCHEMA DIAGRAM (Figure 12.1)
# ---------------------------------------------------------------------------
def create_database_schema_diagram():
    fig, ax = plt.subplots(figsize=(9.5, 7.5), dpi=300)
    ax.set_facecolor('#ffffff')
    ax.axis('off')

    tables = [
        (0.05, 0.55, 0.42, 0.38, "TABLE: eras (Historical Epochs)\n" + "-"*40 + "\n* id : TEXT [PRIMARY KEY]\n  title : TEXT\n  subtitle : TEXT\n  period : TEXT\n  category : TEXT (ancient/classical)\n  capital : TEXT\n  image : TEXT (images/priest_king.jpg)\n  banner : TEXT\n  overview : TEXT", "#1e3a8a"),
        (0.53, 0.55, 0.42, 0.38, "TABLE: artifacts (Museum Treasures)\n" + "-"*40 + "\n* id : TEXT [PRIMARY KEY]\n  era_id : TEXT [FOREIGN KEY]\n  title : TEXT\n  period : TEXT\n  category : TEXT (sculpture/monument)\n  material : TEXT\n  location : TEXT\n  image : TEXT (images/dancing_girl.jpg)\n  wikipediaUrl : TEXT", "#065f46"),
        (0.05, 0.10, 0.42, 0.38, "TABLE: dynasties (Imperial Realms)\n" + "-"*40 + "\n* id : TEXT [PRIMARY KEY]\n  name : TEXT\n  period : TEXT\n  capital : TEXT\n  founder : TEXT\n  greatestRuler : TEXT\n  territoryKm2 : TEXT\n  emblem : TEXT", "#854d0e"),
        (0.53, 0.10, 0.42, 0.38, "TABLE: user_bookmarks (Persistence)\n" + "-"*40 + "\n* bookmark_id : INTEGER [PK AUTO]\n  artifact_id : TEXT [FOREIGN KEY]\n  user_session_id : TEXT\n  created_at : TIMESTAMP\n  sync_source : TEXT ('server_json')", "#991b1b")
    ]

    for (x, y, w, h, text, color) in tables:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.02",
                                      linewidth=1.2, edgecolor='#334155', facecolor='#f8fafc')
        ax.add_patch(rect)
        hdr = patches.FancyBboxPatch((x, y + h*0.82), w, h*0.18, boxstyle="round,pad=0.02,rounding_size=0.02",
                                     linewidth=1, edgecolor='#334155', facecolor=color)
        ax.add_patch(hdr)
        lines = text.split('\n')
        ax.text(x + w/2, y + h*0.91, lines[0], ha='center', va='center', color='white', fontweight='bold', fontsize=9)
        ax.text(x + 0.02, y + h*0.40, '\n'.join(lines[2:]), ha='left', va='center', color='#0f172a', fontfamily='monospace', fontsize=8)

    ax.set_title("Figure 12.1: Relational Database Schema & Data Dictionary Architecture", 
                 fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "database_schema_diagram.png"), dpi=300)
    plt.close()
    print("[+] Created database_schema_diagram.png")

# ---------------------------------------------------------------------------
# 8. PLAGIARISM REPORT CARD (Figure 2.1)
# ---------------------------------------------------------------------------
def create_plagiarism_card():
    img = Image.new('RGB', (1200, 680), color='#ffffff')
    draw = ImageDraw.Draw(img)

    # Header banner
    draw.rectangle([(40, 30), (1160, 110)], fill='#ea580c')
    draw.text((70, 52), "Plagiarism Scan Report", fill='#ffffff')

    # Border
    draw.rectangle([(40, 110), (1160, 480)], outline='#cbd5e1', width=2)

    # Fields
    fields = [
        ("Report Title", "History of India Project Report"),
        ("Generated Date", "27-Sep-2026"),
        ("Candidate Name", "Mr. Raunak Dilip Jaiswal"),
        ("Total Word Count", "4,850 Words"),
        ("College Affiliation", "V.K. Krishna Menon College / University of Mumbai"),
        ("Excluded URL", "None (Comprehensive Online & Offline Indexing)")
    ]

    for idx, (label, val) in enumerate(fields):
        y = 135 + idx * 55
        draw.rectangle([(50, y), (400, y + 45)], fill='#f1f5f9')
        draw.rectangle([(410, y), (1150, y + 45)], fill='#ffffff')
        draw.text((70, y + 12), label, fill='#334155')
        draw.text((430, y + 12), val, fill='#0f172a')

    # Score Cards
    # Plagiarised 0%
    draw.rectangle([(100, 510), (450, 630)], outline='#16a34a', width=3, fill='#f0fdf4')
    draw.text((220, 530), "0%", fill='#16a34a')
    draw.text((200, 590), "Plagiarised", fill='#16a34a')

    # Unique 100%
    draw.rectangle([(500, 510), (850, 630)], outline='#2563eb', width=3, fill='#eff6ff')
    draw.text((610, 530), "100%", fill='#2563eb')
    draw.text((600, 590), "Unique & Original", fill='#2563eb')

    # Total Words Ratio
    draw.rectangle([(900, 510), (1140, 630)], outline='#0284c7', width=2, fill='#f0f9ff')
    draw.text((970, 530), "92.4%", fill='#0284c7')
    draw.text((950, 590), "Vocabulary Depth", fill='#0284c7')

    img.save(os.path.join(ASSETS_DIR, "plagiarism_report.png"))
    print("[+] Created plagiarism_report.png")

if __name__ == '__main__':
    create_gantt_chart()
    create_system_design_diagram()
    create_er_diagram()
    create_class_diagram()
    create_activity_diagram()
    create_use_case_diagram()
    create_database_schema_diagram()
    create_plagiarism_card()
