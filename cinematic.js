/* ==========================================================================
   RAJKUMAR — HYPER-CINEMATIC & MOBILE INTERACTIVITY CONTROLLER
   ========================================================================== */

/* --------------------------------------------------------------------------
   LOADER CUSTOMIZATION SETTINGS
   You can easily customize or disable the loading screen here!
   -------------------------------------------------------------------------- */
window.LOADER_CONFIG = {
    enabled: true,          // Set to false to disable the loading screen completely
    durationMs: 900,        // Speed in milliseconds (e.g., 800 = 0.8s fast, 1200 = 1.2s cinematic)
    monogram: "R.",         // Text inside the central logo
    nameText: "RAJKUMAR",   // Title text
    roleText: "WEB DEVELOPMENT • AI SYSTEMS"
};

document.addEventListener("DOMContentLoaded", () => {
    initCinematicLoaderEngine();
    initMobileActionDock();
    initMobileTouchCanvas();
    initTouchCardTilt();
});

/* --------------------------------------------------------------------------
   1. COMPACT ULTRA-LUXURY LOADER CONTROLLER (CUSTOMIZABLE & FAST)
   -------------------------------------------------------------------------- */
function initCinematicLoaderEngine() {
    const loader = document.getElementById("intro");
    const progressFill = document.getElementById("loaderProgressFill");
    const percentageText = document.getElementById("loaderPercentText");
    const statusFeed = document.getElementById("loaderStatusFeed");

    if (!loader) {
        document.body.classList.add("loaded");
        return;
    }

    // Check if loader is disabled in config
    if (window.LOADER_CONFIG && window.LOADER_CONFIG.enabled === false) {
        loader.remove();
        document.body.classList.add("loaded");
        return;
    }

    // Apply custom text if configured
    if (window.LOADER_CONFIG) {
        const monogramEl = document.getElementById("loaderMonogram");
        const nameEl = document.getElementById("loaderName");
        const roleEl = document.getElementById("loaderRole");
        if (monogramEl && window.LOADER_CONFIG.monogram) monogramEl.textContent = window.LOADER_CONFIG.monogram;
        if (nameEl && window.LOADER_CONFIG.nameText) nameEl.textContent = window.LOADER_CONFIG.nameText;
        if (roleEl && window.LOADER_CONFIG.roleText) roleEl.textContent = window.LOADER_CONFIG.roleText;
    }

    let isDismissed = false;

    function dismissCinematicLoader() {
        if (isDismissed) return;
        isDismissed = true;
        loader.classList.add("loader-hidden");
        document.body.classList.add("loaded");
        document.body.style.overflow = "";

        const heroStage = document.getElementById("portraitStage");
        if (heroStage) {
            heroStage.style.transform = "scale(1)";
        }
    }

    // Click anywhere on loader to skip instantly
    loader.addEventListener("click", dismissCinematicLoader);

    // Status logs
    const telemetryLogs = [
        "INITIALIZING...",
        "LOADING APIS...",
        "READY"
    ];

    let currentPercent = 0;
    const targetPercent = 100;
    let startTime = null;
    const duration = (window.LOADER_CONFIG && window.LOADER_CONFIG.durationMs) || 900;

    function animateLoader(timestamp) {
        if (isDismissed) return;
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progressRatio = Math.min(elapsed / duration, 1);

        const easeProgress = 1 - Math.pow(1 - progressRatio, 2.5);
        currentPercent = Math.min(Math.floor(easeProgress * targetPercent), 100);

        if (progressFill) {
            progressFill.style.width = `${currentPercent}%`;
        }

        if (percentageText) {
            percentageText.textContent = `${String(currentPercent).padStart(2, '0')}%`;
        }

        if (statusFeed) {
            const feedIndex = Math.min(
                Math.floor(progressRatio * telemetryLogs.length),
                telemetryLogs.length - 1
            );
            statusFeed.textContent = telemetryLogs[feedIndex];
        }

        if (progressRatio < 1) {
            requestAnimationFrame(animateLoader);
        } else {
            if (progressFill) progressFill.style.width = "100%";
            if (percentageText) percentageText.textContent = "100%";
            setTimeout(dismissCinematicLoader, 180);
        }
    }

    requestAnimationFrame(animateLoader);

    // Hard failsafe: dismiss after 1.8s
    setTimeout(dismissCinematicLoader, 1800);
}

/* --------------------------------------------------------------------------
   2. MOBILE FLOATING ACTION COMMAND DOCK
   -------------------------------------------------------------------------- */
function initMobileActionDock() {
    const dock = document.getElementById("mobileActionDock");
    if (!dock) return;

    function updateDockVisibility() {
        if (window.innerWidth <= 992) {
            if (window.scrollY > 120) {
                dock.classList.add("dock-visible");
            } else {
                dock.classList.remove("dock-visible");
            }
        } else {
            dock.classList.remove("dock-visible");
        }
    }

    window.addEventListener("scroll", updateDockVisibility, { passive: true });
    window.addEventListener("resize", updateDockVisibility);
    updateDockVisibility();
}

/* --------------------------------------------------------------------------
   3. MOBILE TOUCH PARTICLE INTERACTION
   -------------------------------------------------------------------------- */
function initMobileTouchCanvas() {
    const canvas = document.getElementById("cinematicCanvas");
    if (!canvas) return;

    window.addEventListener("touchmove", (e) => {
        if (e.touches && e.touches.length > 0) {
            const touch = e.touches[0];
            const event = new MouseEvent("mousemove", {
                clientX: touch.clientX,
                clientY: touch.clientY
            });
            window.dispatchEvent(event);
        }
    }, { passive: true });

    window.addEventListener("touchend", () => {
        const event = new MouseEvent("mouseleave");
        window.dispatchEvent(event);
    }, { passive: true });
}

/* --------------------------------------------------------------------------
   4. TOUCH CARD 3D TILT EFFECT
   -------------------------------------------------------------------------- */
function initTouchCardTilt() {
    const cards = document.querySelectorAll(".luxury-work-banner-card, .stat-box-card, .gold-skill-badge");
    
    cards.forEach(card => {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = ((y - centerY) / centerY) * -4;
            const rotateY = ((x - centerX) / centerX) * 4;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)";
        });
    });
}
