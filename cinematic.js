/* ==========================================================================
   RAJKUMAR — HYPER-CINEMATIC & MOBILE INTERACTIVITY CONTROLLER
   Clean, performant editorial reveal and responsive dock
   ========================================================================== */

/* --------------------------------------------------------------------------
   LOADER CUSTOMIZATION SETTINGS
   -------------------------------------------------------------------------- */
window.LOADER_CONFIG = {
    enabled: true,          // Set to false to disable the loading screen completely
    durationMs: 480         // Ultra-fast & sleek 0.48s reveal
};

document.addEventListener("DOMContentLoaded", () => {
    initCinematicLoaderEngine();
    initMobileActionDock();
    initMobileTouchCanvas();
});

/* --------------------------------------------------------------------------
   1. LUXURY MINIMALIST EDITORIAL REVEAL CONTROLLER
   -------------------------------------------------------------------------- */
function initCinematicLoaderEngine() {
    const loader = document.getElementById("intro");
    const progressFill = document.getElementById("loaderProgressFill");

    if (!loader) {
        document.body.classList.add("loaded");
        return;
    }

    if (window.LOADER_CONFIG && window.LOADER_CONFIG.enabled === false) {
        loader.remove();
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

        setTimeout(() => {
            try { loader.remove(); } catch (e) { }
        }, 500);
    }

    loader.addEventListener("click", dismissCinematicLoader);

    // Smooth hairline growth
    setTimeout(() => {
        if (progressFill) {
            progressFill.style.width = "120px";
        }
    }, 40);

    const duration = (window.LOADER_CONFIG && window.LOADER_CONFIG.durationMs) || 480;
    setTimeout(dismissCinematicLoader, duration);

    // Hard failsafe
    setTimeout(dismissCinematicLoader, 1200);
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
