#!/usr/bin/env python3
"""
History of India - Localhost Server & REST API Engine
Built with Python standard library. Zero external dependencies required.
Serves frontend static assets and provides RESTful endpoints for history data, search, quiz, and bookmarks.
"""

import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import socket

# Force UTF-8 stdout if supported
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Ensure working directory is the script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# Data files paths
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
BOOKMARKS_FILE = os.path.join(DATA_DIR, "user_bookmarks.json")

# Sample Quiz Bank for Indian History
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "Which ancient Indus Valley city featured a massive tidal dockyard connected to the Arabian Sea?",
        "options": ["Mohenjo-daro", "Lothal", "Harappa", "Kalibangan"],
        "answer": 1,
        "explanation": "Lothal in modern Gujarat had the world's earliest known tidal dockyard, facilitating trade with Mesopotamia and ancient Egypt."
    },
    {
        "id": 2,
        "question": "Which Mauryan Emperor renounced warfare and adopted Dhamma after the Kalinga War?",
        "options": ["Chandragupta Maurya", "Bindusara", "Ashoka the Great", "Brihadratha"],
        "answer": 2,
        "explanation": "Emperor Ashoka experienced a profound transformation following the devastation of the Kalinga War in 261 BCE, dedicating his reign to moral governance."
    },
    {
        "id": 3,
        "question": "Who composed the mathematical treatise 'Aryabhatiya' calculating the approximation of Pi and heliocentric principles?",
        "options": ["Aryabhata", "Varahamihira", "Brahmagupta", "Bhaskara II"],
        "answer": 0,
        "explanation": "Aryabhata composed the Aryabhatiya in 499 CE during the Gupta Golden Age, asserting that the Earth rotates on its axis."
    },
    {
        "id": 4,
        "question": "The Brihadisvara Temple at Thanjavur was consecrated in 1010 CE by which prominent monarch?",
        "options": ["Rajendra Chola I", "Raja Raja Chola I", "Krishnadevaraya", "Kulothunga Chola"],
        "answer": 1,
        "explanation": "Raja Raja Chola I commissioned the colossal granite Vimana tower topped with an 80-tonne single granite capstone without binding mortar."
    },
    {
        "id": 5,
        "question": "The famous 1930 Dandi Salt March led by Mahatma Gandhi covered approximately what distance?",
        "options": ["100 km", "240 miles (390 km)", "500 miles", "50 km"],
        "answer": 1,
        "explanation": "Mahatma Gandhi and 78 volunteers marched 240 miles from Sabarmati Ashram to the coastal village of Dandi to defy the colonial salt monopoly."
    }
]

def load_json_dataset(filename):
    """Load JSON or extract from JS data files if needed."""
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def get_bookmarks():
    """Load user bookmarks from JSON file."""
    if os.path.exists(BOOKMARKS_FILE):
        try:
            with open(BOOKMARKS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_bookmarks(bookmarks):
    """Save user bookmarks to JSON file."""
    with open(BOOKMARKS_FILE, "w", encoding="utf-8") as f:
        json.dump(bookmarks, f, indent=2, ensure_ascii=False)

class HistoryAPIRequestHandler(SimpleHTTPRequestHandler):
    """Custom request handler that handles both static frontend files and /api/* endpoints."""

    def end_headers(self):
        # Enable CORS and disable aggressive caching for dev localhost
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def copyfile(self, source, outputfile):
        """Override copyfile to cleanly ignore client aborts / broken pipes."""
        try:
            super().copyfile(source, outputfile)
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            pass

    def log_message(self, format, *args):
        """Clean, professional console logging."""
        sys.stdout.write(f"  [HTTP] {self.address_string()} - {format % args}\n")
        sys.stdout.flush()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # ----------------- REST API Endpoints -----------------
        if path.startswith("/api/"):
            self.handle_api_get(path, query)
            return

        # ----------------- Static Frontend Files -----------------
        # Default index
        if path == "/":
            self.path = "/index.html"

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/bookmarks":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            try:
                payload = json.loads(post_data)
                artifact_id = payload.get("id")
                bookmarks = get_bookmarks()
                
                if artifact_id:
                    if artifact_id in bookmarks:
                        bookmarks.remove(artifact_id)
                        saved = False
                    else:
                        bookmarks.append(artifact_id)
                        saved = True
                    save_bookmarks(bookmarks)
                    self.send_json_response({"success": True, "saved": saved, "bookmarks": bookmarks})
                else:
                    self.send_json_response({"error": "Missing artifact id"}, status=400)
            except Exception as e:
                self.send_json_response({"error": str(e)}, status=500)
            return

        self.send_error(404, "Endpoint not found")

    def handle_api_get(self, path, query):
        if path == "/api/status":
            self.send_json_response({
                "status": "online",
                "service": "History of India Python Core",
                "version": "1.0.0",
                "port": self.server.server_port,
                "endpoints": [
                    "/api/status",
                    "/api/quiz",
                    "/api/bookmarks",
                    "/api/search?q=..."
                ]
            })
        elif path == "/api/quiz":
            self.send_json_response({
                "quiz": "Indian Civilizational Knowledge Test",
                "count": len(QUIZ_QUESTIONS),
                "questions": QUIZ_QUESTIONS
            })
        elif path == "/api/bookmarks":
            bookmarks = get_bookmarks()
            self.send_json_response({"bookmarks": bookmarks, "count": len(bookmarks)})
        elif path == "/api/search":
            q = query.get("q", [""])[0].lower()
            results = []
            if q:
                # Basic server-side matching
                for item in QUIZ_QUESTIONS:
                    if q in item["question"].lower() or q in item["explanation"].lower():
                        results.append({
                            "type": "Trivia Quiz Record",
                            "title": item["question"],
                            "detail": item["explanation"]
                        })
            self.send_json_response({"query": q, "count": len(results), "results": results})
        else:
            self.send_json_response({"error": "Unknown API endpoint"}, status=404)

    def send_json_response(self, data, status=200):
        response_bytes = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

def find_available_port(start_port=8000, max_attempts=10):
    """Finds an open port starting from start_port."""
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return start_port

def run_server():
    port = find_available_port(8000)
    server_address = ("127.0.0.1", port)
    
    # Custom MIME Types for modern web
    SimpleHTTPRequestHandler.extensions_map.update({
        ".js": "application/javascript",
        ".css": "text/css",
        ".svg": "image/svg+xml",
        ".json": "application/json",
        ".html": "text/html; charset=utf-8"
    })

    httpd = HTTPServer(server_address, HistoryAPIRequestHandler)
    url = f"http://localhost:{port}"

    print("=" * 68)
    print("  * HISTORY OF INDIA - SONY AESTHETIC WEB PLATFORM *")
    print("=" * 68)
    print(f"  [+] Server running at : {url}")
    print(f"  [+] REST API online   : {url}/api/status")
    print(f"  [+] History Quiz API  : {url}/api/quiz")
    print(f"  [+] Local Root Dir    : {SCRIPT_DIR}")
    print("=" * 68)
    print("  Press Ctrl+C to terminate the local server.\n")

    # Automatically launch web browser
    try:
        webbrowser.open(url)
    except Exception:
        pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Gracefully shutting down Python localhost server...")
        httpd.server_close()
        sys.exit(0)

if __name__ == "__main__":
    run_server()
