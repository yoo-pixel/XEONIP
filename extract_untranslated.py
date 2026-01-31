"""
Script to extract all remaining untranslated words from organized_vocabulary.html
"""
import re

filepath = r"c:\Users\Mostafa\OneDrive\Attachments\MY work\organized_vocabulary.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match untranslated word cards
pattern = r'<div class="word-card no-translation">\s*<div class="word-english">([^<]+)</div>\s*<div class="word-arabic">\1</div>\s*<span class="placeholder-badge">~</span>\s*</div>'

matches = re.findall(pattern, content)
unique_words = sorted(set(word.strip() for word in matches))

print(f"Found {len(unique_words)} unique untranslated words:\n")
for word in unique_words:
    print(f'"{word.lower()}": "",')
