import re
import json

# Read the organized_vocabulary HTML file
with open('organized_vocabulary.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Pattern to extract word cards with English and Arabic (both with and without translation)
pattern_with_translation = r'<div class="word-card has-translation">\s*<div class="word-english">([^<]+)</div>\s*<div class="word-arabic">([^<]+)</div>'
pattern_without_translation = r'<div class="word-card">\s*<div class="word-english">([^<]+)</div>\s*<div class="word-arabic">([^<]+)</div>\s*</div>'

matches_with = re.findall(pattern_with_translation, html_content, re.DOTALL)
matches_without = re.findall(pattern_without_translation, html_content, re.DOTALL)

matches = matches_with + matches_without

# Pattern to extract categories
category_pattern = r'<h2[^>]*>\s*<span[^>]*>[^<]*</span>\s*([^<]+?)\s*<span class="word-count">'

categories = re.findall(category_pattern, html_content)

print(f"Found {len(matches)} words")
print(f"Found {len(categories)} categories")
print(f"\nFirst 10 words:")
for i, (eng, ar) in enumerate(matches[:10]):
    print(f"{i+1}. {eng.strip()} - {ar.strip()}")

print(f"\nFirst 10 categories:")
for i, name in enumerate(categories[:10]):
    print(f"{i+1}. {name.strip()}")

# Save extracted words to file
output = {
    "total_words": len(matches),
    "total_categories": len(categories),
    "words": [{"english": eng.strip(), "arabic": ar.strip()} for eng, ar in matches],
    "categories": [name.strip() for name in categories]
}

with open('extracted_words.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nExtracted {len(matches)} words to extracted_words.json")
