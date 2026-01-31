import json
import re
from pathlib import Path

html_path = Path(r"c:\Users\Mostafa\OneDrive\Attachments\MY work\organized_vocabulary.html")
json_path = Path(r"c:\Users\Mostafa\OneDrive\Attachments\MY work\_categories_with_arabic.json")

html = html_path.read_text(encoding="utf-8")
pattern = r'<div class="word-card no-translation">\s*<div class="word-english">([^<]+)</div>\s*<div class="word-arabic">\1</div>\s*<span class="placeholder-badge">~</span>\s*</div>'
words = sorted(set(w.strip() for w in re.findall(pattern, html)))

data = json.loads(json_path.read_text(encoding="utf-8"))
trans = {}
for cat in data.values():
    for w in cat.get("words", []):
        en = (w.get("en") or "").strip().lower()
        ar = (w.get("ar") or "").strip()
        if en and ar and ar.lower() != en:
            trans[en] = ar

covered = [w for w in words if w.lower() in trans]
missing = [w for w in words if w.lower() not in trans]

print("Untranslated words:", len(words))
print("Covered by categories json:", len(covered))
print("Missing after json:", len(missing))
print("Missing sample:", missing[:50])
