import json

with open('vocabulary-portal-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Count untranslated words
untranslated = []
for level_name, level in data['levels'].items():
    for cat, words_list in level['categories'].items():
        for w in words_list:
            if w['arabic'] == '':
                untranslated.append(w['english'])

print(f"Untranslated words remaining: {len(untranslated)}")
print(f"Total words: {data['total_words']}")
print(f"Translated words: {data['translated_words']}")

print("\nSample newly translated words:")
samples = [
    (w['english'], w['arabic']) 
    for level in data['levels'].values() 
    for words in level['categories'].values() 
    for w in words[:3]
]

for eng, ar in samples[:15]:
    print(f"  {eng:20} → {ar}")
