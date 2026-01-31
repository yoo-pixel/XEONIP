// Vocabulary Loader - Dynamically loads and displays vocabulary words from JSON

class VocabularyLoader {
    constructor(dataFilePath = 'vocabulary-complete.json') {
        this.dataFilePath = dataFilePath;
        this.vocabularyData = null;
    }

    // Load vocabulary data from JSON file
    async loadData() {
        try {
            const response = await fetch(this.dataFilePath);
            if (!response.ok) throw new Error('Failed to load vocabulary data');
            this.vocabularyData = await response.json();
            return this.vocabularyData;
        } catch (error) {
            console.error('Error loading vocabulary:', error);
            return null;
        }
    }

    // Get all words for a specific category
    getCategory(level, categoryName) {
        if (!this.vocabularyData || !this.vocabularyData[level]) {
            return [];
        }
        return this.vocabularyData[level][categoryName] || [];
    }

    // Get all categories for a level
    getCategories(level) {
        if (!this.vocabularyData || !this.vocabularyData[level]) {
            return {};
        }
        return this.vocabularyData[level];
    }

    // Get word count for a category
    getWordCount(level, categoryName) {
        return this.getCategory(level, categoryName).length;
    }

    // Render words in a container
    renderWords(container, words, language = 'both') {
        if (!container) return;

        container.innerHTML = '';

        words.forEach((word, index) => {
            const wordRow = document.createElement('div');
            wordRow.className = 'word-row';
            wordRow.style.animationDelay = `${index * 0.05}s`;

            if (language === 'both' || language === 'english') {
                const englishDiv = document.createElement('div');
                englishDiv.className = 'word-english';
                englishDiv.innerHTML = `
          <div class="label">ENGLISH</div>
          <div class="word">${word.english}</div>
        `;
                wordRow.appendChild(englishDiv);
            }

            if (language === 'both' || language === 'arabic') {
                const arabicDiv = document.createElement('div');
                arabicDiv.className = 'word-arabic';
                arabicDiv.innerHTML = `
          <div class="label">ARABIC</div>
          <div class="word">${word.arabic}</div>
        `;
                wordRow.appendChild(arabicDiv);
            }

            container.appendChild(wordRow);
        });
    }

    // Get total word count for a level
    getTotalWords(level) {
        const categories = this.getCategories(level);
        let total = 0;
        for (const categoryName in categories) {
            total += categories[categoryName].length;
        }
        return total;
    }

    // Get all words across all categories
    getAllWords(level) {
        const categories = this.getCategories(level);
        const allWords = [];
        for (const categoryName in categories) {
            allWords.push(...categories[categoryName]);
        }
        return allWords;
    }

    // Search words (partial match in English or Arabic)
    searchWords(searchTerm, level = null) {
        const results = [];
        const searchLower = searchTerm.toLowerCase();

        const levelsToSearch = level ? [level] : Object.keys(this.vocabularyData);

        for (const lv of levelsToSearch) {
            const categories = this.getCategories(lv);
            for (const categoryName in categories) {
                const words = categories[categoryName];
                words.forEach(word => {
                    if (word.english.toLowerCase().includes(searchLower) ||
                        word.arabic.includes(searchTerm)) {
                        results.push({
                            level: lv,
                            category: categoryName,
                            ...word
                        });
                    }
                });
            }
        }

        return results;
    }

    // Export data as CSV
    exportAsCSV(level = null) {
        let csv = 'Level,Category,English,Arabic\n';

        const levelsToExport = level ? [level] : Object.keys(this.vocabularyData);

        for (const lv of levelsToExport) {
            const categories = this.getCategories(lv);
            for (const categoryName in categories) {
                const words = categories[categoryName];
                words.forEach(word => {
                    csv += `${lv},${categoryName},"${word.english}","${word.arabic}"\n`;
                });
            }
        }

        return csv;
    }
}

// Initialize loader globally
const vocabularyLoader = new VocabularyLoader('vocabulary-complete.json');

// Auto-load data when page loads
document.addEventListener('DOMContentLoaded', async() => {
    await vocabularyLoader.loadData();
    console.log('Vocabulary data loaded successfully');
});