/* ==========================================================================
   RAJKUMAR — HYPER-CINEMATIC & MOBILE INTERACTIVITY CONTROLLER
   Quantum Loader HUD Engine, Mobile Touch Physics & Ambient Telemetry
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
    initCinematicLoaderEngine();
    initMobileActionDock();
    initMobileTouchCanvas();
    initTouchCardTilt();
});

/* --------------------------------------------------------------------------
   1. HYPER-CINEMATIC QUANTUM LOADER CONTROLLER (FAIL-SAFE & ULTRA-SMOOTH)
   -------------------------------------------------------------------------- */
function initCinematicLoaderEngine() {
    const loader = document.getElementById("intro");
    const progressFill = document.getElementById("loaderProgressFill");
    const percentageText = document.getElementById("loaderPercentText");
    const statusFeed = document.getElementById("loaderStatusFeed");
    const enterBtn = document.getElementById("skipLoaderBtn");

    if (!loader) {
        document.body.classList.add("loaded");
        return;
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
    if (enterBtn) {
        enterBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            dismissCinematicLoader();
        });
    }

    // Telemetry logs
    const telemetryLogs = [
        "INITIALIZING FULL-STACK ENGINE...",
        "MOUNTING PYTHON & FLASK APIS...",
        "INTEGRATING SQLITE DATA STORE...",
        "LOADING AI CORE ARCHITECTURE...",
        "SYSTEMS 100% READY • WELCOME TO RAJKUMAR'S PORTFOLIO"
    ];

    let currentPercent = 0;
    const targetPercent = 100;
    let startTime = null;
    const duration = 1400; // Fast & responsive 1.4s

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
            statusFeed.innerHTML = `<span class="hud-pulse"></span> ${telemetryLogs[feedIndex]}`;
        }

        if (progressRatio < 1) {
            requestAnimationFrame(animateLoader);
        } else {
            if (progressFill) progressFill.style.width = "100%";
            if (percentageText) percentageText.textContent = "100%";
            setTimeout(dismissCinematicLoader, 250);
        }
    }

    requestAnimationFrame(animateLoader);

    // Absolute hard failsafe: dismiss after 2s no matter what
    setTimeout(dismissCinematicLoader, 2000);
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
