#!/usr/bin/env python3
"""
Image Grid Visualizer
Usage: python server.py --csv data.csv --images images/ [--port 5000]
"""

import argparse
import ast
import csv
import os
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

CSV_PATH = None
IMAGES_DIR = None
ROWS = []


def parse_list_field(value):
    """Parse a stringified list like '["photo", "image"]' into a Python list."""
    value = value.strip()
    if not value:
        return []
    try:
        result = ast.literal_eval(value)
        if isinstance(result, list):
            return [str(x).strip() for x in result]
    except Exception:
        pass
    # Fallback: treat as comma-separated plain string
    return [x.strip().strip('"').strip("'") for x in value.strip("[]").split(",") if x.strip()]


def load_csv():
    global ROWS
    ROWS = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ROWS.append({
                "id": row["id"].strip(),
                "categories": parse_list_field(row.get("categories", "")),
                "origin": parse_list_field(row.get("origin", "")),
            })


@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "index.html")


@app.route("/api/options")
def options():
    categories = sorted(set(c for row in ROWS for c in row["categories"]))
    origins = sorted(set(o for row in ROWS for o in row["origin"]))
    return jsonify({"categories": categories, "origins": origins})


@app.route("/api/images")
def images():
    sel_cats = request.args.getlist("categories")
    sel_origs = request.args.getlist("origins")

    results = []
    for row in ROWS:
        if sel_cats and not all(c in row["categories"] for c in sel_cats):
            continue
        if sel_origs and not all(o in row["origin"] for o in sel_origs):
            continue
        results.append({
            "id": row["id"],
            "categories": row["categories"],
            "origin": row["origin"],
        })

    return jsonify({"images": results, "total": len(results)})


@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(IMAGES_DIR, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Grid Visualizer")
    parser.add_argument("--csv", required=True, help="Path to the CSV file")
    parser.add_argument("--images", required=True, help="Path to the images folder")
    parser.add_argument("--port", type=int, default=5000, help="Port to serve on (default: 5000)")
    args = parser.parse_args()

    CSV_PATH = os.path.abspath(args.csv)
    IMAGES_DIR = os.path.abspath(args.images)

    if not os.path.exists(CSV_PATH):
        print(f"ERROR: CSV file not found: {CSV_PATH}")
        exit(1)
    if not os.path.isdir(IMAGES_DIR):
        print(f"ERROR: Images directory not found: {IMAGES_DIR}")
        exit(1)

    load_csv()
    print(f"Loaded {len(ROWS)} rows from {CSV_PATH}")
    print(f"Serving images from {IMAGES_DIR}")
    print(f"Open http://localhost:{args.port} in your browser")
    app.run(debug=False, port=args.port)
