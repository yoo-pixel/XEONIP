import os
import re

ROOT = r"c:\Users\Mostafa\OneDrive\Attachments\MY work"

CSP = (
    "default-src 'self'; "
    "img-src 'self' https: data:; "
    "style-src 'self' 'unsafe-inline' https:; "
    "script-src 'self' 'unsafe-inline' https:; "
    "font-src 'self' https: data:; "
    "connect-src 'self' https:; "
    "frame-ancestors 'self'; "
    "base-uri 'self'; "
    "object-src 'none'"
)

META_TAG = f"    <meta http-equiv=\"Content-Security-Policy\" content=\"{CSP}\">\n"

html_files = []
for root, _, files in os.walk(ROOT):
    for f in files:
        if f.lower().endswith('.html'):
            html_files.append(os.path.join(root, f))

updated = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()

    # Skip if CSP already present
    if 'Content-Security-Policy' in content:
        continue

    # Insert after <meta charset=...>
    new_content, count = re.subn(
        r'(<meta\s+charset=[^>]*>\s*\n)',
        r"\1" + META_TAG,
        content,
        count=1,
        flags=re.IGNORECASE,
    )

    # If no charset meta, insert after <head>
    if count == 0:
        new_content, count = re.subn(
            r'(<head>\s*\n)',
            r"\1" + META_TAG,
            content,
            count=1,
            flags=re.IGNORECASE,
        )

    if count > 0:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        updated += 1

print(f"CSP added to {updated} HTML files.")
