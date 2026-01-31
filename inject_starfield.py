from pathlib import Path

workspace = Path(__file__).parent
html_files = list(workspace.glob('*.html'))

head_tag = '</head>'
body_tag = '<body>'

css_link = '    <link rel="stylesheet" href="starfield.css">\n'
js_script = '    <script src="starfield.js" defer></script>\n'

for file_path in html_files:
    content = file_path.read_text(encoding='utf-8')
    updated = content

    if 'starfield.css' not in content:
        if head_tag in updated:
            updated = updated.replace(head_tag, f'{css_link}{head_tag}', 1)

    if 'starfield.js' not in content:
        if head_tag in updated:
            updated = updated.replace(head_tag, f'{js_script}{head_tag}', 1)

    if updated != content:
        file_path.write_text(updated, encoding='utf-8')

print(f'Updated {len(html_files)} files')
