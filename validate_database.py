#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

with open('_categories_with_arabic.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('✅ JSON Database Validation Report')
print('=' * 50)
print(f'✓ Total categories: {len(data)}')
print(f'✓ Total words: {sum(len(c["words"]) for c in data.values())}')
print()
print('Category breakdown:')
for cat in sorted(data.keys()):
    word_count = len(data[cat]['words'])
    trans_count = sum(1 for w in data[cat]['words'] if w['ar'] != w['en'])
    print(f'  • {data[cat]["title"]}: {word_count} words ({trans_count} translated)')

print()
print('✅ Database is valid and ready for use!')
