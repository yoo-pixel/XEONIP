#!/usr/bin/env python3
"""
Update all HTML files with:
1. Black & cyan color scheme
2. Back buttons to previous pages
"""

import re
from pathlib import Path

# Mapping of pages to their back button targets
back_button_map = {
    'english-grammar.html': ('english.html', 'English'),
    'english-grammar-a1a2.html': ('english-grammar.html', 'Grammar Hub'),
    'english-grammar-b1.html': ('english-grammar.html', 'Grammar Hub'),
    'english-grammar-b2.html': ('english-grammar.html', 'Grammar Hub'),
    'english-words.html': ('english.html', 'English'),
    'english-words-a1a2.html': ('english-words.html', 'Vocabulary Hub'),
    'english-words-b1.html': ('english-words.html', 'Vocabulary Hub'),
    'english-words-b2.html': ('english-words.html', 'Vocabulary Hub'),
    'programs.html': ('index.html', 'Home'),
    'programs-accessible.html': ('programs.html', 'Programs'),
    'programs-achievable.html': ('programs.html', 'Programs'),
    'category-everyday-objects.html': ('english.html', 'English'),
}

# Old color gradients to replace
old_gradients = [
    'linear-gradient(180deg, #0a0e2a 0%, #1a1f3f 25%, #1e2847 50%, #17213a 75%, #0f1629 100%)',
]

new_gradient = 'linear-gradient(180deg, #000000 0%, #001a1a 25%, #0a1f1f 50%, #001a1a 75%, #000000 100%)'

back_button_css = '''
        .back-btn {
            display: inline-block;
            padding: 12px 24px;
            margin-bottom: 20px;
            background: rgba(0, 217, 255, 0.1);
            color: #00d9ff;
            text-decoration: none;
            border: 1px solid #00d9ff;
            border-radius: 6px;
            font-size: 0.95rem;
            transition: all 0.3s ease;
        }
        
        .back-btn:hover {
            background: rgba(0, 217, 255, 0.2);
            transform: translateX(-4px);
        }
'''

def update_file(file_path, back_to_page, back_to_label):
    """Update an HTML file with new colors and back button"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update background gradient
    for old_grad in old_gradients:
        if old_grad in content:
            content = content.replace(old_grad, new_gradient)
    
    # Update CSS color variables if present
    content = content.replace('--deep-space: #0a0e1a;', '--deep-space: #000000;')
    content = content.replace('--space-blue: #0f1729;', '--space-blue: #0a1f1f;')
    content = content.replace('--navy-dark: #141b2e;', '--navy-dark: #001a1a;')
    
    # Add back button CSS if not present
    if '.back-btn' not in content and '<style>' in content:
        content = content.replace('    </style>', f'{back_button_css}    </style>')
    
    # Add back button HTML to body if not present
    if 'class="back-btn"' not in content:
        # Find container or first main element and add back button
        patterns = [
            (r'(<div class="container"[^>]*>)', f'\\1\n        <a href="{back_to_page}" class="back-btn">← Back to {back_to_label}</a>'),
            (r'(<body[^>]*>\s*<div[^>]*>)', f'\\1\n        <a href="{back_to_page}" class="back-btn">← Back to {back_to_label}</a>'),
            (r'(<body[^>]*>)', f'\\1\n    <a href="{back_to_page}" class="back-btn" style="position: relative; z-index: 10; display: inline-block; padding: 12px 24px; margin: 20px 24px 0; background: rgba(0, 217, 255, 0.1); color: #00d9ff; text-decoration: none; border: 1px solid #00d9ff; border-radius: 6px; font-size: 0.95rem;">← Back to {back_to_label}</a>'),
        ]
        
        for pattern, replacement in patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content, count=1)
                break
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# Process all files
work_dir = Path('.')
updated_count = 0

for filename, (back_page, back_label) in back_button_map.items():
    file_path = work_dir / filename
    if file_path.exists():
        try:
            if update_file(file_path, back_page, back_label):
                print(f"✓ Updated {filename} - back to {back_page}")
                updated_count += 1
        except Exception as e:
            print(f"✗ Error updating {filename}: {e}")
    else:
        print(f"- Skipped {filename} (not found)")

print(f"\nTotal files updated: {updated_count}")
