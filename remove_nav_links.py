import os
import re

# Directory containing HTML files
html_dir = r"c:\Users\Mostafa\OneDrive\Attachments\MY work"

# Navigation pattern to remove Grammar and Essays links
nav_patterns = [
    # Pattern 1: Grammar and Essays links together
    r'(\s*<a href="[^"]*essays\.html">[^<]*Essays[^<]*</a>\s*\n\s*<a href="[^"]*grammar\.html">[^<]*Grammar[^<]*</a>)',
    # Pattern 2: Grammar and Essays in reverse order
    r'(\s*<a href="[^"]*grammar\.html">[^<]*Grammar[^<]*</a>\s*\n\s*<a href="[^"]*essays\.html">[^<]*Essays[^<]*</a>)',
    # Pattern 3: Essays link alone
    r'(\s*<a href="[^"]*essays\.html">[^<]*Essays[^<]*</a>\s*\n)',
    # Pattern 4: Grammar link alone  
    r'(\s*<a href="[^"]*grammar\.html">[^<]*Grammar[^<]*</a>\s*\n)',
]

# List of files to update
files_to_update = [
    "english-words.html",
    "english-words-a1a2.html", 
    "english-words-b1.html",
    "english-words-b2.html",
    "english-grammar.html",
    "english-grammar-a1a2.html",
    "english-grammar-b1.html",
    "english-grammar-b2.html",
    "vocabulary-portal.html",
    "essay-tips.html",
    "essay-references.html",
]

for filename in files_to_update:
    filepath = os.path.join(html_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"⚠️  {filename} not found, skipping...")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Apply all patterns
    for pattern in nav_patterns:
        content = re.sub(pattern, '\n', content)
    
    # Clean up multiple newlines in nav
    content = re.sub(r'(<nav>[\s\n]*<a)', r'<nav>\n            <a', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated {filename}")
    else:
        print(f"- No changes needed for {filename}")

print("\nDone! All navigation bars updated.")
