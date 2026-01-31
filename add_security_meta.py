import os
import re

ROOT = r"c:\Users\Mostafa\OneDrive\Attachments\MY work"

META_BLOCK = (
    "    <meta name=\"referrer\" content=\"no-referrer\">\n"
)

html_files = []
for root, _, files in os.walk(ROOT):
    for f in files:
        if f.lower().endswith('.html'):
            html_files.append(os.path.join(root, f))

updated = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()

    if 'name="referrer"' in content:
        continue

    # Insert after CSP if present, else after charset
    if 'Content-Security-Policy' in content:
        new_content, count = re.subn(
            r'(<meta\s+http-equiv=\"Content-Security-Policy\"[^>]*>\s*\n)',
            r"\1" + META_BLOCK,
            content,
            count=1,
            flags=re.IGNORECASE,
        )
    else:
        new_content, count = re.subn(
            r'(<meta\s+charset=[^>]*>\s*\n)',
            r"\1" + META_BLOCK,
            content,
            count=1,
            flags=re.IGNORECASE,
        )

    if count == 0:
        new_content, count = re.subn(
            r'(<head>\s*\n)',
            r"\1" + META_BLOCK,
            content,
            count=1,
            flags=re.IGNORECASE,
        )

    if count > 0:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        updated += 1

print(f"Referrer policy added to {updated} HTML files.")
