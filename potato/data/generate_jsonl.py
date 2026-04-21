"""
Generates a JSONL file from image filenames in a given directory.

Each line:
  {"id": "<filename>", "text": "<filename>", "url": "/media/<filename>"}
"""

import os
import json

# ── Config ────────────────────────────────────────────────────────────────────
IMAGE_DIR   = "media_real"
OUTPUT_FILE = "images.jsonl"
# ──────────────────────────────────────────────────────────────────────────────

def main():
    filenames = sorted(
        f for f in os.listdir(IMAGE_DIR)
        if os.path.isfile(os.path.join(IMAGE_DIR, f))
    )

    print(f"Found {len(filenames)} files in '{IMAGE_DIR}'")

    with open(OUTPUT_FILE, "w") as out:
        for fname in filenames:
            record = {
                "id":   fname,
                "text": fname,
                "url":  f"/media/{fname}",
            }
            out.write(json.dumps(record) + "\n")

    print(f"JSONL written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
