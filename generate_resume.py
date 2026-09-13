import os
import base64
import subprocess
import shutil
import re
import pypdf

os.makedirs('resume', exist_ok=True)
os.makedirs('images', exist_ok=True)
os.makedirs('assets', exist_ok=True)

# Load embedded vector fonts CSS
with open('resume/embedded_fonts.css', 'r', encoding='utf-8') as f:
    embedded_fonts_css = f.read()

# Generate the pristine white/black vector resume matching the user's PDF
def build_clean_vector_resume_html(variant='classic_clean'):
    # Color tokens
    if variant == 'luxury_gold':
        gold_accent = "#C59B27"
        gold_deep = "#926700"
        heading_color = "#000000"
        sub_heading_color = "#111115"
        border_box = "#E2DFD6"
        footer_bg = "#F8F6F0"
        link_color = "#926700"
    else:
        # Exact monochrome classic white & black
        gold_accent = "#111115"
        gold_deep = "#22222A"
        heading_color = "#000000"
        sub_heading_color = "#1A1A20"
        border_box = "#E5E5EB"
        footer_bg = "#F7F7FA"
        link_color = "#0A58CA"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAJ KUMAR — WEB DEVELOPER RESUME</title>
    <meta name="description" content="Raj Kumar - Web Developer Resume. Skills: HTML5, CSS3, JavaScript, Python, Flask, Git, GitHub, VS Code.">

    <style>
        /* ==================== EMBEDDED TRUE VECTOR FONTS ==================== */
        {embedded_fonts_css}

        @page {{
            size: A4 portrait;
            margin: 0;
        }}

        :root {{
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
            --text-main: #1D1D24;
            --text-heading: {heading_color};
            --text-sub: {sub_heading_color};
            --text-muted: #555562;
            --accent: {gold_accent};
            --border-line: #E0DFE6;
            --box-border: {border_box};
            --box-bg: {footer_bg};
            --link-color: {link_color};
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        html, body {{
            margin: 0;
            padding: 0;
            width: 210mm;
            height: 297mm;
            max-height: 297mm;
            overflow: hidden;
            background-color: #FFFFFF;
            font-family: var(--font-sans);
            color: var(--text-main);
            line-height: 1.36;
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }}

        body {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
        }}

        /* Web Interactive Action Toolbar (Hidden in Print/PDF) */
        .web-toolbar {{
            width: 210mm;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 8px 0 6px 0;
            background: #0D0D12;
            padding: 8px 18px;
            border-radius: 6px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            border: 1px solid rgba(212, 175, 55, 0.3);
        }}

        .toolbar-title {{
            color: #FFFFFF;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .toolbar-actions {{
            display: flex;
            gap: 8px;
        }}

        .toolbar-btn {{
            background: #1C1C24;
            color: #FFFFFF;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 5px 12px;
            border-radius: 4px;
            font-size: 10.5px;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            text-decoration: none;
            transition: all 0.2s ease;
        }}

        .toolbar-btn:hover {{
            background: #D4AF37;
            color: #000000;
        }}

        .toolbar-btn-primary {{
            background: #D4AF37;
            color: #000000;
            font-weight: 700;
            border: none;
        }}

        /* Master Single-Page Vector Canvas */
        .resume-page {{
            width: 210mm;
            height: 297mm;
            max-height: 297mm;
            min-height: 297mm;
            background-color: #FFFFFF;
            padding: 14mm 18mm 12mm 18mm;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            gap: 9px;
            position: relative;
            overflow: hidden;
            page-break-inside: avoid !important;
            page-break-after: avoid !important;
            break-inside: avoid !important;
            break-after: avoid !important;
        }}

        /* ==================== HEADER SECTION ==================== */
        .header-section {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            width: 100%;
            border-bottom: 1.5px solid var(--border-line);
            padding-bottom: 6px;
            margin-bottom: 2px;
        }}

        .header-left {{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            text-align: left;
            gap: 1.5px;
        }}

        .candidate-name {{
            font-size: 26px;
            font-weight: 800;
            color: var(--text-heading);
            letter-spacing: 0.8px;
            line-height: 1.1;
            text-transform: uppercase;
        }}

        .candidate-role {{
            font-size: 11.5px;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: var(--text-sub);
            text-transform: uppercase;
            margin-top: 1px;
        }}

        .contact-bar {{
            font-size: 9px;
            color: var(--text-muted);
            margin-top: 3px;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 5px;
            line-height: 1.3;
        }}

        .contact-bar a {{
            color: var(--text-main);
            text-decoration: none;
            transition: color 0.15s ease;
        }}

        .contact-bar a:hover {{
            text-decoration: underline;
        }}

        .divider-dot {{
            color: #9999A5;
            font-size: 9px;
        }}

        /* Top-Right Header Portfolio Link */
        .header-right {{
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            text-align: right;
            gap: 2.5px;
            padding-top: 2px;
            flex-shrink: 0;
        }}

        .portfolio-label-badge {{
            font-size: 8.5px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--text-heading);
            background: var(--box-bg);
            border: 1px solid var(--box-border);
            padding: 2px 7px;
            border-radius: 3px;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            text-decoration: none;
            transition: all 0.15s ease;
        }}

        .portfolio-label-badge:hover {{
            border-color: var(--text-heading);
        }}

        .portfolio-hyperlink {{
            font-family: var(--font-mono);
            font-size: 8.4px;
            font-weight: 600;
            color: var(--link-color);
            text-decoration: underline;
            letter-spacing: -0.1px;
            transition: color 0.15s ease;
            display: inline-block;
        }}

        .portfolio-hyperlink:hover {{
            color: #084298;
        }}

        /* ==================== SECTION BLOCKS ==================== */
        .section-block {{
            display: flex;
            flex-direction: column;
            gap: 3px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .section-title {{
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 0.6px;
            text-transform: uppercase;
            color: var(--text-heading);
            border-bottom: 1.2px solid var(--text-heading);
            padding-bottom: 1.5px;
            margin-bottom: 1.5px;
        }}

        .section-body {{
            font-size: 9.3px;
            color: var(--text-main);
            line-height: 1.42;
            text-align: justify;
        }}

        /* Sub-Item Heading & Content */
        .item-block {{
            display: flex;
            flex-direction: column;
            gap: 1.5px;
            margin-bottom: 2.5px;
        }}

        .item-title-row {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }}

        .item-heading {{
            font-size: 10.2px;
            font-weight: 700;
            color: var(--text-heading);
        }}

        .item-subheading {{
            font-size: 9.1px;
            color: var(--text-muted);
            font-weight: 500;
        }}

        .item-desc {{
            font-size: 9.2px;
            color: var(--text-main);
            line-height: 1.4;
        }}

        /* Technical Skills List */
        .skills-list {{
            display: flex;
            flex-direction: column;
            gap: 2px;
            font-size: 9.2px;
            line-height: 1.36;
        }}

        .skill-item {{
            display: flex;
            align-items: flex-start;
            gap: 4px;
        }}

        .skill-label {{
            font-weight: 700;
            color: var(--text-heading);
            flex-shrink: 0;
        }}

        .skill-val {{
            color: var(--text-main);
        }}

        /* Footer Banner Callout */
        .footer-banner {{
            margin-top: auto;
            background: var(--box-bg);
            border: 1px solid var(--box-border);
            border-radius: 4px;
            padding: 6px 12px;
            font-size: 8.8px;
            font-weight: 600;
            color: var(--text-heading);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .footer-banner a {{
            color: var(--text-heading);
            text-decoration: none;
            font-weight: 700;
        }}

        /* Print Strict Settings */
        @media print {{
            @page {{
                size: A4 portrait;
                margin: 0;
            }}
            html, body {{
                background-color: transparent !important;
                margin: 0 !important;
                padding: 0 !important;
                width: 210mm !important;
                height: 297mm !important;
                max-height: 297mm !important;
                overflow: hidden !important;
                box-sizing: border-box !important;
            }}
            .web-toolbar {{
                display: none !important;
            }}
            .resume-page {{
                box-shadow: none !important;
                width: 210mm !important;
                height: 297mm !important;
                max-height: 297mm !important;
                margin: 0 !important;
                padding: 14mm 18mm 12mm 18mm !important;
                page-break-inside: avoid !important;
                page-break-after: avoid !important;
                break-inside: avoid !important;
                break-after: avoid !important;
                overflow: hidden !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- Web Action Toolbar -->
    <div class="web-toolbar">
        <div class="toolbar-title">
            <strong>RAJ KUMAR</strong> &bull; True Vector Resume
        </div>
        <div class="toolbar-actions">
            <a href="../index.html" class="toolbar-btn">
                <span>&larr; Portfolio</span>
            </a>
            <button onclick="window.print()" class="toolbar-btn">
                <span>Print</span>
            </button>
            <a href="../assets/Raj_Kumar_Resume_Full_Page.pdf" download="Raj_Kumar_Resume_Full_Page.pdf" class="toolbar-btn toolbar-btn-primary">
                <span>Download PDF (Vector)</span>
            </a>
        </div>
    </div>

    <!-- Master Single Page Canvas -->
    <main class="resume-page">
        <!-- ==================== HEADER ==================== -->
        <header class="header-section">
            <div class="header-left">
                <h1 class="candidate-name">RAJ KUMAR</h1>
                <div class="candidate-role">WEB DEVELOPER</div>
                <div class="contact-bar">
                    <span>Tirunelveli | Tamil Nadu</span>
                    <span class="divider-dot">&bull;</span>
                    <a href="mailto:vikneshvaren2@gmail.com">vikneshvaren2@gmail.com</a>
                    <span class="divider-dot">&bull;</span>
                    <a href="tel:+919445437069">+91 9445437069</a>
                </div>
            </div>
            <div class="header-right">
                <a href="https://vikneshvaren2007.github.io/portfolioclg/" target="_blank" rel="noopener noreferrer" class="portfolio-label-badge">
                    <span>PORTFOLIO</span>
                    <svg width="8" height="8" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M1 9L9 1M9 1H3M9 1V7"/></svg>
                </a>
                <a href="https://vikneshvaren2007.github.io/portfolioclg/" target="_blank" rel="noopener noreferrer" class="portfolio-hyperlink">
                    https://vikneshvaren2007.github.io/portfolioclg/
                </a>
            </div>
        </header>

        <!-- ==================== PROFILE ==================== -->
        <section class="section-block">
            <h2 class="section-title">PROFILE</h2>
            <p class="section-body">
                Creative and motivated Web Developer with hands-on experience building responsive, modern websites using HTML, CSS, JavaScript, Python and Flask. Interested in creating clean user interfaces, practical web solutions and visually engaging digital experiences.
            </p>
        </section>

        <!-- ==================== EXPERIENCE ==================== -->
        <section class="section-block">
            <h2 class="section-title">EXPERIENCE</h2>
            <div class="item-block">
                <div class="item-heading">Web Development Experience &mdash; 2 Years</div>
                <p class="item-desc">
                    Worked on personal and academic web projects, focusing on responsive layouts, frontend interactions, Flask-based backend features, forms, booking flows, deployment and website improvements.
                </p>
            </div>
        </section>

        <!-- ==================== EDUCATION ==================== -->
        <section class="section-block">
            <h2 class="section-title">EDUCATION</h2>
            <div class="item-block">
                <div class="item-heading">B.Sc. Computer Science &mdash; 3rd Year</div>
                <p class="item-desc">
                    Developing strong foundations in programming, web technologies, databases and software development.
                </p>
            </div>
        </section>

        <!-- ==================== TECHNICAL SKILLS ==================== -->
        <section class="section-block">
            <h2 class="section-title">TECHNICAL SKILLS</h2>
            <div class="skills-list">
                <div class="skill-item">
                    <span class="skill-label">Frontend:</span>
                    <span class="skill-val">HTML5, CSS3, JavaScript</span>
                </div>
                <div class="skill-item">
                    <span class="skill-label">Backend:</span>
                    <span class="skill-val">Python, Flask</span>
                </div>
                <div class="skill-item">
                    <span class="skill-label">Tools:</span>
                    <span class="skill-val">Git, GitHub, VS Code</span>
                </div>
                <div class="skill-item">
                    <span class="skill-label">Core:</span>
                    <span class="skill-val">Responsive Web Design, UI Development, Forms, APIs, Deployment</span>
                </div>
            </div>
        </section>

        <!-- ==================== PROJECTS ==================== -->
        <section class="section-block">
            <h2 class="section-title">PROJECTS</h2>
            
            <div class="item-block">
                <div class="item-heading">PET NEXA &mdash; Pet Care Web Platform</div>
                <p class="item-desc">
                    A pet-care platform featuring services, specialist information, pet shopping, booking management, order tracking and an AI pet-advisor concept.
                </p>
            </div>

            <div class="item-block">
                <div class="item-heading">ROYAL Rose Milk &mdash; Brand Website</div>
                <p class="item-desc">
                    A visually rich product website designed around a premium rose-milk brand identity, with animated sections, product presentation and interactive shopping element.
                </p>
            </div>
        </section>

        <!-- ==================== STRENGTHS ==================== -->
        <section class="section-block">
            <h2 class="section-title">STRENGTHS</h2>
            <p class="section-body">
                Creative problem solving &bull; Quick learner &bull; Responsive design &bull; Clean UI thinking &bull; Project development &bull; Willingness to learn new technologies
            </p>
        </section>

        <!-- ==================== CAREER OBJECTIVE ==================== -->
        <section class="section-block">
            <h2 class="section-title">CAREER OBJECTIVE</h2>
            <p class="section-body">
                To grow as a professional Web Developer by working on real-world projects, improving my technical skills and creating useful, modern and user-friendly websites.
            </p>
        </section>

        <!-- ==================== FOOTER CALLOUT ==================== -->
        <footer class="footer-banner">
            <span>Portfolio: Web Development Projects</span>
            <span>|</span>
            <span>Availability: Open to Web Development Opportunities</span>
        </footer>
    </main>
</body>
</html>
"""
    return html

# Write out the clean vector resume HTML
html_clean = build_clean_vector_resume_html('classic_clean')
html_gold = build_clean_vector_resume_html('luxury_gold')

with open('resume/resume.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

with open('resume/resume_gold_white.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

with open('resume/resume_gold_black.html', 'w', encoding='utf-8') as f:
    f.write(html_gold)

print("[OK] Written resume/resume.html matching reference image!")

# Export to PDF via Headless Chrome
chrome_candidates = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

browser_exe = None
for b in chrome_candidates:
    if os.path.exists(b):
        browser_exe = b
        break

if browser_exe:
    abs_html = os.path.abspath('resume/resume.html').replace('\\', '/')
    abs_pdf = os.path.abspath('resume/Raj_Kumar_Resume.pdf')
    abs_root_pdf = os.path.abspath('Raj_Kumar_Resume.pdf')
    
    # Export Flagship PDF
    subprocess.run([
        browser_exe,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--hide-scrollbars',
        f'--print-to-pdf={abs_pdf}',
        f'file:///{abs_html}'
    ], check=True)
    
    # Copy to workspace root and variants
    shutil.copy(abs_pdf, abs_root_pdf)
    shutil.copy(abs_pdf, 'assets/Raj_Kumar_Resume_Full_Page.pdf')
    shutil.copy(abs_pdf, 'resume/Raj_Kumar_Resume_Full_Page.pdf')
    shutil.copy(abs_pdf, 'Raj_Kumar_Resume_Full_Page.pdf')
    shutil.copy(abs_pdf, 'Raj_Kumar_Resume_Gold_White.pdf')
    shutil.copy(abs_pdf, 'Raj_Kumar_Resume_Gold_Black.pdf')
    shutil.copy(abs_pdf, 'resume/Raj_Kumar_Resume_Gold_White.pdf')
    shutil.copy(abs_pdf, 'resume/Raj_Kumar_Resume_Gold_Black.pdf')
    
    # Verify with pypdf
    reader = pypdf.PdfReader(abs_pdf)
    print(f"[SUCCESS] Exported {abs_pdf} -> Total Pages: {len(reader.pages)}")
    
    page = reader.pages[0]
    print("\n--- Hyperlink Annotations Audit ---")
    if '/Annots' in page:
        for a in page['/Annots']:
            obj = a.get_object()
            uri = obj.get('/A', {}).get('/URI', 'N/A')
            rect = obj.get('/Rect', [])
            print(f"  URI: {uri} | Rect: {rect}")
    else:
        print("  WARNING: No annotations found!")
    
    text_sample = page.extract_text()
    print("\n=== Extracted Text Preview ===")
    print(text_sample[:400])
    print("==============================")
else:
    print("Error: Browser executable not found.")
