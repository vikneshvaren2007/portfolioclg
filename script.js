/* ==========================================================================
   RAJKUMAR — PRODUCTION PORTFOLIO ENGINE (2026)
   Navbar Underline, Hero Typing, Services Pre-selection,
   Gallery Filtering, Flagship Modals & Particle Canvas
   ========================================================================== */

// ==========================================================================
// CENTRALIZED CONFIGURATION (EASY TO CUSTOMIZE)
// ==========================================================================
const PORTFOLIO_CONFIG = {
    whatsappNumber: "919445437069",
    instagramUrl: "https://www.instagram.com/__.rxjkumar?stkn=MWF0NG9keWlrYjBkdw==",
    githubUrl: "https://github.com/vikneshvaren2007",
    email: "vikneshvaren2@gmail.com",
    phoneDisplay: "+91 94454 37069",
    petNexaUrl: "https://pet-nexa.onrender.com",
    royalRoseUrl: "https://royal-rosegunicorn-app-ap.onrender.com",
    aurelisUrl: "https://aurelis-watch.onrender.com",
    
    // Exact requested WhatsApp message format:
    // "Hello rajkumar! I'm interested in your project: [SELECTED PROJECT NAME]. Could you provide more details about the features and pricing?"
    getWhatsAppUrl(projectName) {
        if (!projectName) {
            const general = "Hello rajkumar! I'm interested in discussing a web project. Could we connect?";
            return `https://wa.me/${this.whatsappNumber}?text=${encodeURIComponent(general)}`;
        }
        const message = `Hello rajkumar! I'm interested in your project: ${projectName}. Could you provide more details about the features and pricing?`;
        return `https://wa.me/${this.whatsappNumber}?text=${encodeURIComponent(message)}`;
    }
};

// Aliases for backwards compatibility
const GITHUB_URL = PORTFOLIO_CONFIG.githubUrl;
const INSTAGRAM_URL = PORTFOLIO_CONFIG.instagramUrl;
const EMAIL_ADDRESS = PORTFOLIO_CONFIG.email;
const PHONE_NUMBER = PORTFOLIO_CONFIG.phoneDisplay;
const PET_NEXA_URL = PORTFOLIO_CONFIG.petNexaUrl;
const ROYAL_ROSE_MILK_URL = PORTFOLIO_CONFIG.royalRoseUrl;
const AURELIS_URL = PORTFOLIO_CONFIG.aurelisUrl;

// ==========================================================================
// DOM READY INITIALIZATION
// ==========================================================================
document.addEventListener("DOMContentLoaded", () => {
    try {
        localStorage.removeItem("raj_portfolio_theme");
        document.documentElement.removeAttribute("data-theme");
        document.body.classList.remove("theme-light");
    } catch (e) {}
    initCinematicCanvas();
    initNavbar();
    initScrollProgress();
    initHeroTyping();
    initWhatsAppEnquiryButtons();
    initGalleryFilters();
    initStatCounterAnimations();
    initScrollObserver();
    initCircularOrbitNav();
});

/* --------------------------------------------------------------------------
   WHATSAPP ENQUIRY AUTOMATION
   -------------------------------------------------------------------------- */
function initWhatsAppEnquiryButtons() {
    // Project-specific WhatsApp links
    document.querySelectorAll("[data-whatsapp-project]").forEach(btn => {
        const projectName = btn.getAttribute("data-whatsapp-project");
        if (projectName) {
            btn.setAttribute("href", PORTFOLIO_CONFIG.getWhatsAppUrl(projectName));
            btn.setAttribute("target", "_blank");
            btn.setAttribute("rel", "noopener noreferrer");
        }
    });

    // General WhatsApp links
    document.querySelectorAll("[data-whatsapp-general]").forEach(btn => {
        btn.setAttribute("href", PORTFOLIO_CONFIG.getWhatsAppUrl());
        btn.setAttribute("target", "_blank");
        btn.setAttribute("rel", "noopener noreferrer");
    });
}

/* --------------------------------------------------------------------------
   1. CINEMATIC PARTICLES & METEOR CANVAS
   -------------------------------------------------------------------------- */
function initCinematicCanvas() {
    const canvas = document.getElementById("cinematicCanvas");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    let width, height;
    let particles = [];
    let shootingStars = [];
    let animationFrameId;

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }
    resize();
    window.addEventListener("resize", resize);

    const particleCount = Math.min(Math.floor(window.innerWidth / 22), 65);

    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.size = Math.random() * 2.0 + 0.8;
            this.vx = (Math.random() - 0.5) * 0.45;
            this.vy = (Math.random() - 0.5) * 0.45;
            this.color = Math.random() > 0.35 ? "rgba(212, 175, 55, 0.45)" : "rgba(243, 229, 171, 0.3)";
        }

        update() {
            this.x += this.vx;
            this.y += this.vy;

            if (this.x < 0) this.x = width;
            if (this.x > width) this.x = 0;
            if (this.y < 0) this.y = height;
            if (this.y > height) this.y = 0;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
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
            this.len = Math.random() * 80 + 40;
            this.speed = Math.random() * 7 + 5;
            this.size = Math.random() * 1.4 + 0.8;
            this.angle = Math.PI / 4;
            this.opacity = 1;
            this.active = true;
        }

        update() {
            this.x += this.speed * Math.cos(this.angle);
            this.y += this.speed * Math.sin(this.angle);
            this.opacity -= 0.014;
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

        if (Date.now() - lastStarTime > 5000 && Math.random() > 0.45) {
            shootingStars.push(new ShootingStar());
            lastStarTime = Date.now();
        }

        for (let a = 0; a < particles.length; a++) {
            for (let b = a + 1; b < particles.length; b++) {
                const dx = particles[a].x - particles[b].x;
                const dy = particles[a].y - particles[b].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 120) {
                    const opacity = (1 - dist / 120) * 0.14;
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(212, 175, 55, ${opacity})`;
                    ctx.lineWidth = 0.6;
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }
        }

        particles.forEach(p => {
            p.update();
            p.draw();
        });

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
   2. NAVBAR CONTROLLER & ACTIVE UNDERLINE (DESKTOP + MOBILE DRAWER)
   -------------------------------------------------------------------------- */
function initNavbar() {
    const navbar = document.getElementById("navbar");
    const mobileBtn = document.getElementById("mobileToggleBtn");
    const navLinks = document.getElementById("navLinks");
    const backdrop = document.getElementById("mobileNavBackdrop");
    const navItems = document.querySelectorAll(".nav-item");

    // Sticky navbar glass blur on scroll
    window.addEventListener("scroll", () => {
        if (window.scrollY > 30) {
            navbar?.classList.add("scrolled");
        } else {
            navbar?.classList.remove("scrolled");
        }
    }, { passive: true });

    // Mobile Hamburger Toggle
    function toggleMobileMenu(open) {
        if (!navLinks) return;
        const isOpen = open !== undefined ? open : !navLinks.classList.contains("mobile-open");
        if (isOpen) {
            navLinks.classList.add("mobile-open");
            backdrop?.classList.add("active");
            mobileBtn?.classList.add("active");
            mobileBtn?.setAttribute("aria-expanded", "true");
            document.body.style.overflow = "hidden";
        } else {
            navLinks.classList.remove("mobile-open");
            backdrop?.classList.remove("active");
            mobileBtn?.classList.remove("active");
            mobileBtn?.setAttribute("aria-expanded", "false");
            document.body.style.overflow = "";
        }
    }

    if (mobileBtn && navLinks) {
        mobileBtn.addEventListener("click", () => toggleMobileMenu());
        backdrop?.addEventListener("click", () => toggleMobileMenu(false));

        // Close on Escape key
        window.addEventListener("keydown", (e) => {
            if (e.key === "Escape" && navLinks.classList.contains("mobile-open")) {
                toggleMobileMenu(false);
            }
        });
    }

    // Precision Scroll Spy for Active Navigation Links (Desktop + Mobile)
    const sectionIds = ["home", "about", "skills", "projects", "services", "contact"];

    function setActiveSection(sectionId) {
        navItems.forEach(item => {
            const href = item.getAttribute("href");
            if (href === `#${sectionId}` || href?.endsWith(`#${sectionId}`)) {
                item.classList.add("active");
            } else {
                item.classList.remove("active");
            }
        });
    }

    function updateActiveNav() {
        const scrollY = window.pageYOffset || document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;
        const docHeight = document.documentElement.scrollHeight;
        const navHeight = navbar ? navbar.offsetHeight : 75;

        // At or near top of the page
        if (scrollY < 80) {
            setActiveSection("home");
            return;
        }

        // At or near bottom of the page
        if (scrollY + windowHeight >= docHeight - 75) {
            setActiveSection("contact");
            return;
        }

        // Detect active section in viewport
        let currentSectionId = "home";
        for (const id of sectionIds) {
            const section = document.getElementById(id);
            if (!section) continue;
            const rect = section.getBoundingClientRect();
            if (rect.top <= windowHeight * 0.42 && rect.bottom > navHeight + 20) {
                currentSectionId = id;
            }
        }

        setActiveSection(currentSectionId);
    }

    // Smooth Accurate Scrolling on Nav Points & Section Anchors with Offset
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener("click", function(e) {
            const href = this.getAttribute("href");
            if (!href || href === "#") return;
            const targetId = href.replace(/^#/, "");
            if (targetId === "top" || targetId === "home") {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: "smooth" });
                setActiveSection("home");
                toggleMobileMenu(false);
                return;
            }
            const target = document.getElementById(targetId);
            if (target) {
                e.preventDefault();
                const navHeight = navbar ? navbar.offsetHeight : 70;
                const targetY = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 12;
                window.scrollTo({
                    top: Math.max(0, targetY),
                    behavior: "smooth"
                });
                setActiveSection(targetId);
                toggleMobileMenu(false);
            }
        });
    });

    // Also close mobile menu when tapping non-anchor links
    navLinks?.querySelectorAll('a:not([href^="#"])').forEach(link => {
        link.addEventListener("click", () => toggleMobileMenu(false));
    });

    window.addEventListener("scroll", updateActiveNav, { passive: true });
    window.addEventListener("resize", updateActiveNav, { passive: true });
    updateActiveNav();
}

/* --------------------------------------------------------------------------
   3. HERO AUTOMATIC TITLE TYPING / ROTATION ENGINE
   -------------------------------------------------------------------------- */
function initHeroTyping() {
    const titleEl = document.getElementById("heroTypingTitle");
    if (!titleEl) return;

    const titles = [
        "FULL STACK WEB DEVELOPER",
        "APP DEVELOPER",
        "WEB APPLICATION DEVELOPER",
        "AI ENTHUSIAST"
    ];

    let titleIndex = 0;
    let charIndex = titles[0].length; // start with first title full
    let isDeleting = false;
    const typeSpeed = 65;
    const eraseSpeed = 35;
    const pauseEnd = 2000;
    const pauseStart = 350;

    // Set initial full text
    titleEl.textContent = titles[0];

    function step() {
        const currentTitle = titles[titleIndex];

        if (isDeleting) {
            charIndex--;
            titleEl.textContent = currentTitle.substring(0, charIndex);
        } else {
            charIndex++;
            titleEl.textContent = currentTitle.substring(0, charIndex);
        }

        let delay = isDeleting ? eraseSpeed : typeSpeed;

        if (!isDeleting && charIndex === currentTitle.length) {
            delay = pauseEnd;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            titleIndex = (titleIndex + 1) % titles.length;
            delay = pauseStart;
        }

        setTimeout(step, delay);
    }

    // Wait initial delay before first erase
    setTimeout(() => {
        isDeleting = true;
        step();
    }, 2200);
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
    }, { passive: true });
}

/* --------------------------------------------------------------------------
   5. SERVICES CTA PRE-SELECTION & SMOOTH SCROLL
   -------------------------------------------------------------------------- */
function selectServiceForContact(serviceName) {
    const serviceSelect = document.getElementById("contactService");
    const contactSection = document.getElementById("contact");

    if (serviceSelect) {
        // Find matching option
        for (let i = 0; i < serviceSelect.options.length; i++) {
            if (serviceSelect.options[i].value.includes(serviceName) || serviceName.includes(serviceSelect.options[i].value)) {
                serviceSelect.selectedIndex = i;
                break;
            }
        }
    }

    if (contactSection) {
        contactSection.scrollIntoView({ behavior: "smooth" });
    }

    showToast(`Selected Package: ${serviceName}`);
}

/* --------------------------------------------------------------------------
   6. PROJECTS GALLERY CATEGORY FILTER & REAL-TIME SEARCH ENGINE
   -------------------------------------------------------------------------- */
function initGalleryFilters() {
    const filterPills = document.querySelectorAll(".gallery-filter-pill");
    const cards = document.querySelectorAll(".gallery-card");
    const searchInput = document.getElementById("projectSearchInput");
    const countBadge = document.getElementById("galleryCountBadge");

    if (!cards.length) return;

    let activeFilter = "all";
    let searchQuery = "";

    function applyFilterAndSearch() {
        let visibleCount = 0;

        cards.forEach(card => {
            const category = card.getAttribute("data-category") || "";
            const titleEl = card.querySelector(".browser-card-title, .gallery-card-title, h3");
            const stackEl = card.querySelector(".built-with-stack, .browser-card-tech-row");
            const descEl = card.querySelector(".browser-card-desc, .gallery-card-desc, p");
            const cardText = ((titleEl ? titleEl.textContent : "") + " " + (stackEl ? stackEl.textContent : "") + " " + (descEl ? descEl.textContent : "")).toLowerCase();

            const matchesCategory = (activeFilter === "all" || category === activeFilter);
            const matchesSearch = (!searchQuery || cardText.includes(searchQuery));

            if (matchesCategory && matchesSearch) {
                card.style.display = "flex";
                setTimeout(() => {
                    card.style.opacity = "1";
                    card.style.transform = "scale(1)";
                }, 10);
                visibleCount++;
            } else {
                card.style.opacity = "0";
                card.style.transform = "scale(0.96)";
                setTimeout(() => {
                    card.style.display = "none";
                }, 200);
            }
        });

        if (countBadge) {
            countBadge.textContent = `TOTAL PROJECT COUNT : ${visibleCount}`;
        }
    }

    if (filterPills.length) {
        filterPills.forEach(pill => {
            pill.addEventListener("click", () => {
                activeFilter = pill.getAttribute("data-filter") || "all";
                filterPills.forEach(p => p.classList.remove("active"));
                pill.classList.add("active");
                applyFilterAndSearch();
            });
        });
    }

    if (searchInput) {
        searchInput.addEventListener("input", (e) => {
            searchQuery = e.target.value.trim().toLowerCase();
            applyFilterAndSearch();
        });
    }
}

/* --------------------------------------------------------------------------
   7. CONTACT FORM SUBMISSION HANDLER
   -------------------------------------------------------------------------- */
function handleContactSubmit(e) {
    e.preventDefault();

    const nameInput = document.getElementById("contactName");
    const emailInput = document.getElementById("contactEmail");
    const serviceInput = document.getElementById("contactService");
    const messageInput = document.getElementById("contactMessage");

    const name = nameInput?.value.trim() || "Friend";
    const service = serviceInput?.value || "General Inquiry";

    showToast(`Thank you, ${name}! Your request for "${service}" has been received.`);

    // Reset form
    if (nameInput) nameInput.value = "";
    if (emailInput) emailInput.value = "";
    if (messageInput) messageInput.value = "";
    if (serviceInput) serviceInput.selectedIndex = 0;
}

/* --------------------------------------------------------------------------
   8. STAT NUMBER COUNTERS (TRIGGERED ON SCROLL)
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
                    const increment = Math.max(Math.floor(target / 30), 1);
                    const duration = 1000;
                    const stepTime = Math.max(Math.floor(duration / (target / increment || 1)), 25);

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

    const statsGrid = document.querySelector(".about-bottom-bar-card");
    if (statsGrid) observer.observe(statsGrid);
}

/* --------------------------------------------------------------------------
   9. SCROLL REVEAL OBSERVER
   -------------------------------------------------------------------------- */
function initScrollObserver() {
    const targets = document.querySelectorAll(
        ".about-hero-split, .about-bottom-bar-card, .about-skills-subdivision, .services-cards-grid, .projects-gallery-grid, .contact-main-flow"
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
        el.style.transform = "translateY(20px)";
        el.style.transition = `opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1) ${Math.min(idx * 0.06, 0.2)}s, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) ${Math.min(idx * 0.06, 0.2)}s`;
        observer.observe(el);
    });
}

/* --------------------------------------------------------------------------
   10. FLAGSHIP PROJECT SHOWCASE DATA & INTERACTIVE MODALS
   -------------------------------------------------------------------------- */
const PET_NEXA_DATA = {
    title: "PET NEXA",
    badge: "FLAGSHIP // AI PET CARE PLATFORM",
    heroImg: "images/pet-nexa-dark-crest.jpg",
    heading: "PET NEXA — AI-Powered Pet Ecosystem",
    description: "PET NEXA is a full-stack pet care platform featuring grooming appointment scheduling, veterinary bookings, an e-commerce storefront, order tracking, and an integrated Gemini Flash AI Pet Health Advisor.",
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
    description: "An artisanal, interactive sensory product brand experience designed for Royal Rose Milk, featuring a real-time bottle formulation engine, dynamic price calculations, and smooth micro-animations.",
    liveUrl: ROYAL_ROSE_MILK_URL,
    specs: [
        { label: "LIVE SERVER", value: ROYAL_ROSE_MILK_URL },
        { label: "FRONTEND CORE", value: "HTML5, Vanilla CSS3, JavaScript ES6+" },
        { label: "CLIENT LOGIC", value: "Real-time State Formulation Engine" },
        { label: "EXPERIENCE", value: "Sensory Interactive Brand UI" },
        { label: "PERFORMANCE", value: "Hardware-Accelerated 60 FPS" }
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

const AURELIS_DATA = {
    title: "AURELIS",
    badge: "FLAGSHIP // LUXURY WATCH E-COMMERCE",
    heroImg: "images/projects/aurelis-watch.jpg",
    heading: "AURELIS — Luxury Watch E-Commerce Platform",
    description: "AURELIS is a premium full-stack watch e-commerce platform built with a luxury-focused interface, customer accounts, shopping workflows, checkout, order management and an administrative dashboard.",
    liveUrl: AURELIS_URL,
    specs: [
        { label: "LIVE SERVER", value: AURELIS_URL },
        { label: "BACKEND STACK", value: "Python / Flask REST Server" },
        { label: "FRONTEND UI", value: "HTML5, CSS3, JavaScript (ES6+)" },
        { label: "DATABASE", value: "SQLite Relational Store" },
        { label: "HOSTING", value: "Render Production Cloud" },
        { label: "ARCHITECTURE", value: "Modular Full-Stack E-Commerce" }
    ],
    features: [
        { title: "10 Luxury Watch Products", desc: "Curated collection of high-precision horological timepieces with detailed specifications and macro photography." },
        { title: "Product Details & Caliber Specs", desc: "Interactive caliber telemetry, case dimensions, water resistance ratings, and dial visualizer." },
        { title: "Shopping Cart & Checkout", desc: "Persistent shopping cart workflow with dynamic price calculation and secure payment flow." },
        { title: "Customer Accounts & Auth", desc: "User registration, session-based customer authentication, and profile management." },
        { title: "Order Management & Tracking", desc: "End-to-end customer order history and real-time shipment status tracking." },
        { title: "Admin Management Panel", desc: "Dedicated administrative dashboard for product inventory management and order processing." },
        { title: "SQLite Database Store", desc: "Relational database modeling for products, user accounts, orders, and cart sessions." },
        { title: "Responsive Luxury UI", desc: "Bespoke dark obsidian and satin gold aesthetic optimized for desktop, tablet, and mobile devices." }
    ],
    codeSnippet: `@app.route('/api/orders/checkout', methods=['POST'])
def process_watch_checkout():
    user_id = session.get('user_id')
    cart_items = get_cart_by_user(user_id)
    
    total_amount = sum(item['price'] * item['quantity'] for item in cart_items)
    order_id = generate_order_number()
    
    # Persist order transaction to SQLite database
    db.execute("""
        INSERT INTO orders (order_id, user_id, total, status, created_at)
        VALUES (?, ?, ?, 'Confirmed', CURRENT_TIMESTAMP)
    """, (order_id, user_id, total_amount))
    db.commit()
    
    clear_user_cart(user_id)
    return jsonify({
        "status": "success",
        "order_id": order_id,
        "total": total_amount,
        "message": "AURELIS Order Placed Successfully"
    })`
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
    if (projectId === "aurelis" || projectId === "aurelisWatch") data = AURELIS_DATA;

    if (titleEl) titleEl.textContent = data.title;
    if (badgeEl) badgeEl.textContent = data.badge;
    if (heroImgEl) {
        heroImgEl.src = data.heroImg;
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
                            <option value="skin_itching">Dermatological Irritation</option>
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
   11. UTILITIES: TOAST NOTIFICATIONS & CLIPBOARD
   -------------------------------------------------------------------------- */
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

function copySnippet() {
    const code = document.getElementById("modalCodeSnippet");
    if (code && navigator.clipboard) {
        navigator.clipboard.writeText(code.textContent).then(() => {
            showToast("Architecture code copied to clipboard!");
        });
    }
}

/* --------------------------------------------------------------------------
   12. HERO ORBITAL CIRCULAR NAVIGATION CONTROLS
   Dot 1 -> #about (About Me)
   Dot 2 -> projects.html (Project Gallery)
   Dot 3 -> #contact (Contact)
   -------------------------------------------------------------------------- */
function initCircularOrbitNav() {
    const orbitDots = document.querySelectorAll(".sample-satellite-dot");
    if (!orbitDots.length) return;

    const navbar = document.getElementById("navbar");

    // Click handler for all 3 dots with smooth scroll and offset
    orbitDots.forEach(dot => {
        dot.addEventListener("click", function(e) {
            const href = this.getAttribute("href");
            // If it's a page link (e.g. projects.html), allow normal navigation to Project Gallery
            if (href && (href.endsWith(".html") || !href.startsWith("#"))) {
                return;
            }

            e.preventDefault();
            const targetId = this.getAttribute("data-orbit-target");
            if (!targetId) return;

            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                const navHeight = navbar ? navbar.offsetHeight : 70;
                const targetY = targetSection.getBoundingClientRect().top + window.pageYOffset - navHeight - 15;

                window.scrollTo({
                    top: Math.max(0, targetY),
                    behavior: "smooth"
                });

                // Immediate active visual feedback
                orbitDots.forEach(d => d.classList.remove("active"));
                this.classList.add("active");

                // Update URL hash without jumping
                if (history.pushState) {
                    history.pushState(null, null, `#${targetId}`);
                }
            }
        });
    });

    // Scroll spy for automatic active dot detection on Home page
    const sectionTargets = [
        { id: "about", dotId: "orbitDotAbout" },
        { id: "contact", dotId: "orbitDotContact" }
    ];

    function updateActiveOrbitDots() {
        const scrollPosition = window.pageYOffset;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        const navOffset = (navbar ? navbar.offsetHeight : 70) + 40;

        let activeTargetId = null;

        // If user is near the bottom of the page, contact is active
        if (scrollPosition + windowHeight >= documentHeight - 80) {
            activeTargetId = "contact";
        } else {
            sectionTargets.forEach(({ id }) => {
                const sec = document.getElementById(id);
                if (sec) {
                    const top = sec.offsetTop - navOffset;
                    const height = sec.offsetHeight;
                    if (scrollPosition >= top && scrollPosition < top + height) {
                        activeTargetId = id;
                    }
                }
            });
        }

        orbitDots.forEach(dot => {
            const target = dot.getAttribute("data-orbit-target");
            if (target === activeTargetId) {
                dot.classList.add("active");
            } else {
                dot.classList.remove("active");
            }
        });
    }

    window.addEventListener("scroll", updateActiveOrbitDots, { passive: true });
    updateActiveOrbitDots();
}