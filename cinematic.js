/* ==========================================================================
   RAJ KUMAR — HYPER-CINEMATIC & MOBILE INTERACTIVITY CONTROLLER
   Quantum Loader HUD Engine, Mobile Touch Physics & Ambient Telemetry
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
    initCinematicLoaderEngine();
    initMobileActionDock();
    initMobileTouchCanvas();
    initTouchCardTilt();
});

/* --------------------------------------------------------------------------
   1. HYPER-CINEMATIC QUANTUM LOADER CONTROLLER
   -------------------------------------------------------------------------- */
function initCinematicLoaderEngine() {
    const loader = document.getElementById("intro");
    const progressFill = document.getElementById("loaderProgressFill");
    const percentageText = document.getElementById("loaderPercentText");
    const statusFeed = document.getElementById("loaderStatusFeed");
    const enterBtn = document.getElementById("skipLoaderBtn");

    if (!loader) return;

    // Check if user already saw the intro in this browser session
    const seen = sessionStorage.getItem("raj_kumar_intro_seen_v2");
    if (seen) {
        loader.classList.add("loader-hidden");
        document.body.classList.add("loaded");
        return;
    }

    const telemetryLogs = [
        "INITIALIZING QUANTUM MATRIX...",
        "ACTIVATING NEURAL AI ENGINE...",
        "MOUNTING PYTHON & FLASK ARCHITECTURE...",
        "RENDERING CINEMATIC VIEWPORTS...",
        "CONNECTING SQLITE DATA LAYER...",
        "SYNCHRONIZING INTERACTIVE PARTICLES...",
        "SYSTEMS OPTIMAL • WELCOME TO PORTFOLIO"
    ];

    let currentPercent = 0;
    let targetPercent = 100;
    let startTime = null;
    const duration = 2200; // 2.2 seconds luxury cinematic duration

    function animateLoader(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progressRatio = Math.min(elapsed / duration, 1);

        // Smooth ease-out-cubic curve
        const easeProgress = 1 - Math.pow(1 - progressRatio, 3);
        currentPercent = Math.floor(easeProgress * targetPercent);

        // Update progress bar width
        if (progressFill) {
            progressFill.style.width = `${currentPercent}%`;
        }

        // Update percentage digital readout
        if (percentageText) {
            percentageText.textContent = `${String(currentPercent).padStart(2, '0')}%`;
        }

        // Cycle through status feeds
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
            // Completed
            if (progressFill) progressFill.style.width = "100%";
            if (percentageText) percentageText.textContent = "100%";
            setTimeout(dismissCinematicLoader, 400);
        }
    }

    requestAnimationFrame(animateLoader);

    function dismissCinematicLoader() {
        loader.classList.add("loader-hidden");
        document.body.classList.add("loaded");
        sessionStorage.setItem("raj_kumar_intro_seen_v2", "true");

        // Trigger smooth reveal animation for the hero section
        const heroStage = document.getElementById("portraitStage");
        if (heroStage) {
            heroStage.style.transform = "scale(1)";
        }
    }

    if (enterBtn) {
        enterBtn.addEventListener("click", dismissCinematicLoader);
    }
}

/* --------------------------------------------------------------------------
   2. MOBILE FLOATING ACTION COMMAND DOCK
   -------------------------------------------------------------------------- */
function initMobileActionDock() {
    const dock = document.getElementById("mobileActionDock");
    if (!dock) return;

    let lastScrollY = window.scrollY;

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
   4. TOUCH CARD 3D TILT EFFECT FOR MOBILE & DESKTOP
   -------------------------------------------------------------------------- */
function initTouchCardTilt() {
    const cards = document.querySelectorAll(".cinematic-project-showcase, .skills-card, .editorial-manifesto-card");
    
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
