/* ==========================================================================
   RAJ KUMAR — ULTRA-PREMIUM CINEMATIC DEVELOPER PORTFOLIO ENGINE
   Author: Raj Kumar (B.Sc. Computer Science • Full-Stack Developer • AI)
   ========================================================================== */

// ==========================================================================
// CONFIGURABLE PROJECT DEPLOYMENT URLS (Easily replaceable)
// ==========================================================================
const PET_NOVA_URL = "http://10.31.236.34:5000/"; // <-- Replace with your live PET NOVA URL
const ROYAL_ROSE_MILK_URL = "https://royal-rosegunicorn-app-ap.onrender.com"; // Live Render deployment

document.addEventListener("DOMContentLoaded", () => {
    initCinematicCanvas();
    initLoader();
    initNavbar();
    initScrollProgress();
    initCustomCursor();
    initScrollObserver();
    applyProjectUrls();
});

/* --------------------------------------------------------------------------
   1. CINEMATIC BACKGROUND CANVAS (PARTICLES & CONSTELLATION MESH)
   -------------------------------------------------------------------------- */
function initCinematicCanvas() {
    const canvas = document.getElementById("cinematicCanvas");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    let width, height;
    let particles = [];
    let animationFrameId;
    let mouse = { x: null, y: null, radius: 140 };

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }
    resize();
    window.addEventListener("resize", resize);

    window.addEventListener("mousemove", (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });

    window.addEventListener("mouseleave", () => {
        mouse.x = null;
        mouse.y = null;
    });

    const particleCount = Math.min(Math.floor(window.innerWidth / 22), 65);

    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.size = Math.random() * 2 + 0.8;
            this.baseX = this.x;
            this.baseY = this.y;
            this.vx = (Math.random() - 0.5) * 0.45;
            this.vy = (Math.random() - 0.5) * 0.45;
            this.color = Math.random() > 0.4 ? "rgba(212, 154, 112, 0.45)" : "rgba(163, 216, 200, 0.35)";
        }

        update() {
            this.x += this.vx;
            this.y += this.vy;

            if (this.x < 0) this.x = width;
            if (this.x > width) this.x = 0;
            if (this.y < 0) this.y = height;
            if (this.y > height) this.y = 0;

            // Mouse proximity interaction
            if (mouse.x !== null && mouse.y !== null) {
                const dx = mouse.x - this.x;
                const dy = mouse.y - this.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < mouse.radius) {
                    const force = (mouse.radius - dist) / mouse.radius;
                    const fx = (dx / dist) * force * 1.5;
                    const fy = (dy / dist) * force * 1.5;
                    this.x -= fx;
                    this.y -= fy;
                }
            }
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();
        }
    }

    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        // Draw connections
        for (let a = 0; a < particles.length; a++) {
            for (let b = a + 1; b < particles.length; b++) {
                const dx = particles[a].x - particles[b].x;
                const dy = particles[a].y - particles[b].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 130) {
                    const opacity = (1 - dist / 130) * 0.15;
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(184, 115, 74, ${opacity})`;
                    ctx.lineWidth = 0.7;
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }
        }

        // Update and draw particles
        particles.forEach(p => {
            p.update();
            p.draw();
        });

        animationFrameId = requestAnimationFrame(animate);
    }
    animate();

    // Pause canvas if document is hidden to conserve performance
    document.addEventListener("visibilitychange", () => {
        if (document.hidden) {
            cancelAnimationFrame(animationFrameId);
        } else {
            animate();
        }
    });
}

/* --------------------------------------------------------------------------
   2. CINEMATIC STARTUP LOADER (RK MONOGRAM + GEOMETRIC TELEMETRY)
   -------------------------------------------------------------------------- */
function initLoader() {
    const intro = document.getElementById("intro");
    const loaderFill = document.getElementById("loaderFill");
    const statusText = document.getElementById("loaderStatusText");
    const skipBtn = document.getElementById("skipLoaderBtn");

    if (!intro) return;

    // Check if session has already viewed intro
    const hasViewed = sessionStorage.getItem("raj_kumar_portfolio_intro_seen");
    if (hasViewed) {
        intro.classList.add("loader-hidden");
        document.body.classList.add("loaded");
        return;
    }

    const messages = [
        "INITIALIZING...",
        "LOADING EXPERIENCE...",
        "BUILDING DIGITAL SPACE...",
        "WELCOME."
    ];

    let progress = 0;

    function updateProgress(val) {
        progress = Math.min(val, 100);
        if (loaderFill) {
            loaderFill.style.width = `${progress}%`;
        }
        if (statusText) {
            const msgIndex = Math.min(Math.floor((progress / 100) * messages.length), messages.length - 1);
            statusText.textContent = messages[msgIndex];
        }
    }

    let loaderInterval = setInterval(() => {
        const increment = Math.floor(Math.random() * 8) + 6;
        progress += increment;

        if (progress >= 100) {
            updateProgress(100);
            clearInterval(loaderInterval);
            setTimeout(dismissLoader, 350);
        } else {
            updateProgress(progress);
        }
    }, 40);

    function dismissLoader() {
        clearInterval(loaderInterval);
        intro.classList.add("loader-hidden");
        document.body.classList.add("loaded");
        sessionStorage.setItem("raj_kumar_portfolio_intro_seen", "true");
    }

    if (skipBtn) {
        skipBtn.addEventListener("click", dismissLoader);
    }
}

/* --------------------------------------------------------------------------
   3. MINIMALIST STICKY NAVBAR & MOBILE DRAWER
   -------------------------------------------------------------------------- */
function initNavbar() {
    const navbar = document.getElementById("navbar");
    const mobileBtn = document.getElementById("mobileToggleBtn");
    const navLinks = document.getElementById("navLinks");
    const navItems = document.querySelectorAll(".nav-item");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 40) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });

    if (mobileBtn && navLinks) {
        mobileBtn.addEventListener("click", () => {
            navLinks.classList.toggle("mobile-open");
        });

        navItems.forEach(link => {
            link.addEventListener("click", () => {
                navLinks.classList.remove("mobile-open");
            });
        });
    }

    // Scrollspy for active navigation state
    const sections = document.querySelectorAll("section[id]");
    window.addEventListener("scroll", () => {
        let current = "";
        const scrollPos = window.pageYOffset + 240;

        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            if (scrollPos >= top && scrollPos < top + height) {
                current = section.getAttribute("id");
            }
        });

        navItems.forEach(link => {
            link.classList.remove("active");
            if (link.getAttribute("href") === `#${current}`) {
                link.classList.add("active");
            }
        });
    });
}

/* --------------------------------------------------------------------------
   4. SCROLL PROGRESS INDICATOR
   -------------------------------------------------------------------------- */
function initScrollProgress() {
    const progressLine = document.getElementById("scrollProgress");
    if (!progressLine) return;

    window.addEventListener("scroll", () => {
        const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressLine.style.width = `${scrolled}%`;
    });
}

/* --------------------------------------------------------------------------
   5. DESKTOP CONTEXT CURSOR
   -------------------------------------------------------------------------- */
function initCustomCursor() {
    const cursorDot = document.getElementById("cursorDot");
    const cursorRing = document.getElementById("cursorRing");
    const cursorLabel = document.getElementById("cursorLabel");

    if (!cursorDot || !cursorRing) return;

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let ringX = mouseX;
    let ringY = mouseY;

    window.addEventListener("mousemove", (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;

        cursorDot.style.left = `${mouseX}px`;
        cursorDot.style.top = `${mouseY}px`;
    });

    function renderRing() {
        ringX += (mouseX - ringX) * 0.15;
        ringY += (mouseY - ringY) * 0.15;

        cursorRing.style.left = `${ringX}px`;
        cursorRing.style.top = `${ringY}px`;

        requestAnimationFrame(renderRing);
    }
    renderRing();

    // Hover expansions on project media
    const projectFrames = document.querySelectorAll(".project-media-wrapper");
    projectFrames.forEach(frame => {
        frame.addEventListener("mouseenter", () => {
            cursorRing.classList.add("cursor-project");
            if (cursorLabel) cursorLabel.textContent = "VIEW ↗";
        });
        frame.addEventListener("mouseleave", () => {
            cursorRing.classList.remove("cursor-project");
            if (cursorLabel) cursorLabel.textContent = "";
        });
    });

    // General interactive hover expansions
    const interactives = document.querySelectorAll(
        "a, button, input, select, .skill-card, .stat-card, .channel-card-row, .timeline-card, .pillar-item"
    );
    interactives.forEach(el => {
        el.addEventListener("mouseenter", () => cursorRing.classList.add("cursor-hover"));
        el.addEventListener("mouseleave", () => cursorRing.classList.remove("cursor-hover"));
    });
}

/* --------------------------------------------------------------------------
   6. SCROLL REVEAL OBSERVER
   -------------------------------------------------------------------------- */
function initScrollObserver() {
    const targets = document.querySelectorAll(
        ".manifesto-content-col, .about-stats-grid, .about-editorial-grid, .skill-card, .project-showcase-entry, .timeline-row, .contact-dramatic-layout"
    );

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08 });

    targets.forEach((el, idx) => {
        el.style.opacity = "0";
        el.style.transform = "translateY(22px)";
        el.style.transition = `opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1) ${Math.min((idx % 4) * 0.08, 0.25)}s, transform 0.7s cubic-bezier(0.16, 1, 0.3, 1) ${Math.min((idx % 4) * 0.08, 0.25)}s`;
        observer.observe(el);
    });
}

/* --------------------------------------------------------------------------
   7. APPLY CONFIGURABLE PROJECT URLS ACROSS DOM
   -------------------------------------------------------------------------- */
function applyProjectUrls() {
    // Pet Nova Elements
    const petNovaUrlDisplay = document.getElementById("petNovaUrlDisplay");
    const petNovaDirectBtn = document.getElementById("petNovaDirectBtn");
    if (petNovaUrlDisplay) {
        petNovaUrlDisplay.href = PET_NOVA_URL;
        petNovaUrlDisplay.textContent = PET_NOVA_URL;
    }
    if (petNovaDirectBtn) {
        petNovaDirectBtn.href = PET_NOVA_URL;
    }

    // Royal Rose Milk Elements
    const royalRoseUrlDisplay = document.getElementById("royalRoseUrlDisplay");
    const royalRoseDirectBtn = document.getElementById("royalRoseDirectBtn");
    if (royalRoseUrlDisplay) {
        royalRoseUrlDisplay.href = ROYAL_ROSE_MILK_URL;
        royalRoseUrlDisplay.textContent = ROYAL_ROSE_MILK_URL;
    }
    if (royalRoseDirectBtn) {
        royalRoseDirectBtn.href = ROYAL_ROSE_MILK_URL;
    }
}

/* --------------------------------------------------------------------------
   8. EXPANDABLE CASE STUDY DRAWER TOGGLE
   -------------------------------------------------------------------------- */
function toggleCaseStudy(drawerId) {
    const drawer = document.getElementById(drawerId);
    if (!drawer) return;

    const btn = event.currentTarget;
    drawer.classList.toggle("open");
    if (btn) btn.classList.toggle("active");
}

/* --------------------------------------------------------------------------
   9. PROJECT SHOWCASE DATA & INTERACTIVE MODAL CONTROLLER
   -------------------------------------------------------------------------- */
const PROJECTS_DATA = {
    petNova: {
        title: "PET NOVA",
        badge: "FLAGSHIP // AI PET CARE PLATFORM",
        heroImg: "images/pet-nexa-showcase.jpg",
        heading: "PET NOVA — AI-Powered Pet-Care Platform",
        description: "PET NOVA is a comprehensive pet-care platform engineered to integrate multiple pet services into a single digital ecosystem. It connects pet parents with grooming appointment scheduling, pet specialist consultations, an integrated product shop, order tracking, and an intelligent AI Pet Health Advisor rule engine.",
        liveUrl: PET_NOVA_URL,
        specs: [
            { label: "PROJECT SERVER", value: PET_NOVA_URL },
            { label: "BACKEND STACK", value: "Python / Flask REST Server" },
            { label: "FRONTEND UI", value: "HTML5, CSS3, JavaScript (ES6+)" },
            { label: "DATABASE", value: "SQLite Relational Store" },
            { label: "AI SUBSYSTEM", value: "Rule-Based Health Advisor" },
            { label: "KEY SERVICES", value: "Grooming, Specialist, Shop, Booking" }
        ],
        features: [
            {
                title: "Pet Grooming Service Booking",
                desc: "Customizable service selection allowing pet parents to choose tailored bathing, trimming, and styling packages."
            },
            {
                title: "Pet Specialist & Appointments",
                desc: "Dedicated veterinary specialist profiles with instant appointment reservation workflows and schedule management."
            },
            {
                title: "Pet Product Shop & Categories",
                desc: "Comprehensive e-commerce catalog featuring categorized products for both dogs and cats with direct checkout."
            },
            {
                title: "AI Pet Advisor",
                desc: "Intelligent health assessment engine analyzing pet vitals and symptoms to output diagnostic advice."
            },
            {
                title: "Order Tracking & Manage Booking",
                desc: "Real-time status tracking for customer orders and dynamic booking modification dashboards."
            },
            {
                title: "Database-Driven Architecture",
                desc: "Robust SQLite schema management tracking inventory, users, appointments, and diagnostic records."
            }
        ],
        codeSnippet: `# ==========================================================
# PET NOVA - Flask Backend API & AI Diagnostic Engine
# ==========================================================
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def evaluate_pet_health(symptoms, activity_level, age):
    """AI Pet Advisor Rule Engine"""
    base_score = 100
    deductions = {
        'lethargy': 20,
        'loss_of_appetite': 25,
        'coughing': 15,
        'dental_plaque': 10,
        'skin_itching': 12
    }
    for symptom in symptoms:
        base_score -= deductions.get(symptom, 5)
    
    if activity_level < 40:
        base_score -= 10
    
    score = max(min(base_score, 100), 20)
    
    if score >= 85:
        verdict = "Optimal Vitality: Pet exhibits healthy biometrics."
    elif score >= 65:
        verdict = "Moderate Health: Routine checkup & hydration recommended."
    else:
        verdict = "Attention Required: Schedule a specialist appointment."
        
    return score, verdict

@app.route('/api/pet/advisor', methods=['POST'])
def run_pet_advisor():
    data = request.get_json()
    symptoms = data.get('symptoms', [])
    activity = int(data.get('activity', 70))
    age = float(data.get('age', 2))
    
    score, verdict = evaluate_pet_health(symptoms, activity, age)
    return jsonify({
        "status": "success",
        "health_score": score,
        "diagnosis": verdict
    }), 200`
    },

    royalRose: {
        title: "ROYAL ROSE MILK",
        badge: "BRAND EXPERIENCE // PRODUCT WEBSITE",
        heroImg: "images/royal-rose-milk.jpg",
        heading: "ROYAL ROSE MILK — Interactive Brand & Product Website",
        description: "ROYAL ROSE MILK is a visually immersive product website created for an artisanal rose-flavoured milk brand, focusing on modern UI design, interactive animations, artisanal flavor customizers, and sensory storytelling.",
        liveUrl: ROYAL_ROSE_MILK_URL,
        specs: [
            { label: "LIVE SERVER", value: ROYAL_ROSE_MILK_URL },
            { label: "FRONTEND CORE", value: "HTML5, CSS3, Tailwind CSS" },
            { label: "INTERACTIONS", value: "Vanilla JavaScript ES6+" },
            { label: "DESIGN SYSTEM", value: "Midnight Emerald & Radiant Copper" },
            { label: "RESPONSIVENESS", value: "100% Mobile & Desktop" },
            { label: "KEY HIGHLIGHTS", value: "Artisanal Flavor Customizer & Cart" }
        ],
        features: [
            {
                title: "Interactive Hero Section",
                desc: "High-impact visual opening with sensory branding, animated typography, and fluid transitions."
            },
            {
                title: "Product Showcase & Customizer",
                desc: "Interactive bottle blend customizer adjusting rose essence, sweetness, and milk richness in real-time."
            },
            {
                title: "Cinematic Storytelling",
                desc: "Sensory brand narrative exploring Damascus rose heritage, artisanal ingredients, and farm milk source."
            },
            {
                title: "Interactive Shopping Experience",
                desc: "Dynamic cart addition, package bundle selection, and instant price breakdown calculation."
            }
        ],
        codeSnippet: `/* ==========================================================
 * ROYAL ROSE MILK — Dynamic Sensory Blend Engine
 * ========================================================== */
const RoseBlendEngine = {
    basePrice: 120, // INR
    calculateBlend(essenceLevel, sweetnessType, milkRichness) {
        let multiplier = 1.0;
        if (essenceLevel > 70) multiplier += 0.25;
        if (sweetnessType === 'Wild Forest Honey') multiplier += 0.18;
        if (milkRichness === 'Almond Milk') multiplier += 0.25;
        
        const finalPrice = Math.round(this.basePrice * multiplier);
        return {
            price: finalPrice,
            flavorNotes: \`Damascus Rose (\${essenceLevel}%), \${sweetnessType}, \${milkRichness}\`
        };
    }
};`
    }
};

let currentActiveProject = "petNova";

function openProjectModal(projectId) {
    const data = PROJECTS_DATA[projectId];
    if (!data) return;

    currentActiveProject = projectId;

    const modal = document.getElementById("projectModalBackdrop");
    const badge = document.getElementById("modalBadge");
    const title = document.getElementById("modalTitle");
    const heroImg = document.getElementById("modalHeroImg");
    const heading = document.getElementById("modalOverviewHeading");
    const desc = document.getElementById("modalOverviewDesc");
    const specGrid = document.getElementById("modalSpecGrid");
    const featGrid = document.getElementById("modalFeaturesGrid");
    const codeSnippet = document.getElementById("modalCodeSnippet");
    const codeLang = document.getElementById("codeLangTitle");

    // Dynamic Live Project Links in Modal
    const headerLiveLink = document.getElementById("modalHeaderLiveLink");
    const overviewLiveAnchor = document.getElementById("modalOverviewLiveAnchor");
    const overviewLiveBtn = document.getElementById("modalOverviewLiveBtn");
    const footerLiveLink = document.getElementById("modalFooterLiveLink");

    if (badge) badge.textContent = data.badge;
    if (title) title.textContent = data.title;
    if (heroImg) heroImg.src = data.heroImg;
    if (heading) heading.textContent = data.heading;
    if (desc) desc.textContent = data.description;

    const liveUrl = data.liveUrl || (projectId === "royalRose" ? ROYAL_ROSE_MILK_URL : PET_NOVA_URL);
    if (headerLiveLink) headerLiveLink.href = liveUrl;
    if (overviewLiveAnchor) {
        overviewLiveAnchor.href = liveUrl;
        overviewLiveAnchor.textContent = liveUrl;
    }
    if (overviewLiveBtn) overviewLiveBtn.href = liveUrl;
    if (footerLiveLink) footerLiveLink.href = liveUrl;

    // Populate specs
    if (specGrid) {
        specGrid.innerHTML = data.specs.map(s => `
            <div class="spec-entry">
                <span>${s.label}</span>
                <strong>${s.value}</strong>
            </div>
        `).join("");
    }

    // Populate features
    if (featGrid) {
        featGrid.innerHTML = data.features.map(f => `
            <div class="feat-item">
                <h5>${f.title}</h5>
                <p>${f.desc}</p>
            </div>
        `).join("");
    }

    // Populate code snippet
    if (codeSnippet) codeSnippet.textContent = data.codeSnippet;
    if (codeLang) codeLang.innerHTML = `<i class="fa-solid fa-terminal"></i> ${projectId === 'petNova' ? 'PET_NOVA_FLASK_API.PY' : 'ROYAL_ROSE_BLEND_ENGINE.JS'}`;

    // Render interactive simulator
    renderProjectSimulator(projectId);

    // Switch to Overview Tab by default
    switchModalTab('tabOverview');

    if (modal) {
        modal.classList.add("open");
        modal.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";
    }
}

function closeProjectModal(event) {
    if (event && event.target !== event.currentTarget && !event.target.closest('.modal-close-button') && !event.target.closest('.btn-footer-close')) {
        return;
    }
    const modal = document.getElementById("projectModalBackdrop");
    if (modal) {
        modal.classList.remove("open");
        modal.setAttribute("aria-hidden", "true");
        document.body.style.overflow = "";
    }
}

function switchModalTab(tabId) {
    const tabPanes = document.querySelectorAll(".tab-pane");
    const tabBtns = document.querySelectorAll(".tab-btn");

    tabPanes.forEach(pane => pane.classList.remove("active"));
    tabBtns.forEach(btn => btn.classList.remove("active"));

    const targetPane = document.getElementById(tabId);
    if (targetPane) targetPane.classList.add("active");

    const btnId = "tabBtn" + tabId.replace("tab", "");
    const targetBtn = document.getElementById(btnId);
    if (targetBtn) targetBtn.classList.add("active");
}

/* --------------------------------------------------------------------------
   10. INTERACTIVE SIMULATOR ENGINES
   -------------------------------------------------------------------------- */
function renderProjectSimulator(projectId) {
    const container = document.getElementById("simulatorContainer");
    if (!container) return;

    if (projectId === "petNova") {
        container.innerHTML = `
            <div class="sim-header-row">
                <span class="sim-heading">PET NOVA AI Diagnostic Simulator</span>
                <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper-main);">REST API TELEMETRY</span>
            </div>
            <div class="sim-layout-grid">
                <div class="sim-control-group">
                    <label>Pet Species &amp; Name:</label>
                    <input type="text" id="simPetName" class="sim-text-input" value="Milo (Golden Retriever)">
                </div>
                <div class="sim-control-group">
                    <label>Reported Symptoms:</label>
                    <select id="simPetSymptoms" class="sim-select-input">
                        <option value="none">Routine Wellness Checkup (No symptoms)</option>
                        <option value="lethargy">Lethargy &amp; Reduced Mobility</option>
                        <option value="loss_of_appetite">Loss of Appetite &amp; Water Avoidance</option>
                        <option value="dental_plaque">Dental Plaque &amp; Bad Breath</option>
                        <option value="skin_itching">Skin Itching &amp; Frequent Scratching</option>
                    </select>
                </div>
                <button class="btn-copper-fill" style="margin-top: 10px; width: 100%; justify-content: center;" onclick="runPetNovaDiagnostic()">
                    <span>RUN AI HEALTH SCAN</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </button>
                <div class="sim-results-pane" id="simPetOutput" style="margin-top: 20px;">
                    <div class="sim-score-ring">
                        <span class="sim-score-digit" id="simScoreNum">94</span>
                    </div>
                    <h5 id="simScoreHeading">Optimal Vitality</h5>
                    <p id="simVerdictText">Pet exhibits high energy and normal biometrics. Routine wellness schedule maintained.</p>
                </div>
            </div>
        `;
    } else {
        container.innerHTML = `
            <div class="sim-header-row">
                <span class="sim-heading">ROYAL ROSE MILK Blend Customizer</span>
                <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper-main);">SENSORY FORMULATION</span>
            </div>
            <div class="sim-layout-grid">
                <div class="sim-control-group">
                    <label>Rose Essence Level: <strong id="simRoseVal" style="color:var(--copper-main);">65%</strong></label>
                    <input type="range" id="simRoseEssence" style="width:100%; accent-color:var(--copper-main);" min="20" max="100" value="65" oninput="updateRoyalRoseCustomizer()">
                </div>
                <div class="sim-control-group">
                    <label>Sweetness Infusion:</label>
                    <select id="simSweetness" class="sim-select-input" onchange="updateRoyalRoseCustomizer()">
                        <option value="Organic Cane Sugar">Organic Cane Sugar</option>
                        <option value="Wild Forest Honey">Wild Forest Honey (+₹20)</option>
                        <option value="Palm Jaggery">Palm Jaggery (+₹15)</option>
                    </select>
                </div>
                <div class="sim-control-group">
                    <label>Milk Base Texture:</label>
                    <select id="simMilkBase" class="sim-select-input" onchange="updateRoyalRoseCustomizer()">
                        <option value="Pure Rich Farm Milk">Pure Rich Farm Milk (Creamy)</option>
                        <option value="Almond Milk">Artisanal Almond Milk (+₹30)</option>
                        <option value="Oat Milk">Velvety Oat Milk (+₹25)</option>
                    </select>
                </div>
                <button class="btn-copper-fill" style="margin-top: 10px; width: 100%; justify-content: center;" onclick="handleRoseOrderSimulation()">
                    <span>TEST CART ADDITION</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </button>
                <div class="sim-results-pane" id="simRoseOutput" style="margin-top: 20px;">
                    <div style="font-family: var(--font-serif); font-size: 38px; color: var(--copper-light);" id="simRosePrice">₹120</div>
                    <h5 id="simRoseBlendName" style="font-family: var(--font-serif); font-size: 18px; margin-top: 4px;">Artisanal Rose Classic</h5>
                    <p id="simRoseDescription" style="font-size: 13px; color: var(--cream-soft);">Handcrafted with 65% Damascus rose extract.</p>
                </div>
            </div>
        `;
    }
}

function runPetNovaDiagnostic() {
    const petName = document.getElementById("simPetName") ? document.getElementById("simPetName").value || "Pet" : "Pet";
    const symptom = document.getElementById("simPetSymptoms") ? document.getElementById("simPetSymptoms").value : "none";
    const scoreNum = document.getElementById("simScoreNum");
    const heading = document.getElementById("simScoreHeading");
    const verdict = document.getElementById("simVerdictText");

    let score = 96;
    let headingText = "Optimal Vitality";
    let descText = `${petName} exhibits excellent telemetry data. All biometric indicators are within healthy thresholds.`;

    if (symptom === "lethargy") {
        score = 74;
        headingText = "Fatigue & Low Activity Alert";
        descText = `${petName} shows reduced mobility score. Recommended action: Increase hydration and monitor body temperature.`;
    } else if (symptom === "loss_of_appetite") {
        score = 68;
        headingText = "Nutritional Imbalance Alert";
        descText = `${petName} is experiencing appetite suppression. Recommended action: Transition to probiotic-rich soft diet.`;
    } else if (symptom === "dental_plaque") {
        score = 82;
        headingText = "Dental Hygiene Advisory";
        descText = `Oral plaque detected. Recommended action: Schedule ultrasonic dental cleaning with a Pet Nova specialist.`;
    } else if (symptom === "skin_itching") {
        score = 78;
        headingText = "Dermatological Irritation";
        descText = `Frequent scratching detected. Recommended action: Hypoallergenic medicated oatmeal bath and omega-3 supplement.`;
    }

    if (scoreNum) scoreNum.textContent = score;
    if (heading) heading.textContent = headingText;
    if (verdict) verdict.textContent = descText;

    showToast(`AI Diagnostic complete for ${petName}! Score: ${score}/100`);
}

function updateRoyalRoseCustomizer() {
    const essenceInput = document.getElementById("simRoseEssence");
    const sweetnessInput = document.getElementById("simSweetness");
    const milkInput = document.getElementById("simMilkBase");

    if (!essenceInput || !sweetnessInput || !milkInput) return;

    const essence = parseInt(essenceInput.value, 10);
    const sweetness = sweetnessInput.value;
    const milk = milkInput.value;

    const roseVal = document.getElementById("simRoseVal");
    const priceEl = document.getElementById("simRosePrice");
    const blendEl = document.getElementById("simRoseBlendName");
    const descEl = document.getElementById("simRoseDescription");

    if (roseVal) roseVal.textContent = `${essence}%`;

    let price = 120;
    if (sweetness.includes("Honey")) price += 20;
    if (sweetness.includes("Jaggery")) price += 15;
    if (milk.includes("Almond")) price += 30;
    if (milk.includes("Oat")) price += 25;

    if (priceEl) priceEl.textContent = `₹${price}`;

    if (blendEl) {
        if (essence >= 80) blendEl.textContent = "Royal Damask Reserve (Intense)";
        else if (essence >= 50) blendEl.textContent = "Artisanal Rose Classic";
        else blendEl.textContent = "Subtle Rose Blossom Blend";
    }

    if (descEl) {
        descEl.textContent = `Handcrafted with ${essence}% Damascus rose extract, blended in ${milk} with ${sweetness}.`;
    }
}

function handleRoseOrderSimulation() {
    const price = document.getElementById("simRosePrice") ? document.getElementById("simRosePrice").textContent : "₹120";
    showToast(`Added custom Royal Rose blend (${price}) to cart!`);
}

/* --------------------------------------------------------------------------
   11. COPY TO CLIPBOARD & TOAST NOTIFICATIONS
   -------------------------------------------------------------------------- */
function copyContactInfo(text, message) {
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(() => {
            showToast(message || "Copied to clipboard!");
        }).catch(() => {
            fallbackCopy(text, message);
        });
    } else {
        fallbackCopy(text, message);
    }
}

function fallbackCopy(text, message) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.opacity = "0";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
        document.execCommand('copy');
        showToast(message || "Copied to clipboard!");
    } catch (err) {
        showToast("Press Ctrl+C to copy: " + text);
    }
    document.body.removeChild(textArea);
}

function copySnippet() {
    const code = document.getElementById("modalCodeSnippet");
    if (code) {
        copyContactInfo(code.textContent, "Architecture snippet copied to clipboard!");
    }
}

function showToast(message) {
    const toast = document.getElementById("toastNotification");
    const toastMsg = document.getElementById("toastMessage");

    if (!toast) return;
    if (toastMsg) toastMsg.textContent = message;

    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2800);
}

/* --------------------------------------------------------------------------
   12. RESUME DOWNLOAD HANDLER
   -------------------------------------------------------------------------- */
function handleResumeDownload(event) {
    showToast("Downloading Raj Kumar's Resume (PDF)...");
    
    // Provide programmatic fallback if event is triggered from an element without direct href
    if (event && event.currentTarget && event.currentTarget.tagName.toLowerCase() !== 'a') {
        const link = document.createElement('a');
        link.href = 'resume/Raj_Kumar_Resume.pdf';
        link.download = 'Raj_Kumar_Resume.pdf';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}