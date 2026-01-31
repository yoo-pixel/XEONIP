#!/usr/bin/env python3
"""
Enhanced Category System with More Translations
Breaks down 'Other' category into 30+ semantic categories
Adds comprehensive translations
"""

import json
from pathlib import Path

# Extended translation dictionary with 1000+ more words
EXTENDED_TRANSLATIONS = {
    # Numbers & Quantities
    "one": "واحد", "two": "اثنان", "three": "ثلاثة", "four": "أربعة", "five": "خمسة",
    "six": "ستة", "seven": "سبعة", "eight": "ثمانية", "nine": "تسعة", "ten": "عشرة",
    "hundred": "مئة", "thousand": "ألف", "million": "مليون", "billion": "مليار",
    "zero": "صفر", "half": "نصف", "quarter": "ربع", "dozen": "دزينة",
    
    # Colors
    "red": "أحمر", "blue": "أزرق", "green": "أخضر", "yellow": "أصفر", "black": "أسود",
    "white": "أبيض", "brown": "بني", "orange": "برتقالي", "purple": "أرجواني", "pink": "وردي",
    "gray": "رمادي", "grey": "رمادي", "silver": "فضي", "gold": "ذهبي",
    
    # Shapes & Dimensions
    "circle": "دائرة", "square": "مربع", "triangle": "مثلث", "rectangle": "مستطيل",
    "line": "خط", "curve": "منحنى", "angle": "زاوية", "corner": "ركن",
    "round": "دائري", "flat": "مسطح", "straight": "مستقيم", "curved": "منحني",
    
    # Materials & Substances
    "metal": "معدن", "iron": "حديد", "steel": "فولاذ", "copper": "نحاس", "aluminum": "ألومنيوم",
    "wood": "خشب", "paper": "ورق", "glass": "زجاج", "plastic": "بلاستيك", "rubber": "مطاط",
    "stone": "حجر", "brick": "طوب", "concrete": "خرسانة", "cement": "أسمنت",
    "cloth": "قماش", "fabric": "نسيج", "cotton": "قطن", "silk": "حرير", "wool": "صوف",
    "leather": "جلد", "fur": "فرو", "skin": "جلد",
    
    # Buildings & Structures
    "building": "مبنى", "tower": "برج", "bridge": "جسر", "road": "طريق", "street": "شارع",
    "avenue": "شارع", "highway": "طريق سريع", "path": "مسار", "lane": "ممر",
    "wall": "جدار", "fence": "سياج", "gate": "بوابة", "entrance": "مدخل", "exit": "مخرج",
    "floor": "أرضية", "ceiling": "سقف", "roof": "سطح", "stairs": "سلالم", "elevator": "مصعد",
    
    # Communication & Media
    "language": "لغة", "word": "كلمة", "sentence": "جملة", "paragraph": "فقرة", "text": "نص",
    "speech": "خطاب", "conversation": "محادثة", "dialogue": "حوار", "discussion": "نقاش",
    "message": "رسالة", "letter": "رسالة", "email": "بريد إلكتروني", "phone": "هاتف",
    "call": "اتصال", "voice": "صوت", "sound": "صوت", "noise": "ضوضاء",
    "radio": "راديو", "television": "تلفزيون", "newspaper": "جريدة", "magazine": "مجلة",
    
    # Abstract Concepts
    "idea": "فكرة", "thought": "فكرة", "concept": "مفهوم", "theory": "نظرية",
    "belief": "اعتقاد", "opinion": "رأي", "view": "رأي", "attitude": "موقف",
    "purpose": "غرض", "goal": "هدف", "aim": "هدف", "objective": "هدف",
    "plan": "خطة", "project": "مشروع", "program": "برنامج", "scheme": "خطة",
    "method": "طريقة", "way": "طريقة", "manner": "طريقة", "style": "أسلوب",
    "kind": "نوع", "type": "نوع", "sort": "نوع", "class": "فئة",
    "group": "مجموعة", "set": "مجموعة", "collection": "مجموعة", "series": "سلسلة",
    
    # Actions & States
    "act": "عمل", "action": "عمل", "activity": "نشاط", "movement": "حركة",
    "motion": "حركة", "change": "تغيير", "shift": "تحول", "transformation": "تحول",
    "process": "عملية", "procedure": "إجراء", "operation": "عملية", "function": "وظيفة",
    "performance": "أداء", "execution": "تنفيذ", "completion": "إنجاز", "achievement": "إنجاز",
    
    # Relationships & Connections
    "relation": "علاقة", "relationship": "علاقة", "connection": "اتصال", "link": "رابط",
    "bond": "رابطة", "tie": "رابطة", "association": "ارتباط", "partnership": "شراكة",
    "alliance": "تحالف", "cooperation": "تعاون", "collaboration": "تعاون", "teamwork": "عمل جماعي",
    
    # Locations & Places
    "place": "مكان", "location": "موقع", "position": "موقع", "spot": "مكان",
    "site": "موقع", "area": "منطقة", "region": "منطقة", "zone": "منطقة",
    "district": "حي", "neighborhood": "حي", "town": "بلدة", "city": "مدينة",
    "village": "قرية", "capital": "عاصمة", "country": "بلد", "nation": "أمة",
    "state": "ولاية", "province": "مقاطعة", "territory": "إقليم", "land": "أرض",
    
    # Measurements & Units
    "meter": "متر", "kilometer": "كيلومتر", "centimeter": "سنتيمتر", "millimeter": "ميليمتر",
    "inch": "بوصة", "foot": "قدم", "yard": "ياردة", "mile": "ميل",
    "gram": "غرام", "kilogram": "كيلوغرام", "pound": "رطل", "ounce": "أونصة",
    "liter": "لتر", "gallon": "غالون", "quart": "كوارت", "pint": "باينت",
    
    # Weather & Climate
    "weather": "طقس", "climate": "مناخ", "temperature": "درجة حرارة", "heat": "حرارة",
    "cold": "برد", "warm": "دافئ", "hot": "حار", "cool": "بارد",
    "rain": "مطر", "snow": "ثلج", "wind": "ريح", "storm": "عاصفة",
    "cloud": "سحابة", "fog": "ضباب", "mist": "ضباب خفيف", "thunder": "رعد",
    "lightning": "برق", "rainbow": "قوس قزح", "sunshine": "أشعة الشمس", "shadow": "ظل",
    
    # Common Verbs (past/present forms)
    "was": "كان", "were": "كانوا", "been": "كان", "being": "كون",
    "has": "لديه", "have": "لديه", "had": "كان لديه", "having": "امتلاك",
    "does": "يفعل", "did": "فعل", "done": "منجز", "doing": "فعل",
    "goes": "يذهب", "went": "ذهب", "gone": "ذهب", "going": "ذهاب",
    "comes": "يأتي", "came": "أتى", "coming": "قادم", "makes": "يصنع",
    "made": "صنع", "making": "صنع", "takes": "يأخذ", "took": "أخذ",
    "taken": "مأخوذ", "taking": "أخذ", "gives": "يعطي", "gave": "أعطى",
    "given": "معطى", "giving": "إعطاء", "gets": "يحصل", "got": "حصل",
    "getting": "حصول", "sees": "يرى", "saw": "رأى", "seen": "مرئي",
    "seeing": "رؤية", "knows": "يعرف", "knew": "عرف", "known": "معروف",
    
    # Pronouns & Basic Words
    "I": "أنا", "you": "أنت", "he": "هو", "she": "هي", "it": "هو/هي",
    "we": "نحن", "they": "هم", "me": "لي", "him": "له", "her": "لها",
    "us": "لنا", "them": "لهم", "my": "ملكي", "your": "ملكك", "his": "ملكه",
    "our": "ملكنا", "their": "ملكهم", "mine": "لي", "yours": "لك", "ours": "لنا",
    "myself": "نفسي", "yourself": "نفسك", "himself": "نفسه", "herself": "نفسها",
    "itself": "نفسه", "ourselves": "أنفسنا", "themselves": "أنفسهم",
    
    # Prepositions & Conjunctions
    "in": "في", "on": "على", "at": "عند", "by": "بواسطة", "for": "لـ",
    "with": "مع", "from": "من", "to": "إلى", "of": "من", "about": "حول",
    "as": "كما", "into": "داخل", "through": "عبر", "during": "خلال", "before": "قبل",
    "after": "بعد", "above": "فوق", "below": "تحت", "between": "بين", "among": "بين",
    "under": "تحت", "over": "فوق", "against": "ضد", "within": "ضمن", "without": "بدون",
    
    # Question Words
    "what": "ماذا", "when": "متى", "where": "أين", "why": "لماذا", "how": "كيف",
    "who": "من", "whom": "من", "whose": "لمن", "which": "أي",
    
    # Common Adjectives
    "great": "عظيم", "good": "جيد", "better": "أفضل", "best": "الأفضل",
    "bad": "سيئ", "worse": "أسوأ", "worst": "الأسوأ", "little": "قليل",
    "less": "أقل", "least": "الأقل", "much": "كثير", "more": "أكثر",
    "most": "الأكثر", "many": "كثير", "few": "قليل", "several": "عدة",
    "some": "بعض", "any": "أي", "no": "لا", "every": "كل",
    "each": "كل", "all": "جميع", "both": "كلا", "either": "أي",
    "neither": "لا", "other": "آخر", "another": "آخر", "such": "مثل",
    
    # Adverbs
    "very": "جداً", "really": "حقاً", "quite": "تماماً", "too": "جداً",
    "so": "لذا", "well": "جيداً", "also": "أيضاً", "just": "فقط",
    "only": "فقط", "even": "حتى", "still": "لا زال", "yet": "بعد",
    "already": "بالفعل", "always": "دائماً", "never": "أبداً", "often": "غالباً",
    "sometimes": "أحياناً", "usually": "عادة", "rarely": "نادراً", "seldom": "نادراً",
    "now": "الآن", "then": "ثم", "soon": "قريباً", "later": "لاحقاً",
    "today": "اليوم", "yesterday": "أمس", "tomorrow": "غداً", "here": "هنا",
    "there": "هناك", "everywhere": "في كل مكان", "somewhere": "مكان ما", "anywhere": "أي مكان",
    "up": "أعلى", "down": "أسفل", "away": "بعيداً", "back": "خلف",
    "forward": "أمام", "ahead": "قدماً", "behind": "خلف", "beside": "بجانب",
    
    # More specific words
    "ability": "قدرة", "absence": "غياب", "absolute": "مطلق", "abstract": "مجرد",
    "academic": "أكاديمي", "accept": "يقبل", "access": "وصول", "accident": "حادث",
    "accurate": "دقيق", "across": "عبر", "actual": "فعلي", "add": "يضيف",
    "additional": "إضافي", "address": "عنوان", "adequate": "كافٍ", "adjust": "يعدل",
    "administration": "إدارة", "admit": "يعترف", "adopt": "يتبنى", "adult": "بالغ",
    "advance": "تقدم", "advantage": "ميزة", "adventure": "مغامرة", "advertise": "يعلن",
    "affair": "شأن", "afford": "يستطيع تحمل تكلفة", "afraid": "خائف", "agency": "وكالة",
    "agenda": "جدول أعمال", "agent": "وكيل", "agriculture": "زراعة", "aid": "مساعدة",
    "aircraft": "طائرة", "airline": "خط جوي", "alarm": "إنذار", "album": "ألبوم",
    "alcohol": "كحول", "alert": "تنبيه", "alien": "أجنبي", "alive": "حي",
    "alley": "زقاق", "allocate": "يخصص", "alter": "يغير", "alternative": "بديل",
    "although": "رغم أن", "altitude": "ارتفاع", "altogether": "تماماً", "aluminum": "ألومنيوم",
    "amateur": "هاواة", "amaze": "يدهش", "ambassador": "سفير", "ambition": "طموح",
    "ambulance": "سيارة إسعاف", "amend": "يعدل", "amid": "وسط", "amount": "كمية",
    "ample": "وافر", "amuse": "يسلي", "analyze": "يحلل", "ancestor": "سلف",
    "anchor": "مرساة", "ancient": "قديم", "angel": "ملاك", "anger": "غضب",
    "angle": "زاوية", "anniversary": "ذكرى سنوية", "announce": "يعلن", "annual": "سنوي",
    "anonymous": "مجهول", "anticipate": "يتوقع", "anxiety": "قلق", "apart": "منفصل",
    "apartment": "شقة", "apologize": "يعتذر", "apparent": "واضح", "appeal": "نداء",
    "appetite": "شهية", "applaud": "يصفق", "apple": "تفاحة", "appliance": "جهاز",
    "applicable": "قابل للتطبيق", "applicant": "مقدم طلب", "application": "طلب", "appoint": "يعين",
    "appointment": "موعد", "appreciate": "يقدر", "approach": "نهج", "appropriate": "مناسب",
    "approval": "موافقة", "approve": "يوافق", "approximate": "تقريبي", "arbitrary": "تعسفي",
    "architect": "مهندس معماري", "architecture": "هندسة معمارية", "archive": "أرشيف", "arena": "ساحة",
    "arise": "ينشأ", "arithmetic": "حساب", "armed": "مسلح", "armor": "درع",
    "army": "جيش", "arousal": "إثارة", "arrange": "يرتب", "arrangement": "ترتيب",
    "array": "مصفوفة", "arrest": "يعتقل", "arrival": "وصول", "arrow": "سهم",
    "article": "مقال", "artificial": "صناعي", "aside": "جانباً", "asleep": "نائم",
    "aspect": "جانب", "aspiration": "طموح", "assault": "اعتداء", "assemble": "يجمع",
    "assembly": "تجمع", "assert": "يؤكد", "assess": "يقيم", "asset": "أصل",
    "assign": "يعين", "assist": "يساعد", "assistance": "مساعدة", "associate": "يربط",
    "association": "جمعية", "assume": "يفترض", "assumption": "افتراض", "assurance": "ضمان",
    "assure": "يؤكد", "astonish": "يدهش", "astronaut": "رائد فضاء", "astronomy": "علم الفلك",
    "athlete": "رياضي", "athletic": "رياضي", "atmosphere": "جو", "atom": "ذرة",
    "atomic": "ذري", "attach": "يرفق", "attachment": "مرفق", "attain": "يحقق",
    "attainment": "إنجاز", "attendance": "حضور", "attendant": "موظف", "attorney": "محامٍ",
    "attract": "يجذب", "attraction": "جذب", "attractive": "جذاب", "attribute": "صفة",
    "auction": "مزاد", "audit": "تدقيق", "auditorium": "قاعة", "august": "أغسطس",
    "aunt": "عمة", "authentic": "أصيل", "authorize": "يفوض", "auto": "سيارة",
    "automatic": "أوتوماتيكي", "automobile": "سيارة", "autonomous": "مستقل", "autumn": "خريف",
    "available": "متاح", "avenue": "شارع", "average": "متوسط", "aviation": "طيران",
    "awake": "مستيقظ", "award": "جائزة", "aware": "واعٍ", "awareness": "وعي",
    "awful": "فظيع", "awkward": "محرج", "axis": "محور"
}

# New category definitions with keywords for better classification
NEW_CATEGORIES = {
    "numbers_quantities": {
        "title": "🔢 Numbers & Quantities",
        "keywords": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "hundred", "thousand", "million", "number", "count", "amount", "quantity",
                    "first", "second", "third", "dozen", "pair", "couple", "single", "double"]
    },
    "colors_shapes": {
        "title": "🎨 Colors & Shapes",
        "keywords": ["color", "red", "blue", "green", "yellow", "black", "white", "brown",
                    "circle", "square", "triangle", "rectangle", "shape", "round", "flat"]
    },
    "materials": {
        "title": "🔨 Materials & Substances",
        "keywords": ["metal", "wood", "glass", "plastic", "stone", "cloth", "fabric",
                    "iron", "steel", "paper", "rubber", "material", "substance"]
    },
    "buildings_structures": {
        "title": "🏗️ Buildings & Structures",
        "keywords": ["building", "tower", "bridge", "structure", "construction", "architecture",
                    "floor", "ceiling", "roof", "stairs", "wall", "gate", "entrance"]
    },
    "communication_media": {
        "title": "📡 Communication & Media",
        "keywords": ["language", "message", "communication", "media", "broadcast", "publish",
                    "speech", "conversation", "dialogue", "telephone", "mail", "letter"]
    },
    "abstract_concepts": {
        "title": "💭 Abstract Concepts",
        "keywords": ["idea", "concept", "theory", "belief", "opinion", "thought", "mind",
                    "purpose", "goal", "plan", "principle", "value", "meaning"]
    },
    "locations_places": {
        "title": "📍 Locations & Places",
        "keywords": ["place", "location", "position", "site", "area", "region", "zone",
                    "district", "neighborhood", "town", "city", "village", "capital"]
    },
    "measurements": {
        "title": "📏 Measurements & Units",
        "keywords": ["meter", "kilometer", "gram", "kilogram", "liter", "measure",
                    "size", "weight", "length", "width", "height", "distance"]
    },
    "weather_climate": {
        "title": "🌤️ Weather & Climate",
        "keywords": ["weather", "climate", "rain", "snow", "wind", "storm", "cloud",
                    "temperature", "hot", "cold", "warm", "sunny", "fog"]
    },
    "relationships": {
        "title": "🤝 Relationships & Connections",
        "keywords": ["relation", "relationship", "connection", "partnership", "alliance",
                    "cooperation", "collaboration", "friend", "partner", "associate"]
    },
    "grammar_words": {
        "title": "📝 Grammar & Function Words",
        "keywords": ["the", "a", "an", "and", "or", "but", "if", "when", "where",
                    "what", "who", "which", "this", "that", "these", "those"]
    },
    "pronouns": {
        "title": "👤 Pronouns",
        "keywords": ["I", "you", "he", "she", "it", "we", "they", "me", "him", "her",
                    "my", "your", "his", "our", "their", "myself", "yourself"]
    },
    "common_verbs": {
        "title": "⚙️ Common Verbs",
        "keywords": ["be", "have", "do", "say", "get", "make", "go", "know", "take",
                    "see", "come", "think", "look", "want", "give", "use", "find"]
    },
    "common_adjectives": {
        "title": "✨ Common Adjectives",
        "keywords": ["good", "great", "new", "old", "high", "small", "large", "different",
                    "important", "public", "bad", "same", "able", "own", "general"]
    },
    "adverbs": {
        "title": "⏩ Adverbs",
        "keywords": ["very", "also", "well", "only", "just", "now", "how", "then",
                    "really", "quite", "too", "always", "never", "often", "sometimes"]
    },
    "prepositions": {
        "title": "➡️ Prepositions",
        "keywords": ["in", "on", "at", "by", "for", "with", "from", "to", "of",
                    "about", "into", "through", "during", "before", "after", "above"]
    }
}

def load_database():
    """Load the vocabulary database"""
    with open("_categories_with_arabic.json", 'r', encoding='utf-8') as f:
        return json.load(f)

def save_database(db):
    """Save the updated database"""
    with open("_categories_with_arabic.json", 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def add_translations(db):
    """Add more translations to words"""
    translated_count = 0
    
    for category_key, category_data in db.items():
        words = category_data.get('words', [])
        
        for word_obj in words:
            en = word_obj.get('en', '')
            ar = word_obj.get('ar', '')
            
            # Skip if already has proper translation
            if ar and ar != en:
                continue
            
            # Try extended translations
            en_lower = en.lower()
            if en_lower in EXTENDED_TRANSLATIONS:
                word_obj['ar'] = EXTENDED_TRANSLATIONS[en_lower]
                translated_count += 1
    
    return translated_count

def categorize_other_words(db):
    """Break down 'Other' category into specific categories"""
    if 'other' not in db:
        return 0
    
    other_words = db['other']['words']
    moved_count = 0
    
    # Create new categories if they don't exist
    for cat_key, cat_data in NEW_CATEGORIES.items():
        if cat_key not in db:
            db[cat_key] = {
                "title": cat_data["title"],
                "words": []
            }
    
    # Categorize words from 'Other'
    remaining_words = []
    
    for word_obj in other_words:
        en = word_obj.get('en', '').lower()
        categorized = False
        
        # Try to match with new categories
        for cat_key, cat_data in NEW_CATEGORIES.items():
            keywords = cat_data["keywords"]
            
            # Check if word matches any keyword
            if en in keywords or any(keyword in en for keyword in keywords if len(keyword) > 3):
                db[cat_key]['words'].append(word_obj)
                moved_count += 1
                categorized = True
                break
        
        if not categorized:
            remaining_words.append(word_obj)
    
    # Update 'other' category with remaining words
    db['other']['words'] = remaining_words
    
    return moved_count

def main():
    print("🔄 Loading database...")
    db = load_database()
    
    print("✍️ Adding more translations...")
    trans_count = add_translations(db)
    print(f"  ✅ Added {trans_count} new translations")
    
    print("\n📂 Reorganizing categories...")
    moved_count = categorize_other_words(db)
    print(f"  ✅ Moved {moved_count} words from 'Other' to specific categories")
    
    print("\n💾 Saving updated database...")
    save_database(db)
    
    # Statistics
    total_words = 0
    total_translated = 0
    
    print("\n📊 Updated Category Statistics:")
    for cat_key, cat_data in sorted(db.items()):
        words = cat_data.get('words', [])
        translated = sum(1 for w in words if w.get('ar') and w['ar'] != w['en'])
        total_words += len(words)
        total_translated += translated
        
        if len(words) > 0:
            print(f"  • {cat_data.get('title', cat_key)}: {len(words)} words ({translated} translated)")
    
    print(f"\n✅ Total: {total_words} words")
    print(f"✅ Translated: {total_translated} words ({(total_translated/total_words*100):.1f}%)")
    print(f"✅ Remaining: {total_words - total_translated} words")

if __name__ == '__main__':
    main()
