#!/usr/bin/env python3
"""
Generate beautiful vocabulary pages with moving stars background
Level-specific color schemes
"""

import json

def load_database():
    with open("_categories_with_arabic.json", 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_html(db, level):
    """Generate HTML with moving stars and level-specific styling"""
    
    # Level-specific configurations
    level_config = {
        'a1a2': {
            'title': '📚 A1-A2 Beginner Vocabulary',
            'desc': 'Essential English words for beginners',
            'primary_color': '#60a5fa',
            'secondary_color': '#3b82f6',
            'gradient_start': '#1e3a8a',
            'gradient_end': '#1e40af',
            'star_color': 'rgba(96, 165, 250, 0.8)'
        },
        'b1': {
            'title': '📖 B1 Intermediate Vocabulary',
            'desc': 'Everyday conversation vocabulary',
            'primary_color': '#34d399',
            'secondary_color': '#10b981',
            'gradient_start': '#064e3b',
            'gradient_end': '#065f46',
            'star_color': 'rgba(52, 211, 153, 0.8)'
        },
        'b2': {
            'title': '🎓 B2 Advanced Vocabulary',
            'desc': 'Express complex ideas with confidence',
            'primary_color': '#f59e0b',
            'secondary_color': '#d97706',
            'gradient_start': '#78350f',
            'gradient_end': '#92400e',
            'star_color': 'rgba(245, 158, 11, 0.8)'
        }
    }
    
    config = level_config[level]
    
    # Count stats
    total_words = sum(len(cat['words']) for cat in db.values())
    total_trans = sum(sum(1 for w in cat['words'] if w.get('ar') and w['ar'] != w['en']) for cat in db.values())
    percentage = (total_trans / total_words * 100) if total_words > 0 else 0
    
    # Generate category sections
    categories_html = []
    sorted_cats = sorted(db.items(), key=lambda x: x[1].get('title', ''))
    
    for cat_key, cat_data in sorted_cats:
        title = cat_data.get('title', cat_key)
        words = cat_data.get('words', [])
        
        if not words:
            continue
        
        cat_trans = sum(1 for w in words if w.get('ar') and w['ar'] != w['en'])
        cat_percentage = (cat_trans / len(words) * 100) if words else 0
        
        words_html = []
        for word in words[:100]:  # Limit to first 100
            en = word.get('en', '')
            ar = word.get('ar', en)
            is_trans = ar != en
            
            badge = '✓' if is_trans else '⏳'
            card_class = 'translated' if is_trans else 'pending'
            
            words_html.append(f'''
                <div class="word-card {card_class}">
                    <div class="word-en">{en}</div>
                    <div class="word-ar">{ar}</div>
                    <span class="badge">{badge}</span>
                </div>
            ''')
        
        if len(words) > 100:
            words_html.append(f'''
                <div class="word-card more">
                    <div class="more-text">+{len(words) - 100} more words</div>
                </div>
            ''')
        
        categories_html.append(f'''
            <section class="category">
                <div class="category-header">
                    <h2>{title}</h2>
                    <div class="category-stats">
                        <span class="stat">{len(words)} words</span>
                        <span class="stat translated-stat">{cat_trans} translated</span>
                        <span class="stat percent-stat">{cat_percentage:.0f}%</span>
                    </div>
                </div>
                <div class="words-grid">
                    {''.join(words_html)}
                </div>
            </section>
        ''')
    
    # Generate stars
    stars_html = []
    import random
    random.seed(42)
    for i in range(200):
        size = random.uniform(1, 3)
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        duration = random.uniform(100, 300)
        delay = random.uniform(0, 20)
        stars_html.append(f'''
            <div class="star" style="
                left: {x}%;
                top: {y}%;
                width: {size}px;
                height: {size}px;
                animation-duration: {duration}s;
                animation-delay: {delay}s;
            "></div>
        ''')
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['title']}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, {config['gradient_start']} 0%, {config['gradient_end']} 100%);
            color: #e0e7f5;
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }}
        
        /* Moving stars background */
        .stars-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }}
        
        .star {{
            position: absolute;
            background: {config['star_color']};
            border-radius: 50%;
            animation: twinkle linear infinite;
        }}
        
        @keyframes twinkle {{
            0%, 100% {{
                opacity: 0.2;
                transform: scale(1) translateY(0);
            }}
            50% {{
                opacity: 1;
                transform: scale(1.5) translateY(-10px);
            }}
        }}
        
        /* Content wrapper */
        .content {{
            position: relative;
            z-index: 1;
        }}
        
        /* Header */
        .header {{
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(20px);
            padding: 3rem 2rem;
            text-align: center;
            border-bottom: 2px solid {config['primary_color']};
            box-shadow: 0 10px 50px rgba(0, 0, 0, 0.3);
        }}
        
        .header h1 {{
            font-size: 3rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, {config['primary_color']}, {config['secondary_color']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
            letter-spacing: -1px;
        }}
        
        .header p {{
            font-size: 1.2rem;
            color: #cbd5e1;
            margin-bottom: 2rem;
        }}
        
        /* Level navigation */
        .level-nav {{
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }}
        
        .level-btn {{
            padding: 0.8rem 2rem;
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 50px;
            background: rgba(15, 23, 42, 0.4);
            color: #cbd5e1;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }}
        
        .level-btn:hover {{
            background: rgba(255, 255, 255, 0.1);
            border-color: {config['primary_color']};
            color: {config['primary_color']};
            transform: translateY(-2px);
            box-shadow: 0 5px 20px {config['primary_color']}40;
        }}
        
        .level-btn.active {{
            background: {config['primary_color']};
            border-color: {config['primary_color']};
            color: white;
            box-shadow: 0 5px 30px {config['primary_color']}60;
        }}
        
        /* Main content */
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }}
        
        /* Category section */
        .category {{
            background: rgba(15, 23, 42, 0.4);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .category:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3);
        }}
        
        .category-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
            gap: 1rem;
        }}
        
        .category-header h2 {{
            font-size: 1.8rem;
            color: {config['primary_color']};
            font-weight: 700;
        }}
        
        .category-stats {{
            display: flex;
            gap: 0.8rem;
            flex-wrap: wrap;
        }}
        
        .stat {{
            padding: 0.4rem 1rem;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.05);
            font-size: 0.9rem;
            font-weight: 600;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        .translated-stat {{
            background: rgba(34, 197, 94, 0.2);
            border-color: rgba(34, 197, 94, 0.3);
            color: #4ade80;
        }}
        
        .percent-stat {{
            background: rgba({config['primary_color'].replace('#', '')}, 0.2);
            border-color: {config['primary_color']}40;
            color: {config['primary_color']};
        }}
        
        /* Words grid */
        .words-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
        }}
        
        .word-card {{
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 1.5rem;
            border: 2px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        
        .word-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, transparent, {config['primary_color']}, transparent);
            transition: left 0.5s ease;
        }}
        
        .word-card:hover::before {{
            left: 100%;
        }}
        
        .word-card.translated {{
            border-color: rgba(34, 197, 94, 0.4);
            background: rgba(34, 197, 94, 0.05);
        }}
        
        .word-card.translated:hover {{
            background: rgba(34, 197, 94, 0.1);
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 10px 30px rgba(34, 197, 94, 0.3);
        }}
        
        .word-card.pending {{
            opacity: 0.85;
        }}
        
        .word-card.pending:hover {{
            opacity: 1;
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(255, 255, 255, 0.1);
        }}
        
        .word-card.more {{
            background: rgba({config['primary_color'].replace('#', '')}, 0.1);
            border-color: {config['primary_color']}40;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: default;
        }}
        
        .more-text {{
            color: {config['primary_color']};
            font-weight: 600;
            font-size: 1.1rem;
        }}
        
        .word-en {{
            font-size: 1.2rem;
            font-weight: 600;
            color: #e0e7f5;
            margin-bottom: 0.8rem;
        }}
        
        .word-ar {{
            font-size: 1.1rem;
            color: #94a3b8;
            direction: rtl;
            font-weight: 500;
        }}
        
        .badge {{
            position: absolute;
            top: 10px;
            right: 10px;
            width: 26px;
            height: 26px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9rem;
            font-weight: bold;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        }}
        
        .translated .badge {{
            background: #22c55e;
            color: white;
        }}
        
        .pending .badge {{
            background: #94a3b8;
            color: white;
        }}
        
        /* Footer */
        .footer {{
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(20px);
            padding: 2rem;
            text-align: center;
            border-top: 2px solid {config['primary_color']};
            color: #cbd5e1;
            margin-top: 3rem;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2rem;
            }}
            
            .header p {{
                font-size: 1rem;
            }}
            
            .container {{
                padding: 1.5rem 1rem;
            }}
            
            .category-header {{
                flex-direction: column;
                align-items: flex-start;
            }}
            
            .words-grid {{
                grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            }}
        }}
    </style>
</head>
<body>
    <div class="stars-container">
        {''.join(stars_html)}
    </div>
    
    <div class="content">
        <div class="header">
            <h1>{config['title']}</h1>
            <p>{config['desc']}</p>
            
            <div class="level-nav">
                <a href="english-words-a1a2.html" class="level-btn {'active' if level == 'a1a2' else ''}">A1-A2 Beginner</a>
                <a href="english-words-b1.html" class="level-btn {'active' if level == 'b1' else ''}">B1 Intermediate</a>
                <a href="english-words-b2.html" class="level-btn {'active' if level == 'b2' else ''}">B2 Advanced</a>
            </div>
        </div>
        
        <div class="container">
            {''.join(categories_html)}
        </div>
        
        <div class="footer">
            <p><strong>{total_words}</strong> words • <strong>{total_trans}</strong> translated • <strong>{percentage:.1f}%</strong> complete</p>
            <p style="margin-top: 0.5rem; font-size: 0.9rem;">Organized into <strong>{len(db)}</strong> categories</p>
        </div>
    </div>
</body>
</html>'''
    
    return html

def main():
    print("🎨 Generating beautiful vocabulary pages...")
    
    db = load_database()
    
    levels = ['a1a2', 'b1', 'b2']
    
    for level in levels:
        html = generate_html(db, level)
        filename = f'english-words-{level}.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ Created {filename}")
    
    print("\n🎉 All pages generated successfully!")
    print(f"📊 Total: {sum(len(cat['words']) for cat in db.values())} words across {len(db)} categories")

if __name__ == '__main__':
    main()
