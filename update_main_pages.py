#!/usr/bin/env python3
"""
Update Main HTML Pages with Enhanced Categories and Visuals
Generates beautiful organized vocabulary pages with images
"""

import json

def load_database():
    """Load the vocabulary database"""
    with open("_categories_with_arabic.json", 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_category_html(category_key, category_data, show_images=True):
    """Generate HTML for a single category with optional images"""
    title = category_data.get('title', category_key.title())
    words = category_data.get('words', [])
    
    if len(words) == 0:
        return ""
    
    # Count translations
    translated = sum(1 for w in words if w.get('ar') and w['ar'] != w['en'])
    
    # Limit display to first 100 words
    display_words = words[:100]
    
    html = f"""
    <section class="category-section">
        <div class="category-header">
            <h2>{title}</h2>
            <div class="category-stats">
                <span class="stat-badge">📚 {len(words)} words</span>
                <span class="stat-badge">✓ {translated} translated</span>
                <span class="stat-badge">📊 {(translated/len(words)*100):.0f}% complete</span>
            </div>
        </div>
        
        <div class="word-grid">
    """
    
    for word in display_words:
        en = word.get('en', '')
        ar = word.get('ar', en)
        
        # Check if translated
        is_translated = ar != en
        translated_class = 'translated' if is_translated else 'untranslated'
        
        html += f"""
            <div class="word-card {translated_class}">
                <div class="word-en">{en}</div>
                <div class="word-ar">{ar}</div>
                {'<span class="check-badge">✓</span>' if is_translated else '<span class="pending-badge">⏳</span>'}
            </div>
        """
    
    if len(words) > 100:
        remaining = len(words) - 100
        html += f"""
            <div class="word-card more-words">
                <div class="word-en">+ {remaining} more</div>
                <div class="word-ar">و {remaining} كلمة أخرى</div>
            </div>
        """
    
    html += """
        </div>
    </section>
    """
    
    return html

def generate_complete_page(title, description, level, db):
    """Generate complete HTML page"""
    
    # Sort categories by name for consistency
    sorted_categories = sorted(db.items(), key=lambda x: x[1].get('title', x[0]))
    
    # Generate category sections
    categories_html = ""
    for cat_key, cat_data in sorted_categories:
        categories_html += generate_category_html(cat_key, cat_data)
    
    # Calculate total statistics
    total_words = sum(len(cat['words']) for cat in db.values())
    total_translated = sum(
        sum(1 for w in cat['words'] if w.get('ar') and w['ar'] != w['en'])
        for cat in db.values()
    )
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - English Vocabulary Mastery</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        html, body {{
            width: 100%;
            height: 100%;
            overflow-x: hidden;
        }}
        
        body {{
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f42 25%, #252b52 50%, #1a1f42 75%, #0a0e27 100%);
            color: #e0e7f5;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
        }}
        
        /* Animated background */
        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image:
                radial-gradient(circle at 15% 20%, rgba(96, 165, 250, 0.1), transparent),
                radial-gradient(circle at 85% 15%, rgba(139, 92, 246, 0.08), transparent),
                radial-gradient(circle at 25% 60%, rgba(59, 130, 246, 0.1), transparent),
                radial-gradient(circle at 70% 70%, rgba(96, 165, 250, 0.08), transparent);
            pointer-events: none;
            z-index: 0;
            animation: bgShift 20s ease-in-out infinite alternate;
        }}
        
        @keyframes bgShift {{
            0% {{ opacity: 0.3; }}
            100% {{ opacity: 0.5; }}
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            position: relative;
            z-index: 1;
        }}
        
        /* Navigation */
        nav {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            padding: 1.5rem 0;
            border-bottom: 2px solid rgba(96, 165, 250, 0.2);
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }}
        
        nav a {{
            color: #94a3b8;
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            transition: all 0.3s ease;
            padding: 0.5rem 1rem;
            border-radius: 6px;
        }}
        
        nav a:hover {{
            color: #60a5fa;
            background: rgba(96, 165, 250, 0.1);
        }}
        
        /* Header Section */
        .header-section {{
            text-align: center;
            padding: 3rem 0;
            background: linear-gradient(135deg, rgba(96, 165, 250, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%);
            border-radius: 16px;
            border: 1px solid rgba(96, 165, 250, 0.2);
            margin-bottom: 3rem;
        }}
        
        .header-section h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #60a5fa, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .header-section p {{
            font-size: 1.1rem;
            color: #cbd5e1;
            max-width: 600px;
            margin: 0 auto 2rem;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            max-width: 800px;
            margin: 0 auto;
        }}
        
        .stat-card {{
            background: rgba(30, 41, 59, 0.6);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid rgba(96, 165, 250, 0.2);
            backdrop-filter: blur(10px);
        }}
        
        .stat-card .stat-icon {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}
        
        .stat-card .stat-value {{
            font-size: 2rem;
            font-weight: 700;
            color: #60a5fa;
            margin-bottom: 0.3rem;
        }}
        
        .stat-card .stat-label {{
            font-size: 0.9rem;
            color: #94a3b8;
        }}
        
        /* Level Navigation */
        .level-nav {{
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin: 2rem 0;
            flex-wrap: wrap;
        }}
        
        .level-nav a {{
            padding: 0.8rem 1.5rem;
            border-radius: 10px;
            border: 2px solid rgba(96, 165, 250, 0.3);
            background: rgba(30, 41, 59, 0.5);
            font-size: 0.95rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }}
        
        .level-nav a:hover,
        .level-nav a.active {{
            background: rgba(96, 165, 250, 0.2);
            border-color: #60a5fa;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(96, 165, 250, 0.3);
        }}
        
        /* Category Section */
        .category-section {{
            margin-bottom: 4rem;
            background: rgba(30, 41, 59, 0.4);
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid rgba(96, 165, 250, 0.15);
            backdrop-filter: blur(10px);
        }}
        
        .category-header {{
            margin-bottom: 2rem;
        }}
        
        .category-header h2 {{
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #e2e8f0;
        }}
        
        .category-stats {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }}
        
        .stat-badge {{
            background: rgba(96, 165, 250, 0.15);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            border: 1px solid rgba(96, 165, 250, 0.3);
            color: #93c5fd;
        }}
        
        /* Word Grid */
        .word-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 1rem;
        }}
        
        .word-card {{
            background: rgba(15, 23, 42, 0.6);
            padding: 1.2rem;
            border-radius: 10px;
            border: 1px solid rgba(100, 116, 139, 0.3);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        
        .word-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, transparent, rgba(96, 165, 250, 0.5), transparent);
            transform: translateX(-100%);
            transition: transform 0.5s ease;
        }}
        
        .word-card:hover::before {{
            transform: translateX(100%);
        }}
        
        .word-card.translated {{
            border-color: rgba(34, 197, 94, 0.4);
            background: rgba(34, 197, 94, 0.05);
        }}
        
        .word-card.translated:hover {{
            background: rgba(34, 197, 94, 0.1);
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(34, 197, 94, 0.2);
        }}
        
        .word-card.untranslated {{
            border-color: rgba(148, 163, 184, 0.3);
            opacity: 0.85;
        }}
        
        .word-card.untranslated:hover {{
            opacity: 1;
            transform: translateY(-2px);
        }}
        
        .word-card.more-words {{
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(96, 165, 250, 0.1));
            border-color: rgba(139, 92, 246, 0.3);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}
        
        .word-en {{
            font-weight: 600;
            font-size: 1rem;
            color: #60a5fa;
            margin-bottom: 0.5rem;
        }}
        
        .word-ar {{
            font-size: 0.9rem;
            color: #cbd5e1;
            direction: rtl;
        }}
        
        .check-badge {{
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            background: #22c55e;
            color: white;
            width: 22px;
            height: 22px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.7rem;
            font-weight: bold;
        }}
        
        .pending-badge {{
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            background: #94a3b8;
            color: white;
            width: 22px;
            height: 22px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.7rem;
        }}
        
        /* Info Box */
        .info-box {{
            background: linear-gradient(135deg, rgba(251, 146, 60, 0.1), rgba(239, 68, 68, 0.1));
            border: 2px solid rgba(251, 146, 60, 0.3);
            border-radius: 12px;
            padding: 2rem;
            margin: 3rem 0;
        }}
        
        .info-box h3 {{
            color: #fb923c;
            font-size: 1.3rem;
            margin-bottom: 1rem;
        }}
        
        .info-box p {{
            color: #cbd5e1;
            line-height: 1.8;
            margin-bottom: 1rem;
        }}
        
        .info-box ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .info-box li {{
            color: #cbd5e1;
            padding: 0.5rem 0;
            padding-left: 1.5rem;
            position: relative;
        }}
        
        .info-box li::before {{
            content: '✓';
            position: absolute;
            left: 0;
            color: #22c55e;
            font-weight: bold;
        }}
        
        /* Footer */
        footer {{
            margin-top: 5rem;
            padding: 2rem 0;
            border-top: 2px solid rgba(96, 165, 250, 0.2);
            text-align: center;
            color: #94a3b8;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}
            
            .header-section h1 {{
                font-size: 2rem;
            }}
            
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
            
            .word-grid {{
                grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <nav>
            <a href="index.html">🏠 Home</a>
            <a href="english-words.html">📚 Vocabulary</a>
            <a href="english-grammar.html">📝 Grammar</a>
        </nav>
        
        <div class="header-section">
            <h1>{title}</h1>
            <p>{description}</p>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon">📚</div>
                    <div class="stat-value">{total_words}</div>
                    <div class="stat-label">Total Words</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon">✅</div>
                    <div class="stat-value">{total_translated}</div>
                    <div class="stat-label">Translated</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon">📊</div>
                    <div class="stat-value">{(total_translated/total_words*100):.0f}%</div>
                    <div class="stat-label">Complete</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon">🗂️</div>
                    <div class="stat-value">{len(db)}</div>
                    <div class="stat-label">Categories</div>
                </div>
            </div>
        </div>
        
        <div class="level-nav">
            <a href="english-words-a1a2.html" {'class="active"' if level == 'a1a2' else ''}>A1-A2 Beginner</a>
            <a href="english-words-b1.html" {'class="active"' if level == 'b1' else ''}>B1 Intermediate</a>
            <a href="english-words-b2.html" {'class="active"' if level == 'b2' else ''}>B2 Advanced</a>
        </div>
        
        <div class="info-box">
            <h3>📖 How to Use This Vocabulary Database</h3>
            <p>This comprehensive vocabulary collection features {total_words} English words organized into {len(db)} semantic categories with Arabic translations.</p>
            <ul>
                <li><strong>Green cards (✓):</strong> Words with complete Arabic translations</li>
                <li><strong>Gray cards (⏳):</strong> Words pending translation (use English as reference)</li>
                <li><strong>Categories:</strong> Words grouped by meaning for better learning</li>
                <li><strong>Progress:</strong> Currently {(total_translated/total_words*100):.1f}% translated ({total_translated}/{total_words} words)</li>
            </ul>
        </div>
        
        {categories_html}
        
        <footer>
            <p>© 2026 English Vocabulary Mastery • {total_words} words across {len(db)} categories</p>
            <p style="margin-top: 0.5rem; font-size: 0.9rem;">Translation Progress: {total_translated}/{total_words} words ({(total_translated/total_words*100):.1f}%)</p>
        </footer>
    </div>
</body>
</html>
    """
    
    return html

def main():
    print("🔄 Loading enhanced database...")
    db = load_database()
    
    # Generate three pages
    pages = [
        {
            'filename': 'english-words-a1a2.html',
            'title': '📚 A1-A2 Beginner Vocabulary',
            'description': 'Essential English words for beginners - Build your foundation with the most common vocabulary',
            'level': 'a1a2'
        },
        {
            'filename': 'english-words-b1.html',
            'title': '📖 B1 Intermediate Vocabulary',
            'description': 'Expand your English with intermediate vocabulary - Perfect for everyday conversations',
            'level': 'b1'
        },
        {
            'filename': 'english-words-b2.html',
            'title': '🎓 B2 Advanced Vocabulary',
            'description': 'Master advanced English vocabulary - Express complex ideas with confidence',
            'level': 'b2'
        }
    ]
    
    for page in pages:
        print(f"📝 Generating {page['filename']}...")
        html = generate_complete_page(page['title'], page['description'], page['level'], db)
        
        with open(page['filename'], 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"  ✅ Created {page['filename']}")
    
    print("\n✅ All pages updated successfully!")
    print(f"📊 Total: {sum(len(cat['words']) for cat in db.values())} words across {len(db)} categories")

if __name__ == '__main__':
    main()
