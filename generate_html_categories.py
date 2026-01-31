#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

os.chdir(r'c:\Users\Mostafa\OneDrive\Attachments\MY work')

# Read categories JSON
with open('_categories_with_arabic.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

# HTML template for categories section
html_categories_template = '''
        <!-- Auto-generated categories from database -->
        <section id="categorized-vocabulary">
            <h2 style="text-align: center; font-size: 1.8rem; margin-bottom: 2rem; color: #dbe7f9;">
                📚 Vocabulary by Category
            </h2>
            {categories_html}
        </section>
'''

category_template = '''
            <section style="background: rgba(17, 22, 44, 0.7); border: 1px solid rgba(124, 157, 214, 0.15); border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; backdrop-filter: blur(10px);">
                <h3 style="color: #dbe7f9; font-size: 1.3rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    {title}
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.8rem;">
                    {words_html}
                </div>
            </section>
'''

word_template = '                    <span style="color: #c3cee0; padding: 0.5rem; font-size: 0.9rem;">{en} ({ar})</span>'

# Generate HTML for categories
categories_html_list = []
for cat_name, cat_data in sorted(categories.items()):
    words_html_list = []
    for word in cat_data['words'][:100]:  # Limit to 100 words per category for display
        words_html_list.append(word_template.format(en=word['en'], ar=word['ar']))
    
    words_html = '\n'.join(words_html_list)
    category_html = category_template.format(
        title=cat_data['title'],
        words_html=words_html
    )
    categories_html_list.append(category_html)

categories_html = '\n'.join(categories_html_list)
html_categories = html_categories_template.format(categories_html=categories_html)

print(f"✅ Generated HTML for {len(categories)} categories")
print(f"📊 Total words displayed: {sum(min(100, len(cat['words'])) for cat in categories.values())}")
print("\n📋 Category display order:")
for i, cat_name in enumerate(sorted(categories.keys()), 1):
    print(f"  {i}. {categories[cat_name]['title']}")

# Save HTML to file for reference
with open('_categories_html_section.txt', 'w', encoding='utf-8') as f:
    f.write(html_categories)

print("\n✅ HTML section saved to '_categories_html_section.txt'")
print("   You can now insert this into your HTML files before the </body> tag")
