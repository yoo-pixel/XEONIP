#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

os.chdir(r'c:\Users\Mostafa\OneDrive\Attachments\MY work')

# Read all words
with open('_bulk_a1.txt', 'r', encoding='utf-8') as f:
    a1_words = [w.strip() for w in f.read().split(',') if w.strip()]
with open('_bulk_a2.txt', 'r', encoding='utf-8') as f:
    a2_words = [w.strip() for w in f.read().split(',') if w.strip()]
with open('_bulk_b1.txt', 'r', encoding='utf-8') as f:
    b1_words = [w.strip() for w in f.read().split(',') if w.strip()]
with open('_bulk_b2.txt', 'r', encoding='utf-8') as f:
    b2_words = [w.strip() for w in f.read().split(',') if w.strip()]

all_words = set()
all_words.update(a1_words)
all_words.update(a2_words)
all_words.update(b1_words)
all_words.update(b2_words)

print(f"📊 Processing {len(all_words)} unique words...\n")

# Comprehensive Arabic translations
translations = {
    # A1 Common
    'a': 'ا', 'able': 'قادر', 'about': 'عن', 'acid': 'حمضي', 'act': 'فعل', 'add': 'أضاف', 'age': 'عمر',
    'ago': 'منذ', 'aid': 'مساعدة', 'aim': 'هدف', 'air': 'هواء', 'all': 'الكل', 'also': 'أيضا', 'and': 'و',
    'animal': 'حيوان', 'another': 'آخر', 'any': 'أي', 'area': 'منطقة', 'argue': 'جادل', 'arm': 'ذراع',
    'army': 'جيش', 'art': 'فن', 'ask': 'سأل', 'at': 'في', 'away': 'بعيدا', 'baby': 'رضيع', 'back': 'خلف',
    'bad': 'سيء', 'bag': 'حقيبة', 'ball': 'كرة', 'band': 'فرقة', 'bank': 'بنك', 'bar': 'حانة', 'base': 'قاعدة',
    'be': 'يكون', 'beach': 'شاطئ', 'bear': 'دب', 'beat': 'ضرب', 'bed': 'سرير', 'beer': 'بيرة', 'before': 'قبل',
    'begin': 'بدأ', 'bell': 'جرس', 'belt': 'حزام', 'bend': 'ثني', 'best': 'أفضل', 'better': 'أحسن', 'between': 'بين',
    'bicycle': 'دراجة', 'bid': 'عرض', 'big': 'كبير', 'bike': 'دراجة', 'bill': 'فاتورة', 'bird': 'طائر',
    'birth': 'ميلاد', 'black': 'أسود', 'blade': 'شفرة', 'blood': 'دم', 'blow': 'نفخ', 'blue': 'أزرق',
    'board': 'لوحة', 'boat': 'قارب', 'body': 'جسم', 'boil': 'غلي', 'bold': 'جريء', 'bond': 'رابطة',
    'bone': 'عظم', 'book': 'كتاب', 'boost': 'دفعة', 'border': 'حدود', 'born': 'مولود', 'boss': 'رئيس',
    'both': 'كلاهما', 'bottle': 'زجاجة', 'bottom': 'قاع', 'bounce': 'ارتداد', 'bow': 'انحناء', 'bowl': 'وعاء',
    'box': 'صندوق', 'boy': 'ولد', 'brain': 'دماغ', 'brake': 'فرامل', 'branch': 'فرع', 'brand': 'ماركة',
    'brass': 'نحاس', 'brave': 'شجاع', 'bread': 'خبز', 'break': 'كسر', 'breast': 'صدر', 'breath': 'نفس',
    'breathe': 'تنفس', 'breed': 'سلالة', 'brick': 'طوب', 'bridge': 'جسر', 'brief': 'قصير', 'bright': 'مشرق',
    'bring': 'احضر', 'brink': 'حافة', 'brisk': 'نشيط', 'broad': 'واسع', 'broke': 'كسر', 'broken': 'مكسور',
    'bronze': 'برونز', 'brother': 'أخ', 'brown': 'بني', 'brush': 'فرشاة', 'bubble': 'فقاعة', 'buck': 'ذكر',
    'budget': 'ميزانية', 'bug': 'حشرة', 'build': 'بناء', 'bulk': 'حجم', 'bullet': 'رصاصة', 'bundle': 'حزمة',
    'burden': 'عبء', 'burn': 'احترق', 'burst': 'انفجر', 'bury': 'دفن', 'bush': 'شجيرة', 'business': 'عمل',
    'busy': 'مشغول', 'but': 'لكن', 'butter': 'زبدة', 'button': 'زر', 'buy': 'شراء', 'by': 'بواسطة',
    'buzz': 'طنين', 'bye': 'وداعا', 'cable': 'كابل', 'cage': 'قفص', 'cake': 'كعكة', 'call': 'اتصال',
    'calm': 'هادئ', 'came': 'جاء', 'camera': 'كاميرا', 'camp': 'معسكر', 'can': 'يمكن', 'canal': 'قناة',
    'cancel': 'إلغاء', 'candy': 'حلوى', 'candle': 'شمعة', 'cannon': 'مدفع', 'cannot': 'لا يمكن', 'canvas': 'كنفاس',
    'canyon': 'كانيون', 'cap': 'غطاء', 'cape': 'رأس', 'capital': 'عاصمة', 'card': 'بطاقة', 'care': 'رعاية',
    'career': 'مسيرة', 'cargo': 'شحنة', 'carpet': 'سجادة', 'carriage': 'عربة', 'carrier': 'ناقل', 'carry': 'حمل',
    'cart': 'عربة', 'case': 'حالة', 'cash': 'نقد', 'cast': 'صب', 'castle': 'قلعة', 'casual': 'عارض',
    'cat': 'قطة', 'catalog': 'فهرس', 'catch': 'امسك', 'category': 'فئة', 'cause': 'سبب', 'caution': 'احذر',
    'cave': 'كهف', 'cease': 'توقف', 'ceiling': 'سقف', 'celebrate': 'احتفل', 'cell': 'خلية', 'cement': 'أسمنت',
    'cemetery': 'مقبرة', 'census': 'تعداد', 'center': 'مركز', 'century': 'قرن', 'cereal': 'حبوب', 'certain': 'مؤكد',
    'certificate': 'شهادة', 'chain': 'سلسلة', 'chair': 'كرسي', 'chalk': 'طباشير', 'challenge': 'تحدي', 'chamber': 'غرفة',
    'champion': 'بطل', 'chance': 'فرصة', 'change': 'تغيير', 'channel': 'قناة', 'chaos': 'فوضى', 'chapel': 'كنيسة',
    'chapter': 'فصل', 'character': 'شخصية', 'charge': 'شحنة', 'charm': 'سحر', 'chart': 'رسم', 'chase': 'ملاحقة',
    'cheap': 'رخيص', 'cheat': 'غش', 'check': 'فحص', 'cheek': 'خد', 'cheer': 'هتاف', 'cheese': 'جبن',
    'chef': 'طاه', 'chemical': 'كيميائي', 'cherry': 'كرز', 'chess': 'شطرنج', 'chest': 'صدر', 'chew': 'مضغ',
    'chicken': 'دجاج', 'chief': 'رئيس', 'child': 'طفل', 'chill': 'برد', 'chilly': 'بارد', 'chime': 'جرس',
    'chin': 'ذقن', 'china': 'الصين', 'chip': 'قطعة', 'choice': 'اختيار', 'choir': 'جوقة', 'choke': 'اختناق',
    'choose': 'اختار', 'chop': 'قطع', 'chord': 'وتر', 'chore': 'مهمة', 'church': 'كنيسة', 'cider': 'سيدر',
    'cigar': 'سيجار', 'cigarette': 'سيجارة', 'circle': 'دائرة', 'circuit': 'دائرة كهربية', 'circular': 'دائري',
    'circulate': 'دوران', 'circumstance': 'ظرف', 'circus': 'سيرك', 'citizen': 'مواطن', 'city': 'مدينة', 'civic': 'مدني',
    'civil': 'مدني', 'civilian': 'مدني', 'claim': 'ادعاء', 'clamp': 'مشبك', 'clan': 'عشيرة', 'clap': 'صفقة',
    'clarify': 'توضيح', 'clarity': 'وضوح', 'clash': 'تصادم', 'class': 'فئة', 'classic': 'كلاسيكي', 'classify': 'تصنيف',
    'classroom': 'فصل دراسي', 'clause': 'بند', 'claw': 'مخلب', 'clay': 'طين', 'clean': 'نظيف', 'clear': 'واضح',
    'clearly': 'بوضوح', 'clerk': 'كاتب', 'clever': 'ذكي', 'click': 'نقرة', 'client': 'عميل', 'cliff': 'جرف',
    'climate': 'مناخ', 'climb': 'تسلق', 'cling': 'التصق', 'clinic': 'عيادة', 'clip': 'مشبك', 'cloak': 'عباءة',
    'clock': 'ساعة', 'clog': 'تسد', 'clone': 'استنساخ', 'close': 'قريب', 'closely': 'بقرب', 'closet': 'خزانة',
    'closure': 'إغلاق', 'cloth': 'قماش', 'clothe': 'الملابس', 'clothes': 'ملابس', 'clothing': 'الملابس', 'cloud': 'سحابة',
    'cloudy': 'غائم', 'clove': 'قرنفل', 'clown': 'مهرج', 'club': 'نادي', 'clue': 'تلميح', 'clump': 'كتلة',
    'clumsy': 'أخرق', 'cluster': 'مجموعة', 'clutch': 'قبضة', 'clutter': 'فوضى', 'coach': 'مدرب', 'coal': 'فحم',
    'coalition': 'تحالف', 'coarse': 'خشن', 'coast': 'ساحل', 'coastal': 'ساحلي', 'coat': 'معطف', 'coating': 'طلاء',
    'coax': 'إغراء', 'cobalt': 'كوبالت', 'cobra': 'كوبرا', 'cobweb': 'شبكة العنكبوت', 'cocaine': 'كوكايين', 'cock': 'ديك',
    'cocktail': 'كوكتيل', 'cocoa': 'كاكاو', 'coconut': 'جوز الهند', 'cod': 'سمك القد', 'code': 'رمز', 'codec': 'برنامج ترميز',
    'codeine': 'كودايين', 'codon': 'كودون', 'coerce': 'إجبار', 'coercion': 'إجبار', 'coexist': 'تعايش', 'coffee': 'قهوة',
    'coffer': 'تابوت', 'coffin': 'تابوت', 'cog': 'ترس', 'cognac': 'كونياك', 'cognate': 'مرتبط', 'cognition': 'إدراك',
    'cognitive': 'معرفي', 'cognizance': 'علم', 'cognizant': 'عالم', 'cognomen': 'اسم', 'cognoscenti': 'الخبراء',
    'cogwheel': 'عجلة مسننة', 'cohabit': 'المعاشرة', 'cohabitation': 'معاشرة', 'cohabitee': 'شريك', 'coheir': 'شريك وريث',
    'coheirs': 'شركاء وريث', 'cohere': 'التصاق', 'coherence': 'اتساق', 'coherent': 'متسق', 'cohesion': 'تماسك',
    'cohesive': 'متماسك', 'cohesively': 'بتماسك', 'cohesiveness': 'تماسك', 'coho': 'سلمون', 'cohobate': 'تقطير',
    'cohobation': 'تقطير', 'cohog': 'محار', 'cohort': 'جماعة', 'cohost': 'مضيف مشارك', 'coif': 'غطاء الرأس',
    'coiffeur': 'حلاق', 'coiffure': 'تسريحة', 'coign': 'زاوية', 'coil': 'ملف', 'coiled': 'ملفوف', 'coin': 'عملة',
    'coinage': 'سك النقود', 'coincide': 'توافق', 'coincidence': 'صدفة', 'coincident': 'متزامن', 'coincidental': 'صدفة',
    'coincidentally': 'بالصدفة', 'coiner': 'سك', 'coir': 'جوز الهند', 'coit': 'كويت', 'coitus': 'جماع', 'coke': 'كوك',
    'col': 'تمرير', 'cola': 'كولا', 'colander': 'مصفاة', 'colander': 'مصفاة', 'cold': 'بارد', 'coldly': 'ببرود',
    'coldness': 'برودة', 'cole': 'كرنب', 'coleopteran': 'جعل', 'coles': 'الملفوف', 'coleslaw': 'سلطة الملفوف',
    'coley': 'سمك', 'colic': 'مغص', 'colicky': 'مغصي', 'coliseum': 'كولوسيوم', 'colitis': 'التهاب القولون',
    'collaborate': 'تعاون', 'collaboration': 'تعاون', 'collaborationist': 'متعاون', 'collaborative': 'تعاوني',
    'collaborator': 'متعاون', 'collage': 'كولاج', 'collagen': 'الكولاجين', 'collapse': 'انهيار', 'collapsible': 'قابل للطي',
    'collar': 'ياقة', 'collarband': 'شريط الياقة', 'collarbone': 'عظم الترقوة', 'collard': 'كرنب', 'collars': 'ياقات',
    'collate': 'ترتيب', 'collateral': 'ضمان', 'collaterally': 'بشكل جانبي', 'collation': 'ترتيب', 'colleague': 'زميل',
    'colleagues': 'زملاء', 'collect': 'جمع', 'collected': 'محصول', 'collectedly': 'بهدوء', 'collectible': 'قابل للجمع',
    'collection': 'مجموعة', 'collective': 'جماعي', 'collectively': 'بشكل جماعي', 'collectiveness': 'طبيعة جماعية',
    'collectivism': 'الجماعية', 'collectivist': 'جماعي', 'collectivistic': 'جماعي', 'collectivity': 'جماعة',
    'collector': 'جامع', 'collectorship': 'منصب', 'colleen': 'فتاة', 'college': 'كلية', 'collegial': 'جماعي',
    'collegiality': 'زمالة', 'collegian': 'طالب', 'collegians': 'طلاب', 'colleges': 'كليات', 'collegium': 'كلية',
    'collide': 'تصادم', 'collider': 'محطم', 'collie': 'كلب', 'collier': 'عامل فحم', 'colliery': 'منجم فحم',
    'colliers': 'عمال فحم', 'colligate': 'ربط', 'colligation': 'ربط', 'collimate': 'محاذاة', 'collimator': 'محاذاة',
    'collimators': 'محاذاة', 'collinear': 'خطي', 'collinearity': 'خطية', 'collision': 'تصادم', 'collisions': 'تصادمات',
    'collocate': 'موضع', 'collocation': 'موضع', 'colloid': 'غروي', 'colloidal': 'غروي', 'colloids': 'غرويات',
    'collop': 'شريحة لحم', 'colloquial': 'محاوري', 'colloquialism': 'تعبير عامي', 'colloquially': 'بشكل محاوري',
    'colloquies': 'محادثات', 'colloquist': 'محاور', 'colloquium': 'ندوة', 'colloquy': 'محادثة', 'collotype': 'نوع طباعة',
    'collude': 'تآمر', 'colluder': 'متآمر', 'collusive': 'تآمري', 'collusively': 'بشكل تآمري', 'collusory': 'تآمري',
    'colluvium': 'رواسب', 'collyrium': 'دواء للعين', 'collywobbles': 'أرق', 'colocynth': 'تفاح العلقم', 'colog': 'عطر',
    'cologne': 'كولونيا', 'colombian': 'كولومبي', 'colon': 'القولون', 'colonel': 'عقيد', 'colonelcy': 'رتبة عقيد',
    'colonial': 'استعماري', 'colonialism': 'الاستعمار', 'colonialist': 'استعماري', 'colonialistic': 'استعماري',
    'colonially': 'بشكل استعماري', 'colonic': 'قولوني', 'colonies': 'مستعمرات', 'colonist': 'مستعمر', 'colonitis': 'التهاب',
    'colonization': 'استعمار', 'colonize': 'استعمر', 'colonized': 'مستعمر', 'colonizer': 'محتل', 'colonnade': 'رواق',
    'colonnades': 'أروقة', 'colonoscope': 'منظار', 'colonoscopy': 'فحص', 'colony': 'مستعمرة', 'colophon': 'ختم',
    'color': 'لون', 'colorado': 'كولورادو', 'coloradoan': 'كولورادي', 'colorant': 'صبغ', 'colorants': 'صبغات',
    'colorate': 'ملون', 'coloration': 'تلوين', 'coloratura': 'ألحان', 'coloratura': 'ألحان', 'colorature': 'ألحان',
    'colorblind': 'عمى ألوان', 'colorblindness': 'عمى ألوان', 'colored': 'ملون', 'colorer': 'ملون', 'colorfast': 'ثابت اللون',
    'colorimetry': 'قياس اللون', 'coloring': 'تلوين', 'colorings': 'تلوينات', 'colorist': 'ملون', 'coloristic': 'لوني',
    'colorize': 'تلوين', 'colorized': 'ملون', 'colorless': 'بلا لون', 'colorlessly': 'بدون لون', 'colorlessness': 'عدم وجود لون',
    'colorway': 'مزيج لوني', 'colors': 'ألوان', 'colossal': 'ضخم', 'colossally': 'بشكل ضخم', 'colossi': 'عمالقة',
    'colossus': 'عملاق', 'colostomy': 'فتحة', 'colostrum': 'حليب أول', 'colour': 'لون', 'coloured': 'ملون',
    'colourer': 'ملون', 'colourfast': 'ثابت اللون', 'colouring': 'تلوين', 'colourings': 'تلوينات', 'colourist': 'ملون',
    'colouristic': 'لوني', 'colourize': 'تلوين', 'colourized': 'ملون', 'colourless': 'بلا لون', 'colourlessly': 'بدون لون',
    'colourlessness': 'عدم وجود لون', 'colourway': 'مزيج لوني', 'colours': 'ألوان', 'colourway': 'مزيج لوني',
    'colt': 'مهر', 'coltish': 'مثل المهر', 'coltishly': 'مثل المهر', 'coltishness': 'صفة المهر', 'colts': 'مهور',
    'coltsfoot': 'أفيون', 'coluber': 'ثعبان', 'colubriform': 'مثل الثعبان', 'colubrine': 'ثعبان', 'columba': 'حمامة',
    'columbaria': 'حمام', 'columbary': 'حمام', 'columbine': 'زهرة', 'columbium': 'نيوبيوم', 'columbus': 'كولومبوس',
    'columbuses': 'مكتشفون', 'columel': 'عمود', 'columella': 'عمود صغير', 'columellar': 'عمودي', 'columellate': 'عمودي',
    'column': 'عمود', 'columnar': 'عمودي', 'columnaris': 'مرض', 'columnation': 'عمود', 'columniform': 'عمودي',
    'columnist': 'كاتب عمود', 'columnists': 'كتاب أعمدة', 'columns': 'أعمدة', 'colure': 'دائرة', 'colures': 'دوائر',
    'colza': 'السلجم', 'coma': 'غيبوبة', 'comalike': 'مثل الغيبوبة', 'comae': 'شعر', 'comaker': 'شريك', 'comas': 'غيبوبات',
    'comatose': 'غيبوبة', 'comatosely': 'بغيبوبة', 'comatoseness': 'حالة غيبوبة', 'comatous': 'غيبوبة', 'comb': 'مشط',
    'combat': 'قتال', 'combatant': 'محارب', 'combatants': 'محاربون', 'combate': 'قتال', 'combated': 'قوتل',
    'combater': 'محارب', 'combating': 'قتال', 'combats': 'قتالات', 'combative': 'حربي', 'combatively': 'بشكل حربي',
    'combativeness': 'روح حربية', 'combed': 'مشطوط', 'comber': 'مشط', 'combers': 'مشاطون', 'combflower': 'زهرة', 'combing': 'مشط',
    'combings': 'مشاطة', 'combination': 'مزيج', 'combinational': 'مزيجي', 'combinations': 'مزائج', 'combinative': 'مزيجي',
    'combinatorial': 'توليفي', 'combinatorially': 'بشكل توليفي', 'combinatorics': 'التوليفات', 'combine': 'ادمج',
    'combined': 'مدمج', 'combinedly': 'بشكل مدمج', 'combiner': 'دامج', 'combiners': 'دامجون', 'combines': 'يدمج',
    'combings': 'مشاطة', 'combining': 'دمج', 'combo': 'مزيج', 'combos': 'مزائج', 'combs': 'مشاطات', 'comby': 'مشطوط',
    'combustibility': 'قابلية الاشتعال', 'combustible': 'قابل للاشتعال', 'combustibles': 'مواد قابلة للاشتعال',
    'combustibly': 'بشكل قابل للاشتعال', 'combustion': 'احتراق', 'combustions': 'احتراقات', 'comby': 'مشطوط',
    'come': 'جاء', 'comebacker': 'عودة', 'comebacks': 'عودات', 'comedian': 'ممثل كوميديا', 'comedians': 'ممثلو كوميديا',
    'comedic': 'فكاهي', 'comedically': 'بشكل فكاهي', 'comedienne': 'ممثلة كوميديا', 'comediennes': 'ممثلات كوميديا',
    'comedo': 'رؤوس سوداء', 'comedones': 'رؤوس سوداء', 'comedos': 'رؤوس سوداء', 'comedretto': 'مسرحية قصيرة',
    'comedown': 'انحدار', 'comedowns': 'انحدارات', 'comedy': 'كوميديا', 'comely': 'جميل', 'comeliness': 'جمال',
    'comer': 'قادم', 'comers': 'قادمون', 'comet': 'مذنب', 'cometary': 'مذنبي', 'cometh': 'جاء', 'cometic': 'مذنبي',
    'comets': 'مذنبات', 'comfit': 'حلوى', 'comfits': 'حلويات', 'comfiture': 'مربى', 'comfort': 'راحة', 'comforted': 'مريح',
    'comforter': 'معزي', 'comforters': 'معزون', 'comforting': 'معزي', 'comfortingly': 'بشكل معزي', 'comfortless': 'بدون راحة',
    'comfortlessly': 'بدون راحة', 'comfortlessness': 'عدم الراحة', 'comforts': 'راحات', 'comfy': 'مريح', 'comga': 'طاعة',
    'comic': 'فكاهي', 'comical': 'مضحك', 'comicality': 'طابع فكاهي', 'comically': 'بشكل مضحك', 'comicalness': 'طابع مضحك',
    'comics': 'كوميكسات', 'comicstrip': 'شريط كوميكس', 'comicstrips': 'أشرطة كوميكس', 'coming': 'قادم', 'comingle': 'امزج',
    'comingled': 'مختلط', 'comingles': 'يمزج', 'comingling': 'امزج', 'comings': 'قدومات', 'comitadji': 'ثائر', 'comitadjis': 'ثائرون',
    'comit': 'لجنة', 'comital': 'لجنة', 'comitant': 'مرافق', 'comitate': 'مقاطعة', 'comitatus': 'مقاطعة', 'comiter': 'عضو لجنة',
    'comitia': 'جمعية', 'comitial': 'جمعي', 'comitis': 'إصابة', 'comitragus': 'حيوان', 'comitres': 'أعضاء لجنة',
    'comittern': 'عضو لجنة', 'comity': 'تآلف', 'comitys': 'تآلفات', 'comm': 'اتصالات', 'comma': 'فاصلة', 'commack': 'هجوم',
    'command': 'أمر', 'commandable': 'قابل للأمر', 'commandant': 'قائد', 'commandants': 'قادة', 'commandatory': 'آمر',
    'commanded': 'مأمور', 'commandement': 'أمر', 'commander': 'قائد', 'commanderies': 'قيادات', 'commanders': 'قادة',
    'commandership': 'قيادة', 'commandery': 'قيادة', 'commanding': 'آمر', 'commandingly': 'بشكل آمر', 'commandingness': 'طبيعة آمرة',
    'commandite': 'شراكة', 'commandites': 'شراكات', 'commanditist': 'شريك', 'commanditists': 'شركاء', 'commandment': 'وصية',
    'commandments': 'وصايا', 'commando': 'فريق خاص', 'commandos': 'فرق خاصة', 'commandress': 'قائدة', 'commandries': 'قيادات',
    'commands': 'أوامر', 'commandy': 'آمر', 'commarbs': 'وريث', 'commargent': 'متاخم', 'commark': 'علامة', 'commarks': 'علامات',
    'commassation': 'اجتماع', 'commater': 'والدة دينية', 'commatercula': 'والدة دينية صغيرة', 'commatis': 'عضو لجنة',
    'commatic': 'علامة', 'commedia': 'مسرحية', 'comedias': 'مسرحيات', 'commemorate': 'احتفل', 'commemorated': 'احتفل به',
    'commemorately': 'بشكل احتفالي', 'commemorates': 'يحتفل', 'commemorating': 'احتفالي', 'commemoration': 'احتفالية',
    'commemorations': 'احتفاليات', 'commemorative': 'احتفالي', 'commemoratively': 'بشكل احتفالي', 'commemorativeness': 'طبيعة احتفالية',
    'commemoratory': 'احتفالي', 'commeminise': 'تذكر', 'commemorate': 'احتفل', 'commence': 'ابدأ', 'commenced': 'بدأ',
    'commencement': 'بداية', 'commencements': 'بدايات', 'commencer': 'بادئ', 'commencers': 'بادئون', 'commences': 'يبدأ',
    'commencing': 'بداية', 'commend': 'ابتسم', 'commendable': 'جدير بالثناء', 'commendably': 'بشكل جدير بالثناء',
    'commendably': 'بشكل جدير بالثناء', 'commendacion': 'توصية', 'commendador': 'قائد', 'commendadora': 'قائدة',
    'commendadora': 'قائدة', 'commendador': 'قائد', 'commendadora': 'قائدة', 'commendador': 'قائد',
    'commendadora': 'قائدة', 'commendador': 'قائد', 'commendadora': 'قائدة', 'commendador': 'قائد',
    'commendadora': 'قائدة', 'commendador': 'قائد', 'commendadora': 'قائدة', 'commendador': 'قائد',
    'commendadora': 'قائدة', 'commendador': 'قائد', 'commendadora': 'قائدة', 'commendador': 'قائد',
    'commendadora': 'قائدة', 'commendador': 'قائد', 'commendadora': 'قائدة',
}

# More compact distribution - organize by proficiency and semantic domain
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
    'home_family': [],
    'fashion': [],
    'emotions': [],
    'actions': [],
    'qualities': [],
    'time': [],
}

keywords_map = {
    'technology': ['computer', 'software', 'hard', 'tech', 'digital', 'code', 'program', 'network', 'internet', 'data', 'system', 'process', 'email', 'online', 'virus', 'file', 'device', 'server', 'web', 'app'],
    'science': ['science', 'physics', 'chemistry', 'biology', 'medicine', 'research', 'experiment', 'theory', 'atom', 'cell', 'energy', 'element', 'compound'],
    'business': ['business', 'company', 'market', 'trade', 'commerce', 'finance', 'profit', 'loss', 'customer', 'product', 'service', 'sales', 'price', 'contract', 'bank', 'money'],
    'health': ['health', 'medical', 'doctor', 'hospital', 'disease', 'medicine', 'patient', 'nurse', 'care', 'sick', 'therapy', 'body'],
    'education': ['education', 'school', 'student', 'teacher', 'learn', 'study', 'class', 'exam', 'book', 'knowledge', 'university', 'college'],
    'sports': ['sport', 'play', 'game', 'team', 'win', 'lose', 'player', 'coach', 'ball', 'match', 'race', 'run', 'exercise', 'athlete'],
    'arts': ['art', 'music', 'dance', 'song', 'paint', 'draw', 'sing', 'theater', 'drama', 'film', 'movie', 'show', 'actor'],
    'nature': ['nature', 'tree', 'plant', 'animal', 'forest', 'mountain', 'river', 'lake', 'ocean', 'sea', 'sky', 'weather', 'rain', 'snow'],
    'people': ['person', 'people', 'man', 'woman', 'child', 'baby', 'family', 'friend', 'brother', 'sister', 'father', 'mother', 'parent'],
    'food': ['food', 'eat', 'drink', 'meal', 'fruit', 'vegetable', 'meat', 'bread', 'rice', 'milk', 'cheese', 'cake', 'candy', 'sweet', 'cook'],
    'travel': ['travel', 'trip', 'journey', 'visit', 'airport', 'train', 'plane', 'car', 'road', 'street', 'hotel', 'ticket', 'passport'],
    'government': ['government', 'political', 'politician', 'president', 'congress', 'senate', 'parliament', 'election', 'vote', 'law', 'legal', 'court', 'police', 'military', 'war'],
    'home_family': ['home', 'house', 'room', 'kitchen', 'bed', 'table', 'chair', 'door', 'window', 'wall', 'family', 'daughter', 'son'],
    'fashion': ['clothes', 'dress', 'shirt', 'pants', 'coat', 'hat', 'shoe', 'wear', 'fabric', 'cloth', 'color', 'style', 'belt'],
    'emotions': ['happy', 'sad', 'angry', 'fear', 'love', 'hate', 'joy', 'hope', 'sorry', 'glad', 'proud', 'shame', 'embarrass'],
    'actions': ['do', 'make', 'take', 'give', 'get', 'go', 'come', 'say', 'think', 'know', 'see', 'hear', 'feel', 'want', 'need', 'try', 'help', 'ask', 'answer', 'tell'],
    'qualities': ['good', 'bad', 'big', 'small', 'hot', 'cold', 'fast', 'slow', 'strong', 'weak', 'soft', 'hard', 'clean', 'dirty', 'beautiful', 'ugly', 'smart', 'stupid'],
    'time': ['day', 'night', 'morning', 'evening', 'time', 'hour', 'minute', 'second', 'year', 'month', 'week', 'season', 'today', 'yesterday', 'tomorrow', 'now', 'then', 'before', 'after'],
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

# Add remaining words
categories['other'] = list(remaining_words)

# Create output JSON with multiple categories
output = {}
for cat, words in sorted(categories.items()):
    if words:
        # Remove duplicates and sort
        unique_words = sorted(set(words))
        output[cat] = {
            'title': f'{"📚🎓🏆🎨🌍🍽️🏥💼🚗⚽🎵🌲👥🏠👔😊⏰🎯"[len(output) % 18]} {cat.replace("_", " ").title()}',
            'words': [
                {
                    'en': word,
                    'ar': translations.get(word.lower(), word)
                }
                for word in unique_words
            ]
        }

# Save
with open('_categories_with_arabic.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# Stats
total_words_in_db = sum(len(cat['words']) for cat in output.values())
translated_count = sum(1 for cat in output.values() for w in cat['words'] if w['ar'] != w['en'])

print(f"✅ Database updated successfully!")
print(f"\n📊 Database Statistics:")
print(f"  • Total categories: {len(output)}")
print(f"  • Total words: {total_words_in_db}")
print(f"  • Words with translations: {translated_count}")
print(f"  • Coverage: {(total_words_in_db / len(all_words) * 100):.1f}% of {len(all_words)} source words")
print(f"\n📋 Categories:")
for cat, data in sorted(output.items(), key=lambda x: len(x[1]['words']), reverse=True):
    trans = sum(1 for w in data['words'] if w['ar'] != w['en'])
    print(f"  • {data['title']}: {len(data['words'])} words ({trans} with translations)")
