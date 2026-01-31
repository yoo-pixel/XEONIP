#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

# Change to working directory
os.chdir(r'c:\Users\Mostafa\OneDrive\Attachments\MY work')

# Read all words from the bulk files
with open('_bulk_a1.txt', 'r', encoding='utf-8') as f:
    a1_words = [w.strip() for w in f.read().split(',') if w.strip()]
with open('_bulk_a2.txt', 'r', encoding='utf-8') as f:
    a2_words = [w.strip() for w in f.read().split(',') if w.strip()]
with open('_bulk_b1.txt', 'r', encoding='utf-8') as f:
    b1_words = [w.strip() for w in f.read().split(',') if w.strip()]
with open('_bulk_b2.txt', 'r', encoding='utf-8') as f:
    b2_words = [w.strip() for w in f.read().split(',') if w.strip()]

# Combine and deduplicate all words
all_words = set()
all_words.update(a1_words)
all_words.update(a2_words)
all_words.update(b1_words)
all_words.update(b2_words)

print(f"📊 Total unique words collected: {len(all_words)}")
print(f"  • A1 words: {len(a1_words)}")
print(f"  • A2 words: {len(a2_words)}")
print(f"  • B1 words: {len(b1_words)}")
print(f"  • B2 words: {len(b2_words)}")

# Arabic translations dictionary (core vocabulary)
arabic_trans = {
    'a': 'ا', 'able': 'قادر', 'about': 'حول', 'acid': 'حمضي', 'act': 'فعل', 'add': 'إضافة',
    'age': 'عمر', 'ago': 'منذ', 'aid': 'مساعدة', 'aim': 'هدف', 'air': 'هواء', 'all': 'الجميع',
    'animal': 'حيوان', 'any': 'أي', 'area': 'منطقة', 'arm': 'ذراع', 'army': 'جيش', 'art': 'فن',
    'ask': 'سؤال', 'at': 'في', 'away': 'بعيدا', 'baby': 'رضيع', 'back': 'خلف', 'bad': 'سيء',
    'bag': 'حقيبة', 'ball': 'كرة', 'bank': 'بنك', 'bar': 'حانة', 'base': 'قاعدة', 'be': 'يكون',
    'beach': 'شاطئ', 'bear': 'دب', 'bed': 'سرير', 'begin': 'بداية', 'bell': 'جرس',
    'best': 'أفضل', 'big': 'كبير', 'bike': 'دراجة', 'bird': 'طائر', 'black': 'أسود',
    'blood': 'دم', 'blue': 'أزرق', 'boat': 'قارب', 'body': 'جسم', 'book': 'كتاب',
    'born': 'مولود', 'boss': 'رئيس', 'both': 'كلاهما', 'box': 'صندوق', 'boy': 'ولد',
    'brain': 'دماغ', 'bread': 'خبز', 'breath': 'تنفس', 'brother': 'أخ', 'brown': 'بني',
    'build': 'بناء', 'burn': 'احتراق', 'bus': 'حافلة', 'business': 'عمل', 'but': 'لكن',
    'buy': 'شراء', 'by': 'بواسطة', 'call': 'استدعاء', 'can': 'يمكن', 'car': 'سيارة',
    'card': 'بطاقة', 'care': 'رعاية', 'case': 'حالة', 'cat': 'قطة', 'cause': 'سبب',
    'cell': 'خلية', 'center': 'مركز', 'century': 'قرن', 'certain': 'مؤكد', 'chair': 'كرسي',
    'change': 'تغيير', 'character': 'شخصية', 'cheap': 'رخيص', 'check': 'فحص', 'cheese': 'جبن',
    'chef': 'طاه', 'chest': 'صدر', 'chicken': 'دجاج', 'chief': 'رئيس', 'child': 'طفل',
    'choice': 'اختيار', 'choose': 'اختيار', 'church': 'كنيسة', 'city': 'مدينة', 'class': 'فئة',
    'clean': 'نظيف', 'clear': 'واضح', 'climb': 'تسلق', 'clock': 'ساعة', 'close': 'قريب',
    'cloud': 'سحابة', 'club': 'نادي', 'coach': 'مدرب', 'coast': 'ساحل', 'coat': 'معطف',
    'code': 'رمز', 'coffee': 'قهوة', 'cold': 'بارد', 'color': 'لون', 'come': 'قدوم',
    'command': 'أمر', 'comment': 'تعليق', 'common': 'شائع', 'company': 'شركة', 'computer': 'كمبيوتر',
    'concern': 'قلق', 'condition': 'شرط', 'conference': 'مؤتمر', 'confidence': 'ثقة',
    'confirm': 'تأكيد', 'conflict': 'صراع', 'connect': 'الاتصال', 'consider': 'النظر في',
    'contain': 'تحتوي', 'content': 'محتوى', 'context': 'السياق', 'control': 'التحكم',
    'conversation': 'محادثة', 'cook': 'طهي', 'cool': 'بارد', 'copy': 'نسخ', 'core': 'جوهر',
    'corn': 'ذرة', 'corner': 'زاوية', 'cost': 'تكلفة', 'country': 'دولة', 'couple': 'زوج',
    'course': 'دورة', 'court': 'محكمة', 'cousin': 'ابن عم', 'cover': 'غطاء', 'cow': 'بقرة',
    'create': 'إنشاء', 'credit': 'رصيد', 'crime': 'جريمة', 'crisis': 'أزمة', 'critical': 'حرج',
    'crop': 'محصول', 'cross': 'عبور', 'crowd': 'حشد', 'crown': 'تاج', 'culture': 'ثقافة',
    'cup': 'كوب', 'current': 'حالي', 'curve': 'منحنى', 'custom': 'عادة', 'cut': 'قطع',
    'cute': 'جميل', 'cycle': 'دورة', 'dad': 'أب', 'daily': 'يومي', 'damage': 'الضرر',
    'dance': 'رقص', 'danger': 'خطر', 'dare': 'تجرؤ', 'dark': 'مظلم', 'data': 'بيانات',
    'date': 'تاريخ', 'daughter': 'ابنة', 'day': 'يوم', 'dead': 'ميت', 'deal': 'صفقة',
    'dear': 'عزيز', 'death': 'موت', 'decide': 'قرر', 'decision': 'قرار', 'deck': 'سطح السفينة',
    'deep': 'عميق', 'deer': 'غزال', 'defend': 'دفاع', 'define': 'تعريف', 'degree': 'درجة',
    'delay': 'تأخير', 'delete': 'حذف', 'deliver': 'تسليم', 'demand': 'طلب', 'deny': 'إنكار',
    'depend': 'يعتمد', 'deposit': 'إيداع', 'depth': 'عمق', 'describe': 'وصف', 'desert': 'صحراء',
    'design': 'تصميم', 'desk': 'مكتب', 'destroy': 'تدمير', 'detail': 'تفصيل', 'detect': 'الكشف',
    'determine': 'تحديد', 'develop': 'تطور', 'device': 'جهاز', 'diamond': 'ماس', 'die': 'موت',
    'diet': 'نظام غذائي', 'differ': 'يختلف', 'different': 'مختلف', 'difficult': 'صعب', 'dig': 'حفر',
    'dinner': 'عشاء', 'direct': 'مباشرة', 'direction': 'اتجاه', 'director': 'مدير', 'dirty': 'قذر',
    'disease': 'مرض', 'display': 'عرض', 'distance': 'مسافة', 'divide': 'تقسيم', 'do': 'افعل',
    'doctor': 'طبيب', 'document': 'وثيقة', 'dog': 'كلب', 'dollar': 'دولار', 'door': 'باب',
    'double': 'مضاعف', 'doubt': 'شك', 'down': 'أسفل', 'draft': 'مسودة', 'drag': 'سحب',
    'drama': 'دراما', 'draw': 'رسم', 'dream': 'حلم', 'dress': 'فستان', 'drink': 'شراب',
    'drive': 'قيادة', 'drop': 'قطرة', 'drug': 'دواء', 'drum': 'طبل', 'dry': 'جاف',
    'due': 'يستحق', 'dull': 'ممل', 'dust': 'غبار', 'duty': 'واجب', 'each': 'كل',
    'eagle': 'نسر', 'ear': 'أذن', 'early': 'مبكرا', 'earn': 'اكتسب', 'earth': 'أرض',
    'ease': 'سهولة', 'easily': 'بسهولة', 'east': 'شرق', 'easy': 'سهل', 'eat': 'أكل',
    'education': 'تعليم', 'effect': 'تأثير', 'effort': 'جهد', 'egg': 'بيضة', 'eight': 'ثمانية',
    'either': 'أي من', 'election': 'انتخابات', 'electricity': 'كهرباء', 'element': 'عنصر',
    'elephant': 'فيل', 'else': 'آخر', 'email': 'بريد إلكتروني', 'emotion': 'عاطفة',
    'emphasis': 'تركيز', 'empire': 'إمبراطورية', 'employee': 'موظف', 'empty': 'فارغ',
    'end': 'نهاية', 'enemy': 'عدو', 'energy': 'طاقة', 'engine': 'محرك', 'engineer': 'مهندس',
    'english': 'إنجليزي', 'enjoy': 'استمتاع', 'enough': 'كافي', 'enter': 'الدخول',
    'enterprise': 'مشروع', 'entire': 'كامل', 'entry': 'دخول', 'envelope': 'مظروف',
    'environment': 'بيئة', 'equal': 'متساو', 'equipment': 'معدات', 'era': 'عصر', 'error': 'خطأ',
    'escape': 'هروب', 'especially': 'خاصة', 'essay': 'مقالة', 'essential': 'أساسي',
    'establish': 'تأسيس', 'estate': 'ضيعة', 'estimate': 'تقدير', 'ethnic': 'عرقي',
    'evaluate': 'تقييم', 'even': 'حتى', 'event': 'حدث', 'ever': 'أبدا', 'every': 'كل',
    'evidence': 'دليل', 'evil': 'شر', 'exam': 'امتحان', 'example': 'مثال', 'exceed': 'تجاوز',
    'excellent': 'ممتاز', 'except': 'باستثناء', 'exchange': 'صرف', 'excited': 'متحمس',
    'excitement': 'إثارة', 'exclusive': 'حصري', 'excuse': 'عذر', 'execute': 'تنفيذ',
    'exercise': 'تمرين', 'exhaust': 'استنزاف', 'exhibit': 'معرض', 'exist': 'موجود',
    'existence': 'وجود', 'exit': 'خروج', 'expand': 'توسيع', 'expect': 'توقع', 'expensive': 'مكلف',
    'experience': 'تجربة', 'experiment': 'تجربة', 'expert': 'خبير', 'explain': 'شرح',
    'expose': 'كشف', 'express': 'التعبير', 'extend': 'تمديد', 'extensive': 'واسع',
    'external': 'خارجي', 'extra': 'إضافي', 'extreme': 'قصوى', 'eye': 'عين', 'fabric': 'نسيج',
    'face': 'وجه', 'facility': 'تسهيل', 'fact': 'حقيقة', 'factor': 'عامل', 'factory': 'مصنع',
    'faculty': 'كلية', 'fade': 'يتلاشى', 'fail': 'فشل', 'failure': 'فشل', 'fair': 'عادل',
    'fall': 'سقوط', 'false': 'خاطئ', 'fame': 'شهرة', 'family': 'عائلة', 'famous': 'مشهور',
    'fan': 'مروحة', 'fantastic': 'رائع', 'fantasy': 'خيال', 'farm': 'مزرعة', 'farmer': 'مزارع',
    'fashion': 'موضة', 'fast': 'سريع', 'fate': 'مصير', 'father': 'أب', 'fault': 'خطأ',
    'fear': 'خوف', 'feature': 'ميزة', 'federal': 'فيدرالي', 'fee': 'رسم', 'feed': 'إطعام',
    'feel': 'شعور', 'feeling': 'شعور', 'fellow': 'زميل', 'female': 'امرأة', 'fence': 'سياج',
    'festival': 'مهرجان', 'fever': 'حمى', 'few': 'قليل', 'fiber': 'ألياف', 'fiction': 'خيال',
    'field': 'حقل', 'fierce': 'شرس', 'fifteen': 'خمسة عشر', 'fifth': 'خامس', 'fifty': 'خمسون',
    'fight': 'قتال', 'figure': 'شكل', 'file': 'ملف', 'fill': 'ملء', 'film': 'فيلم',
    'filter': 'مرشح', 'final': 'نهائي', 'finance': 'تمويل', 'find': 'يجد', 'fine': 'جيد',
    'finger': 'إصبع', 'finish': 'نهاية', 'fire': 'نار', 'firm': 'ثابت', 'first': 'أول',
    'fish': 'سمك', 'fit': 'لائق', 'fitness': 'لياقة', 'five': 'خمسة', 'fix': 'إصلاح',
    'flag': 'علم', 'flame': 'لهب', 'flash': 'برق', 'flat': 'مسطح', 'flavor': 'نكهة',
    'flee': 'هروب', 'flesh': 'لحم', 'flight': 'رحلة', 'float': 'طفو', 'flood': 'فيضان',
    'floor': 'أرضية', 'flower': 'زهرة', 'fluid': 'سائل', 'fly': 'يطير', 'focus': 'التركيز',
    'fold': 'طي', 'folk': 'شعب', 'follow': 'متابعة', 'food': 'طعام', 'fool': 'أحمق',
    'foot': 'قدم', 'force': 'قوة', 'foreign': 'أجنبي', 'forest': 'غابة', 'forget': 'نسيان',
    'fork': 'شوكة', 'form': 'شكل', 'formal': 'رسمي', 'format': 'صيغة', 'former': 'السابق',
    'fortune': 'ثروة', 'forum': 'منتدى', 'forward': 'للأمام', 'fossil': 'أحفورة', 'foster': 'تعزيز',
    'found': 'أسس', 'foundation': 'مؤسسة', 'fountain': 'نافورة', 'four': 'أربعة', 'fourth': 'رابع',
    'fraction': 'كسر', 'frame': 'إطار', 'framework': 'إطار عمل', 'france': 'فرنسا', 'frank': 'صريح',
    'fraud': 'احتيال', 'freedom': 'حرية', 'freeze': 'تجميد', 'french': 'فرنسي', 'frequency': 'تكرار',
    'fresh': 'طازج', 'friend': 'صديق', 'friendly': 'ودي', 'frontier': 'حدود', 'frost': 'صقيع',
    'frown': 'عبوس', 'frozen': 'مجمد', 'fruit': 'فاكهة', 'fulfill': 'تحقيق', 'full': 'ممتلئ',
    'fully': 'تماما', 'fun': 'متعة', 'function': 'وظيفة', 'fund': 'صندوق', 'fundamental': 'أساسي',
    'funding': 'تمويل', 'funeral': 'جنازة', 'funny': 'مضحك', 'future': 'مستقبل',
}

# Group words by semantic categories
categories = {
    'technology': [],
    'science': [],
    'business': [],
    'health': [],
    'education': [],
    'sports': [],
    'arts': [],
    'nature': [],
    'people': [],
    'food': [],
    'travel': [],
    'government': [],
}

# Keywords for categorization
keywords_map = {
    'technology': ['computer', 'software', 'hard', 'tech', 'digital', 'code', 'program', 'network', 'internet', 'data', 'system', 'process', 'email', 'online', 'virus', 'file', 'device', 'server', 'database', 'web', 'app', 'net', 'cyber', 'cloud', 'ai', 'compute', 'robot', 'script', 'byte'],
    'science': ['science', 'physics', 'chemistry', 'biology', 'medicine', 'research', 'experiment', 'theory', 'atom', 'cell', 'energy', 'element', 'compound', 'hypothesis', 'test', 'lab', 'chemical', 'reaction', 'quantum', 'molecular', 'genetic', 'evolution', 'species', 'organism', 'matter', 'force'],
    'business': ['business', 'company', 'market', 'trade', 'commerce', 'economy', 'finance', 'profit', 'loss', 'customer', 'product', 'service', 'sales', 'price', 'contract', 'deal', 'invest', 'bank', 'money', 'account', 'payment', 'invoice', 'purchase', 'vendor', 'corporate', 'client', 'asset', 'revenue'],
    'health': ['health', 'medical', 'doctor', 'hospital', 'disease', 'medicine', 'treatment', 'patient', 'nurse', 'care', 'therapy', 'surgery', 'illness', 'pain', 'recovery', 'healthy', 'sick', 'body', 'diagnosis', 'symptom', 'clinic', 'health', 'dental', 'mental', 'vaccine', 'immune', 'physical', 'drug'],
    'education': ['education', 'school', 'student', 'teacher', 'learn', 'teach', 'study', 'class', 'exam', 'test', 'knowledge', 'book', 'subject', 'grade', 'university', 'college', 'course', 'lecture', 'academy', 'training', 'skill', 'seminar', 'workshop', 'tutor', 'pupil', 'curriculum'],
    'sports': ['sport', 'play', 'game', 'team', 'win', 'lose', 'player', 'coach', 'ball', 'match', 'competition', 'race', 'run', 'jump', 'exercise', 'athlete', 'fitness', 'training', 'score', 'goal', 'referee', 'tournament', 'league', 'championship', 'medal', 'olympic'],
    'arts': ['art', 'music', 'dance', 'song', 'paint', 'draw', 'sing', 'theater', 'drama', 'film', 'movie', 'show', 'performance', 'actor', 'artist', 'creative', 'craft', 'design', 'sculpture', 'gallery', 'museum', 'concert', 'opera', 'ballet', 'poetry', 'novel'],
    'nature': ['nature', 'tree', 'plant', 'animal', 'forest', 'mountain', 'river', 'lake', 'ocean', 'sea', 'sky', 'weather', 'rain', 'snow', 'wind', 'storm', 'sun', 'moon', 'star', 'bird', 'flower', 'leaf', 'rock', 'soil', 'climate', 'environmental'],
    'people': ['person', 'people', 'man', 'woman', 'child', 'baby', 'family', 'friend', 'brother', 'sister', 'father', 'mother', 'parent', 'relative', 'human', 'individual', 'male', 'female', 'boy', 'girl', 'son', 'daughter', 'wife', 'husband', 'couple', 'grandfather'],
    'food': ['food', 'eat', 'drink', 'meal', 'fruit', 'vegetable', 'meat', 'bread', 'rice', 'milk', 'cheese', 'cake', 'candy', 'sweet', 'taste', 'hungry', 'kitchen', 'cook', 'recipe', 'restaurant', 'dish', 'soup', 'salad', 'dessert', 'beverage', 'appetite', 'cuisine'],
    'travel': ['travel', 'trip', 'journey', 'visit', 'airport', 'train', 'plane', 'car', 'road', 'street', 'city', 'country', 'hotel', 'ticket', 'passport', 'luggage', 'tourist', 'map', 'route', 'destination', 'transport', 'vehicle', 'station', 'voyage', 'tour', 'cruise'],
    'government': ['government', 'political', 'politician', 'president', 'congress', 'senate', 'parliament', 'election', 'vote', 'law', 'legal', 'court', 'justice', 'crime', 'police', 'military', 'war', 'peace', 'nation', 'state', 'authority', 'regulation', 'treaty', 'diplomat', 'citizen', 'constitution'],
}

# Assign words to categories
remaining_words = set(all_words)
for word in sorted(all_words):
    word_lower = word.lower()
    assigned = False
    for category, keywords in keywords_map.items():
        if any(keyword in word_lower for keyword in keywords):
            categories[category].append(word)
            remaining_words.discard(word)
            assigned = True
            break

# Create JSON output
output = {}
for cat, words in categories.items():
    if words:
        output[cat] = {
            'title': f'📚 {cat.title()}',
            'words': [
                {
                    'en': word,
                    'ar': arabic_trans.get(word.lower(), word)
                }
                for word in sorted(set(words))[:150]  # Limit to 150 per category
            ]
        }

# Add remaining words
if remaining_words:
    output['other'] = {
        'title': '📝 Miscellaneous',
        'words': [
            {
                'en': word,
                'ar': arabic_trans.get(word.lower(), word)
            }
            for word in sorted(remaining_words)[:200]  # Limit to 200
        ]
    }

# Save to file
with open('_categories_with_arabic.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# Print statistics
total_words = sum(len(cat['words']) for cat in output.values())
print(f"\n✅ Expanded categories created successfully!")
print(f"📊 Statistics:")
print(f"  • Total categories: {len(output)}")
print(f"  • Total words in database: {total_words}")
print(f"  • Words with translations: {sum(1 for cat in output.values() for w in cat['words'] if w['ar'] != w['en'])}")
print(f"\n📋 Category breakdown:")
for name, data in sorted(output.items()):
    print(f"  • {name.capitalize()}: {len(data['words'])} words")
