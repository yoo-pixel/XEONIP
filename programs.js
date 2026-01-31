// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// PROGRAMS PAGE - FILTER & DISPLAY LOGIC
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

// Sample program data
const programsData = {
    top: [{
            id: 1,
            name: "Research Science Institute (RSI)",
            institution: "MIT & Center for Excellence in Education",
            description: "Six-week intensive research program connecting exceptional students with STEM professionals for independent research projects.",
            duration: "6 weeks",
            cost: "Free",
            location: "On-Campus",
            type: "research",
            field: "stem",
            eligibility: "High school juniors with exceptional STEM achievement",
            dates: "Late June - Early August",
            website: "https://www.cee.org/rsi",
            fullDescription: "The Research Science Institute is the premier summer research program for high school students. Participants conduct original research in mathematics, science, and engineering under the guidance of mentors from MIT and other leading institutions.",
            aid: "Fully funded including travel, room, and board for all admitted students."
        },
        {
            id: 2,
            name: "Telluride Association Summer Programs (TASP/TASS)",
            institution: "Telluride Association",
            description: "Free six-week humanities and social sciences seminar programs for high-achieving high school juniors.",
            duration: "6 weeks",
            cost: "Free",
            location: "On-Campus",
            type: "summer",
            field: "humanities",
            eligibility: "Rising high school seniors with strong critical thinking skills",
            dates: "Late June - Early August",
            website: "https://www.tellurideassociation.org/",
            fullDescription: "TASP and TASS offer intellectually curious students the opportunity to engage in intensive seminars on diverse topics in humanities, social sciences, and cultural studies. Programs are held at university campuses and include group discussions, lectures, and collaborative learning.",
            aid: "Completely free including all expenses."
        }
    ],
    achievable: [{
            id: 3,
            name: "Stanford Pre-Collegiate Summer Institutes",
            institution: "Stanford University",
            description: "Academic courses and research opportunities for motivated high school students interested in STEM and humanities.",
            duration: "3-4 weeks",
            cost: "Paid (Aid Available)",
            location: "On-Campus",
            type: "summer",
            field: "interdisciplinary",
            eligibility: "Current high school students grades 9-11",
            dates: "June - August (multiple sessions)",
            website: "https://summer.stanford.edu/",
            fullDescription: "Stanford Summer Session offers courses taught by Stanford faculty and instructors, allowing students to experience college-level academics while living on campus. Topics range from artificial intelligence to creative writing.",
            aid: "Need-based financial aid available covering tuition and fees."
        },
        {
            id: 4,
            name: "Google Code-in",
            institution: "Google",
            description: "Online open-source coding competition for students aged 13-17 to work with open source organizations.",
            duration: "7 weeks",
            cost: "Free",
            location: "Online",
            type: "competition",
            field: "stem",
            eligibility: "Students aged 13-17 with basic programming knowledge",
            dates: "October - December (annual)",
            website: "https://codein.withgoogle.com/",
            fullDescription: "Students complete tasks in categories like code, documentation, quality assurance, design, and outreach for various open-source projects. Grand prize winners receive a trip to Google headquarters.",
            aid: "Free to participate with prizes for top performers."
        }
    ],
    accessible: [{
            id: 5,
            name: "Coursera High School Courses",
            institution: "Coursera & Partner Universities",
            description: "Self-paced online courses from top universities covering various academic subjects with certificates upon completion.",
            duration: "Flexible (4-12 weeks typical)",
            cost: "Free",
            location: "Online",
            type: "summer",
            field: "interdisciplinary",
            eligibility: "Open to all high school students",
            dates: "Year-round enrollment",
            website: "https://www.coursera.org/",
            fullDescription: "Access university-level courses in computer science, mathematics, humanities, social sciences, and more. Many courses offer free audit options with certificates available for a fee.",
            aid: "Financial aid available for paid certificates."
        },
        {
            id: 6,
            name: "Khan Academy",
            institution: "Khan Academy",
            description: "Free educational platform offering practice exercises and instructional videos across all subjects.",
            duration: "Self-paced",
            cost: "Free",
            location: "Online",
            type: "research",
            field: "interdisciplinary",
            eligibility: "Open to all students",
            dates: "Available year-round",
            website: "https://www.khanacademy.org/",
            fullDescription: "Comprehensive learning platform covering math, science, humanities, test prep, and more. Personalized learning dashboards track progress and identify knowledge gaps.",
            aid: "Completely free for all users."
        },
        {
            id: 7,
            name: "Future Business Leaders of America (FBLA)",
            institution: "FBLA-PBL",
            description: "Student organization offering business competitions, leadership conferences, and networking opportunities.",
            duration: "Year-round",
            cost: "Paid (Aid Available)",
            location: "International",
            type: "competition",
            field: "interdisciplinary",
            eligibility: "Middle and high school students",
            dates: "School year + summer conferences",
            website: "https://www.fbla-pbl.org/",
            fullDescription: "Members compete in business-related events at local, state, and national levels. Leadership development workshops and scholarship opportunities available.",
            aid: "Membership fees vary by chapter; some scholarships available."
        }
    ]
};

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// INITIALIZE PAGE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

document.addEventListener('DOMContentLoaded', function() {
    renderPrograms();
    initializeFilters();
    initializeModal();
    initializeMobileFilter();
});

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// RENDER PROGRAMS
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

function renderPrograms() {
    renderTier('topTierPrograms', programsData.top);
    renderTier('achievablePrograms', programsData.achievable);
    renderTier('accessiblePrograms', programsData.accessible);
}

function renderTier(containerId, programs) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = programs.map(program => createProgramCard(program)).join('');

    // Attach click handlers
    container.querySelectorAll('.program-card').forEach(card => {
        card.addEventListener('click', function() {
            const programId = parseInt(this.dataset.id);
            openProgramModal(programId);
        });
    });
}

function createProgramCard(program) {
    return `
        <div class="program-card" 
             data-id="${program.id}"
             data-type="${program.type}"
             data-cost="${program.cost.toLowerCase().includes('free') ? 'free' : 'paid-aid'}"
             data-location="${program.location.toLowerCase().replace(' ', '-')}"
             data-field="${program.field}">
            <div class="program-header">
                <h3 class="program-name">${program.name}</h3>
                <p class="program-institution">${program.institution}</p>
            </div>
            <p class="program-description">${program.description}</p>
            <div class="program-meta">
                <div class="meta-item">
                    <span class="meta-label">Duration:</span>
                    <span class="meta-value">${program.duration}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Cost:</span>
                    <span class="meta-value">${program.cost}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Location:</span>
                    <span class="meta-value">${program.location}</span>
                </div>
            </div>
            <div class="program-actions">
                <button class="btn btn-primary" onclick="event.stopPropagation(); openProgramModal(${program.id})">View Details</button>
                <a href="${program.website}" class="btn btn-secondary" target="_blank" onclick="event.stopPropagation()">Visit Website</a>
            </div>
        </div>
    `;
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// FILTER FUNCTIONALITY
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

function initializeFilters() {
    const filterCheckboxes = document.querySelectorAll('.filter-option input[type="checkbox"]');
    const clearButton = document.getElementById('clearFilters');

    filterCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', applyFilters);
    });

    clearButton.addEventListener('click', clearAllFilters);
}

function applyFilters() {
    const activeFilters = {
        type: [],
        cost: [],
        location: [],
        field: []
    };

    // Collect active filters
    document.querySelectorAll('.filter-option input[type="checkbox"]:checked').forEach(checkbox => {
        const category = checkbox.name;
        const value = checkbox.value;
        activeFilters[category].push(value);
    });

    // Filter programs
    const allCards = document.querySelectorAll('.program-card');

    allCards.forEach(card => {
        const cardType = card.dataset.type;
        const cardCost = card.dataset.cost;
        const cardLocation = card.dataset.location;
        const cardField = card.dataset.field;

        const matchesType = activeFilters.type.length === 0 || activeFilters.type.includes(cardType);
        const matchesCost = activeFilters.cost.length === 0 || activeFilters.cost.includes(cardCost);
        const matchesLocation = activeFilters.location.length === 0 || activeFilters.location.includes(cardLocation);
        const matchesField = activeFilters.field.length === 0 || activeFilters.field.includes(cardField);

        if (matchesType && matchesCost && matchesLocation && matchesField) {
            card.classList.remove('hidden');
        } else {
            card.classList.add('hidden');
        }
    });
}

function clearAllFilters() {
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(checkbox => {
        checkbox.checked = false;
    });
    applyFilters();
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// MODAL FUNCTIONALITY
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

function initializeModal() {
    const modal = document.getElementById('programModal');
    const closeBtn = document.getElementById('modalClose');

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // ESC key to close
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
}

function openProgramModal(programId) {
    const program = findProgramById(programId);
    if (!program) return;

    const modalBody = document.getElementById('modalBody');
    modalBody.innerHTML = `
        <h2 class="modal-title">${program.name}</h2>
        <p class="modal-institution">${program.institution}</p>

        <div class="detail-section">
            <h3 class="detail-heading">About This Program</h3>
            <p class="detail-text">${program.fullDescription}</p>
        </div>

        <div class="detail-section">
            <h3 class="detail-heading">Eligibility</h3>
            <p class="detail-text">${program.eligibility}</p>
        </div>

        <div class="detail-section">
            <h3 class="detail-heading">Program Details</h3>
            <ul class="detail-list">
                <li><strong>Duration:</strong> ${program.duration}</li>
                <li><strong>Dates:</strong> ${program.dates}</li>
                <li><strong>Cost:</strong> ${program.cost}</li>
                <li><strong>Location:</strong> ${program.location}</li>
            </ul>
        </div>

        <div class="detail-section">
            <h3 class="detail-heading">Financial Aid</h3>
            <p class="detail-text">${program.aid}</p>
        </div>

        <div class="modal-actions">
            <a href="${program.website}" class="btn btn-primary" target="_blank">Visit Official Website</a>
            <button class="btn btn-secondary" onclick="closeModal()">Close</button>
        </div>
    `;

    document.getElementById('programModal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    document.getElementById('programModal').classList.remove('active');
    document.body.style.overflow = '';
}

function findProgramById(id) {
    const allPrograms = [...programsData.top, ...programsData.achievable, ...programsData.accessible];
    return allPrograms.find(p => p.id === id);
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// MOBILE FILTER TOGGLE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

function initializeMobileFilter() {
    const filterToggle = document.getElementById('filterToggle');
    const filterPanel = document.getElementById('filterPanel');

    if (filterToggle && filterPanel) {
        filterToggle.addEventListener('click', function() {
            filterPanel.classList.toggle('active');
        });

        // Close when clicking outside on mobile
        document.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                if (!filterPanel.contains(e.target) && !filterToggle.contains(e.target)) {
                    filterPanel.classList.remove('active');
                }
            }
        });
    }
}