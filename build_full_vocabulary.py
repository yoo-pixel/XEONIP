import json
from pathlib import Path

workspace = Path(__file__).parent

# Load translated words extracted from HTML
translated_path = workspace / "extracted_words.json"
translated_data = json.loads(translated_path.read_text(encoding="utf-8"))
translated_words = translated_data.get("words", [])

# Index translated words by lowercase English
translated_index = {}
for item in translated_words:
    english = item.get("english", "").strip()
    if not english:
        continue
    translated_index[english.lower()] = {
        "english": english,
        "arabic": item.get("arabic", "").strip()
    }

# Load bulk word lists by level
bulk_files = sorted(workspace.glob("_bulk_*.txt"))
level_map = {
    "_bulk_a1.txt": "a1",
    "_bulk_a2.txt": "a2",
    "_bulk_b1.txt": "b1",
    "_bulk_b2.txt": "b2",
}

levels = {
    "a1": [],
    "a2": [],
    "b1": [],
    "b2": [],
}

for path in bulk_files:
    level = level_map.get(path.name)
    if not level:
        continue
    content = path.read_text(encoding="utf-8")
    words = []
    seen = set()
    for part in content.split(","):
        word = part.strip()
        if not word:
            continue
        key = word.lower()
        if key in seen:
            continue
        seen.add(key)
        translated = translated_index.get(key)
        if translated:
            words.append(translated)
        else:
            words.append({"english": word, "arabic": ""})
    levels[level] = sorted(words, key=lambda w: w["english"].lower())

def bucket_key(word: str) -> str:
    if not word:
        return "Other"
    first = word[0].upper()
    if first.isalpha():
        if "A" <= first <= "F":
            return "A–F"
        if "G" <= first <= "L":
            return "G–L"
        if "M" <= first <= "R":
            return "M–R"
        return "S–Z"
    return "Other"

def build_categories(words):
    buckets = {
        "A–F": [],
        "G–L": [],
        "M–R": [],
        "S–Z": [],
        "Other": []
    }
    for item in words:
        key = bucket_key(item.get("english", ""))
        buckets[key].append(item)
    return {k: v for k, v in buckets.items() if v}

# Count stats
total_words = sum(len(words) for words in levels.values())
translated_count = sum(1 for words in levels.values() for w in words if w.get("arabic"))

output = {
    "total_words": total_words,
    "translated_words": translated_count,
    "sources": [p.name for p in bulk_files],
    "levels": {
        level: {
            "total_words": len(words),
            "translated_words": sum(1 for w in words if w.get("arabic")),
            "categories": build_categories(words),
        }
        for level, words in levels.items()
    },
}

output_path = workspace / "vocabulary-portal-data.json"
output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Translated words: {translated_count}")
print(f"Total words: {total_words}")
print(f"Output: {output_path}")
