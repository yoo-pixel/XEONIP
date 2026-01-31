// Programs Level Page JavaScript

// Determine which level we're on based on URL
const currentLevel = (() => {
    const path = window.location.pathname;
    if (path.includes('top-tier')) return 'topTier';
    if (path.includes('achievable')) return 'achievable';
    if (path.includes('accessible')) return 'accessible';
    return 'topTier';
})();

// Get programs for current level
let allPrograms = programsDatabase[currentLevel] || [];
let filteredPrograms = [...allPrograms];

// DOM Elements
const programsGrid = document.getElementById('programsGrid');
const filterPanel = document.getElementById('filterPanel');
const filterToggle = document.getElementById('filterToggle');
const clearFiltersBtn = document.getElementById('clearFilters');
const programModal = document.getElementById('programModal');
const modalClose = document.getElementById('modalClose');
const modalBody = document.getElementById('modalBody');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    renderPrograms();
    setupFilters();
    setupModal();
    setupMobileFilter();
});

// Render programs to the grid
function renderPrograms() {
    if (filteredPrograms.length === 0) {
        programsGrid.innerHTML = `
            <div class="no-results">
                <p>No programs match your filters.</p>
                <button onclick="clearAllFilters()" class="clear-button">Clear all filters</button>
            </div>
        `;
        return;
    }

    programsGrid.innerHTML = filteredPrograms.map(program => `
        <div class="program-card" data-program-id="${program.id}">
            <div class="program-header">
                <h3 class="program-name">${program.name}</h3>
                <div class="program-tags">
                    <span class="program-tag program-tag-${program.type}">${formatTag(program.type)}</span>
                    <span class="program-tag program-tag-${program.cost}">${formatTag(program.cost)}</span>
                </div>
            </div>
            <p class="program-institution">${program.institution}</p>
            <p class="program-description">${program.description}</p>
            <div class="program-meta">
                <span class="meta-item">
                    <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                    ${program.duration}
                </span>
                <span class="meta-item">
                    <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                    </svg>
                    ${formatTag(program.location)}
                </span>
            </div>
            <div class="program-actions">
                <button class="btn-primary" onclick="openProgramModal('${program.id}')">View Details</button>
                <a href="${program.website}" target="_blank" class="btn-secondary" rel="noopener noreferrer">Visit Website →</a>
            </div>
        </div>
    `).join('');
}

// Format tags for display
function formatTag(tag) {
    const tagMap = {
        'competition': 'Competition',
        'summer': 'Summer Program',
        'research': 'Research',
        'free': 'Free',
        'paid-aid': 'Paid (Aid Available)',
        'online': 'Online',
        'on-campus': 'On-Campus',
        'international': 'International',
        'stem': 'STEM',
        'humanities': 'Humanities',
        'interdisciplinary': 'Interdisciplinary'
    };
    return tagMap[tag] || tag;
}

// Setup filter functionality
function setupFilters() {
    const filterInputs = filterPanel.querySelectorAll('input[type="checkbox"]');

    filterInputs.forEach(input => {
        input.addEventListener('change', applyFilters);
    });

    clearFiltersBtn.addEventListener('click', clearAllFilters);
}

// Apply filters
function applyFilters() {
    const activeFilters = {
        type: [],
        cost: [],
        location: [],
        field: []
    };

    // Collect active filters
    filterPanel.querySelectorAll('input[type="checkbox"]:checked').forEach(input => {
        const category = input.name;
        const value = input.value;
        if (activeFilters[category]) {
            activeFilters[category].push(value);
        }
    });

    // Filter programs
    filteredPrograms = allPrograms.filter(program => {
        // If no filters in a category, don't filter by it
        for (let category in activeFilters) {
            if (activeFilters[category].length > 0) {
                if (!activeFilters[category].includes(program[category])) {
                    return false;
                }
            }
        }
        return true;
    });

    renderPrograms();
}

// Clear all filters
function clearAllFilters() {
    filterPanel.querySelectorAll('input[type="checkbox"]').forEach(input => {
        input.checked = false;
    });
    filteredPrograms = [...allPrograms];
    renderPrograms();
}

// Open program detail modal
function openProgramModal(programId) {
    const program = allPrograms.find(p => p.id === programId);
    if (!program) return;

    modalBody.innerHTML = `
        <div class="program-detail">
            <div class="program-detail-header">
                <h2>${program.name}</h2>
                <p class="detail-institution">${program.institution}</p>
            </div>

            <div class="program-tags">
                <span class="program-tag program-tag-${program.type}">${formatTag(program.type)}</span>
                <span class="program-tag program-tag-${program.cost}">${formatTag(program.cost)}</span>
                <span class="program-tag program-tag-${program.field}">${formatTag(program.field)}</span>
            </div>

            <div class="detail-section">
                <h3>Overview</h3>
                <p>${program.description}</p>
            </div>

            <div class="detail-grid">
                <div class="detail-section">
                    <h3>Duration</h3>
                    <p>${program.duration}</p>
                </div>

                <div class="detail-section">
                    <h3>Location</h3>
                    <p>${formatTag(program.location)}</p>
                </div>

                <div class="detail-section">
                    <h3>Dates</h3>
                    <p>${program.dates}</p>
                </div>

                <div class="detail-section">
                    <h3>Cost</h3>
                    <p>${formatTag(program.cost)}</p>
                </div>
            </div>

            <div class="detail-section">
                <h3>Eligibility</h3>
                <p>${program.eligibility}</p>
            </div>

            <div class="detail-section">
                <h3>Financial Aid</h3>
                <p>${program.financialAid}</p>
            </div>

            <div class="detail-actions">
                <a href="${program.website}" target="_blank" class="btn-primary" rel="noopener noreferrer">
                    Visit Official Website →
                </a>
            </div>
        </div>
    `;

    programModal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// Setup modal close functionality
function setupModal() {
    modalClose.addEventListener('click', closeModal);

    programModal.addEventListener('click', (e) => {
        if (e.target === programModal) {
            closeModal();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && programModal.classList.contains('active')) {
            closeModal();
        }
    });
}

function closeModal() {
    programModal.classList.remove('active');
    document.body.style.overflow = '';
}

// Setup mobile filter toggle
function setupMobileFilter() {
    if (filterToggle) {
        filterToggle.addEventListener('click', () => {
            filterPanel.classList.toggle('mobile-active');
        });

        // Close filter panel when clicking outside on mobile
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                if (!filterPanel.contains(e.target) && !filterToggle.contains(e.target)) {
                    filterPanel.classList.remove('mobile-active');
                }
            }
        });
    }
}