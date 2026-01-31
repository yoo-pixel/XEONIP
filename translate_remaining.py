#!/usr/bin/env python3
"""
Translate all remaining untranslated words in vocabulary-portal-data.json
Uses deep-translator library for reliable English to Arabic translation
"""

import json
import time
from pathlib import Path

try:
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False
    print("deep-translator not installed. Installing...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "deep-translator"])
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True

def translate_word(word, translator):
    """Translate a single English word to Arabic with error handling"""
    try:
        # Skip if already translated
        if not word:
            return ""
        
        # Handle special cases
        special_translations = {
            "n't": "ليس",
            "vs": "مقابل",
            "ie": "أي",
            "etc": "إلخ",
            "ok": "موافق",
            "okay": "موافق",
            "AM": "صباحاً",
            "PM": "مساءً",
            "TV": "تلفاز",
            "PC": "حاسوب",
            "DNA": "الحمض النووي",
            "CEO": "المدير التنفيذي",
            "AIDS": "الإيدز",
            "Mr": "السيد",
            "Mrs": "السيدة",
            "Ms": "الآنسة",
        }
        
        if word in special_translations:
            return special_translations[word]
        
        # Translate using Google Translator
        translation = translator.translate(word)
        
        # Small delay to avoid rate limiting
        time.sleep(0.1)
        
        return translation if translation else ""
        
    except Exception as e:
        print(f"Error translating '{word}': {e}")
        return ""

def main():
    """Main translation function"""
    input_file = Path("vocabulary-portal-data.json")
    output_file = Path("vocabulary-portal-data.json")
    
    if not input_file.exists():
        print(f"Error: {input_file} not found!")
        return
    
    print("Loading vocabulary data...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Initialize translator
    print("Initializing translator...")
    translator = GoogleTranslator(source='en', target='ar')
    
    # Count untranslated words
    total_untranslated = 0
    total_words = 0
    
    for level_name, level_data in data['levels'].items():
        for category_name, words_list in level_data['categories'].items():
            for word_obj in words_list:
                total_words += 1
                if word_obj['arabic'] == '':
                    total_untranslated += 1
    
    print(f"\nFound {total_untranslated} untranslated words out of {total_words} total")
    print("Starting translation...\n")
    
    # Translate missing words
    translated_count = 0
    
    for level_name, level_data in data['levels'].items():
        print(f"Processing level: {level_name.upper()}")
        
        for category_name, words_list in level_data['categories'].items():
            for word_obj in words_list:
                if word_obj['arabic'] == '':
                    english_word = word_obj['english']
                    
                    # Translate
                    arabic_translation = translate_word(english_word, translator)
                    
                    if arabic_translation:
                        word_obj['arabic'] = arabic_translation
                        translated_count += 1
                        
                        # Progress update every 10 words
                        if translated_count % 10 == 0:
                            print(f"  Translated {translated_count}/{total_untranslated} words...")
    
    # Update statistics
    data['translated_words'] = total_words
    
    for level_name, level_data in data['levels'].items():
        translated_in_level = sum(
            1 for words_list in level_data['categories'].values()
            for word in words_list if word['arabic'] != ''
        )
        level_data['translated_words'] = translated_in_level
    
    # Save updated data
    print(f"\nSaving translations...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Successfully translated {translated_count} words!")
    print(f"✓ Total translated: {total_words}/{total_words}")
    print(f"✓ Output saved to: {output_file}")

if __name__ == "__main__":
    main()
