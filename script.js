/* ==========================================================================
   RAJKUMAR — ULTRA-LUXURY OBSIDIAN & ROYAL GOLD PORTFOLIO ENGINE
   Interactivity, Canvas Particles & Meteors, 3D Hero Parallax, Counters & Modals
   ========================================================================== */

// ==========================================================================
// CONFIGURABLE PROJECT DEPLOYMENT URLS
// ==========================================================================
const PET_NEXA_URL = "https://pet-nexa.onrender.com";
const PET_NOVA_URL = PET_NEXA_URL;
const ROYAL_ROSE_MILK_URL = "https://royal-rosegunicorn-app-ap.onrender.com";

document.addEventListener("DOMContentLoaded", () => {
    initThemeToggle();
    initCinematicCanvas();
    initNavbar();
    initScrollProgress();
    initCustomCursor();
    initScrollObserver();
    initHeroParallaxTilt();
    initCard3DTiltAndSpotlight();
    initStatCounterAnimations();
    applyProjectUrls();
    initLaptopDefaults();
});

/* --------------------------------------------------------------------------
   0. BRIGHT / DARK OBSIDIAN MODE THEME SWITCHER
   -------------------------------------------------------------------------- */
function initThemeToggle() {
    const themeBtn = document.getElementById("themeToggleBtn");
    const savedTheme = localStorage.getItem("raj_portfolio_theme") || "dark";

    function applyTheme(theme) {
        if (theme === "light") {
            document.documentElement.setAttribute("data-theme", "light");
            document.body.classList.add("theme-light");
            if (themeBtn) {
                const label = themeBtn.querySelector(".theme-toggle-text");
                if (label) label.textContent = "DARK";
                themeBtn.setAttribute("title", "Switch to Dark Obsidian Mode");
            }
        } else {
            document.documentElement.removeAttribute("data-theme");
            document.body.classList.remove("theme-light");
            if (themeBtn) {
                const label = themeBtn.querySelector(".theme-toggle-text");
                if (label) label.textContent = "BRIGHT";
                themeBtn.setAttribute("title", "Switch to Bright Mode");
            }
        }
    }

    applyTheme(savedTheme);

    if (themeBtn) {
        themeBtn.addEventListener("click", () => {
            const currentTheme = document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
            const newTheme = currentTheme === "light" ? "dark" : "light";
            applyTheme(newTheme);
            localStorage.setItem("raj_portfolio_theme", newTheme);
            showToast(newTheme === "light" ? "Switched to Bright Alabaster Gold ☀️" : "Switched to Dark Obsidian Gold 🌙");
        });
    }
}

/* --------------------------------------------------------------------------
   1. CINEMATIC GOLD PARTICLES & METEOR SHOOTING STAR CANVAS
   -------------------------------------------------------------------------- */
function initCinematicCanvas() {
    const canvas = document.getElementById("cinematicCanvas");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    let width, height;
    let particles = [];
    let shootingStars = [];
    let animationFrameId;
    let mouse = { x: null, y: null, radius: 160 };

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

    const particleCount = Math.min(Math.floor(window.innerWidth / 20), 75);

    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.size = Math.random() * 2.2 + 0.8;
            this.baseX = this.x;
            this.baseY = this.y;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.color = Math.random() > 0.35 ? "rgba(212, 175, 55, 0.5)" : "rgba(243, 229, 171, 0.35)";
        }

        update() {
            this.x += this.vx;
            this.y += this.vy;

            if (this.x < 0) this.x = width;
            if (this.x > width) this.x = 0;
            if (this.y < 0) this.y = height;
            if (this.y > height) this.y = 0;

            if (mouse.x !== null && mouse.y !== null) {
                const dx = mouse.x - this.x;
                const dy = mouse.y - this.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < mouse.radius) {
                    const force = (mouse.radius - dist) / mouse.radius;
                    const fx = (dx / dist) * force * 1.8;
                    const fy = (dy / dist) * force * 1.8;
                    this.x -= fx;
                    this.y -= fy;
                }
            }
        }

        draw() {
            const isLight = document.documentElement.getAttribute("data-theme") === "light";
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = isLight ? "rgba(184, 134, 11, 0.5)" : this.color;
            ctx.fill();
        }
    }

    class ShootingStar {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * width;
            this.y = 0;
            this.len = Math.random() * 90 + 50;
            this.speed = Math.random() * 8 + 6;
            this.size = Math.random() * 1.5 + 0.8;
            this.angle = Math.PI / 4;
            this.opacity = 1;
            this.active = true;
        }

        update() {
            this.x += this.speed * Math.cos(this.angle);
            this.y += this.speed * Math.sin(this.angle);
            this.opacity -= 0.012;
            if (this.opacity <= 0 || this.x > width || this.y > height) {
                this.active = false;
            }
        }

        draw() {
            if (!this.active) return;
            const tailX = this.x - this.len * Math.cos(this.angle);
            const tailY = this.y - this.len * Math.sin(this.angle);

            const gradient = ctx.createLinearGradient(tailX, tailY, this.x, this.y);
            gradient.addColorStop(0, "rgba(212, 175, 55, 0)");
            gradient.addColorStop(1, `rgba(255, 235, 175, ${this.opacity})`);

            ctx.beginPath();
            ctx.moveTo(tailX, tailY);
            ctx.lineTo(this.x, this.y);
            ctx.strokeStyle = gradient;
            ctx.lineWidth = this.size;
            ctx.stroke();
        }
    }

    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }

    let lastStarTime = Date.now();

    function animate() {
        ctx.clearRect(0, 0, width, height);
        const isLight = document.documentElement.getAttribute("data-theme") === "light";

        // Spawn meteor shooting stars periodically
        if (Date.now() - lastStarTime > 4000 && Math.random() > 0.4) {
            shootingStars.push(new ShootingStar());
            lastStarTime = Date.now();
        }

        // Draw connections
        for (let a = 0; a < particles.length; a++) {
            for (let b = a + 1; b < particles.length; b++) {
                const dx = particles[a].x - particles[b].x;
                const dy = particles[a].y - particles[b].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 135) {
                    const opacity = (1 - dist / 135) * (isLight ? 0.25 : 0.18);
                    ctx.beginPath();
                    ctx.strokeStyle = isLight ? `rgba(184, 134, 11, ${opacity})` : `rgba(212, 175, 55, ${opacity})`;
                    ctx.lineWidth = 0.7;
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }
        }

        // Update particles
        particles.forEach(p => {
            p.update();
            p.draw();
        });

        // Update shooting stars
        shootingStars = shootingStars.filter(s => s.active);
        shootingStars.forEach(s => {
            s.update();
            s.draw();
        });

        animationFrameId = requestAnimationFrame(animate);
    }
    animate();

    document.addEventListener("visibilitychange", () => {
        if (document.hidden) {
            cancelAnimationFrame(animationFrameId);
        } else {
            animate();
        }
    });
}

/* --------------------------------------------------------------------------
   2. HERO PORTRAIT 3D MAGNETIC PARALLAX & TILT PHYSICS
   -------------------------------------------------------------------------- */
function initHeroParallaxTilt() {
    const stage = document.getElementById("portraitStage");
    if (!stage) return;

    window.addEventListener("mousemove", (e) => {
        if (window.innerWidth < 992) return;
        const rect = stage.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        const deltaX = (e.clientX - centerX) / (window.innerWidth / 2);
        const deltaY = (e.clientY - centerY) / (window.innerHeight / 2);

        const tiltX = deltaY * -12;
        const tiltY = deltaX * 12;

        stage.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale(1.02)`;

        // Parallax inner photo and chips
        const img = stage.querySelector(".portrait-hero-img");
        if (img) img.style.transform = `translateX(${deltaX * -10}px) translateY(${deltaY * -10}px) scale(1.04)`;

        const chips = stage.querySelectorAll(".hero-floating-chip");
        chips.forEach((chip, i) => {
            const factor = (i + 1) * 8;
            chip.style.transform = `translateX(${deltaX * factor}px) translateY(${deltaY * factor}px)`;
        });
    });

    stage.addEventListener("mouseleave", () => {
        stage.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)";
        const img = stage.querySelector(".portrait-hero-img");
        if (img) img.style.transform = "translateX(0) translateY(0) scale(1)";
        const chips = stage.querySelectorAll(".hero-floating-chip");
        chips.forEach(chip => chip.style.transform = "");
    });
}

/* --------------------------------------------------------------------------
   3. 3D CARD TILT & SPOTLIGHT FOLLOWER PHYSICS
   -------------------------------------------------------------------------- */
function initCard3DTiltAndSpotlight() {
    const cards = document.querySelectorAll(".stat-box-card, .gold-skill-badge, .luxury-work-banner-card");

    cards.forEach(card => {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Calculate tilt angle
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -8;
            const rotateY = ((x - centerX) / centerX) * 8;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
            card.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(212, 175, 55, 0.12) 0%, rgba(18, 18, 24, 0.85) 60%)`;
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "";
            card.style.background = "";
        });
    });
}

/* --------------------------------------------------------------------------
   4. ANIMATED STAT NUMBER COUNTERS (TRIGGERED ON SCROLL)
   -------------------------------------------------------------------------- */
function initStatCounterAnimations() {
    const counters = document.querySelectorAll(".counter-number");
    let animated = false;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animated) {
                animated = true;
                counters.forEach(counter => {
                    const target = parseInt(counter.getAttribute("data-target"), 10);
                    const suffix = counter.getAttribute("data-suffix") || "";
                    let current = 0;
                    const increment = Math.max(Math.floor(target / 40), 1);
                    const duration = 1200;
                    const stepTime = Math.max(Math.floor(duration / (target / increment || 1)), 20);

                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            current = target;
                            clearInterval(timer);
                        }
                        counter.textContent = `${current}${suffix}`;
                    }, stepTime);
                });
            }
        });
    }, { threshold: 0.2 });

    const statsGrid = document.querySelector(".about-bottom-bar-card, .about-stats-2x2");
    if (statsGrid) observer.observe(statsGrid);
}

/* --------------------------------------------------------------------------
   5. STICKY NAVBAR & MOBILE DRAWER
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
   6. SCROLL PROGRESS INDICATOR
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
   7. DESKTOP CONTEXT CURSOR
   -------------------------------------------------------------------------- */
function initCustomCursor() {
    const cursorDot = document.getElementById("cursorDot");
    const cursorRing = document.getElementById("cursorRing");

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

    const interactives = document.querySelectorAll(
        "a, button, input, select, .gold-skill-badge, .stat-box-card, .channel-card-row, .timeline-card, .luxury-work-banner-card, .hero-floating-chip"
    );
    interactives.forEach(el => {
        el.addEventListener("mouseenter", () => document.body.classList.add("cursor-hover"));
        el.addEventListener("mouseleave", () => document.body.classList.remove("cursor-hover"));
    });
}

/* --------------------------------------------------------------------------
   8. SCROLL REVEAL OBSERVER
   -------------------------------------------------------------------------- */
function initScrollObserver() {
    const targets = document.querySelectorAll(
        ".about-split-layout, .skills-cards-grid, .selected-works-layout, .timeline-row, .contact-dramatic-layout"
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
   9. INTERACTIVE LAPTOP SHOWCASE CONTROLLER ("and the laptop.....")
   -------------------------------------------------------------------------- */
const LAPTOP_PROJECTS = {
    petNexa: {
        name: "PET NEXA",
        url: PET_NEXA_URL,
        img: "images/pet-nexa-dark-crest.jpg",
        fallback: "images/pet-nexa-showcase.jpg",
        badge: "GEMINI FLASH AI PLATFORM"
    },
    royalRose: {
        name: "ROYAL ROSE MILK",
        url: ROYAL_ROSE_MILK_URL,
        img: "images/royal-rose-milk.jpg",
        fallback: "images/royal-rose-milk.jpg",
        badge: "INTERACTIVE BRAND WEBSITE"
    },
    portfolio: {
        name: "PORTFOLIO WEBSITE",
        url: "#home",
        img: "portfolio_desktop.png",
        fallback: "images/pet-nexa-ui.jpg",
        badge: "LUXURY OBSIDIAN PORTFOLIO"
    }
};

function initLaptopDefaults() {
    switchLaptopProject('petNexa');
}

function switchLaptopProject(projectId) {
    const project = LAPTOP_PROJECTS[projectId];
    if (!project) return;

    document.querySelectorAll('.laptop-tab-pill').forEach(btn => btn.classList.remove('active'));
    if (projectId === 'petNexa') document.getElementById('laptopTabPetNexa')?.classList.add('active');
    if (projectId === 'royalRose') document.getElementById('laptopTabRoyalRose')?.classList.add('active');
    if (projectId === 'portfolio') document.getElementById('laptopTabPortfolio')?.classList.add('active');

    const imgEl = document.getElementById('laptopScreenImg');
    const nameEl = document.getElementById('laptopProjectName');
    const urlEl = document.getElementById('laptopProjectUrl');
    const liveBtn = document.getElementById('laptopLiveBtn');

    if (imgEl) {
        imgEl.style.opacity = '0';
        imgEl.style.transform = 'scale(0.98)';
        setTimeout(() => {
            imgEl.src = project.img;
            imgEl.onerror = () => { imgEl.src = project.fallback; };
            imgEl.style.opacity = '1';
            imgEl.style.transform = 'scale(1)';
        }, 200);
    }

    if (nameEl) nameEl.textContent = project.name;
    if (urlEl) urlEl.textContent = project.url;
    if (liveBtn) {
        liveBtn.href = project.url;
        if (project.url.startsWith('http')) {
            liveBtn.target = '_blank';
        } else {
            liveBtn.removeAttribute('target');
        }
    }

    showToast(`Laptop preview switched to ${project.name}`);
}

function setLaptopMode(mode) {
    const chassis = document.getElementById('macbookChassis');
    const btnLaptop = document.getElementById('modeBtnLaptop');
    const btnMobile = document.getElementById('modeBtnMobile');

    if (!chassis) return;

    if (mode === 'mobile') {
        chassis.classList.add('mobile-view');
        btnMobile?.classList.add('active');
        btnLaptop?.classList.remove('active');
        showToast("Switched to Mobile Viewport Mode 📱");
    } else {
        chassis.classList.remove('mobile-view');
        btnLaptop?.classList.add('active');
        btnMobile?.classList.remove('active');
        showToast("Switched to MacBook Pro 16\" Display View 💻");
    }
}

/* --------------------------------------------------------------------------
   10. APPLY CONFIGURABLE PROJECT URLS ACROSS DOM
   -------------------------------------------------------------------------- */
function applyProjectUrls() {
    // Project URLs directly synchronized
}

/* --------------------------------------------------------------------------
   11. PROJECT SHOWCASE DATA & INTERACTIVE MODAL CONTROLLER
   -------------------------------------------------------------------------- */
const PET_NEXA_DATA = {
    title: "PET NEXA",
    badge: "FLAGSHIP // AI PET CARE PLATFORM",
    heroImg: "images/pet-nexa-dark-crest.jpg",
    heading: "PET NEXA — AI-Powered Multi-Service Platform",
    description: "PET NEXA is a full-stack pet care ecosystem combining pet grooming appointment scheduling, veterinary specialist bookings, e-commerce shop, order tracking, and an intelligent Gemini Flash AI Pet Health Advisor.",
    liveUrl: PET_NEXA_URL,
    specs: [
        { label: "LIVE SERVER", value: PET_NEXA_URL },
        { label: "BACKEND STACK", value: "Python / Flask REST Server" },
        { label: "FRONTEND UI", value: "HTML5, CSS3, JavaScript (ES6+)" },
        { label: "DATABASE", value: "SQLite Relational Store" },
        { label: "AI ENGINE", value: "Gemini Flash AI Model" },
        { label: "ARCHITECTURE", value: "Modular MVC Pattern" }
    ],
    features: [
        { title: "Pet Grooming Booking", desc: "Customized grooming package selections with real-time slot scheduling." },
        { title: "Veterinary Specialists", desc: "Browse qualified vets, book consultations, and view care history." },
        { title: "E-Commerce Pet Shop", desc: "Dynamic product catalog, shopping cart, and persistent order tracking." },
        { title: "Gemini AI Health Advisor", desc: "Evaluates multi-symptom pet diagnostics and generates instant guidance." },
        { title: "Booking Management", desc: "Live dashboard to modify appointments and persist user session records." },
        { title: "Responsive Layout", desc: "Engineered with 60fps micro-animations and zero-lag mobile responsiveness." }
    ],
    codeSnippet: `@app.route('/api/ai/diagnose', methods=['POST'])
def diagnose_pet_symptom():
    data = request.get_json()
    pet_name = data.get('pet_name', 'Pet')
    symptoms = data.get('symptoms', [])
    
    # Gemini AI Diagnostic Assessment
    prompt = f"Evaluate symptoms for {pet_name}: {', '.join(symptoms)}"
    evaluation = gemini_model.generate_content(prompt)
    
    # Persist log to SQLite database
    db.execute("INSERT INTO diagnostic_logs (pet_name, symptoms, verdict) VALUES (?, ?, ?)",
               (pet_name, str(symptoms), evaluation.text))
    db.commit()
    
    return jsonify({
        "status": "success",
        "pet": pet_name,
        "assessment": evaluation.text
    })`
};

const ROYAL_ROSE_DATA = {
    title: "ROYAL ROSE MILK",
    badge: "INTERACTIVE SENSORY BRAND EXPERIENCE",
    heroImg: "images/royal-rose-milk.jpg",
    heading: "ROYAL ROSE MILK — Sensory Brand Website",
    description: "An artisanal, interactive sensory product brand experience designed for Royal Rose Milk, featuring real-time bottle formulation engine, dynamic price calculations, and smooth 60fps micro-animations.",
    liveUrl: ROYAL_ROSE_MILK_URL,
    specs: [
        { label: "LIVE SERVER", value: ROYAL_ROSE_MILK_URL },
        { label: "FRONTEND CORE", value: "HTML5 & Tailwind CSS" },
        { label: "CLIENT LOGIC", value: "JavaScript (ES6+ State Engine)" },
        { label: "EXPERIENCE", value: "Sensory Interactive Design" },
        { label: "PERFORMANCE", value: "60 FPS Hardware-Accelerated" }
    ],
    features: [
        { title: "Cinematic Visuals", desc: "Atmospheric dark palette with obsidian and rose gold accents." },
        { title: "Dynamic Customizer", desc: "Real-time bottle blend formulation adjusting rose essence and milk base." },
        { title: "Interactive Storytelling", desc: "Heritage exploration of Damascus rose extract craftsmanship." },
        { title: "Shopping Workflow", desc: "Responsive product catalog with instant price calculation algorithms." }
    ],
    codeSnippet: `// Real-Time Sensory Flavor Formulation Engine
function calculateCustomRoseBlend(essenceRatio, sweetnessType, baseMilk) {
    let basePrice = 120;
    const sweetnessMultiplier = { "Pure Honey": 20, "Organic Jaggery": 15, "Stevia": 10 };
    const milkMultiplier = { "Almond Milk": 30, "Oat Milk": 25, "Whole Farm Milk": 0 };
    
    const finalPrice = basePrice + (sweetnessMultiplier[sweetnessType] || 0) + (milkMultiplier[baseMilk] || 0);
    const blendGrade = essenceRatio >= 80 ? "Royal Damask Reserve" : "Artisanal Classic";
    
    return { finalPrice, blendGrade, ratio: essenceRatio };
}`
};

const PORTFOLIO_DATA = {
    title: "PORTFOLIO WEBSITE",
    badge: "ENGINEERING SHOWCASE // OBSIDIAN & GOLD",
    heroImg: "portfolio_desktop.png",
    heading: "Rajkumar — Developer Portfolio Architecture",
    description: "Personal portfolio website engineered with an ultra-luxury obsidian and royal gold design system, 3D interactive MacBook device workbench, quantum loader, and responsive client-side engines.",
    liveUrl: "#home",
    specs: [
        { label: "DESIGN PALETTE", value: "Velvet Obsidian (#08080A) & Royal Gold (#D4AF37)" },
        { label: "CORE STACK", value: "HTML5, Vanilla CSS3, JavaScript (ES6+)" },
        { label: "ANIMATIONS", value: "Canvas Constellation Particles & 3D Tilt" },
        { label: "RESPONSIVENESS", value: "Mobile, Tablet, Laptop, 4K Display" }
    ],
    features: [
        { title: "Golden Halo Hero", desc: "Art-directed portrait with glowing orbital rings and dotted grid accent." },
        { title: "MacBook Pro Workbench", desc: "Realistic 3D laptop chassis with live project switching and viewport toggles." },
        { title: "2x2 Stat Cards", desc: "Glassmorphic metric indicators highlighting experience and skills." },
        { title: "Quantum Loader", desc: "Startup telemetry sequence with laser progress bar and monogram glow." }
    ],
    codeSnippet: `/* Ultra-Luxury Obsidian & Royal Gold Design Token Architecture */
:root {
    --bg-obsidian: #08080A;
    --gold-main: #D4AF37;
    --gold-light: #F3E5AB;
    --gold-glow: rgba(212, 175, 55, 0.38);
    --font-serif: 'Cormorant Garamond', serif;
    --font-sans: 'Plus Jakarta Sans', sans-serif;
}`
};

let currentModalProject = "petNexa";

function openProjectModal(projectId) {
    currentModalProject = projectId;
    const backdrop = document.getElementById("projectModalBackdrop");
    const titleEl = document.getElementById("modalTitle");
    const badgeEl = document.getElementById("modalBadge");
    const heroImgEl = document.getElementById("modalHeroImg");
    const headingEl = document.getElementById("modalOverviewHeading");
    const descEl = document.getElementById("modalOverviewDesc");
    const liveAnchor = document.getElementById("modalOverviewLiveAnchor");
    const liveBtn = document.getElementById("modalOverviewLiveBtn");
    const headerLiveLink = document.getElementById("modalHeaderLiveLink");
    const footerLiveLink = document.getElementById("modalFooterLiveLink");
    const specGrid = document.getElementById("modalSpecGrid");
    const featuresGrid = document.getElementById("modalFeaturesGrid");
    const codeSnippet = document.getElementById("modalCodeSnippet");

    let data = PET_NEXA_DATA;
    if (projectId === "royalRose") data = ROYAL_ROSE_DATA;
    if (projectId === "portfolio") data = PORTFOLIO_DATA;

    if (titleEl) titleEl.textContent = data.title;
    if (badgeEl) badgeEl.textContent = data.badge;
    if (heroImgEl) {
        heroImgEl.src = data.heroImg;
        heroImgEl.onerror = () => { heroImgEl.src = "images/pet-nexa-dark-crest.jpg"; };
    }
    if (headingEl) headingEl.textContent = data.heading;
    if (descEl) descEl.textContent = data.description;
    if (liveAnchor) {
        liveAnchor.href = data.liveUrl;
        liveAnchor.textContent = data.liveUrl;
    }
    if (liveBtn) liveBtn.href = data.liveUrl;
    if (headerLiveLink) headerLiveLink.href = data.liveUrl;
    if (footerLiveLink) footerLiveLink.href = data.liveUrl;
    if (codeSnippet) codeSnippet.textContent = data.codeSnippet;

    if (specGrid) {
        specGrid.innerHTML = data.specs.map(s => `
            <div style="padding: 10px; background: rgba(255,255,255,0.03); border: 1px solid var(--border-obsidian); border-radius: 8px; margin-bottom: 8px;">
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold-main);">${s.label}</div>
                <div style="font-size: 13px; color: var(--text-pure); font-weight: 600;">${s.value}</div>
            </div>
        `).join('');
    }

    if (featuresGrid) {
        featuresGrid.innerHTML = data.features.map(f => `
            <div style="padding: 16px; background: var(--gradient-card); border: 1px solid var(--border-obsidian); border-radius: 12px; margin-bottom: 12px;">
                <h5 style="font-family: var(--font-serif); font-size: 16px; color: var(--gold-light); margin-bottom: 6px;">${f.title}</h5>
                <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">${f.desc}</p>
            </div>
        `).join('');
    }

    switchModalTab("tabOverview");

    if (backdrop) {
        backdrop.classList.add("active");
        document.body.style.overflow = "hidden";
    }
}

function closeProjectModal(e) {
    if (e && e.target && e.target.id !== "projectModalBackdrop" && !e.target.closest(".modal-close-button") && !e.target.closest(".btn-footer-close")) {
        return;
    }
    const backdrop = document.getElementById("projectModalBackdrop");
    if (backdrop) {
        backdrop.classList.remove("active");
        document.body.style.overflow = "";
    }
}

function switchModalTab(tabId) {
    document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
    document.querySelectorAll(".tab-pane").forEach(pane => pane.classList.remove("active"));

    const tabBtn = document.getElementById(`tabBtn${tabId.replace("tab", "")}`);
    const tabPane = document.getElementById(tabId);

    if (tabBtn) tabBtn.classList.add("active");
    if (tabPane) tabPane.classList.add("active");

    if (tabId === "tabSimulator") {
        renderModalSimulator(currentModalProject);
    }
}

function renderModalSimulator(projectId) {
    const container = document.getElementById("simulatorContainer");
    if (!container) return;

    if (projectId === "petNexa") {
        container.innerHTML = `
            <div style="padding: 20px; background: rgba(18, 18, 24, 0.9); border: 1px solid var(--border-gold-subtle); border-radius: 14px;">
                <h4 style="font-family: var(--font-serif); font-size: 20px; color: var(--gold-light); margin-bottom: 12px;">Gemini Flash AI Pet Health Evaluation</h4>
                <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">Test the AI diagnostic rule engine with simulated clinical biometrics:</p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
                    <div>
                        <label style="font-size: 11px; font-family: var(--font-mono); color: var(--gold-main); display: block; margin-bottom: 6px;">PET NAME</label>
                        <input type="text" id="simPetName" value="Bruno" style="width: 100%; padding: 10px; border-radius: 6px; background: #0A0A0D; border: 1px solid var(--border-obsidian); color: #fff;">
                    </div>
                    <div>
                        <label style="font-size: 11px; font-family: var(--font-mono); color: var(--gold-main); display: block; margin-bottom: 6px;">SELECT SYMPTOM</label>
                        <select id="simPetSymptoms" style="width: 100%; padding: 10px; border-radius: 6px; background: #0A0A0D; border: 1px solid var(--border-obsidian); color: #fff;">
                            <option value="none">Normal Activity (Healthy Baseline)</option>
                            <option value="lethargy">Reduced Energy & Lethargy</option>
                            <option value="loss_of_appetite">Appetite Suppression</option>
                            <option value="dental_plaque">Dental Plaque & Breath Odor</option>
                            <option value="skin_itching">Dermatological Irritation & Scratching</option>
                        </select>
                    </div>
                </div>
                <button class="btn-gold-solid" style="width: 100%; justify-content: center;" onclick="runPetDiagnosticSim()">
                    <span>RUN GEMINI AI DIAGNOSTIC EVALUATION</span>
                    <i class="fa-solid fa-brain"></i>
                </button>
                <div id="simDiagnosticOutput" style="margin-top: 18px; padding: 16px; border-radius: 8px; background: rgba(212, 175, 55, 0.06); border: 1px solid var(--border-gold-subtle);">
                    <div style="font-family: var(--font-serif); font-size: 28px; color: var(--gold-main);" id="simScoreNum">96/100</div>
                    <h5 id="simScoreHeading" style="color: var(--text-pure); font-size: 16px; margin: 4px 0 8px;">Optimal Vitality Status</h5>
                    <p id="simVerdictText" style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">Biometric indicators are within optimal healthy thresholds. No intervention needed.</p>
                </div>
            </div>
        `;
    } else {
        container.innerHTML = `
            <div style="padding: 20px; background: rgba(18, 18, 24, 0.9); border: 1px solid var(--border-gold-subtle); border-radius: 14px;">
                <h4 style="font-family: var(--font-serif); font-size: 20px; color: var(--gold-light); margin-bottom: 12px;">Sensory Flavor Formulation Simulator</h4>
                <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">Adjust recipe parameters to calculate live price and flavor balance:</p>
                <div style="margin-bottom: 14px;">
                    <label style="font-size: 11px; font-family: var(--font-mono); color: var(--gold-main); display: block; margin-bottom: 6px;">DAMASCUS ROSE ESSENCE RATIO: <span id="simRoseVal">65%</span></label>
                    <input type="range" id="simRoseEssence" min="30" max="95" value="65" style="width: 100%; accent-color: var(--gold-main);" oninput="updateRoseCustomizerSim()">
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
                    <div>
                        <label style="font-size: 11px; font-family: var(--font-mono); color: var(--gold-main); display: block; margin-bottom: 6px;">ORGANIC SWEETENER</label>
                        <select id="simSweetness" style="width: 100%; padding: 10px; border-radius: 6px; background: #0A0A0D; border: 1px solid var(--border-obsidian); color: #fff;" onchange="updateRoseCustomizerSim()">
                            <option value="Organic Cane Sugar">Organic Cane Sugar (+₹0)</option>
                            <option value="Pure Honey">Wild Pure Honey (+₹20)</option>
                            <option value="Jaggery Extract">Organic Jaggery (+₹15)</option>
                        </select>
                    </div>
                    <div>
                        <label style="font-size: 11px; font-family: var(--font-mono); color: var(--gold-main); display: block; margin-bottom: 6px;">MILK BASE</label>
                        <select id="simMilkBase" style="width: 100%; padding: 10px; border-radius: 6px; background: #0A0A0D; border: 1px solid var(--border-obsidian); color: #fff;" onchange="updateRoseCustomizerSim()">
                            <option value="Whole Farm Milk">Whole Farm Milk (+₹0)</option>
                            <option value="Almond Milk">Silky Almond Milk (+₹30)</option>
                            <option value="Oat Milk">Creamy Oat Milk (+₹25)</option>
                        </select>
                    </div>
                </div>
                <div id="simRoseOutput" style="padding: 16px; border-radius: 8px; background: rgba(212, 175, 55, 0.06); border: 1px solid var(--border-gold-subtle);">
                    <div style="font-family: var(--font-serif); font-size: 28px; color: var(--gold-main);" id="simRosePrice">₹120</div>
                    <h5 id="simRoseBlendName" style="color: var(--text-pure); font-size: 16px; margin: 4px 0 8px;">Artisanal Rose Classic</h5>
                    <p id="simRoseDescription" style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">Handcrafted with 65% Damascus rose extract blended in Whole Farm Milk with Organic Cane Sugar.</p>
                </div>
            </div>
        `;
    }
}

function runPetDiagnosticSim() {
    const petName = document.getElementById("simPetName")?.value || "Pet";
    const symptom = document.getElementById("simPetSymptoms")?.value || "none";
    const scoreNum = document.getElementById("simScoreNum");
    const heading = document.getElementById("simScoreHeading");
    const verdict = document.getElementById("simVerdictText");

    let score = 96;
    let headingText = "Optimal Vitality Status";
    let descText = `${petName} exhibits excellent biometric telemetry. All indicators within normal range.`;

    if (symptom === "lethargy") {
        score = 74;
        headingText = "Fatigue & Low Activity Alert";
        descText = `${petName} exhibits reduced mobility index. Recommend hydration & monitoring.`;
    } else if (symptom === "loss_of_appetite") {
        score = 68;
        headingText = "Nutritional Imbalance Alert";
        descText = `${petName} has appetite suppression. Recommend probiotic soft-diet regimen.`;
    } else if (symptom === "dental_plaque") {
        score = 82;
        headingText = "Dental Hygiene Advisory";
        descText = `Oral plaque detected. Recommend scheduling ultrasonic dental cleaning with a Pet Nexa specialist.`;
    } else if (symptom === "skin_itching") {
        score = 78;
        headingText = "Dermatological Irritation";
        descText = `Frequent scratching observed. Recommend hypoallergenic medicated oatmeal bath.`;
    }

    if (scoreNum) scoreNum.textContent = `${score}/100`;
    if (heading) heading.textContent = headingText;
    if (verdict) verdict.textContent = descText;

    showToast(`AI diagnostic completed for ${petName}! Score: ${score}/100`);
}

function updateRoseCustomizerSim() {
    const essence = parseInt(document.getElementById("simRoseEssence")?.value || "65", 10);
    const sweetness = document.getElementById("simSweetness")?.value || "Organic Cane Sugar";
    const milk = document.getElementById("simMilkBase")?.value || "Whole Farm Milk";

    document.getElementById("simRoseVal").textContent = `${essence}%`;

    let price = 120;
    if (sweetness.includes("Honey")) price += 20;
    if (sweetness.includes("Jaggery")) price += 15;
    if (milk.includes("Almond")) price += 30;
    if (milk.includes("Oat")) price += 25;

    document.getElementById("simRosePrice").textContent = `₹${price}`;
    document.getElementById("simRoseBlendName").textContent = essence >= 80 ? "Royal Damask Reserve" : "Artisanal Rose Classic";
    document.getElementById("simRoseDescription").textContent = `Handcrafted with ${essence}% Damascus rose extract blended in ${milk} with ${sweetness}.`;
}

/* --------------------------------------------------------------------------
   12. COPY TO CLIPBOARD & TOAST NOTIFICATIONS
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
        copyContactInfo(code.textContent, "Architecture code copied to clipboard!");
    }
}

function showToast(message) {
    const toast = document.getElementById("toastNotification");
    const toastMsg = document.getElementById("toastMessage");

    if (!toast) return;
    if (toastMsg) toastMsg.textContent = message;

    toast.classList.add("active");

    setTimeout(() => {
        toast.classList.remove("active");
    }, 2800);
}

/* --------------------------------------------------------------------------
   13. RESUME DOWNLOAD HANDLER
   -------------------------------------------------------------------------- */
function handleResumeDownload(event) {
    showToast("Downloading Rajkumar's Resume (PDF)...");
}