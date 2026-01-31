#!/usr/bin/env python3
"""
Massive Category Expansion + Complete Translation
Creates 100+ specific categories and translates remaining words
"""

import json
import re

# Comprehensive translation dictionary (1000+ more words)
MEGA_TRANSLATIONS = {
    # A-C words
    "abandon": "يتخلى", "ability": "قدرة", "able": "قادر", "about": "حول", "above": "فوق",
    "abroad": "خارج البلاد", "absence": "غياب", "absent": "غائب", "absolute": "مطلق", "absolutely": "تماماً",
    "absorb": "يمتص", "abstract": "مجرد", "abuse": "سوء استخدام", "academic": "أكاديمي", "academy": "أكاديمية",
    "accelerate": "يسرع", "accent": "لهجة", "accept": "يقبل", "acceptable": "مقبول", "acceptance": "قبول",
    "access": "وصول", "accessible": "متاح", "accident": "حادث", "accidental": "عرضي", "accidentally": "عن طريق الخطأ",
    "accommodate": "يستوعب", "accommodation": "إقامة", "accompany": "يرافق", "accomplish": "ينجز", "accord": "اتفاق",
    "accordance": "وفقاً", "according": "وفقاً", "accordingly": "وفقاً لذلك", "account": "حساب", "accountant": "محاسب",
    "accounting": "محاسبة", "accumulate": "يتراكم", "accuracy": "دقة", "accurate": "دقيق", "accurately": "بدقة",
    "accuse": "يتهم", "achieve": "يحقق", "achievement": "إنجاز", "acid": "حمض", "acknowledge": "يعترف",
    "acquire": "يكتسب", "acquisition": "استحواذ", "across": "عبر", "act": "يتصرف", "action": "عمل",
    "activate": "ينشط", "active": "نشط", "actively": "بنشاط", "activist": "ناشط", "activity": "نشاط",
    "actor": "ممثل", "actress": "ممثلة", "actual": "فعلي", "actually": "فعلياً", "acute": "حاد",
    "adapt": "يتكيف", "adaptation": "تكيف", "add": "يضيف", "addition": "إضافة", "additional": "إضافي",
    "additionally": "إضافة إلى ذلك", "address": "عنوان", "adequate": "كافٍ", "adequately": "بشكل كافٍ", "adhere": "يلتزم",
    "adjacent": "مجاور", "adjust": "يعدل", "adjustment": "تعديل", "administer": "يدير", "administration": "إدارة",
    "administrative": "إداري", "administrator": "مدير", "admire": "يعجب", "admission": "قبول", "admit": "يعترف",
    "adolescent": "مراهق", "adopt": "يتبنى", "adoption": "تبني", "adult": "بالغ", "advance": "تقدم",
    "advanced": "متقدم", "advantage": "ميزة", "adventure": "مغامرة", "adverse": "ضار", "advertise": "يعلن",
    "advertisement": "إعلان", "advertising": "إعلان", "advice": "نصيحة", "advise": "ينصح", "adviser": "مستشار",
    "advisor": "مستشار", "advisory": "استشاري", "advocate": "يدافع", "affair": "شأن", "affect": "يؤثر",
    "affection": "مودة", "afford": "يستطيع", "affordable": "ميسور", "afraid": "خائف", "after": "بعد",
    "afternoon": "بعد الظهر", "afterward": "بعد ذلك", "afterwards": "بعد ذلك", "again": "مرة أخرى", "against": "ضد",
    "age": "عمر", "aged": "كبير السن", "agency": "وكالة", "agenda": "جدول أعمال", "agent": "وكيل",
    "aggressive": "عدواني", "ago": "منذ", "agree": "يوافق", "agreement": "اتفاقية", "agricultural": "زراعي",
    "agriculture": "زراعة", "ahead": "أمام", "aid": "مساعدة", "aim": "هدف", "air": "هواء",
    "aircraft": "طائرة", "airline": "شركة طيران", "airport": "مطار", "alarm": "إنذار", "album": "ألبوم",
    "alcohol": "كحول", "alcoholic": "كحولي", "alert": "تنبيه", "alien": "أجنبي", "align": "يوائم",
    "alike": "متشابه", "alive": "حي", "all": "كل", "allege": "يزعم", "allegedly": "يُزعم",
    "alliance": "تحالف", "allied": "متحالف", "allocate": "يخصص", "allocation": "تخصيص", "allow": "يسمح",
    "allowance": "بدل", "ally": "حليف", "almost": "تقريباً", "alone": "وحده", "along": "على طول",
    "alongside": "بجانب", "aloud": "بصوت عالٍ", "alphabet": "أبجدية", "already": "بالفعل", "also": "أيضاً",
    "alter": "يغير", "alternative": "بديل", "alternatively": "بدلاً من ذلك", "although": "على الرغم", "altogether": "تماماً",
    "always": "دائماً", "amateur": "هاوٍ", "amaze": "يدهش", "amazed": "مندهش", "amazing": "مذهل",
    "ambassador": "سفير", "ambiguous": "غامض", "ambition": "طموح", "ambitious": "طموح", "ambulance": "سيارة إسعاف",
    "amend": "يعدل", "amendment": "تعديل", "among": "بين", "amongst": "بين", "amount": "كمية",
    "ample": "وافر", "amuse": "يسلي", "amused": "مستمتع", "amusement": "تسلية", "amusing": "مسلٍ",
    "analyze": "يحلل", "analysis": "تحليل", "analyst": "محلل", "analytical": "تحليلي", "ancestor": "سلف",
    "anchor": "مرساة", "ancient": "قديم", "and": "و", "anecdote": "حكاية", "angel": "ملاك",
    "anger": "غضب", "angle": "زاوية", "angry": "غاضب", "animal": "حيوان", "ankle": "كاحل",
    "anniversary": "ذكرى سنوية", "announce": "يعلن", "announcement": "إعلان", "annoy": "يزعج", "annoyed": "منزعج",
    "annoying": "مزعج", "annual": "سنوي", "annually": "سنوياً", "anonymous": "مجهول", "another": "آخر",
    "answer": "جواب", "ant": "نملة", "anticipate": "يتوقع", "anticipation": "توقع", "anxiety": "قلق",
    "anxious": "قلق", "any": "أي", "anybody": "أي شخص", "anyhow": "على أي حال", "anymore": "بعد الآن",
    "anyone": "أي شخص", "anything": "أي شيء", "anyway": "على أي حال", "anywhere": "أي مكان", "apart": "منفصل",
    "apartment": "شقة", "apologize": "يعتذر", "apology": "اعتذار", "apparatus": "جهاز", "apparent": "واضح",
    "apparently": "على ما يبدو", "appeal": "نداء", "appealing": "جذاب", "appear": "يظهر", "appearance": "مظهر",
    "appetite": "شهية", "apple": "تفاحة", "appliance": "جهاز", "applicable": "قابل للتطبيق", "applicant": "متقدم",
    "application": "تطبيق", "apply": "يطبق", "appoint": "يعين", "appointment": "موعد", "appraisal": "تقييم",
    "appreciate": "يقدر", "appreciation": "تقدير", "approach": "نهج", "appropriate": "مناسب", "appropriately": "بشكل مناسب",
    "approval": "موافقة", "approve": "يوافق", "approximate": "تقريبي", "approximately": "تقريباً", "arbitrary": "تعسفي",
    "arc": "قوس", "arch": "قوس", "architect": "مهندس معماري", "architecture": "هندسة معمارية", "archive": "أرشيف",
    "area": "منطقة", "arena": "ساحة", "argue": "يجادل", "argument": "حجة", "arise": "ينشأ",
    "arithmetic": "حساب", "arm": "ذراع", "armed": "مسلح", "armor": "درع", "army": "جيش",
    "around": "حول", "arouse": "يثير", "arrange": "يرتب", "arrangement": "ترتيب", "array": "مصفوفة",
    "arrest": "يعتقل", "arrival": "وصول", "arrive": "يصل", "arrogant": "متكبر", "arrow": "سهم",
    "art": "فن", "artery": "شريان", "article": "مقال", "articulate": "يعبر", "artificial": "صناعي",
    "artist": "فنان", "artistic": "فني", "as": "كما", "ash": "رماد", "ashamed": "خجلان",
    "aside": "جانباً", "ask": "يسأل", "asleep": "نائم", "aspect": "جانب", "aspiration": "طموح",
    "aspire": "يطمح", "assault": "اعتداء", "assemble": "يجمع", "assembly": "تجمع", "assert": "يؤكد",
    "assertion": "تأكيد", "assess": "يقيم", "assessment": "تقييم", "asset": "أصل", "assign": "يعين",
    "assignment": "مهمة", "assist": "يساعد", "assistance": "مساعدة", "assistant": "مساعد", "associate": "يربط",
    "association": "جمعية", "assume": "يفترض", "assumption": "افتراض", "assurance": "ضمان", "assure": "يؤكد",
    "astonish": "يدهش", "astonished": "مندهش", "astonishing": "مذهل", "astronaut": "رائد فضاء", "astronomy": "علم الفلك",
    "at": "عند", "athlete": "رياضي", "athletic": "رياضي", "atmosphere": "جو", "atom": "ذرة",
    "atomic": "ذري", "attach": "يرفق", "attached": "مرفق", "attachment": "مرفق", "attack": "يهاجم",
    "attacker": "مهاجم", "attain": "يحقق", "attainment": "إنجاز", "attempt": "محاولة", "attend": "يحضر",
    "attendance": "حضور", "attendant": "موظف", "attention": "انتباه", "attitude": "موقف", "attorney": "محامٍ",
    "attract": "يجذب", "attraction": "جاذبية", "attractive": "جذاب", "attribute": "صفة", "auction": "مزاد",
    "audience": "جمهور", "audio": "صوتي", "audit": "تدقيق", "auditor": "مدقق", "auditorium": "قاعة",
    "august": "أغسطس", "aunt": "عمة", "authentic": "أصيل", "author": "مؤلف", "authority": "سلطة",
    "authorization": "تفويض", "authorize": "يفوض", "auto": "سيارة", "automatic": "أوتوماتيكي", "automatically": "تلقائياً",
    "automobile": "سيارة", "autonomous": "مستقل", "autonomy": "استقلالية", "autumn": "خريف", "available": "متاح",
    "availability": "توفر", "avenue": "شارع", "average": "متوسط", "aviation": "طيران", "avoid": "يتجنب",
    "await": "ينتظر", "awake": "مستيقظ", "award": "جائزة", "aware": "واعٍ", "awareness": "وعي",
    "away": "بعيداً", "awesome": "رائع", "awful": "فظيع", "awkward": "محرج", "axis": "محور",
    
    # B words
    "baby": "طفل رضيع", "back": "خلف", "background": "خلفية", "backward": "للخلف", "backwards": "للخلف",
    "bacteria": "بكتيريا", "bad": "سيئ", "badly": "بشكل سيء", "bag": "حقيبة", "baggage": "أمتعة",
    "bake": "يخبز", "balance": "توازن", "balanced": "متوازن", "balcony": "شرفة", "ball": "كرة",
    "ballet": "باليه", "balloon": "بالون", "ballot": "اقتراع", "ban": "يحظر", "banana": "موز",
    "band": "فرقة", "bandage": "ضمادة", "bang": "ضجة", "bank": "بنك", "banker": "مصرفي",
    "banking": "مصرفي", "bankrupt": "مفلس", "bankruptcy": "إفلاس", "banner": "لافتة", "bar": "حانة",
    "barbecue": "شواء", "bare": "عارٍ", "barely": "بالكاد", "bargain": "صفقة", "barrier": "حاجز",
    "base": "قاعدة", "baseball": "بيسبول", "based": "مبني", "basement": "قبو", "basic": "أساسي",
    "basically": "أساساً", "basin": "حوض", "basis": "أساس", "basket": "سلة", "basketball": "كرة سلة",
    "bat": "مضرب", "batch": "دفعة", "bath": "حمام", "bathe": "يستحم", "bathroom": "حمام",
    "battery": "بطارية", "battle": "معركة", "bay": "خليج", "be": "يكون", "beach": "شاطئ",
    "beam": "شعاع", "bean": "فاصوليا", "bear": "دب", "beard": "لحية", "beast": "وحش",
    "beat": "يضرب", "beating": "ضرب", "beautiful": "جميل", "beautifully": "بشكل جميل", "beauty": "جمال",
    "because": "لأن", "become": "يصبح", "bed": "سرير", "bedroom": "غرفة نوم", "bee": "نحلة",
    "beef": "لحم بقر", "beer": "بيرة", "before": "قبل", "beforehand": "مسبقاً", "beg": "يتوسل",
    "begin": "يبدأ", "beginner": "مبتدئ", "beginning": "بداية", "behalf": "نيابة", "behave": "يتصرف",
    "behavior": "سلوك", "behaviour": "سلوك", "behind": "خلف", "being": "كائن", "belief": "معتقد",
    "believe": "يؤمن", "bell": "جرس", "belly": "بطن", "belong": "ينتمي", "beloved": "محبوب",
    "below": "تحت", "belt": "حزام", "bench": "مقعد", "bend": "ينحني", "beneath": "تحت",
    "beneficial": "مفيد", "benefit": "فائدة", "beside": "بجانب", "besides": "إلى جانب", "best": "أفضل",
    "bet": "يراهن", "betray": "يخون", "betrayal": "خيانة", "better": "أفضل", "between": "بين",
    "beverage": "مشروب", "beyond": "أبعد من", "bias": "تحيز", "Bible": "الكتاب المقدس", "bicycle": "دراجة",
    "bid": "عرض", "big": "كبير", "bike": "دراجة", "bill": "فاتورة", "billion": "مليار",
    "bin": "صندوق", "bind": "يربط", "binding": "ملزم", "biology": "أحياء", "bird": "طائر",
    "birth": "ولادة", "birthday": "عيد ميلاد", "biscuit": "بسكويت", "bit": "قليل", "bite": "يعض",
    "bitter": "مر", "black": "أسود", "blade": "شفرة", "blame": "يلوم", "blank": "فارغ",
    "blanket": "بطانية", "blast": "انفجار", "bleed": "ينزف", "blend": "يمزج", "bless": "يبارك",
    "blessing": "بركة", "blind": "أعمى", "block": "يسد", "blog": "مدونة", "blonde": "أشقر",
    "blood": "دم", "bloody": "دموي", "bloom": "يزهر", "blow": "ينفخ", "blue": "أزرق",
    "board": "لوحة", "boast": "يتفاخر", "boat": "قارب", "body": "جسم", "boil": "يغلي",
    "bold": "جريء", "bomb": "قنبلة", "bombing": "قصف", "bond": "رابطة", "bone": "عظم",
    "bonus": "مكافأة", "book": "كتاب", "booking": "حجز", "boom": "ازدهار", "boost": "يعزز",
    "boot": "حذاء", "booth": "كشك", "border": "حدود", "bore": "يمل", "bored": "ملل",
    "boring": "ممل", "born": "مولود", "borrow": "يستعير", "boss": "رئيس", "both": "كلا",
    "bother": "يزعج", "bottle": "زجاجة", "bottom": "قاع", "bounce": "يرتد", "bound": "ملزم",
    "boundary": "حد", "bow": "ينحني", "bowl": "وعاء", "box": "صندوق", "boxing": "ملاكمة",
    "boy": "صبي", "boyfriend": "صديق", "brain": "دماغ", "branch": "فرع", "brand": "علامة تجارية",
    "brave": "شجاع", "bravery": "شجاعة", "bread": "خبز", "break": "يكسر", "breakdown": "انهيار",
    "breakfast": "إفطار", "breakthrough": "اختراق", "breast": "ثدي", "breath": "نفس", "breathe": "يتنفس",
    "breathing": "تنفس", "breed": "يربي", "breeze": "نسيم", "brick": "طوبة", "bride": "عروس",
    "bridge": "جسر", "brief": "موجز", "briefly": "بإيجاز", "bright": "مشرق", "brilliant": "لامع",
    "bring": "يحضر", "British": "بريطاني", "broad": "واسع", "broadcast": "يبث", "broadly": "على نطاق واسع",
    "broken": "مكسور", "bronze": "برونز", "brother": "أخ", "brown": "بني", "brush": "فرشاة",
    "bubble": "فقاعة", "bucket": "دلو", "budget": "ميزانية", "buffer": "حاجز", "build": "يبني",
    "builder": "بناء", "building": "مبنى", "bulb": "مصباح", "bulk": "كتلة", "bullet": "رصاصة",
    "bunch": "حزمة", "bundle": "حزمة", "burden": "عبء", "bureau": "مكتب", "bureaucracy": "بيروقراطية",
    "burn": "يحرق", "burning": "احتراق", "burst": "ينفجر", "bury": "يدفن", "bus": "حافلة",
    "bush": "شجيرة", "business": "عمل", "businessman": "رجل أعمال", "busy": "مشغول", "but": "لكن",
    "butcher": "جزار", "butter": "زبدة", "butterfly": "فراشة", "button": "زر", "buy": "يشتري",
    "buyer": "مشتري", "by": "بواسطة", "bye": "وداعاً", "bypass": "يتجاوز",
    
    # C words
    "cab": "سيارة أجرة", "cabin": "كابينة", "cabinet": "خزانة", "cable": "كابل", "cafe": "مقهى",
    "cage": "قفص", "cake": "كعكة", "calculate": "يحسب", "calculation": "حساب", "calculator": "آلة حاسبة",
    "calendar": "تقويم", "calf": "عجل", "call": "ينادي", "calm": "هادئ", "calmly": "بهدوء",
    "calorie": "سعرة حرارية", "camera": "كاميرا", "camp": "مخيم", "campaign": "حملة", "camping": "تخييم",
    "campus": "حرم جامعي", "can": "يستطيع", "cancel": "يلغي", "cancellation": "إلغاء", "cancer": "سرطان",
    "candidate": "مرشح", "candle": "شمعة", "candy": "حلوى", "cannon": "مدفع", "cannot": "لا يستطيع",
    "canoe": "زورق", "canvas": "قماش", "cap": "قبعة", "capability": "قدرة", "capable": "قادر",
    "capacity": "سعة", "cape": "رأس", "capital": "عاصمة", "capitalism": "رأسمالية", "capitalist": "رأسمالي",
    "captain": "قبطان", "caption": "تعليق", "capture": "يأسر", "car": "سيارة", "carbon": "كربون",
    "card": "بطاقة", "cardboard": "كرتون", "care": "يهتم", "career": "مهنة", "careful": "حذر",
    "carefully": "بعناية", "careless": "مهمل", "cargo": "شحنة", "carpenter": "نجار", "carpet": "سجادة",
    "carriage": "عربة", "carrier": "ناقل", "carrot": "جزرة", "carry": "يحمل", "cart": "عربة",
    "carve": "ينحت", "case": "حالة", "cash": "نقد", "cashier": "أمين صندوق", "casino": "كازينو",
    "cast": "يلقي", "castle": "قلعة", "casual": "غير رسمي", "casually": "بشكل غير رسمي", "cat": "قطة",
    "catalog": "كتالوج", "catalogue": "كتالوج", "catastrophe": "كارثة", "catch": "يمسك", "category": "فئة",
    "cater": "يلبي", "catering": "تقديم الطعام", "cathedral": "كاتدرائية", "Catholic": "كاثوليكي", "cattle": "ماشية",
    "caught": "أمسك", "cause": "يسبب", "caution": "حذر", "cautious": "حذر", "cave": "كهف",
    "cease": "يتوقف", "ceiling": "سقف", "celebrate": "يحتفل", "celebration": "احتفال", "celebrity": "مشهور",
    "cell": "خلية", "cellar": "قبو", "cement": "أسمنت", "cemetery": "مقبرة", "census": "تعداد",
    "cent": "سنت", "center": "مركز", "central": "مركزي", "centre": "مركز", "century": "قرن",
    "cereal": "حبوب", "ceremony": "حفل", "certain": "مؤكد", "certainly": "بالتأكيد", "certainty": "يقين",
    "certificate": "شهادة", "chain": "سلسلة", "chair": "كرسي", "chairman": "رئيس", "chairperson": "رئيس",
    "chalk": "طباشير", "challenge": "تحدٍ", "challenging": "صعب", "chamber": "غرفة", "champion": "بطل",
    "championship": "بطولة", "chance": "فرصة", "change": "يتغير", "channel": "قناة", "chaos": "فوضى",
    "chaotic": "فوضوي", "chap": "رجل", "chapel": "كنيسة صغيرة", "chapter": "فصل", "character": "شخصية",
    "characteristic": "مميز", "characterize": "يميز", "charcoal": "فحم", "charge": "يشحن", "charity": "خيرية",
    "charm": "سحر", "charming": "ساحر", "chart": "مخطط", "charter": "ميثاق", "chase": "يطارد",
    "chat": "يدردش", "cheap": "رخيص", "cheat": "يغش", "check": "يفحص", "checkout": "الدفع",
    "cheek": "خد", "cheer": "يشجع", "cheerful": "مبتهج", "cheese": "جبن", "chef": "طاه",
    "chemical": "كيميائي", "chemist": "كيميائي", "chemistry": "كيمياء", "cheque": "شيك", "cherry": "كرز",
    "chess": "شطرنج", "chest": "صدر", "chew": "يمضغ", "chicken": "دجاج", "chief": "رئيس",
    "chiefly": "بشكل رئيسي", "child": "طفل", "childhood": "طفولة", "childish": "طفولي", "chill": "يبرد",
    "chilly": "بارد", "chimney": "مدخنة", "chin": "ذقن", "chip": "رقاقة", "chocolate": "شوكولاتة",
    "choice": "خيار", "choir": "جوقة", "choke": "يختنق", "cholesterol": "كوليسترول", "choose": "يختار",
    "chop": "يقطع", "chord": "وتر", "chorus": "كورس", "chosen": "مختار", "Christian": "مسيحي",
    "Christmas": "عيد الميلاد", "chronic": "مزمن", "church": "كنيسة", "cigarette": "سيجارة", "cinema": "سينما",
    "circle": "دائرة", "circuit": "دائرة", "circular": "دائري", "circulate": "يتداول", "circulation": "دوران",
    "circumstance": "ظرف", "cite": "يستشهد", "citizen": "مواطن", "citizenship": "جنسية", "city": "مدينة",
    "civic": "مدني", "civil": "مدني", "civilian": "مدني", "civilization": "حضارة", "civilized": "متحضر",
    "claim": "يدعي", "clap": "يصفق", "clarify": "يوضح", "clarity": "وضوح", "clash": "يصطدم",
    "class": "صف", "classic": "كلاسيكي", "classical": "كلاسيكي", "classification": "تصنيف", "classify": "يصنف",
    "classmate": "زميل صف", "classroom": "فصل دراسي", "clause": "بند", "claw": "مخلب", "clay": "طين",
    "clean": "نظيف", "cleaning": "تنظيف", "clear": "واضح", "clearance": "تصريح", "clearing": "مقاصة",
    "clearly": "بوضوح", "clergy": "رجال دين", "clerk": "موظف", "clever": "ذكي", "click": "ينقر",
    "client": "عميل", "cliff": "جرف", "climate": "مناخ", "climb": "يتسلق", "climbing": "تسلق",
    "clinic": "عيادة", "clinical": "سريري", "clip": "مشبك", "cloak": "عباءة", "clock": "ساعة",
    "clone": "نسخة", "close": "يغلق", "closed": "مغلق", "closely": "عن كثب", "closet": "خزانة",
    "closure": "إغلاق", "cloth": "قماش", "clothes": "ملابس", "clothing": "ملابس", "cloud": "سحابة",
    "cloudy": "غائم", "club": "نادي", "clue": "دليل", "clumsy": "أخرق", "cluster": "عنقود",
    "clutch": "يمسك", "coach": "مدرب", "coal": "فحم", "coalition": "تحالف", "coast": "ساحل",
    "coastal": "ساحلي", "coat": "معطف", "cocaine": "كوكايين", "cock": "ديك", "cocktail": "كوكتيل",
    "code": "رمز", "coffee": "قهوة", "coffin": "تابوت", "coherent": "متماسك", "coil": "لفافة",
    "coin": "عملة", "coincide": "يتزامن", "coincidence": "صدفة", "cold": "بارد", "collaborate": "يتعاون",
    "collaboration": "تعاون", "collapse": "ينهار", "collar": "ياقة", "colleague": "زميل", "collect": "يجمع",
    "collection": "مجموعة", "collective": "جماعي", "collectively": "بشكل جماعي", "collector": "جامع", "college": "كلية",
    "collide": "يصطدم", "collision": "تصادم", "colonial": "استعماري", "colony": "مستعمرة", "color": "لون",
    "column": "عمود", "comb": "يمشط", "combat": "يقاتل", "combination": "مجموعة", "combine": "يجمع",
    "come": "يأتي", "comeback": "عودة", "comedy": "كوميديا", "comfort": "راحة", "comfortable": "مريح",
    "comfortably": "بشكل مريح", "comic": "كوميدي", "coming": "قادم", "comma": "فاصلة", "command": "يأمر",
    "commander": "قائد", "commemorate": "يحيي ذكرى", "commence": "يبدأ", "comment": "يعلق", "commentary": "تعليق",
    "commentator": "معلق", "commerce": "تجارة", "commercial": "تجاري", "commission": "عمولة", "commissioner": "مفوض",
    "commit": "يرتكب", "commitment": "التزام", "committed": "ملتزم", "committee": "لجنة", "commodity": "سلعة",
    "common": "شائع", "commonly": "عادة", "commonwealth": "كومنولث", "communicate": "يتواصل", "communication": "تواصل",
    "communism": "شيوعية", "communist": "شيوعي", "community": "مجتمع", "companion": "رفيق", "company": "شركة",
    "comparable": "قابل للمقارنة", "comparative": "نسبي", "comparatively": "نسبياً", "compare": "يقارن", "comparison": "مقارنة",
    "compartment": "مقصورة", "compass": "بوصلة", "compassion": "تعاطف", "compassionate": "رحيم", "compatible": "متوافق",
    "compel": "يجبر", "compelling": "مقنع", "compensate": "يعوض", "compensation": "تعويض", "compete": "يتنافس",
    "competence": "كفاءة", "competent": "كفؤ", "competition": "منافسة", "competitive": "تنافسي", "competitor": "منافس",
    "compile": "يجمع", "complain": "يشتكي", "complaint": "شكوى", "complement": "يكمل", "complete": "يكمل",
    "completed": "مكتمل", "completely": "تماماً", "completion": "إكمال", "complex": "معقد", "complexity": "تعقيد",
    "compliance": "امتثال", "complicate": "يعقد", "complicated": "معقد", "complication": "تعقيد", "compliment": "مجاملة",
    "comply": "يمتثل", "component": "مكون", "compose": "يؤلف", "composition": "تركيب", "compound": "مركب",
    "comprehension": "فهم", "comprehensive": "شامل", "compress": "يضغط", "comprise": "يتكون من", "compromise": "حل وسط",
    "compulsory": "إلزامي", "compute": "يحسب", "computer": "كمبيوتر", "computing": "حوسبة", "comrade": "رفيق",
    "conceal": "يخفي", "concede": "يعترف", "conceive": "يتصور", "concentrate": "يركز", "concentration": "تركيز",
    "concept": "مفهوم", "conception": "تصور", "concern": "يقلق", "concerned": "معني", "concerning": "بشأن",
    "concert": "حفلة موسيقية", "concession": "تنازل", "conclude": "يستنتج", "conclusion": "استنتاج", "concrete": "خرسانة",
    "condemn": "يدين", "condemnation": "إدانة", "condition": "حالة", "conditional": "مشروط", "conduct": "يجري",
    "conductor": "موصل", "cone": "مخروط", "confer": "يمنح", "conference": "مؤتمر", "confess": "يعترف",
    "confession": "اعتراف", "confidence": "ثقة", "confident": "واثق", "confidential": "سري", "confine": "يحصر",
    "confined": "محصور", "confirm": "يؤكد", "confirmation": "تأكيد", "conflict": "صراع", "conform": "يتوافق",
    "confront": "يواجه", "confrontation": "مواجهة", "confuse": "يربك", "confused": "مرتبك", "confusing": "مربك",
    "confusion": "ارتباك", "congratulate": "يهنئ", "congratulation": "تهنئة", "congregation": "جماعة", "congress": "كونغرس",
    "conjunction": "اقتران", "connect": "يربط", "connected": "متصل", "connection": "اتصال", "conquer": "يغزو",
    "conquest": "غزو", "conscience": "ضمير", "conscious": "واعٍ", "consciousness": "وعي", "consecutive": "متتالي",
    "consensus": "إجماع", "consent": "موافقة", "consequence": "نتيجة", "consequently": "وبالتالي", "conservation": "حفظ",
    "conservative": "محافظ", "conserve": "يحفظ", "consider": "يعتبر", "considerable": "كبير", "considerably": "إلى حد كبير",
    "consideration": "اعتبار", "considering": "بالنظر إلى", "consist": "يتكون", "consistency": "اتساق", "consistent": "متسق",
    "consistently": "باستمرار", "console": "يواسي", "consolidate": "يوطد", "consolidation": "توطيد", "conspiracy": "مؤامرة",
    "constant": "ثابت", "constantly": "باستمرار", "constitute": "يشكل", "constitution": "دستور", "constitutional": "دستوري",
    "constraint": "قيد", "construct": "يبني", "construction": "بناء", "constructive": "بناء", "consult": "يستشير",
    "consultant": "استشاري", "consultation": "استشارة", "consume": "يستهلك", "consumer": "مستهلك", "consumption": "استهلاك",
    "contact": "اتصال", "contain": "يحتوي", "container": "حاوية", "contamination": "تلوث", "contemplate": "يتأمل",
    "contemporary": "معاصر", "contempt": "ازدراء", "contend": "يجادل", "content": "محتوى", "contention": "جدل",
    "contest": "مسابقة", "context": "سياق", "continent": "قارة", "continental": "قاري", "continual": "متواصل",
    "continually": "باستمرار", "continuation": "استمرار", "continue": "يستمر", "continued": "مستمر", "continuity": "استمرارية",
    "continuous": "مستمر", "continuously": "باستمرار", "contract": "عقد", "contractor": "مقاول", "contradict": "يناقض",
    "contradiction": "تناقض", "contrary": "عكس", "contrast": "تباين", "contribute": "يساهم", "contribution": "مساهمة",
    "contributor": "مساهم", "control": "سيطرة", "controversial": "مثير للجدل", "controversy": "جدل", "convenience": "راحة",
    "convenient": "مريح", "conveniently": "بشكل مريح", "convention": "اتفاقية", "conventional": "تقليدي", "conversation": "محادثة",
    "conversely": "على العكس", "conversion": "تحويل", "convert": "يحول", "convey": "ينقل", "convict": "يدين",
    "conviction": "إدانة", "convince": "يقنع", "convinced": "مقتنع", "convincing": "مقنع", "cook": "يطبخ",
    "cooker": "طباخ", "cookie": "بسكويت", "cooking": "طبخ", "cool": "بارد", "cooperate": "يتعاون",
    "cooperation": "تعاون", "cooperative": "تعاوني", "coordinate": "ينسق", "coordination": "تنسيق", "cop": "شرطي",
    "cope": "يتعامل", "copper": "نحاس", "copy": "نسخة", "copyright": "حقوق نشر", "coral": "مرجان",
    "cord": "حبل", "core": "جوهر", "cork": "فلين", "corn": "ذرة", "corner": "ركن",
    "corporate": "شركة", "corporation": "شركة", "corps": "فيلق", "corpse": "جثة", "correct": "صحيح",
    "correction": "تصحيح", "correctly": "بشكل صحيح", "correlate": "يربط", "correlation": "ارتباط", "correspond": "يتوافق",
    "correspondence": "مراسلة", "correspondent": "مراسل", "corresponding": "مقابل", "corridor": "ممر", "corrupt": "فاسد",
    "corruption": "فساد", "cost": "تكلفة", "costly": "مكلف", "costume": "زي", "cottage": "كوخ",
    "cotton": "قطن", "couch": "أريكة", "cough": "سعال", "could": "استطاع", "council": "مجلس",
    "councillor": "عضو مجلس", "counsel": "ينصح", "counseling": "استشارة", "counselling": "استشارة", "counsellor": "مستشار",
    "counselor": "مستشار", "count": "يعد", "counter": "عداد", "counterpart": "نظير", "countless": "لا يحصى",
    "country": "بلد", "countryside": "ريف", "county": "مقاطعة", "couple": "زوجان", "coupon": "قسيمة",
    "courage": "شجاعة", "courageous": "شجاع", "course": "مسار", "court": "محكمة", "courtesy": "أدب",
    "courtyard": "فناء", "cousin": "ابن عم", "cove": "خليج صغير", "cover": "يغطي", "coverage": "تغطية",
    "covered": "مغطى", "covering": "غطاء", "cow": "بقرة", "coward": "جبان", "cowboy": "راعي بقر",
    "crab": "سرطان", "crack": "شق", "craft": "حرفة", "craftsman": "حرفي", "cram": "يحشو",
    "cramp": "تشنج", "crane": "رافعة", "crash": "يصطدم", "crate": "صندوق", "crawl": "يزحف",
    "crazy": "مجنون", "cream": "كريم", "create": "يخلق", "creation": "خلق", "creative": "إبداعي",
    "creativity": "إبداع", "creator": "خالق", "creature": "مخلوق", "credibility": "مصداقية", "credible": "موثوق",
    "credit": "ائتمان", "creditor": "دائن", "creek": "جدول", "creep": "يزحف", "crew": "طاقم",
    "cricket": "كريكيت", "crime": "جريمة", "criminal": "مجرم", "crisis": "أزمة", "crisp": "مقرمش",
    "criteria": "معايير", "criterion": "معيار", "critic": "ناقد", "critical": "حاسم", "critically": "بشكل حاسم",
    "criticism": "نقد", "criticize": "ينتقد", "crop": "محصول", "cross": "يعبر", "crossing": "عبور",
    "crossroads": "مفترق طرق", "crouch": "ينحني", "crow": "غراب", "crowd": "حشد", "crowded": "مزدحم",
    "crown": "تاج", "crucial": "حاسم", "crude": "خام", "cruel": "قاسٍ", "cruelty": "قسوة",
    "cruise": "رحلة بحرية", "crumb": "فتات", "crumble": "يتفتت", "crush": "يسحق", "cry": "يبكي",
    "crystal": "كريستال", "cube": "مكعب", "cucumber": "خيار", "cue": "إشارة", "cultivate": "يزرع",
    "cultural": "ثقافي", "culturally": "ثقافياً", "culture": "ثقافة", "cultured": "مثقف", "cup": "كوب",
    "cupboard": "خزانة", "curb": "يكبح", "cure": "علاج", "curiosity": "فضول", "curious": "فضولي",
    "curiously": "بفضول", "curl": "يلف", "curly": "مجعد", "currency": "عملة", "current": "حالي",
    "currently": "حالياً", "curriculum": "منهج", "curry": "كاري", "curse": "لعنة", "curtain": "ستارة",
    "curve": "منحنى", "curved": "منحني", "cushion": "وسادة", "custody": "حضانة", "custom": "عادة",
    "customary": "معتاد", "customer": "زبون", "customs": "جمارك", "cut": "يقطع", "cute": "لطيف",
    "cutting": "قطع", "cycle": "دورة", "cycling": "ركوب الدراجات", "cylinder": "أسطوانة", "cynical": "циничный"
}

# 100+ highly specific categories
MEGA_CATEGORIES = {
    "animals_mammals": {"title": "🦁 Mammals & Large Animals", "keywords": ["dog", "cat", "horse", "cow", "pig", "sheep", "goat", "lion", "tiger", "bear", "wolf", "fox", "deer", "rabbit", "mouse", "rat", "elephant", "giraffe", "zebra", "monkey", "ape", "whale", "dolphin", "seal", "bat"]},
    "animals_birds": {"title": "🦅 Birds & Flying Animals", "keywords": ["bird", "eagle", "hawk", "owl", "crow", "pigeon", "parrot", "duck", "goose", "swan", "chicken", "turkey", "peacock", "sparrow", "robin"]},
    "animals_insects": {"title": "🐛 Insects & Small Creatures", "keywords": ["insect", "ant", "bee", "butterfly", "moth", "spider", "fly", "mosquito", "beetle", "cricket", "grasshopper", "worm", "snail", "slug"]},
    "animals_aquatic": {"title": "🐠 Fish & Aquatic Life", "keywords": ["fish", "shark", "whale", "dolphin", "seal", "crab", "lobster", "shrimp", "octopus", "squid", "jellyfish", "starfish", "coral"]},
    "animals_reptiles": {"title": "🦎 Reptiles & Amphibians", "keywords": ["snake", "lizard", "turtle", "tortoise", "crocodile", "alligator", "frog", "toad", "salamander"]},
    
    "body_head": {"title": "👤 Head & Face Parts", "keywords": ["head", "face", "eye", "ear", "nose", "mouth", "lip", "tooth", "teeth", "tongue", "cheek", "chin", "forehead", "eyebrow", "eyelash", "hair", "beard", "mustache", "jaw"]},
    "body_torso": {"title": "🫁 Torso & Organs", "keywords": ["chest", "breast", "stomach", "belly", "abdomen", "back", "shoulder", "waist", "hip", "heart", "lung", "liver", "kidney", "intestine"]},
    "body_limbs": {"title": "🦵 Limbs & Extremities", "keywords": ["arm", "hand", "finger", "thumb", "wrist", "elbow", "leg", "foot", "toe", "ankle", "knee", "thigh", "calf"]},
    "body_internal": {"title": "🧠 Internal Body Systems", "keywords": ["brain", "nerve", "blood", "vein", "artery", "bone", "muscle", "skin", "tissue", "cell", "organ"]},
    
    "food_fruits": {"title": "🍎 Fruits", "keywords": ["fruit", "apple", "orange", "banana", "grape", "lemon", "lime", "strawberry", "raspberry", "blueberry", "watermelon", "melon", "peach", "pear", "plum", "cherry", "mango", "pineapple", "kiwi"]},
    "food_vegetables": {"title": "🥕 Vegetables", "keywords": ["vegetable", "potato", "tomato", "onion", "garlic", "carrot", "cabbage", "lettuce", "cucumber", "pepper", "bean", "pea", "corn", "broccoli", "cauliflower", "spinach", "mushroom", "eggplant", "pumpkin", "squash"]},
    "food_meat": {"title": "🥩 Meat & Protein", "keywords": ["meat", "beef", "pork", "chicken", "turkey", "lamb", "mutton", "bacon", "ham", "sausage", "steak", "chop"]},
    "food_dairy": {"title": "🥛 Dairy Products", "keywords": ["milk", "cheese", "butter", "cream", "yogurt", "ice cream"]},
    "food_grains": {"title": "🌾 Grains & Bread", "keywords": ["bread", "rice", "wheat", "flour", "grain", "cereal", "oat", "barley", "corn", "pasta", "noodle"]},
    "food_sweets": {"title": "🍰 Desserts & Sweets", "keywords": ["cake", "cookie", "biscuit", "candy", "chocolate", "sugar", "honey", "jam", "pie", "pudding", "ice cream"]},
    "food_drinks": {"title": "🥤 Beverages", "keywords": ["drink", "water", "juice", "milk", "coffee", "tea", "wine", "beer", "soda", "cola", "lemonade", "cocktail", "alcohol"]},
    "food_cooking": {"title": "🍳 Cooking & Preparation", "keywords": ["cook", "bake", "fry", "boil", "grill", "roast", "steam", "chop", "cut", "slice", "mix", "stir", "pour", "season", "recipe", "ingredient", "spice", "herb", "sauce", "salt", "pepper", "oil"]},
    
    "clothes_upper": {"title": "👕 Upper Body Clothing", "keywords": ["shirt", "blouse", "sweater", "jacket", "coat", "vest", "suit", "tie", "collar", "sleeve", "button"]},
    "clothes_lower": {"title": "👖 Lower Body Clothing", "keywords": ["pants", "trousers", "jeans", "shorts", "skirt", "dress", "leggings", "tights"]},
    "clothes_footwear": {"title": "👟 Shoes & Footwear", "keywords": ["shoe", "boot", "sandal", "slipper", "sneaker", "heel", "sole", "lace", "sock"]},
    "clothes_accessories": {"title": "👒 Accessories", "keywords": ["hat", "cap", "scarf", "glove", "belt", "bag", "purse", "backpack", "umbrella", "jewelry", "watch", "glasses", "sunglasses"]},
    "clothes_materials": {"title": "🧵 Fabrics & Materials", "keywords": ["fabric", "cloth", "cotton", "silk", "wool", "leather", "fur", "nylon", "polyester", "linen", "denim"]},
    
    "home_rooms": {"title": "🚪 Rooms & Spaces", "keywords": ["room", "kitchen", "bedroom", "bathroom", "living room", "dining room", "hall", "hallway", "closet", "basement", "attic", "garage", "balcony", "porch"]},
    "home_furniture": {"title": "🛋️ Furniture", "keywords": ["furniture", "table", "chair", "desk", "bed", "sofa", "couch", "armchair", "stool", "bench", "shelf", "cabinet", "drawer", "wardrobe", "cupboard"]},
    "home_appliances": {"title": "📺 Appliances & Electronics", "keywords": ["television", "tv", "radio", "phone", "computer", "laptop", "tablet", "refrigerator", "fridge", "freezer", "stove", "oven", "microwave", "dishwasher", "washing machine", "dryer", "vacuum", "fan", "heater", "air conditioner"]},
    "home_kitchen": {"title": "🍽️ Kitchen Items", "keywords": ["plate", "dish", "bowl", "cup", "glass", "mug", "fork", "knife", "spoon", "pot", "pan", "kettle", "bottle", "jar", "can"]},
    "home_decor": {"title": "🖼️ Decoration & Accessories", "keywords": ["picture", "photo", "painting", "mirror", "lamp", "light", "candle", "vase", "cushion", "pillow", "blanket", "sheet", "towel", "curtain", "carpet", "rug", "mat"]},
    
    "transport_vehicles": {"title": "🚗 Vehicles & Cars", "keywords": ["car", "automobile", "vehicle", "truck", "van", "jeep", "taxi", "cab", "limousine", "motorcycle", "bike", "scooter", "bicycle", "cycle"]},
    "transport_public": {"title": "🚌 Public Transportation", "keywords": ["bus", "train", "subway", "metro", "tram", "railway", "station", "platform", "ticket", "fare"]},
    "transport_air": {"title": "✈️ Air Travel", "keywords": ["plane", "airplane", "aircraft", "jet", "helicopter", "flight", "airport", "terminal", "pilot", "crew", "passenger"]},
    "transport_water": {"title": "⛵ Water Transport", "keywords": ["boat", "ship", "ferry", "yacht", "sailboat", "canoe", "kayak", "cruise", "port", "harbor", "dock", "pier", "captain", "sailor"]},
    "transport_parts": {"title": "⚙️ Vehicle Parts", "keywords": ["engine", "motor", "wheel", "tire", "brake", "steering", "gear", "pedal", "seat", "door", "window", "trunk", "hood", "bumper", "mirror"]},
    
    "nature_plants": {"title": "🌱 Plants & Vegetation", "keywords": ["plant", "tree", "bush", "shrub", "grass", "weed", "vine", "moss", "fern", "cactus", "palm"]},
    "nature_flowers": {"title": "🌺 Flowers & Blooms", "keywords": ["flower", "rose", "lily", "tulip", "daisy", "sunflower", "orchid", "blossom", "bloom", "petal", "bud"]},
    "nature_landscape": {"title": "🏔️ Landscapes & Terrain", "keywords": ["mountain", "hill", "valley", "plain", "plateau", "cliff", "canyon", "cave", "peak", "slope"]},
    "nature_water": {"title": "💧 Water Bodies", "keywords": ["river", "stream", "creek", "brook", "lake", "pond", "pool", "sea", "ocean", "bay", "gulf", "strait", "channel"]},
    "nature_weather": {"title": "⛈️ Weather Phenomena", "keywords": ["weather", "rain", "snow", "hail", "sleet", "storm", "thunder", "lightning", "wind", "breeze", "gale", "hurricane", "tornado", "typhoon", "fog", "mist", "dew", "frost", "rainbow"]},
    "nature_sky": {"title": "🌌 Sky & Space", "keywords": ["sky", "sun", "moon", "star", "planet", "comet", "meteor", "asteroid", "galaxy", "universe", "space", "orbit", "satellite", "constellation"]},
    "nature_disasters": {"title": "🌋 Natural Disasters", "keywords": ["earthquake", "volcano", "eruption", "tsunami", "flood", "drought", "avalanche", "landslide", "wildfire", "disaster"]},
    
    "buildings_residential": {"title": "🏠 Residential Buildings", "keywords": ["house", "home", "apartment", "flat", "cottage", "bungalow", "mansion", "villa", "cabin", "hut", "tent", "dwelling"]},
    "buildings_commercial": {"title": "🏪 Commercial Buildings", "keywords": ["store", "shop", "mall", "market", "supermarket", "boutique", "restaurant", "cafe", "bar", "pub", "hotel", "motel", "inn"]},
    "buildings_public": {"title": "🏛️ Public Buildings", "keywords": ["library", "museum", "gallery", "theater", "cinema", "stadium", "arena", "gym", "hospital", "clinic", "school", "university", "college", "church", "temple", "mosque", "synagogue", "cathedral", "chapel"]},
    "buildings_industrial": {"title": "🏭 Industrial Buildings", "keywords": ["factory", "plant", "mill", "warehouse", "workshop", "laboratory", "lab", "office", "tower", "skyscraper"]},
    
    "education_subjects": {"title": "📚 School Subjects", "keywords": ["math", "mathematics", "algebra", "geometry", "calculus", "science", "physics", "chemistry", "biology", "history", "geography", "literature", "language", "english", "art", "music", "drama", "sport", "physical education"]},
    "education_activities": {"title": "✏️ Learning Activities", "keywords": ["study", "learn", "read", "write", "draw", "calculate", "solve", "practice", "rehearse", "memorize", "understand", "explain", "teach", "instruct", "train", "educate"]},
    "education_materials": {"title": "📖 Study Materials", "keywords": ["book", "textbook", "notebook", "workbook", "dictionary", "encyclopedia", "manual", "guide", "map", "chart", "diagram", "graph", "table"]},
    "education_tools": {"title": "✂️ School Supplies", "keywords": ["pen", "pencil", "crayon", "marker", "chalk", "eraser", "ruler", "compass", "protractor", "calculator", "scissors", "glue", "tape", "stapler", "paper", "card", "folder"]},
    
    "work_occupations": {"title": "👨‍💼 Jobs & Occupations", "keywords": ["job", "work", "career", "profession", "occupation", "employment", "position", "role"]},
    "work_office": {"title": "💼 Office Work", "keywords": ["office", "desk", "meeting", "conference", "presentation", "report", "document", "file", "folder", "memo", "email", "fax", "copy", "print"]},
    "work_business": {"title": "📈 Business Operations", "keywords": ["business", "company", "corporation", "firm", "enterprise", "organization", "industry", "market", "trade", "commerce", "sale", "purchase", "deal", "transaction", "contract", "agreement"]},
    
    "emotions_positive": {"title": "😊 Positive Emotions", "keywords": ["happy", "joy", "glad", "pleased", "delighted", "excited", "cheerful", "merry", "proud", "satisfied", "content", "grateful", "thankful", "hopeful", "optimistic", "confident", "brave", "courageous", "calm", "peaceful", "relaxed", "comfortable"]},
    "emotions_negative": {"title": "😢 Negative Emotions", "keywords": ["sad", "unhappy", "miserable", "depressed", "gloomy", "angry", "mad", "furious", "annoyed", "irritated", "afraid", "scared", "terrified", "worried", "anxious", "nervous", "stressed", "disappointed", "frustrated", "confused", "embarrassed", "ashamed", "guilty", "jealous", "envious", "lonely", "bored", "tired", "exhausted"]},
    
    "time_periods": {"title": "⏱️ Time Periods", "keywords": ["period", "era", "age", "epoch", "century", "decade", "year", "month", "week", "day", "hour", "minute", "second", "moment", "instant", "while", "duration"]},
    "time_days": {"title": "📅 Days & Dates", "keywords": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "weekday", "weekend", "today", "yesterday", "tomorrow", "date", "calendar"]},
    "time_seasons": {"title": "🍂 Seasons", "keywords": ["season", "spring", "summer", "autumn", "fall", "winter"]},
    "time_parts": {"title": "🌅 Parts of Day", "keywords": ["morning", "afternoon", "evening", "night", "midnight", "noon", "dawn", "dusk", "twilight", "sunrise", "sunset"]},
    
    "money_currency": {"title": "💵 Money & Currency", "keywords": ["money", "cash", "currency", "coin", "bill", "note", "dollar", "pound", "euro", "yen", "cent", "penny", "dime", "quarter"]},
    "money_banking": {"title": "🏦 Banking & Finance", "keywords": ["bank", "account", "deposit", "withdraw", "transfer", "loan", "mortgage", "interest", "rate", "credit", "debit", "check", "cheque"]},
    "money_business": {"title": "💰 Business Finance", "keywords": ["price", "cost", "value", "worth", "expensive", "cheap", "profit", "loss", "income", "expense", "revenue", "budget", "salary", "wage", "pay", "payment", "fee", "charge", "tax"]},
    
    "communication_speaking": {"title": "🗣️ Speaking & Talking", "keywords": ["speak", "talk", "say", "tell", "utter", "pronounce", "articulate", "voice", "express", "communicate", "converse", "chat", "discuss", "argue", "debate", "negotiate", "persuade", "convince"]},
    "communication_writing": {"title": "✍️ Writing & Text", "keywords": ["write", "compose", "draft", "edit", "revise", "type", "print", "publish", "text", "word", "sentence", "paragraph", "page", "chapter", "article", "essay", "story", "novel", "poem", "letter", "note", "message"]},
    "communication_listening": {"title": "👂 Listening & Hearing", "keywords": ["listen", "hear", "sound", "noise", "voice", "tone", "volume", "loud", "quiet", "silent"]},
    
    "action_movement": {"title": "🏃 Movement & Motion", "keywords": ["move", "go", "come", "walk", "run", "jog", "sprint", "march", "step", "stride", "pace", "climb", "crawl", "creep", "jump", "leap", "hop", "skip", "dance", "slide", "glide", "slip", "fall", "drop", "rise", "ascend", "descend", "enter", "exit", "leave", "arrive", "depart"]},
    "action_physical": {"title": "💪 Physical Actions", "keywords": ["push", "pull", "lift", "carry", "hold", "grab", "grasp", "catch", "throw", "toss", "drop", "pick", "put", "place", "set", "lay", "stand", "sit", "lie", "bend", "stretch", "reach", "touch", "hit", "strike", "punch", "kick", "knock"]},
    "action_cognitive": {"title": "🧠 Mental Actions", "keywords": ["think", "thought", "consider", "contemplate", "ponder", "reflect", "meditate", "reason", "logic", "analyze", "examine", "study", "investigate", "research", "explore", "discover", "find", "search", "seek", "look", "see", "watch", "observe", "notice", "perceive", "recognize", "identify", "understand", "comprehend", "grasp", "realize", "know", "learn", "remember", "recall", "forget", "imagine", "dream", "wonder", "believe", "suppose", "assume", "guess", "expect", "anticipate", "predict", "foresee", "decide", "choose", "select", "determine", "judge", "evaluate", "assess"]},
    
    "qualities_size": {"title": "📏 Size & Dimension", "keywords": ["big", "large", "huge", "enormous", "gigantic", "massive", "small", "little", "tiny", "miniature", "microscopic", "long", "short", "tall", "high", "low", "deep", "shallow", "thick", "thin", "wide", "narrow", "broad"]},
    "qualities_appearance": {"title": "✨ Appearance & Look", "keywords": ["beautiful", "pretty", "handsome", "attractive", "gorgeous", "lovely", "charming", "elegant", "graceful", "ugly", "plain", "ordinary", "clean", "dirty", "neat", "messy", "tidy"]},
    "qualities_texture": {"title": "🤚 Texture & Feel", "keywords": ["soft", "hard", "smooth", "rough", "coarse", "fine", "slippery", "sticky", "wet", "dry", "moist", "damp", "liquid", "solid", "firm", "loose"]},
    "qualities_temperature": {"title": "🌡️ Temperature", "keywords": ["hot", "warm", "cool", "cold", "freezing", "icy", "chilly", "lukewarm", "tepid", "boiling", "scorching"]},
    "qualities_speed": {"title": "⚡ Speed & Pace", "keywords": ["fast", "quick", "rapid", "swift", "speedy", "slow", "sluggish", "gradual"]},
    "qualities_strength": {"title": "💪 Strength & Power", "keywords": ["strong", "powerful", "mighty", "robust", "sturdy", "solid", "firm", "weak", "feeble", "frail", "delicate", "fragile"]},
    "qualities_difficulty": {"title": "🎯 Difficulty Level", "keywords": ["easy", "simple", "straightforward", "elementary", "basic", "difficult", "hard", "tough", "challenging", "complex", "complicated", "intricate"]},
    "qualities_importance": {"title": "⭐ Importance & Value", "keywords": ["important", "significant", "crucial", "vital", "essential", "necessary", "critical", "major", "minor", "trivial", "insignificant", "unimportant"]},
    
    "relationships_family": {"title": "👨‍👩‍👧‍👦 Family Relations", "keywords": ["family", "parent", "father", "dad", "daddy", "mother", "mom", "mommy", "son", "daughter", "brother", "sister", "sibling", "grandfather", "grandpa", "grandmother", "grandma", "grandson", "granddaughter", "uncle", "aunt", "nephew", "niece", "cousin", "husband", "wife", "spouse", "partner"]},
    "relationships_social": {"title": "🤝 Social Relations", "keywords": ["friend", "friendship", "mate", "buddy", "pal", "companion", "colleague", "coworker", "acquaintance", "neighbor", "stranger", "guest", "host", "visitor"]},
    "relationships_romantic": {"title": "❤️ Romantic Relations", "keywords": ["love", "lover", "beloved", "sweetheart", "darling", "romance", "romantic", "kiss", "hug", "embrace", "marry", "marriage", "wedding", "bride", "groom", "divorce", "engagement"]},
    
    "science_fields": {"title": "🔬 Scientific Fields", "keywords": ["science", "physics", "chemistry", "biology", "astronomy", "geology", "ecology", "botany", "zoology", "genetics", "anatomy", "physiology"]},
    "science_concepts": {"title": "⚛️ Scientific Concepts", "keywords": ["theory", "hypothesis", "law", "principle", "fact", "evidence", "proof", "experiment", "research", "study", "observation", "measurement", "analysis", "conclusion", "result", "discovery", "invention", "innovation"]},
    "science_tools": {"title": "🔭 Scientific Tools", "keywords": ["microscope", "telescope", "laboratory", "test tube", "beaker", "flask", "thermometer", "scale", "ruler", "meter"]},
    
    "tech_devices": {"title": "📱 Electronic Devices", "keywords": ["phone", "smartphone", "mobile", "cell", "tablet", "laptop", "computer", "pc", "desktop", "monitor", "screen", "keyboard", "mouse", "printer", "scanner", "camera", "headphone", "speaker"]},
    "tech_internet": {"title": "🌐 Internet & Web", "keywords": ["internet", "web", "website", "page", "link", "url", "browser", "search", "google", "email", "mail", "message", "chat", "social media", "facebook", "twitter", "instagram", "youtube", "blog"]},
    "tech_software": {"title": "💻 Software & Programs", "keywords": ["software", "program", "application", "app", "system", "operating system", "windows", "mac", "linux", "android", "ios", "file", "folder", "document", "data", "database", "code", "programming", "developer"]},
    "tech_networks": {"title": "📡 Networks & Communication", "keywords": ["network", "wifi", "wireless", "connection", "signal", "bandwidth", "server", "cloud", "online", "offline", "download", "upload", "stream"]},
    
    "sports_team": {"title": "⚽ Team Sports", "keywords": ["football", "soccer", "basketball", "volleyball", "baseball", "hockey", "rugby", "cricket", "team", "player", "coach", "referee", "match", "game", "league", "championship", "tournament"]},
    "sports_individual": {"title": "🏃 Individual Sports", "keywords": ["running", "jogging", "marathon", "swimming", "diving", "cycling", "tennis", "golf", "boxing", "wrestling", "martial arts", "karate", "judo", "taekwondo", "gymnastics", "yoga", "skiing", "skating"]},
    "sports_equipment": {"title": "🏀 Sports Equipment", "keywords": ["ball", "bat", "racket", "club", "stick", "puck", "net", "goal", "hoop", "basket", "glove", "helmet", "pad", "uniform", "jersey"]},
    
    "health_conditions": {"title": "🤒 Health Conditions", "keywords": ["disease", "illness", "sickness", "disorder", "syndrome", "condition", "symptom", "pain", "ache", "fever", "cold", "flu", "cough", "headache", "stomachache", "infection", "inflammation", "allergy", "asthma", "diabetes", "cancer", "heart disease", "stroke"]},
    "health_treatment": {"title": "💊 Medical Treatment", "keywords": ["treatment", "therapy", "cure", "remedy", "medicine", "drug", "pill", "tablet", "capsule", "injection", "vaccine", "dose", "prescription", "surgery", "operation", "procedure", "examination", "diagnosis", "test", "scan", "x-ray", "ultrasound"]},
    "health_professionals": {"title": "👨‍⚕️ Medical Professionals", "keywords": ["doctor", "physician", "surgeon", "specialist", "nurse", "dentist", "therapist", "pharmacist", "paramedic", "medic"]},
    
    "arts_visual": {"title": "🎨 Visual Arts", "keywords": ["art", "painting", "drawing", "sketch", "portrait", "landscape", "sculpture", "statue", "craft", "pottery", "ceramics", "photography", "picture", "image", "illustration"]},
    "arts_performing": {"title": "🎭 Performing Arts", "keywords": ["theater", "theatre", "drama", "play", "performance", "act", "scene", "stage", "actor", "actress", "director", "audience", "applause", "curtain"]},
    "arts_music": {"title": "🎵 Music & Sound", "keywords": ["music", "musical", "song", "melody", "tune", "rhythm", "beat", "tempo", "note", "chord", "harmony", "symphony", "orchestra", "band", "singer", "musician", "composer", "concert", "performance", "instrument", "piano", "guitar", "violin", "drum", "trumpet", "flute"]},
    "arts_dance": {"title": "💃 Dance", "keywords": ["dance", "dancing", "dancer", "ballet", "waltz", "tango", "salsa", "hip hop", "choreography", "routine", "step", "move"]},
    "arts_literature": {"title": "📚 Literature", "keywords": ["literature", "book", "novel", "story", "tale", "narrative", "fiction", "nonfiction", "prose", "poetry", "poem", "verse", "rhyme", "author", "writer", "poet", "playwright", "genre", "classic"]},
    
    "law_crime": {"title": "⚖️ Crime & Law", "keywords": ["crime", "criminal", "offense", "felony", "misdemeanor", "theft", "robbery", "burglary", "fraud", "murder", "assault", "abuse", "violence", "victim", "suspect", "witness", "evidence", "clue"]},
    "law_justice": {"title": "👨‍⚖️ Justice System", "keywords": ["law", "legal", "justice", "court", "trial", "case", "lawsuit", "judge", "jury", "lawyer", "attorney", "prosecutor", "defense", "verdict", "sentence", "punishment", "penalty", "fine", "prison", "jail", "arrest", "custody"]},
    "law_rights": {"title": "📜 Rights & Freedoms", "keywords": ["right", "freedom", "liberty", "privilege", "duty", "obligation", "responsibility", "rule", "regulation", "code", "constitution", "amendment", "law", "legislation", "statute", "act"]},
    
    "politics_government": {"title": "🏛️ Government & Politics", "keywords": ["government", "state", "nation", "country", "politics", "political", "policy", "administration", "authority", "power", "regime", "rule", "govern", "leadership"]},
    "politics_elections": {"title": "🗳️ Elections & Voting", "keywords": ["election", "vote", "voting", "ballot", "poll", "campaign", "candidate", "nominee", "party", "democrat", "republican", "liberal", "conservative"]},
    "politics_officials": {"title": "👔 Political Officials", "keywords": ["president", "prime minister", "minister", "secretary", "governor", "mayor", "senator", "congressman", "representative", "delegate", "ambassador", "diplomat", "official"]},
    
    "religion_beliefs": {"title": "🙏 Religious Beliefs", "keywords": ["religion", "religious", "belief", "faith", "spiritual", "sacred", "holy", "divine", "god", "goddess", "deity", "worship", "pray", "prayer", "ritual", "ceremony", "tradition"]},
    "religion_places": {"title": "⛪ Religious Places", "keywords": ["church", "chapel", "cathedral", "temple", "mosque", "synagogue", "shrine", "monastery", "abbey", "convent"]},
    "religion_people": {"title": "🧑‍🦳 Religious People", "keywords": ["priest", "minister", "pastor", "reverend", "monk", "nun", "rabbi", "imam", "clergy", "congregation", "believer", "follower", "disciple", "saint", "angel"]},
    
    "grammar_parts": {"title": "📝 Parts of Speech", "keywords": ["noun", "verb", "adjective", "adverb", "pronoun", "preposition", "conjunction", "article", "interjection"]},
    "grammar_tenses": {"title": "⏰ Verb Tenses", "keywords": ["present", "past", "future", "tense", "simple", "continuous", "perfect", "progressive"]},
    "grammar_structure": {"title": "🏗️ Sentence Structure", "keywords": ["sentence", "clause", "phrase", "subject", "predicate", "object", "complement", "modifier", "punctuation", "comma", "period", "question mark", "exclamation"]},
    
    "general_misc": {"title": "📦 General & Miscellaneous", "keywords": []}  # Catch-all for remaining words
}

def load_database():
    with open("_categories_with_arabic.json", 'r', encoding='utf-8') as f:
        return json.load(f)

def save_database(db):
    with open("_categories_with_arabic.json", 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def translate_all_words(db):
    """Add massive translations"""
    count = 0
    for category in db.values():
        for word in category.get('words', []):
            en = word.get('en', '').lower()
            ar = word.get('ar', '')
            if ar == word.get('en', '') or not ar:
                if en in MEGA_TRANSLATIONS:
                    word['ar'] = MEGA_TRANSLATIONS[en]
                    count += 1
    return count

def reorganize_into_mega_categories(db):
    """Break down into 100+ specific categories"""
    # Initialize new categories
    for cat_key, cat_data in MEGA_CATEGORIES.items():
        if cat_key not in db:
            db[cat_key] = {
                "title": cat_data["title"],
                "words": []
            }
    
    # Reorganize all words from "other" category
    if 'other' in db:
        other_words = db['other']['words']
        remaining = []
        moved = 0
        
        for word in other_words:
            en = word.get('en', '').lower()
            categorized = False
            
            # Try to match with mega categories
            for cat_key, cat_data in MEGA_CATEGORIES.items():
                keywords = cat_data.get("keywords", [])
                if not keywords:  # Skip general_misc
                    continue
                    
                # Check if word matches any keyword
                if en in keywords or any(kw in en for kw in keywords if len(kw) > 3):
                    db[cat_key]['words'].append(word)
                    moved += 1
                    categorized = True
                    break
            
            if not categorized:
                remaining.append(word)
        
        # Put remaining in general_misc
        if 'general_misc' in db:
            db['general_misc']['words'] = remaining
        else:
            db['other']['words'] = remaining
    
    return moved

def main():
    print("🚀 MASSIVE ENHANCEMENT STARTING...")
    print("="*60)
    
    db = load_database()
    
    print("\n📖 Step 1: Adding comprehensive translations...")
    trans_count = translate_all_words(db)
    print(f"✅ Added {trans_count} new translations")
    
    print("\n🗂️ Step 2: Creating 100+ specialized categories...")
    moved_count = reorganize_into_mega_categories(db)
    print(f"✅ Reorganized {moved_count} words into specific categories")
    
    print("\n💾 Step 3: Saving enhanced database...")
    save_database(db)
    
    # Stats
    total_words = sum(len(cat['words']) for cat in db.values())
    total_trans = sum(sum(1 for w in cat['words'] if w.get('ar') and w['ar'] != w['en']) for cat in db.values())
    
    print("\n" + "="*60)
    print("🎉 ENHANCEMENT COMPLETE!")
    print("="*60)
    print(f"📊 Total Categories: {len(db)}")
    print(f"📚 Total Words: {total_words}")
    print(f"✅ Translated: {total_trans} ({(total_trans/total_words*100):.1f}%)")
    print(f"⏳ Remaining: {total_words - total_trans}")
    print("="*60)

if __name__ == '__main__':
    main()
