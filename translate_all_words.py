#!/usr/bin/env python3
"""
Comprehensive Arabic Translation Script
Translates all English words to Modern Standard Arabic (MSA)
"""

import json
from pathlib import Path

# Comprehensive English to Arabic translation dictionary
TRANSLATIONS = {
    # Actions & Verbs
    "abandon": "يتخلى عن", "accept": "يقبل", "achieve": "يحقق", "act": "يتصرف", "add": "يضيف",
    "adopt": "يتبنى", "affect": "يؤثر", "agree": "يوافق", "allow": "يسمح", "answer": "يجيب",
    "appear": "يظهر", "apply": "يطبق", "argue": "يجادل", "arrive": "يصل", "ask": "يسأل",
    "attack": "يهاجم", "attempt": "يحاول", "attend": "يحضر", "avoid": "يتجنب", "become": "يصبح",
    "begin": "يبدأ", "believe": "يؤمن", "belong": "ينتمي", "break": "يكسر", "bring": "يحضر",
    "build": "يبني", "buy": "يشتري", "call": "يتصل", "carry": "يحمل", "catch": "يمسك",
    "cause": "يسبب", "change": "يغير", "choose": "يختار", "claim": "يدعي", "clean": "ينظف",
    "close": "يغلق", "come": "يأتي", "compare": "يقارن", "complete": "يكمل", "consider": "يعتبر",
    "contain": "يحتوي", "continue": "يستمر", "control": "يتحكم", "cook": "يطبخ", "cost": "يكلف",
    "could": "استطاع", "count": "يعد", "cover": "يغطي", "create": "يخلق", "cut": "يقطع",
    "dance": "يرقص", "deal": "يتعامل", "decide": "يقرر", "define": "يعرف", "deliver": "يسلم",
    "describe": "يصف", "design": "يصمم", "destroy": "يدمر", "develop": "يطور", "die": "يموت",
    "discover": "يكتشف", "discuss": "يناقش", "do": "يفعل", "draw": "يرسم", "dream": "يحلم",
    "drink": "يشرب", "drive": "يقود", "drop": "يسقط", "earn": "يكسب", "eat": "يأكل",
    "educate": "يعلم", "elect": "ينتخب", "end": "ينهي", "enjoy": "يستمتع", "enter": "يدخل",
    "establish": "يؤسس", "examine": "يفحص", "exist": "يوجد", "expect": "يتوقع", "explain": "يشرح",
    "explore": "يستكشف", "express": "يعبر", "face": "يواجه", "fail": "يفشل", "fall": "يسقط",
    "feel": "يشعر", "fight": "يقاتل", "fill": "يملأ", "find": "يجد", "finish": "ينهي",
    "fly": "يطير", "follow": "يتبع", "forget": "ينسى", "form": "يشكل", "freeze": "يتجمد",
    "gain": "يكسب", "get": "يحصل", "give": "يعطي", "go": "يذهب", "govern": "يحكم",
    "grow": "ينمو", "happen": "يحدث", "hate": "يكره", "have": "يملك", "hear": "يسمع",
    "help": "يساعد", "hide": "يخبئ", "hit": "يضرب", "hold": "يمسك", "hope": "يأمل",
    "hurt": "يؤذي", "identify": "يحدد", "imagine": "يتخيل", "impact": "يؤثر", "implement": "ينفذ",
    "improve": "يحسن", "include": "يتضمن", "increase": "يزيد", "indicate": "يشير", "influence": "يؤثر",
    "inform": "يخبر", "introduce": "يقدم", "invest": "يستثمر", "involve": "يشمل", "join": "ينضم",
    "jump": "يقفز", "keep": "يحتفظ", "kill": "يقتل", "know": "يعرف", "lack": "يفتقر",
    "laugh": "يضحك", "lead": "يقود", "learn": "يتعلم", "leave": "يغادر", "let": "يترك",
    "lie": "يكذب", "lift": "يرفع", "like": "يحب", "listen": "يستمع", "live": "يعيش",
    "look": "ينظر", "lose": "يخسر", "love": "يحب", "maintain": "يحافظ", "make": "يصنع",
    "manage": "يدير", "mark": "يعلم", "matter": "يهم", "mean": "يعني", "measure": "يقيس",
    "meet": "يلتقي", "mention": "يذكر", "mind": "يمانع", "miss": "يفتقد", "move": "يتحرك",
    "need": "يحتاج", "note": "يلاحظ", "notice": "يلاحظ", "obtain": "يحصل على", "occur": "يحدث",
    "offer": "يعرض", "open": "يفتح", "operate": "يشغل", "order": "يأمر", "organize": "ينظم",
    "own": "يملك", "paint": "يرسم", "pass": "يمرر", "pay": "يدفع", "perform": "يؤدي",
    "pick": "يختار", "place": "يضع", "plan": "يخطط", "play": "يلعب", "point": "يشير",
    "practice": "يمارس", "prepare": "يحضر", "present": "يقدم", "prevent": "يمنع", "produce": "ينتج",
    "protect": "يحمي", "prove": "يثبت", "provide": "يوفر", "publish": "ينشر", "pull": "يسحب",
    "push": "يدفع", "put": "يضع", "raise": "يرفع", "reach": "يصل", "read": "يقرأ",
    "realize": "يدرك", "receive": "يستقبل", "recognize": "يتعرف", "record": "يسجل", "reduce": "يقلل",
    "refer": "يشير", "reflect": "يعكس", "refuse": "يرفض", "regard": "يعتبر", "relate": "يتعلق",
    "release": "يطلق", "remain": "يبقى", "remember": "يتذكر", "remove": "يزيل", "repeat": "يكرر",
    "replace": "يستبدل", "report": "يبلغ", "represent": "يمثل", "require": "يتطلب", "research": "يبحث",
    "respond": "يستجيب", "rest": "يستريح", "result": "ينتج", "return": "يعود", "reveal": "يكشف",
    "ride": "يركب", "rise": "يرتفع", "run": "يركض", "save": "يحفظ", "say": "يقول",
    "see": "يرى", "seek": "يبحث", "seem": "يبدو", "sell": "يبيع", "send": "يرسل",
    "serve": "يخدم", "set": "يضع", "share": "يشارك", "shoot": "يطلق", "shop": "يتسوق",
    "show": "يظهر", "shut": "يغلق", "sing": "يغني", "sit": "يجلس", "sleep": "ينام",
    "smile": "يبتسم", "speak": "يتحدث", "spend": "ينفق", "stand": "يقف", "start": "يبدأ",
    "state": "يصرح", "stay": "يبقى", "stop": "يتوقف", "study": "يدرس", "succeed": "ينجح",
    "suffer": "يعاني", "suggest": "يقترح", "support": "يدعم", "suppose": "يفترض", "survive": "ينجو",
    "swim": "يسبح", "take": "يأخذ", "talk": "يتحدث", "teach": "يعلم", "tell": "يخبر",
    "tend": "يميل", "test": "يختبر", "thank": "يشكر", "think": "يفكر", "throw": "يرمي",
    "touch": "يلمس", "train": "يدرب", "travel": "يسافر", "treat": "يعالج", "try": "يحاول",
    "turn": "يدور", "understand": "يفهم", "use": "يستخدم", "visit": "يزور", "vote": "يصوت",
    "wait": "ينتظر", "walk": "يمشي", "want": "يريد", "warn": "يحذر", "wash": "يغسل",
    "watch": "يشاهد", "wear": "يرتدي", "win": "يفوز", "wish": "يتمنى", "wonder": "يتساءل",
    "work": "يعمل", "worry": "يقلق", "write": "يكتب",
    
    # People & Society
    "man": "رجل", "woman": "امرأة", "person": "شخص", "people": "ناس", "child": "طفل",
    "boy": "صبي", "girl": "فتاة", "friend": "صديق", "family": "عائلة", "mother": "أم",
    "father": "أب", "parent": "والد", "brother": "أخ", "sister": "أخت", "son": "ابن",
    "daughter": "ابنة", "husband": "زوج", "wife": "زوجة", "baby": "طفل رضيع", "kid": "طفل",
    "adult": "بالغ", "teenager": "مراهق", "youth": "شباب", "elder": "مسن", "citizen": "مواطن",
    "student": "طالب", "teacher": "معلم", "doctor": "طبيب", "nurse": "ممرض", "worker": "عامل",
    "employee": "موظف", "boss": "رئيس", "manager": "مدير", "leader": "قائد", "president": "رئيس",
    "member": "عضو", "team": "فريق", "group": "مجموعة", "community": "مجتمع", "society": "مجتمع",
    "neighbor": "جار", "stranger": "غريب", "guest": "ضيف", "host": "مضيف", "customer": "زبون",
    "client": "عميل", "patient": "مريض", "victim": "ضحية", "hero": "بطل", "villain": "شرير",
    "artist": "فنان", "writer": "كاتب", "singer": "مغني", "actor": "ممثل", "dancer": "راقص",
    "musician": "موسيقي", "player": "لاعب", "coach": "مدرب", "judge": "قاضي", "lawyer": "محامي",
    "police": "شرطة", "soldier": "جندي", "officer": "ضابط", "guard": "حارس", "driver": "سائق",
    "pilot": "طيار", "captain": "قبطان", "sailor": "بحار", "farmer": "مزارع", "chef": "طاه",
    "waiter": "نادل", "clerk": "موظف", "cashier": "أمين صندوق", "mechanic": "ميكانيكي", "engineer": "مهندس",
    "scientist": "عالم", "researcher": "باحث", "professor": "أستاذ", "principal": "مدير", "secretary": "سكرتير",
    "assistant": "مساعد", "volunteer": "متطوع", "immigrant": "مهاجر", "refugee": "لاجئ", "tourist": "سائح",
    "adolescent": "مراهق", "relative": "قريب", "ancestor": "جد", "descendant": "نسل", "generation": "جيل",
    
    # Qualities & Attributes
    "good": "جيد", "bad": "سيئ", "big": "كبير", "small": "صغير", "large": "كبير",
    "little": "قليل", "long": "طويل", "short": "قصير", "high": "عالي", "low": "منخفض",
    "hot": "حار", "cold": "بارد", "warm": "دافئ", "cool": "بارد", "wet": "مبلل",
    "dry": "جاف", "clean": "نظيف", "dirty": "قذر", "new": "جديد", "old": "قديم",
    "young": "شاب", "fresh": "طازج", "strong": "قوي", "weak": "ضعيف", "hard": "صعب",
    "soft": "ناعم", "easy": "سهل", "difficult": "صعب", "simple": "بسيط", "complex": "معقد",
    "fast": "سريع", "slow": "بطيء", "quick": "سريع", "early": "مبكر", "late": "متأخر",
    "heavy": "ثقيل", "light": "خفيف", "thick": "سميك", "thin": "رقيق", "wide": "عريض",
    "narrow": "ضيق", "deep": "عميق", "shallow": "ضحل", "full": "ممتلئ", "empty": "فارغ",
    "rich": "غني", "poor": "فقير", "cheap": "رخيص", "expensive": "غالي", "free": "مجاني",
    "right": "صحيح", "wrong": "خاطئ", "true": "صحيح", "false": "خاطئ", "real": "حقيقي",
    "safe": "آمن", "dangerous": "خطير", "calm": "هادئ", "busy": "مشغول", "quiet": "هادئ",
    "loud": "صاخب", "bright": "مشرق", "dark": "مظلم", "beautiful": "جميل", "ugly": "قبيح",
    "pretty": "جميل", "handsome": "وسيم", "nice": "لطيف", "kind": "لطيف", "mean": "لئيم",
    "friendly": "ودود", "happy": "سعيد", "sad": "حزين", "angry": "غاضب", "glad": "سعيد",
    "sorry": "آسف", "proud": "فخور", "brave": "شجاع", "afraid": "خائف", "careful": "حذر",
    "smart": "ذكي", "stupid": "غبي", "wise": "حكيم", "funny": "مضحك", "serious": "جاد",
    "strange": "غريب", "normal": "عادي", "common": "شائع", "rare": "نادر", "special": "خاص",
    "important": "مهم", "necessary": "ضروري", "possible": "ممكن", "impossible": "مستحيل", "sure": "متأكد",
    "certain": "مؤكد", "clear": "واضح", "obvious": "واضح", "simple": "بسيط", "main": "رئيسي",
    "basic": "أساسي", "extra": "إضافي", "total": "كلي", "whole": "كامل", "complete": "كامل",
    "perfect": "مثالي", "excellent": "ممتاز", "wonderful": "رائع", "terrible": "فظيع", "awful": "سيء جداً",
    "amazing": "مذهل", "interesting": "مثير", "boring": "ممل", "exciting": "مثير", "comfortable": "مريح",
    "popular": "شعبي", "famous": "مشهور", "public": "عام", "private": "خاص", "personal": "شخصي",
    "social": "اجتماعي", "natural": "طبيعي", "human": "بشري", "medical": "طبي", "legal": "قانوني",
    "political": "سياسي", "economic": "اقتصادي", "financial": "مالي", "cultural": "ثقافي", "traditional": "تقليدي",
    "modern": "حديث", "ancient": "قديم", "current": "حالي", "recent": "حديث", "future": "مستقبلي",
    "past": "ماضي", "present": "حاضر", "final": "نهائي", "last": "أخير", "next": "تالي",
    "first": "أول", "second": "ثاني", "third": "ثالث", "single": "واحد", "double": "مزدوج",
    "several": "عدة", "many": "كثير", "few": "قليل", "much": "كثير", "less": "أقل",
    "more": "أكثر", "most": "معظم", "all": "كل", "every": "كل", "each": "كل",
    "both": "كلا", "either": "أي", "neither": "لا", "none": "لا شيء", "other": "آخر",
    "another": "آخر", "same": "نفس", "different": "مختلف", "similar": "مماثل", "equal": "متساو",
    "opposite": "معاكس", "positive": "إيجابي", "negative": "سلبي", "active": "نشط", "passive": "سلبي",
    
    # Time & Dates
    "time": "وقت", "day": "يوم", "week": "أسبوع", "month": "شهر", "year": "سنة",
    "hour": "ساعة", "minute": "دقيقة", "second": "ثانية", "moment": "لحظة", "period": "فترة",
    "season": "موسم", "spring": "ربيع", "summer": "صيف", "autumn": "خريف", "winter": "شتاء",
    "morning": "صباح", "afternoon": "بعد الظهر", "evening": "مساء", "night": "ليل", "midnight": "منتصف الليل",
    "today": "اليوم", "yesterday": "أمس", "tomorrow": "غداً", "now": "الآن", "then": "ثم",
    "ago": "منذ", "soon": "قريباً", "later": "لاحقاً", "before": "قبل", "after": "بعد",
    "during": "أثناء", "while": "بينما", "until": "حتى", "since": "منذ", "always": "دائماً",
    "never": "أبداً", "often": "غالباً", "sometimes": "أحياناً", "usually": "عادة", "rarely": "نادراً",
    "Monday": "الاثنين", "Tuesday": "الثلاثاء", "Wednesday": "الأربعاء", "Thursday": "الخميس", "Friday": "الجمعة",
    "Saturday": "السبت", "Sunday": "الأحد", "January": "يناير", "February": "فبراير", "March": "مارس",
    "April": "أبريل", "May": "مايو", "June": "يونيو", "July": "يوليو", "August": "أغسطس",
    "September": "سبتمبر", "October": "أكتوبر", "November": "نوفمبر", "December": "ديسمبر",
    "date": "تاريخ", "calendar": "تقويم", "clock": "ساعة", "schedule": "جدول", "deadline": "موعد نهائي",
    "century": "قرن", "decade": "عقد", "era": "عصر", "age": "عمر", "lifetime": "حياة",
    
    # Nature & Environment
    "nature": "طبيعة", "world": "عالم", "earth": "أرض", "land": "أرض", "ground": "أرض",
    "sky": "سماء", "sun": "شمس", "moon": "قمر", "star": "نجم", "planet": "كوكب",
    "water": "ماء", "air": "هواء", "fire": "نار", "wind": "ريح", "rain": "مطر",
    "snow": "ثلج", "ice": "جليد", "cloud": "سحابة", "storm": "عاصفة", "weather": "طقس",
    "climate": "مناخ", "temperature": "درجة حرارة", "season": "فصل", "environment": "بيئة",
    "tree": "شجرة", "plant": "نبات", "flower": "زهرة", "grass": "عشب", "leaf": "ورقة",
    "forest": "غابة", "wood": "خشب", "branch": "فرع", "root": "جذر", "seed": "بذرة",
    "mountain": "جبل", "hill": "تل", "valley": "وادي", "river": "نهر", "lake": "بحيرة",
    "sea": "بحر", "ocean": "محيط", "beach": "شاطئ", "island": "جزيرة", "desert": "صحراء",
    "rock": "صخرة", "stone": "حجر", "sand": "رمل", "soil": "تربة", "mud": "طين",
    "animal": "حيوان", "bird": "طائر", "fish": "سمك", "dog": "كلب", "cat": "قطة",
    "horse": "حصان", "cow": "بقرة", "pig": "خنزير", "sheep": "خروف", "chicken": "دجاج",
    "lion": "أسد", "tiger": "نمر", "bear": "دب", "wolf": "ذئب", "fox": "ثعلب",
    "deer": "غزال", "rabbit": "أرنب", "mouse": "فأر", "rat": "جرذ", "snake": "ثعبان",
    "insect": "حشرة", "butterfly": "فراشة", "bee": "نحلة", "ant": "نملة", "spider": "عنكبوت",
    
    # Food & Cooking
    "food": "طعام", "meal": "وجبة", "breakfast": "إفطار", "lunch": "غداء", "dinner": "عشاء",
    "bread": "خبز", "rice": "أرز", "meat": "لحم", "fish": "سمك", "chicken": "دجاج",
    "beef": "لحم بقر", "pork": "لحم خنزير", "egg": "بيضة", "milk": "حليب", "cheese": "جبن",
    "butter": "زبدة", "oil": "زيت", "salt": "ملح", "sugar": "سكر", "pepper": "فلفل",
    "fruit": "فاكهة", "apple": "تفاحة", "orange": "برتقال", "banana": "موز", "grape": "عنب",
    "lemon": "ليمون", "strawberry": "فراولة", "watermelon": "بطيخ", "peach": "خوخ", "pear": "كمثرى",
    "vegetable": "خضار", "potato": "بطاطا", "tomato": "طماطم", "onion": "بصل", "carrot": "جزر",
    "cabbage": "ملفوف", "lettuce": "خس", "cucumber": "خيار", "pepper": "فلفل", "bean": "فاصوليا",
    "soup": "شوربة", "salad": "سلطة", "sandwich": "شطيرة", "pizza": "بيتزا", "pasta": "معكرونة",
    "cake": "كعكة", "cookie": "بسكويت", "chocolate": "شوكولاتة", "candy": "حلوى", "ice cream": "آيس كريم",
    "drink": "مشروب", "water": "ماء", "juice": "عصير", "coffee": "قهوة", "tea": "شاي",
    "wine": "نبيذ", "beer": "بيرة", "soda": "صودا", "restaurant": "مطعم", "menu": "قائمة",
    "cook": "يطبخ", "bake": "يخبز", "fry": "يقلي", "boil": "يغلي", "grill": "يشوي",
    "taste": "طعم", "flavor": "نكهة", "delicious": "لذيذ", "sweet": "حلو", "sour": "حامض",
    "bitter": "مر", "spicy": "حار", "fresh": "طازج", "raw": "نيء", "cooked": "مطبوخ",
    "recipe": "وصفة", "ingredient": "مكون", "spice": "بهار", "herb": "عشب", "sauce": "صلصة",
    
    # Home & Family
    "home": "بيت", "house": "منزل", "apartment": "شقة", "room": "غرفة", "kitchen": "مطبخ",
    "bedroom": "غرفة نوم", "bathroom": "حمام", "living room": "غرفة معيشة", "dining room": "غرفة طعام", "office": "مكتب",
    "door": "باب", "window": "نافذة", "wall": "جدار", "floor": "أرضية", "ceiling": "سقف",
    "roof": "سطح", "stairs": "سلالم", "garden": "حديقة", "yard": "فناء", "garage": "مرآب",
    "furniture": "أثاث", "table": "طاولة", "chair": "كرسي", "bed": "سرير", "sofa": "أريكة",
    "desk": "مكتب", "shelf": "رف", "cabinet": "خزانة", "drawer": "درج", "closet": "خزانة ملابس",
    "lamp": "مصباح", "light": "ضوء", "mirror": "مرآة", "picture": "صورة", "clock": "ساعة",
    "television": "تلفزيون", "radio": "راديو", "phone": "هاتف", "computer": "كمبيوتر", "refrigerator": "ثلاجة",
    "stove": "موقد", "oven": "فرن", "microwave": "ميكروويف", "dishwasher": "غسالة صحون", "washing machine": "غسالة",
    "plate": "صحن", "cup": "كوب", "glass": "كأس", "bowl": "وعاء", "fork": "شوكة",
    "knife": "سكين", "spoon": "ملعقة", "pot": "قدر", "pan": "مقلاة", "bottle": "زجاجة",
    "towel": "منشفة", "blanket": "بطانية", "pillow": "وسادة", "sheet": "ملاءة", "curtain": "ستارة",
    "carpet": "سجادة", "rug": "سجادة صغيرة", "basket": "سلة", "box": "صندوق", "bag": "حقيبة",
    
    # Fashion & Clothing
    "clothes": "ملابس", "dress": "فستان", "shirt": "قميص", "pants": "بنطال", "skirt": "تنورة",
    "coat": "معطف", "jacket": "سترة", "sweater": "سترة صوفية", "suit": "بدلة", "uniform": "زي موحد",
    "shoe": "حذاء", "boot": "حذاء طويل", "sandal": "صندل", "sock": "جورب", "hat": "قبعة",
    "cap": "قبعة", "scarf": "وشاح", "glove": "قفاز", "belt": "حزام", "tie": "ربطة عنق",
    "pocket": "جيب", "button": "زر", "zipper": "سحاب", "sleeve": "كم", "collar": "ياقة",
    "fashion": "موضة", "style": "أسلوب", "color": "لون", "size": "حجم", "fit": "ملائم",
    "wear": "يرتدي", "put on": "يلبس", "take off": "يخلع", "change": "يغير", "wash": "يغسل",
    "clean": "ينظف", "iron": "يكوي", "sew": "يخيط", "design": "يصمم", "fabric": "قماش",
    "cotton": "قطن", "silk": "حرير", "wool": "صوف", "leather": "جلد", "plastic": "بلاستيك",
    "jewelry": "مجوهرات", "ring": "خاتم", "necklace": "عقد", "bracelet": "سوار", "earring": "قرط",
    
    # Education & Learning
    "school": "مدرسة", "class": "صف", "lesson": "درس", "subject": "مادة", "course": "دورة",
    "teacher": "معلم", "student": "طالب", "professor": "أستاذ", "principal": "مدير", "classmate": "زميل صف",
    "test": "اختبار", "exam": "امتحان", "quiz": "اختبار قصير", "homework": "واجب منزلي", "assignment": "مهمة",
    "grade": "درجة", "score": "نتيجة", "mark": "علامة", "certificate": "شهادة", "degree": "درجة علمية",
    "book": "كتاب", "page": "صفحة", "chapter": "فصل", "paragraph": "فقرة", "sentence": "جملة",
    "word": "كلمة", "letter": "حرف", "notebook": "دفتر", "pen": "قلم", "pencil": "قلم رصاص",
    "paper": "ورق", "desk": "مكتب", "board": "لوح", "chalk": "طباشير", "eraser": "ممحاة",
    "library": "مكتبة", "dictionary": "قاموس", "encyclopedia": "موسوعة", "magazine": "مجلة", "newspaper": "جريدة",
    "read": "يقرأ", "write": "يكتب", "study": "يدرس", "learn": "يتعلم", "teach": "يعلم",
    "understand": "يفهم", "know": "يعرف", "remember": "يتذكر", "forget": "ينسى", "practice": "يمارس",
    "research": "بحث", "project": "مشروع", "report": "تقرير", "presentation": "عرض تقديمي", "discussion": "نقاش",
    "knowledge": "معرفة", "skill": "مهارة", "ability": "قدرة", "talent": "موهبة", "intelligence": "ذكاء",
    "university": "جامعة", "college": "كلية", "institute": "معهد", "academy": "أكاديمية", "campus": "حرم جامعي",
    
    # Business & Economics
    "business": "عمل تجاري", "company": "شركة", "corporation": "شركة", "firm": "شركة", "organization": "منظمة",
    "office": "مكتب", "factory": "مصنع", "shop": "متجر", "store": "متجر", "market": "سوق",
    "bank": "بنك", "money": "مال", "cash": "نقد", "coin": "عملة معدنية", "bill": "فاتورة",
    "dollar": "دولار", "price": "سعر", "cost": "تكلفة", "value": "قيمة", "profit": "ربح",
    "loss": "خسارة", "income": "دخل", "expense": "نفقة", "budget": "ميزانية", "tax": "ضريبة",
    "buy": "يشتري", "sell": "يبيع", "pay": "يدفع", "spend": "ينفق", "save": "يوفر",
    "invest": "يستثمر", "earn": "يكسب", "owe": "يدين", "lend": "يقرض", "borrow": "يستعير",
    "trade": "تجارة", "deal": "صفقة", "contract": "عقد", "agreement": "اتفاقية", "sale": "بيع",
    "customer": "زبون", "client": "عميل", "consumer": "مستهلك", "buyer": "مشتري", "seller": "بائع",
    "product": "منتج", "service": "خدمة", "goods": "بضائع", "item": "عنصر", "brand": "علامة تجارية",
    "advertising": "إعلان", "marketing": "تسويق", "promotion": "ترويج", "campaign": "حملة", "sales": "مبيعات",
    "economy": "اقتصاد", "finance": "مالية", "industry": "صناعة", "commerce": "تجارة", "capital": "رأس مال",
    "investment": "استثمار", "stock": "أسهم", "share": "سهم", "bond": "سند", "dividend": "أرباح",
    "debt": "دين", "credit": "ائتمان", "loan": "قرض", "interest": "فائدة", "account": "حساب",
    
    # Technology & Science
    "computer": "كمبيوتر", "laptop": "كمبيوتر محمول", "tablet": "جهاز لوحي", "phone": "هاتف", "smartphone": "هاتف ذكي",
    "internet": "إنترنت", "website": "موقع إلكتروني", "email": "بريد إلكتروني", "app": "تطبيق", "software": "برمجيات",
    "program": "برنامج", "system": "نظام", "data": "بيانات", "information": "معلومات", "file": "ملف",
    "screen": "شاشة", "keyboard": "لوحة مفاتيح", "mouse": "فأرة", "printer": "طابعة", "camera": "كاميرا",
    "technology": "تقنية", "digital": "رقمي", "electronic": "إلكتروني", "automatic": "أوتوماتيكي", "mechanical": "ميكانيكي",
    "science": "علم", "physics": "فيزياء", "chemistry": "كيمياء", "biology": "أحياء", "mathematics": "رياضيات",
    "experiment": "تجربة", "research": "بحث", "theory": "نظرية", "hypothesis": "فرضية", "discovery": "اكتشاف",
    "invention": "اختراع", "innovation": "ابتكار", "development": "تطوير", "progress": "تقدم", "advance": "تقدم",
    "machine": "آلة", "engine": "محرك", "motor": "محرك", "device": "جهاز", "tool": "أداة",
    "network": "شبكة", "connection": "اتصال", "signal": "إشارة", "wireless": "لاسلكي", "satellite": "قمر صناعي",
    "robot": "روبوت", "artificial": "صناعي", "intelligence": "ذكاء", "algorithm": "خوارزمية", "code": "شفرة",
    "database": "قاعدة بيانات", "server": "خادم", "cloud": "سحابة", "security": "أمن", "password": "كلمة مرور",
    
    # Sports & Recreation
    "sport": "رياضة", "game": "لعبة", "play": "يلعب", "player": "لاعب", "team": "فريق",
    "match": "مباراة", "competition": "منافسة", "championship": "بطولة", "tournament": "دورة", "race": "سباق",
    "win": "يفوز", "lose": "يخسر", "draw": "تعادل", "score": "نتيجة", "goal": "هدف",
    "point": "نقطة", "victory": "نصر", "defeat": "هزيمة", "champion": "بطل", "trophy": "كأس",
    "football": "كرة قدم", "soccer": "كرة قدم", "basketball": "كرة سلة", "tennis": "تنس", "volleyball": "كرة طائرة",
    "baseball": "بيسبول", "hockey": "هوكي", "golf": "غولف", "swimming": "سباحة", "running": "جري",
    "cycling": "ركوب الدراجات", "boxing": "ملاكمة", "wrestling": "مصارعة", "martial arts": "فنون قتالية", "yoga": "يوغا",
    "ball": "كرة", "bat": "مضرب", "racket": "مضرب", "club": "عصا", "stick": "عصا",
    "field": "ملعب", "court": "ملعب", "stadium": "ملعب", "gym": "صالة رياضية", "pool": "مسبح",
    "coach": "مدرب", "referee": "حكم", "fan": "مشجع", "spectator": "متفرج", "audience": "جمهور",
    "exercise": "تمرين", "training": "تدريب", "practice": "ممارسة", "fitness": "لياقة", "health": "صحة",
    "run": "يركض", "jump": "يقفز", "throw": "يرمي", "catch": "يمسك", "kick": "يركل",
    
    # Health & Medicine
    "health": "صحة", "medical": "طبي", "medicine": "دواء", "drug": "دواء", "pill": "حبة",
    "hospital": "مستشفى", "clinic": "عيادة", "doctor": "طبيب", "nurse": "ممرض", "patient": "مريض",
    "disease": "مرض", "illness": "مرض", "sickness": "مرض", "pain": "ألم", "ache": "وجع",
    "fever": "حمى", "cold": "برد", "flu": "إنفلونزا", "cough": "سعال", "headache": "صداع",
    "injury": "إصابة", "wound": "جرح", "cut": "جرح", "bruise": "كدمة", "burn": "حرق",
    "surgery": "جراحة", "operation": "عملية", "treatment": "علاج", "therapy": "علاج", "cure": "شفاء",
    "vaccine": "لقاح", "injection": "حقنة", "prescription": "وصفة طبية", "dose": "جرعة", "symptom": "عرض",
    "diagnosis": "تشخيص", "examination": "فحص", "test": "اختبار", "scan": "مسح", "x-ray": "أشعة سينية",
    "blood": "دم", "heart": "قلب", "lung": "رئة", "stomach": "معدة", "brain": "دماغ",
    "body": "جسم", "head": "رأس", "face": "وجه", "eye": "عين", "ear": "أذن",
    "nose": "أنف", "mouth": "فم", "tooth": "سن", "tongue": "لسان", "throat": "حلق",
    "neck": "رقبة", "shoulder": "كتف", "arm": "ذراع", "hand": "يد", "finger": "إصبع",
    "chest": "صدر", "back": "ظهر", "leg": "ساق", "foot": "قدم", "toe": "إصبع القدم",
    
    # Government & Politics
    "government": "حكومة", "state": "دولة", "country": "بلد", "nation": "أمة", "republic": "جمهورية",
    "democracy": "ديمقراطية", "politics": "سياسة", "political": "سياسي", "policy": "سياسة", "law": "قانون",
    "rule": "قاعدة", "regulation": "لائحة", "order": "أمر", "authority": "سلطة", "power": "قوة",
    "president": "رئيس", "minister": "وزير", "senator": "عضو مجلس الشيوخ", "congressman": "نائب", "mayor": "عمدة",
    "official": "مسؤول", "leader": "قائد", "representative": "ممثل", "delegate": "مندوب", "ambassador": "سفير",
    "election": "انتخاب", "vote": "تصويت", "ballot": "اقتراع", "campaign": "حملة", "candidate": "مرشح",
    "party": "حزب", "parliament": "برلمان", "congress": "كونغرس", "senate": "مجلس الشيوخ", "assembly": "جمعية",
    "constitution": "دستور", "amendment": "تعديل", "bill": "مشروع قانون", "act": "قانون", "statute": "تشريع",
    "court": "محكمة", "judge": "قاضي", "jury": "هيئة محلفين", "lawyer": "محامي", "attorney": "محامي",
    "justice": "عدالة", "trial": "محاكمة", "case": "قضية", "verdict": "حكم", "sentence": "عقوبة",
    "crime": "جريمة", "criminal": "مجرم", "punishment": "عقوبة", "prison": "سجن", "jail": "سجن",
    "police": "شرطة", "officer": "ضابط", "arrest": "اعتقال", "investigation": "تحقيق", "evidence": "دليل",
    "right": "حق", "freedom": "حرية", "liberty": "حرية", "citizen": "مواطن", "citizenship": "مواطنة",
    "tax": "ضريبة", "budget": "ميزانية", "public": "عام", "private": "خاص", "service": "خدمة",
    
    # Arts & Culture
    "art": "فن", "artist": "فنان", "painting": "لوحة", "drawing": "رسم", "sculpture": "نحت",
    "music": "موسيقى", "song": "أغنية", "singer": "مغني", "musician": "موسيقي", "band": "فرقة",
    "instrument": "آلة موسيقية", "piano": "بيانو", "guitar": "غيتار", "drum": "طبل", "violin": "كمان",
    "dance": "رقص", "dancer": "راقص", "ballet": "باليه", "performance": "أداء", "show": "عرض",
    "theater": "مسرح", "play": "مسرحية", "actor": "ممثل", "actress": "ممثلة", "stage": "مسرح",
    "film": "فيلم", "movie": "فيلم", "cinema": "سينما", "director": "مخرج", "producer": "منتج",
    "television": "تلفزيون", "radio": "راديو", "program": "برنامج", "channel": "قناة", "broadcast": "بث",
    "book": "كتاب", "novel": "رواية", "story": "قصة", "poem": "قصيدة", "poetry": "شعر",
    "writer": "كاتب", "author": "مؤلف", "poet": "شاعر", "journalist": "صحفي", "reporter": "مراسل",
    "literature": "أدب", "culture": "ثقافة", "tradition": "تقليد", "custom": "عادة", "heritage": "تراث",
    "museum": "متحف", "gallery": "معرض", "exhibition": "معرض", "collection": "مجموعة", "masterpiece": "تحفة",
    "style": "أسلوب", "genre": "نوع", "technique": "تقنية", "method": "طريقة", "form": "شكل",
    "creative": "إبداعي", "artistic": "فني", "cultural": "ثقافي", "classical": "كلاسيكي", "modern": "حديث",
    
    # Travel & Transportation
    "travel": "سفر", "trip": "رحلة", "journey": "رحلة", "tour": "جولة", "vacation": "إجازة",
    "tourist": "سائح", "visitor": "زائر", "guide": "مرشد", "passport": "جواز سفر", "visa": "تأشيرة",
    "ticket": "تذكرة", "reservation": "حجز", "booking": "حجز", "hotel": "فندق", "motel": "موتيل",
    "airport": "مطار", "station": "محطة", "port": "ميناء", "terminal": "محطة", "platform": "رصيف",
    "train": "قطار", "bus": "حافلة", "car": "سيارة", "taxi": "تاكسي", "truck": "شاحنة",
    "plane": "طائرة", "airplane": "طائرة", "flight": "رحلة جوية", "pilot": "طيار", "crew": "طاقم",
    "ship": "سفينة", "boat": "قارب", "ferry": "عبارة", "cruise": "رحلة بحرية", "sail": "إبحار",
    "bicycle": "دراجة", "motorcycle": "دراجة نارية", "scooter": "دراجة", "subway": "مترو", "metro": "مترو",
    "road": "طريق", "street": "شارع", "highway": "طريق سريع", "bridge": "جسر", "tunnel": "نفق",
    "map": "خريطة", "direction": "اتجاه", "distance": "مسافة", "route": "مسار", "destination": "وجهة",
    "luggage": "أمتعة", "baggage": "أمتعة", "suitcase": "حقيبة سفر", "backpack": "حقيبة ظهر", "bag": "حقيبة",
    "departure": "مغادرة", "arrival": "وصول", "delay": "تأخير", "cancel": "إلغاء", "schedule": "جدول",
    
    # Emotions & Feelings
    "happy": "سعيد", "sad": "حزين", "angry": "غاضب", "afraid": "خائف", "scared": "خائف",
    "excited": "متحمس", "nervous": "متوتر", "worried": "قلق", "anxious": "قلق", "stressed": "متوتر",
    "calm": "هادئ", "relaxed": "مسترخي", "comfortable": "مرتاح", "peaceful": "مسالم", "content": "راضي",
    "proud": "فخور", "ashamed": "خجل", "embarrassed": "محرج", "guilty": "مذنب", "sorry": "آسف",
    "grateful": "شاكر", "thankful": "ممتن", "appreciated": "يقدر", "loved": "محبوب", "loving": "محب",
    "hate": "كره", "jealous": "غيور", "envious": "حسود", "angry": "غاضب", "furious": "غاضب جداً",
    "disappointed": "خائب الأمل", "frustrated": "محبط", "confused": "مرتبك", "surprised": "مندهش", "shocked": "صدم",
    "interested": "مهتم", "curious": "فضولي", "bored": "ملل", "tired": "متعب", "exhausted": "منهك",
    "lonely": "وحيد", "isolated": "معزول", "depressed": "مكتئب", "hopeful": "متفائل", "optimistic": "متفائل",
    "pessimistic": "متشائم", "confident": "واثق", "doubt": "شك", "trust": "ثقة", "believe": "يؤمن",
    
    # Common Words
    "the": "ال", "a": "أحد", "an": "أحد", "and": "و", "or": "أو",
    "but": "لكن", "if": "إذا", "so": "لذا", "because": "لأن", "when": "عندما",
    "where": "أين", "why": "لماذا", "how": "كيف", "what": "ماذا", "who": "من",
    "which": "أي", "whose": "من", "whom": "من", "this": "هذا", "that": "ذلك",
    "these": "هؤلاء", "those": "أولئك", "here": "هنا", "there": "هناك", "everywhere": "في كل مكان",
    "somewhere": "مكان ما", "anywhere": "أي مكان", "nowhere": "لا مكان", "yes": "نعم", "no": "لا",
    "maybe": "ربما", "perhaps": "ربما", "probably": "محتمل", "definitely": "بالتأكيد", "certainly": "بالتأكيد",
    "really": "حقاً", "very": "جداً", "too": "أيضاً", "also": "أيضاً", "even": "حتى",
    "just": "فقط", "only": "فقط", "still": "لا يزال", "yet": "بعد", "already": "بالفعل",
    "almost": "تقريباً", "quite": "تماماً", "rather": "بدلاً من", "enough": "كافٍ", "much": "كثير",
    "thing": "شيء", "something": "شيء ما", "anything": "أي شيء", "nothing": "لا شيء", "everything": "كل شيء",
    "place": "مكان", "way": "طريقة", "problem": "مشكلة", "question": "سؤال", "answer": "جواب",
    "idea": "فكرة", "fact": "حقيقة", "truth": "حقيقة", "reason": "سبب", "cause": "سبب",
    "effect": "تأثير", "result": "نتيجة", "example": "مثال", "case": "حالة", "situation": "موقف",
    "condition": "حالة", "position": "موضع", "level": "مستوى", "rate": "معدل", "degree": "درجة",
    "type": "نوع", "kind": "نوع", "sort": "نوع", "form": "شكل", "way": "طريقة",
    "method": "طريقة", "system": "نظام", "process": "عملية", "part": "جزء", "piece": "قطعة",
    "side": "جانب", "end": "نهاية", "beginning": "بداية", "middle": "وسط", "center": "مركز",
    "top": "أعلى", "bottom": "أسفل", "front": "أمام", "back": "خلف", "inside": "داخل",
    "outside": "خارج", "above": "فوق", "below": "تحت", "over": "فوق", "under": "تحت",
    "between": "بين", "among": "بين", "through": "عبر", "across": "عبر", "around": "حول",
    "near": "قريب", "far": "بعيد", "close": "قريب", "away": "بعيد", "together": "معاً",
    "apart": "منفصل", "alone": "وحده", "separate": "منفصل", "with": "مع", "without": "بدون",
    
    # Additional words
    "God": "الله", "category": "فئة", "budget": "ميزانية", "basket": "سلة",
    "age": "عمر", "area": "منطقة", "century": "قرن", "action": "عمل", "activity": "نشاط",
    "advantage": "ميزة", "advice": "نصيحة", "affair": "شأن", "attention": "انتباه", "attitude": "موقف",
    "audience": "جمهور", "background": "خلفية", "balance": "توازن", "basis": "أساس", "behavior": "سلوك",
    "benefit": "فائدة", "border": "حدود", "capacity": "قدرة", "career": "مهنة", "challenge": "تحدي",
    "chance": "فرصة", "choice": "خيار", "circumstance": "ظرف", "claim": "مطالبة", "commission": "عمولة",
    "committee": "لجنة", "comparison": "مقارنة", "concept": "مفهوم", "concern": "قلق", "conclusion": "خاتمة",
    "conflict": "صراع", "connection": "اتصال", "consequence": "نتيجة", "consideration": "اعتبار", "consumer": "مستهلك",
    "contact": "اتصال", "content": "محتوى", "context": "سياق", "contribution": "مساهمة", "control": "سيطرة",
    "cooperation": "تعاون", "cost": "تكلفة", "council": "مجلس", "couple": "زوجان", "course": "مسار",
    "coverage": "تغطية", "crisis": "أزمة", "criterion": "معيار", "criticism": "نقد", "critic": "ناقد",
    "crowd": "حشد", "debate": "نقاش", "debt": "دين", "decision": "قرار", "decline": "انخفاض",
    "definition": "تعريف", "demand": "طلب", "democracy": "ديمقراطية", "department": "قسم", "description": "وصف",
    "detail": "تفصيل", "determination": "تصميم", "difference": "فرق", "difficulty": "صعوبة", "dimension": "بُعد",
    "direction": "اتجاه", "discussion": "نقاش", "distribution": "توزيع", "division": "قسم", "document": "وثيقة",
    "doubt": "شك", "drama": "دراما", "duty": "واجب", "economy": "اقتصاد", "editor": "محرر",
    "education": "تعليم", "effect": "تأثير", "efficiency": "كفاءة", "effort": "جهد", "element": "عنصر",
    "emergency": "طوارئ", "emphasis": "تأكيد", "employment": "توظيف", "energy": "طاقة", "engineering": "هندسة",
    "entertainment": "ترفيه", "entry": "دخول", "equipment": "معدات", "error": "خطأ", "establishment": "مؤسسة",
    "estate": "عقار", "estimate": "تقدير", "evaluation": "تقييم", "event": "حدث", "evidence": "دليل",
    "evolution": "تطور", "examination": "فحص", "exchange": "تبادل", "executive": "تنفيذي", "exercise": "تمرين",
    "exhibition": "معرض", "existence": "وجود", "expansion": "توسع", "expectation": "توقع", "expenditure": "نفقات",
    "experience": "خبرة", "experiment": "تجربة", "expert": "خبير", "explanation": "تفسير", "export": "تصدير",
    "expression": "تعبير", "extension": "امتداد", "extent": "مدى", "facility": "منشأة", "factor": "عامل",
    "failure": "فشل", "feature": "ميزة", "federal": "فيدرالي", "fee": "رسوم", "feedback": "ملاحظات",
    "figure": "رقم", "finding": "نتيجة", "focus": "تركيز", "force": "قوة", "forecast": "توقع",
    "foundation": "مؤسسة", "framework": "إطار", "function": "وظيفة", "fund": "صندوق", "fundamental": "أساسي",
    "funding": "تمويل", "gathering": "تجمع", "goal": "هدف", "goods": "بضائع", "grant": "منحة",
    "growth": "نمو", "guarantee": "ضمان", "guideline": "دليل", "habitat": "موطن", "harm": "ضرر",
    "headquarters": "مقر", "hearing": "جلسة استماع", "height": "ارتفاع", "hierarchy": "تسلسل هرمي", "highlight": "تسليط الضوء",
    "hypothesis": "فرضية", "identity": "هوية", "image": "صورة", "immigration": "هجرة", "impact": "تأثير",
    "implementation": "تنفيذ", "implication": "تداعيات", "import": "استيراد", "impression": "انطباع", "improvement": "تحسن",
    "incentive": "حافز", "incident": "حادث", "indication": "مؤشر", "individual": "فرد", "inequality": "عدم المساواة",
    "inflation": "تضخم", "infrastructure": "بنية تحتية", "initiative": "مبادرة", "innovation": "ابتكار", "input": "مدخلات",
    "inquiry": "استفسار", "insight": "رؤية", "inspection": "تفتيش", "instance": "مثال", "instruction": "تعليمات",
    "insurance": "تأمين", "integration": "تكامل", "integrity": "نزاهة", "interaction": "تفاعل", "interface": "واجهة",
    "interpretation": "تفسير", "intervention": "تدخل", "interview": "مقابلة", "invasion": "غزو", "investigation": "تحقيق",
    "investor": "مستثمر", "issue": "قضية", "item": "عنصر", "journal": "دورية", "journalism": "صحافة",
    "judgment": "حكم", "labor": "عمالة", "lack": "نقص", "landscape": "منظر طبيعي", "launch": "إطلاق",
    "layer": "طبقة", "leadership": "قيادة", "league": "دوري", "legislation": "تشريع", "legislature": "هيئة تشريعية",
    "length": "طول", "link": "رابط", "list": "قائمة", "location": "موقع", "logic": "منطق",
    "loss": "خسارة", "maintenance": "صيانة", "majority": "أغلبية", "management": "إدارة", "manufacturer": "مصنع",
    "margin": "هامش", "mass": "كتلة", "material": "مادة", "matter": "مادة", "maximum": "أقصى",
    "meaning": "معنى", "means": "وسائل", "mechanism": "آلية", "media": "وسائل الإعلام", "medium": "وسط",
    "membership": "عضوية", "memory": "ذاكرة", "message": "رسالة", "migration": "هجرة", "military": "عسكري",
    "minimum": "أدنى", "minority": "أقلية", "minute": "دقيقة", "mission": "مهمة", "mistake": "خطأ",
    "mode": "وضع", "model": "نموذج", "modification": "تعديل", "momentum": "زخم", "monitoring": "مراقبة",
    "motion": "حركة", "motivation": "دافع", "movement": "حركة", "mystery": "غموض", "myth": "أسطورة",
    "narrative": "سرد", "network": "شبكة", "norm": "معيار", "notion": "فكرة", "obligation": "التزام",
    "observation": "ملاحظة", "obstacle": "عائق", "occasion": "مناسبة", "occupation": "مهنة", "occurrence": "حدوث",
    "offense": "جريمة", "oil": "نفط", "operation": "عملية", "opponent": "خصم", "opportunity": "فرصة",
    "opposition": "معارضة", "option": "خيار", "outcome": "نتيجة", "output": "مخرجات", "outline": "مخطط",
    "outlook": "نظرة", "overall": "شامل", "pace": "وتيرة", "package": "حزمة", "panel": "لوحة",
    "participation": "مشاركة", "partner": "شريك", "partnership": "شراكة", "passage": "مقطع", "passion": "شغف",
    "pattern": "نمط", "penalty": "عقوبة", "perception": "إدراك", "personality": "شخصية", "perspective": "منظور",
    "phase": "مرحلة", "phenomenon": "ظاهرة", "philosophy": "فلسفة", "phrase": "عبارة", "planet": "كوكب",
    "pleasure": "متعة", "plot": "حبكة", "pollution": "تلوث", "portion": "جزء", "portrait": "صورة",
    "poverty": "فقر", "practice": "ممارسة", "precedent": "سابقة", "prediction": "توقع", "preference": "تفضيل",
    "premise": "مقدمة", "pressure": "ضغط", "prevention": "وقاية", "principle": "مبدأ", "priority": "أولوية",
    "procedure": "إجراء", "proceeding": "إجراء", "productivity": "إنتاجية", "profession": "مهنة", "profile": "ملف شخصي",
    "programming": "برمجة", "proportion": "نسبة", "proposal": "مقترح", "prospect": "احتمال", "protection": "حماية",
    "protest": "احتجاج", "provider": "مزود", "provision": "توفير", "publication": "نشر", "publicity": "دعاية",
    "purchase": "شراء", "purpose": "غرض", "pursuit": "سعي", "quality": "جودة", "quantity": "كمية",
    "quarter": "ربع", "race": "عرق", "radiation": "إشعاع", "range": "نطاق", "ratio": "نسبة",
    "reaction": "رد فعل", "reader": "قارئ", "reality": "واقع", "realm": "مجال", "reasoning": "استدلال",
    "receipt": "إيصال", "reception": "استقبال", "recipe": "وصفة", "recognition": "اعتراف", "recommendation": "توصية",
    "recovery": "تعافي", "recruitment": "توظيف", "reduction": "تخفيض", "reference": "مرجع", "reform": "إصلاح",
    "refugee": "لاجئ", "region": "منطقة", "registration": "تسجيل", "regulation": "تنظيم", "rehabilitation": "تأهيل",
    "reinforcement": "تعزيز", "rejection": "رفض", "relation": "علاقة", "relationship": "علاقة", "relevance": "صلة",
    "relief": "راحة", "religion": "دين", "remains": "بقايا", "remedy": "علاج", "removal": "إزالة",
    "renaissance": "نهضة", "renewal": "تجديد", "rent": "إيجار", "repair": "إصلاح", "repetition": "تكرار",
    "replacement": "استبدال", "reputation": "سمعة", "request": "طلب", "requirement": "متطلب", "rescue": "إنقاذ",
    "residence": "إقامة", "resident": "مقيم", "resistance": "مقاومة", "resolution": "قرار", "resource": "مورد",
    "respect": "احترام", "response": "استجابة", "responsibility": "مسؤولية", "restoration": "ترميم", "restraint": "قيد",
    "restriction": "تقييد", "retirement": "تقاعد", "retreat": "تراجع", "revenue": "إيرادات", "reverse": "عكس",
    "review": "مراجعة", "revision": "مراجعة", "revolution": "ثورة", "reward": "مكافأة", "rhythm": "إيقاع",
    "risk": "خطر", "ritual": "طقوس", "rivalry": "منافسة", "role": "دور", "romance": "رومانسية",
    "routine": "روتين", "rumor": "شائعة", "sacrifice": "تضحية", "safety": "سلامة", "sanction": "عقوبة",
    "satisfaction": "رضا", "scale": "مقياس", "scandal": "فضيحة", "scenario": "سيناريو", "scene": "مشهد",
    "scheme": "خطة", "scope": "نطاق", "screening": "فحص", "script": "نص", "seal": "ختم",
    "search": "بحث", "sector": "قطاع", "segment": "قطاع", "selection": "اختيار", "self": "ذات",
    "sensation": "إحساس", "sense": "حاسة", "sensitivity": "حساسية", "sequence": "تسلسل", "series": "سلسلة",
    "session": "جلسة", "settlement": "تسوية", "sex": "جنس", "shift": "تحول", "shortage": "نقص",
    "significance": "أهمية", "silence": "صمت", "similarity": "تشابه", "site": "موقع", "skill": "مهارة",
    "slavery": "عبودية", "smell": "رائحة", "smoke": "دخان", "socialism": "اشتراكية", "soil": "تربة",
    "solution": "حل", "source": "مصدر", "sovereignty": "سيادة", "space": "فضاء", "span": "فترة",
    "speaker": "متحدث", "specialist": "أخصائي", "species": "نوع", "specification": "مواصفات", "spectrum": "طيف",
    "speculation": "مضاربة", "speech": "خطاب", "speed": "سرعة", "spirit": "روح", "stability": "استقرار",
    "staff": "موظفون", "stake": "حصة", "standard": "معيار", "standing": "مكانة", "statistics": "إحصائيات",
    "status": "حالة", "statute": "قانون", "steel": "فولاذ", "step": "خطوة", "stock": "مخزون",
    "storage": "تخزين", "strain": "إجهاد", "strand": "خصلة", "stranger": "غريب", "strategic": "استراتيجي",
    "strategy": "استراتيجية", "stream": "تيار", "strength": "قوة", "strike": "إضراب", "string": "سلسلة",
    "structure": "هيكل", "struggle": "نضال", "submission": "تقديم", "substance": "مادة", "substitute": "بديل",
    "suburb": "ضاحية", "success": "نجاح", "succession": "خلافة", "suicide": "انتحار", "summit": "قمة",
    "supervision": "إشراف", "supplement": "ملحق", "supply": "إمداد", "supporter": "مؤيد", "surface": "سطح",
    "surgery": "جراحة", "surplus": "فائض", "surprise": "مفاجأة", "survey": "مسح", "survival": "بقاء",
    "suspect": "مشتبه به", "suspension": "تعليق", "sustainability": "استدامة", "symbol": "رمز", "sympathy": "تعاطف",
    "syndrome": "متلازمة", "synthesis": "تركيب", "target": "هدف", "tariff": "تعريفة", "task": "مهمة",
    "taste": "ذوق", "tax": "ضريبة", "teaspoon": "ملعقة صغيرة", "technique": "تقنية", "teen": "مراهق",
    "temperature": "درجة حرارة", "temple": "معبد", "temporary": "مؤقت", "tendency": "ميل", "tension": "توتر",
    "term": "مصطلح", "territory": "إقليم", "terrorism": "إرهاب", "testimony": "شهادة", "text": "نص",
    "texture": "نسيج", "thanks": "شكر", "theme": "موضوع", "theology": "لاهوت", "therapist": "معالج",
    "thinking": "تفكير", "thread": "خيط", "threat": "تهديد", "threshold": "عتبة", "tide": "مد",
    "timber": "أخشاب", "timing": "توقيت", "tissue": "نسيج", "title": "عنوان", "tolerance": "تسامح",
    "tone": "نبرة", "topic": "موضوع", "torture": "تعذيب", "tourism": "سياحة", "trace": "أثر",
    "track": "مسار", "tradition": "تقليد", "traffic": "مرور", "tragedy": "مأساة", "trait": "سمة",
    "transaction": "معاملة", "transfer": "نقل", "transformation": "تحول", "transition": "انتقال", "translation": "ترجمة",
    "transmission": "نقل", "transportation": "نقل", "treasure": "كنز", "treaty": "معاهدة", "trend": "اتجاه",
    "tribe": "قبيلة", "tribute": "تكريم", "trick": "خدعة", "trouble": "مشكلة", "trunk": "جذع",
    "tube": "أنبوب", "tumor": "ورم", "uncertainty": "عدم يقين", "understanding": "فهم", "unemployment": "بطالة",
    "union": "اتحاد", "unit": "وحدة", "unity": "وحدة", "universe": "كون", "update": "تحديث",
    "upgrade": "ترقية", "urban": "حضري", "usage": "استخدام", "utility": "فائدة", "vacation": "عطلة",
    "valley": "وادي", "validity": "صلاحية", "variation": "تباين", "variety": "تنوع", "vehicle": "مركبة",
    "venture": "مشروع", "version": "نسخة", "vessel": "وعاء", "veteran": "محارب قديم", "vice": "نائب",
    "video": "فيديو", "view": "رأي", "viewer": "مشاهد", "village": "قرية", "violation": "انتهاك",
    "violence": "عنف", "virtue": "فضيلة", "vision": "رؤية", "volume": "حجم", "wage": "أجر",
    "waste": "نفايات", "wave": "موجة", "wealth": "ثروة", "weapon": "سلاح", "welfare": "رفاهية",
    "width": "عرض", "wilderness": "برية", "will": "إرادة", "wing": "جناح", "wisdom": "حكمة",
    "witness": "شاهد", "workshop": "ورشة عمل", "worship": "عبادة", "worth": "قيمة", "wound": "جرح",
    "zone": "منطقة"
}

def translate_database(input_file, output_file):
    """Add Arabic translations to all words in the database"""
    print("🔄 Loading vocabulary database...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        db = json.load(f)
    
    total_words = 0
    translated_count = 0
    already_translated = 0
    
    print("✍️ Translating words...")
    
    for category_key, category_data in db.items():
        words = category_data.get('words', [])
        
        for word_obj in words:
            en = word_obj.get('en', '')
            ar = word_obj.get('ar', '')
            total_words += 1
            
            # Check if already has a proper translation
            if ar and ar != en:
                already_translated += 1
                continue
            
            # Try to find translation
            en_lower = en.lower()
            if en_lower in TRANSLATIONS:
                word_obj['ar'] = TRANSLATIONS[en_lower]
                translated_count += 1
            else:
                # Keep English as fallback
                word_obj['ar'] = en
    
    print(f"\n📊 Translation Statistics:")
    print(f"  • Total words: {total_words}")
    print(f"  • Already translated: {already_translated}")
    print(f"  • Newly translated: {translated_count}")
    print(f"  • Still need translation: {total_words - already_translated - translated_count}")
    print(f"  • Total coverage: {already_translated + translated_count}/{total_words} ({((already_translated + translated_count)/total_words*100):.1f}%)")
    
    # Save updated database
    print(f"\n💾 Saving updated database to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    
    print("✅ Translation complete!")
    return translated_count

if __name__ == '__main__':
    input_file = "_categories_with_arabic.json"
    output_file = "_categories_with_arabic.json"
    
    translated = translate_database(input_file, output_file)
    print(f"\n🎉 Successfully translated {translated} new words!")
