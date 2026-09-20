import os
import subprocess
import shutil
import pypdf

os.makedirs('resume', exist_ok=True)
os.makedirs('images', exist_ok=True)
os.makedirs('assets', exist_ok=True)

# Load embedded vector fonts CSS
with open('resume/embedded_fonts.css', 'r', encoding='utf-8') as f:
    embedded_fonts_css = f.read()

def build_vector_resume_html(variant='classic_clean'):
    # Colors
    if variant == 'luxury_gold':
        heading_color = "#000000"
        sub_heading_color = "#926700"
        border_rule = "#C59B27"
        link_color = "#926700"
    else:
        heading_color = "#000000"
        sub_heading_color = "#111111"
        border_rule = "#B0B0BA"
        link_color = "#0A58CA"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>B.K RAJ KUMAR — RESUME</title>
    <meta name="description" content="B.K Raj Kumar - Web Developer | AI Enthusiast | Fresher Resume. Skills: HTML5, CSS3, JavaScript, Python, Flask, SQLite, Git, GitHub, VS Code.">

    <style>
        /* ==================== EMBEDDED TRUE VECTOR FONTS ==================== */
        {embedded_fonts_css}

        @page {{
            size: A4 portrait;
            margin: 0;
        }}

        :root {{
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            --text-heading: {heading_color};
            --text-sub: {sub_heading_color};
            --text-body: #1E1E24;
            --border-rule: {border_rule};
            --link-color: {link_color};
            --footer-text: #767682;
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
            background-color: #EFEFF3;
            font-family: var(--font-sans);
            color: var(--text-body);
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }}

        body {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding: 12px 0 24px 0;
            min-height: 100vh;
        }}

        /* Web Interactive Action Toolbar (Hidden in Print/PDF) */
        .web-toolbar {{
            width: 210mm;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            background: #0E0E14;
            padding: 9px 18px;
            border-radius: 6px;
            box-shadow: 0 4px 18px rgba(0,0,0,0.25);
            border: 1px solid rgba(212, 175, 55, 0.3);
        }}

        .toolbar-title {{
            color: #FFFFFF;
            font-size: 12.5px;
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
            padding: 6px 14px;
            border-radius: 4px;
            font-size: 11px;
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

        /* Master Single-Page A4 Canvas */
        .resume-page {{
            width: 210mm;
            height: 297mm;
            max-height: 297mm;
            min-height: 297mm;
            background-color: #FFFFFF;
            padding: 17mm 22mm 14mm 22mm;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            page-break-inside: avoid !important;
            page-break-after: avoid !important;
            break-inside: avoid !important;
            break-after: avoid !important;
        }}

        /* ==================== HEADER ==================== */
        .header-section {{
            text-align: center;
            width: 100%;
            margin-bottom: 18px;
        }}

        .candidate-name {{
            font-size: 26px;
            font-weight: 800;
            color: var(--text-heading);
            letter-spacing: 0.6px;
            line-height: 1.15;
            text-transform: uppercase;
        }}

        .candidate-role {{
            font-size: 13.5px;
            font-weight: 700;
            color: var(--text-sub);
            letter-spacing: 0.3px;
            margin-top: 5px;
            line-height: 1.2;
        }}

        .contact-bar {{
            font-size: 10.5px;
            color: var(--text-body);
            margin-top: 6px;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 7px;
            line-height: 1.35;
        }}

        .contact-bar a {{
            color: var(--text-body);
            text-decoration: none;
            transition: color 0.15s ease;
        }}

        .contact-bar a.contact-link-portfolio {{
            color: var(--link-color);
            text-decoration: underline;
        }}

        .contact-bar a:hover {{
            text-decoration: underline;
        }}

        .divider-bar {{
            color: #888888;
            font-weight: 400;
        }}

        /* ==================== SECTION BLOCKS ==================== */
        .section-block {{
            margin-bottom: 18px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .section-title {{
            font-size: 14px;
            font-weight: 700;
            color: var(--text-heading);
            border-bottom: 1.2px solid var(--border-rule);
            padding-bottom: 3.5px;
            margin-bottom: 9px;
            letter-spacing: 0.1px;
        }}

        .section-paragraph {{
            font-size: 10.4px;
            color: var(--text-body);
            line-height: 1.54;
            text-align: left;
        }}

        /* Projects */
        .project-item {{
            margin-bottom: 12px;
        }}

        .project-item:last-child {{
            margin-bottom: 0;
        }}

        .project-title {{
            font-size: 11.2px;
            font-weight: 700;
            color: var(--text-heading);
            margin-bottom: 4px;
            line-height: 1.32;
        }}

        /* Project Bullets (Indented) */
        ul.project-bullets {{
            margin: 0 0 0 20px;
            padding: 0;
            list-style-type: disc;
        }}

        ul.project-bullets li {{
            font-size: 10.2px;
            line-height: 1.48;
            color: var(--text-body);
            margin-bottom: 3.5px;
        }}

        ul.project-bullets li:last-child {{
            margin-bottom: 0;
        }}

        /* Standard Section Bullets (Skills, Soft Skills) */
        ul.standard-bullets {{
            margin: 0 0 0 18px;
            padding: 0;
            list-style-type: disc;
        }}

        ul.standard-bullets li {{
            font-size: 10.2px;
            line-height: 1.48;
            color: var(--text-body);
            margin-bottom: 3.5px;
        }}

        ul.standard-bullets li:last-child {{
            margin-bottom: 0;
        }}

        .item-label {{
            font-weight: 700;
            color: var(--text-heading);
        }}

        /* Soft Skills items with clean spacing */
        .soft-skills-list li {{
            margin-bottom: 3px;
        }}

        /* Footer */
        .resume-footer {{
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 9.5px;
            color: var(--footer-text);
            padding-top: 6px;
        }}

        /* Print Strict Settings */
        @media print {{
            @page {{
                size: A4 portrait;
                margin: 0;
            }}
            html, body {{
                background-color: transparent !important;
                background: transparent !important;
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
                min-height: 297mm !important;
                margin: 0 !important;
                padding: 17mm 22mm 14mm 22mm !important;
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

    <!-- Web Action Toolbar (Screen Only) -->
    <div class="web-toolbar">
        <div class="toolbar-title">
            <strong>B.K RAJ KUMAR</strong> &bull; True Vector Resume
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
            <h1 class="candidate-name">B.K RAJ KUMAR</h1>
            <div class="candidate-role">Web Developer | AI Enthusiast | Fresher</div>
            <div class="contact-bar">
                <span>Tamil Nadu, India</span>
                <span class="divider-bar">|</span>
                <a href="mailto:vikneshvaren2@gmail.com">vikneshvaren2@gmail.com</a>
                <span class="divider-bar">|</span>
                <a href="tel:+919445437069">+91 9445437069</a>
                <span class="divider-bar">|</span>
                <a href="https://vikneshvaren2007.github.io/portfolioclg/" target="_blank" rel="noopener noreferrer" class="contact-link-portfolio">https://vikneshvaren2007.github.io/portfolioclg/</a>
            </div>
        </header>

        <!-- ==================== PROFESSIONAL SUMMARY ==================== -->
        <section class="section-block">
            <h2 class="section-title">Professional Summary</h2>
            <p class="section-paragraph">
                I am a motivated Web Developer and AI Enthusiast with hands-on experience building responsive and user-friendly websites using HTML, CSS, JavaScript, Python, and Flask. I focus on creating clean interfaces, practical web solutions, backend functionality, and continuously improving my web development skills. As a fresher, I am eager to apply my technical skills to real-world software projects and learn modern web development practices.
            </p>
        </section>

        <!-- ==================== PROJECTS ==================== -->
        <section class="section-block">
            <h2 class="section-title">Projects</h2>
            
            <div class="project-item">
                <div class="project-title">1. PET NEXA — Pet Care Web Platform:</div>
                <ul class="project-bullets">
                    <li><span class="item-label">Full-Stack Platform:</span> Developed a pet-care website with services, specialist information, pet shopping, booking management, and order tracking.</li>
                    <li><span class="item-label">AI Feature:</span> Added an AI pet-advisor concept for dog and cat related guidance and situational tips.</li>
                    <li><span class="item-label">Web Experience:</span> Focused on responsive layouts, practical workflows, and user-friendly navigation across devices.</li>
                </ul>
            </div>

            <div class="project-item">
                <div class="project-title">2. AURELIS-WATCH — Luxury E-commerce Website:</div>
                <ul class="project-bullets">
                    <li><span class="item-label">E-commerce Platform:</span> Built a luxury watch shopping website with product browsing, customer accounts, and order management.</li>
                    <li><span class="item-label">Backend Features:</span> Implemented Flask-based backend functionality, SQLite database integration, and customer order history.</li>
                    <li><span class="item-label">Order Flow:</span> Added checkout, order success flow, confirmation emails, and admin-side order details.</li>
                </ul>
            </div>

            <div class="project-item">
                <div class="project-title">3. ROYAL Rose Milk — Brand &amp; Shopping Website:</div>
                <ul class="project-bullets">
                    <li><span class="item-label">Brand Website:</span> Built a premium rose-milk product website with a strong visual identity and product presentation.</li>
                    <li><span class="item-label">Interactive Features:</span> Added product sections, shopping interactions, and animated website sections.</li>
                    <li><span class="item-label">Responsive Design:</span> Designed the interface for smooth use across desktop and mobile devices.</li>
                </ul>
            </div>
        </section>

        <!-- ==================== TECHNICAL SKILLS ==================== -->
        <section class="section-block">
            <h2 class="section-title">Technical Skills</h2>
            <ul class="standard-bullets">
                <li><span class="item-label">Frontend:</span> HTML5, CSS3, JavaScript (ES6+), Responsive Web Design</li>
                <li><span class="item-label">Backend:</span> Python, Flask</li>
                <li><span class="item-label">Database:</span> SQLite</li>
                <li><span class="item-label">Version Control:</span> Git, GitHub</li>
                <li><span class="item-label">Tools &amp; Technologies:</span> VS Code, Git, Antigravity, GitHub</li>
                <li><span class="item-label">Other Skills:</span> Responsive Web Design, UI Development, Forms, API Integration, Deployment, Debugging</li>
                <li><span class="item-label">Programming Languages:</span> Python (Intermediate), JavaScript (Intermediate)</li>
            </ul>
        </section>

        <!-- ==================== SOFT SKILLS ==================== -->
        <section class="section-block">
            <h2 class="section-title">Soft Skills</h2>
            <ul class="standard-bullets soft-skills-list">
                <li>Teamwork</li>
                <li>Quick Learning</li>
                <li>Communication</li>
                <li>Time Management</li>
                <li>Adaptability</li>
                <li>Willingness to Learn</li>
            </ul>
        </section>

        <!-- ==================== FOOTER ==================== -->
        <footer class="resume-footer">
            <span>Raj Kumar — Resume</span>
            <span>Page 1 of 1</span>
        </footer>
    </main>
</body>
</html>
"""
    return html

# Write out the clean vector resume HTML
html_clean = build_vector_resume_html('classic_clean')
html_gold = build_vector_resume_html('luxury_gold')

with open('resume/resume.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

with open('resume/resume_gold_white.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

with open('resume/resume_gold_black.html', 'w', encoding='utf-8') as f:
    f.write(html_gold)

print("[OK] Written resume/resume.html and variants successfully!")

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
    shutil.copy(abs_pdf, 'B_K_Raj_Kumar_Resume.pdf')
    shutil.copy(abs_pdf, 'assets/Raj_Kumar_Resume_Full_Page.pdf')
    shutil.copy(abs_pdf, 'assets/Raj_Kumar_Resume.pdf')
    shutil.copy(abs_pdf, 'assets/B_K_Raj_Kumar_Resume.pdf')
    shutil.copy(abs_pdf, 'resume/Raj_Kumar_Resume_Full_Page.pdf')
    shutil.copy(abs_pdf, 'resume/B_K_Raj_Kumar_Resume.pdf')
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
    print(text_sample)
    print("==============================")
else:
    print("Error: Browser executable not found.")
