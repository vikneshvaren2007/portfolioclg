import os
import base64
import subprocess
import shutil

os.makedirs('resume', exist_ok=True)

img_b64 = ""
profile_path = 'images/profile.jpg'
if os.path.exists(profile_path):
    with open(profile_path, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode('utf-8')

# High quality SVG icons definitions
svg_contact = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"></circle><path d="M20 21a8 8 0 1 0-16 0"></path></svg>'
svg_phone = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
svg_email = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>'
svg_location = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>'
svg_github = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>'

svg_skills = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'
svg_tool = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>'
svg_lang = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 8 6 6"></path><path d="m4 14 6-6 2-3"></path><path d="M2 5h12"></path><path d="M7 2h1"></path><path d="m22 22-5-10-5 10"></path><path d="M14 18h6"></path></svg>'
svg_star = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'

svg_edu = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"></path><path d="M22 10v6"></path><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"></path></svg>'
svg_proj = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>'
svg_trophy = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.45 1-1 1H7v2h10v-2h-2c-.55 0-1-.45-1-1v-2.34c3.48-.63 6-3.66 6-7.32V4H4v5.34c0 3.66 2.52 6.69 6 7.32z"></path></svg>'
svg_check = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
svg_check_round = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="16 10 11 15 8 12"></polyline></svg>'
svg_shield = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
svg_sparkle = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'
svg_paw = '<svg width="13" height="13" viewBox="0 0 24 24" fill="#D4AF37"><circle cx="12" cy="14" r="4"/><circle cx="6.5" cy="9.5" r="2.5"/><circle cx="17.5" cy="9.5" r="2.5"/><circle cx="9" cy="5.5" r="2"/><circle cx="15" cy="5.5" r="2"/></svg>'
svg_cert = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"></circle><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"></path></svg>'
svg_calendar = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>'

# Interests SVGs
svg_coding = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'
svg_bot = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="12" x="3" y="6" rx="2"></rect><circle cx="9" cy="12" r="1.5"></circle><circle cx="15" cy="12" r="1.5"></circle><line x1="12" x2="12" y1="2" y2="6"></line></svg>'
svg_book = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path><path d="M6 6h10"></path><path d="M6 10h10"></path></svg>'
svg_plane = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 11 22 2 13 21 11 13 3 11"></polygon></svg>'


def build_exact_reference_resume_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raj Kumar — Professional Full-Stack Developer Resume</title>
    
    <!-- Google Fonts: Inter & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {{
            --gold-primary: #D4AF37;
            --gold-light: #F3E5AB;
            --gold-dark: #B8860B;
            --bg-sidebar: #050507;
            --bg-main: #FFFFFF;
            --border-card: #E8E5DD;
            --text-dark: #111114;
            --text-muted: #555562;
            --text-dim: #777785;
            --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        body {{
            font-family: var(--font-main);
            background-color: #E5E3DC;
            color: var(--text-dark);
            line-height: 1.35;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px 0;
            min-height: 100vh;
        }}

        /* Web Toolbar */
        .web-toolbar {{
            width: 210mm;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            background: #08080C;
            padding: 10px 20px;
            border-radius: 8px;
            border: 1px solid rgba(212, 175, 55, 0.35);
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        }}

        .toolbar-title {{
            color: #FFFFFF;
            font-size: 13px;
            font-weight: 600;
        }}

        .toolbar-btn {{
            background: var(--gold-primary);
            color: #0A0A0D;
            padding: 7px 16px;
            border-radius: 6px;
            font-size: 11.5px;
            font-weight: 700;
            cursor: pointer;
            border: none;
            text-decoration: none;
        }}

        /* Exact A4 Document Canvas */
        .resume-page {{
            width: 210mm;
            height: 297mm;
            max-height: 297mm;
            display: grid;
            grid-template-columns: 75mm 135mm;
            background-color: var(--bg-main);
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.35);
            overflow: hidden;
            position: relative;
            box-sizing: border-box;
        }}

        /* LEFT COLUMN (Obsidian & Gold) */
        .sidebar {{
            background: var(--bg-sidebar);
            color: #FFFFFF;
            padding: 20px 16px 16px 18px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border-right: 2px solid var(--gold-primary);
            position: relative;
            height: 100%;
        }}

        .profile-wrap {{
            display: flex;
            justify-content: center;
            margin-bottom: 6px;
        }}

        .profile-circle {{
            width: 105px;
            height: 105px;
            border-radius: 50%;
            border: 2.5px solid var(--gold-primary);
            padding: 2px;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.25);
        }}

        .profile-img {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            display: block;
        }}

        .side-section-title {{
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            color: var(--gold-primary);
            display: flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 6px;
        }}

        .contact-list {{
            display: flex;
            flex-direction: column;
            gap: 5px;
            font-size: 9.8px;
            color: #E2E2EC;
        }}

        .contact-row {{
            display: flex;
            align-items: center;
            gap: 7px;
            word-break: break-all;
        }}

        .contact-row svg {{
            color: var(--gold-primary);
            flex-shrink: 0;
        }}

        .gold-divider-node {{
            display: flex;
            align-items: center;
            width: 100%;
            margin: 4px 0;
            position: relative;
        }}

        .gold-divider-node::before {{
            content: '';
            flex: 1;
            height: 1px;
            background: rgba(212, 175, 55, 0.4);
        }}

        .gold-divider-node::after {{
            content: '';
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background: var(--gold-primary);
            box-shadow: 0 0 6px var(--gold-primary);
            margin-left: 2px;
        }}

        .skill-item {{
            margin-bottom: 5.5px;
        }}

        .skill-header {{
            display: flex;
            justify-content: space-between;
            font-size: 9.5px;
            font-weight: 600;
            margin-bottom: 2.5px;
            color: #FFFFFF;
        }}

        .skill-bar-track {{
            height: 3.5px;
            background: rgba(255, 255, 255, 0.12);
            border-radius: 2px;
            overflow: hidden;
        }}

        .skill-bar-fill {{
            height: 100%;
            background: var(--gold-primary);
            border-radius: 2px;
        }}

        .pill-wrap {{
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
        }}

        .tool-pill {{
            font-family: var(--font-mono);
            font-size: 8.8px;
            font-weight: 600;
            color: var(--gold-primary);
            border: 1px solid rgba(212, 175, 55, 0.45);
            background: rgba(212, 175, 55, 0.06);
            padding: 2.5px 7px;
            border-radius: 4px;
        }}

        .interests-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 4px;
            text-align: center;
        }}

        .interest-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3px;
        }}

        .interest-label {{
            font-size: 8.5px;
            color: #E2E2EC;
        }}

        /* RIGHT MAIN COLUMN */
        .main-col {{
            padding: 20px 20px 16px 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
            background: var(--bg-main);
        }}

        .header-wrap {{
            margin-bottom: 2px;
        }}

        .header-name {{
            font-size: 28px;
            font-weight: 900;
            letter-spacing: -0.5px;
            color: #0A0A0D;
            line-height: 1.05;
        }}

        .header-name span {{
            color: var(--gold-primary);
        }}

        .header-role {{
            font-family: var(--font-mono);
            font-size: 10.8px;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: var(--gold-primary);
            text-transform: uppercase;
            margin: 2px 0 5px 0;
        }}

        .header-summary {{
            font-size: 9.8px;
            color: var(--text-muted);
            line-height: 1.48;
            text-align: justify;
        }}

        .main-divider-dot {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            margin: 4px 0;
            position: relative;
        }}

        .main-divider-dot::before,
        .main-divider-dot::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: rgba(212, 175, 55, 0.45);
        }}

        .main-divider-dot span {{
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--gold-primary);
            margin: 0 6px;
        }}

        .main-section-title {{
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--gold-primary);
            display: flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 4px;
        }}

        .main-section-title svg {{
            color: var(--gold-primary);
        }}

        .edu-box {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid var(--border-card);
            border-left: 3.5px solid var(--gold-primary);
            border-radius: 5px;
            padding: 6px 12px;
            background: #FAFAF8;
        }}

        .edu-title {{
            font-size: 11.2px;
            font-weight: 700;
            color: #0A0A0D;
        }}

        .edu-sub {{
            font-size: 10px;
            color: #8C6200;
            margin: 1px 0;
        }}

        .edu-date {{
            font-size: 9.2px;
            color: var(--text-dim);
            display: flex;
            align-items: center;
            gap: 4px;
        }}

        .edu-percent {{
            font-size: 20px;
            font-weight: 800;
            color: var(--gold-primary);
            padding-left: 10px;
        }}

        .proj-card {{
            border: 1px solid var(--border-card);
            border-left: 3.5px solid var(--gold-primary);
            border-radius: 5px;
            padding: 6px 10px;
            background: #FAFAF8;
            margin-bottom: 4px;
        }}

        .proj-header {{
            font-size: 11px;
            font-weight: 700;
            color: #8C6200;
            display: flex;
            align-items: center;
            gap: 4px;
            margin-bottom: 2px;
        }}

        .proj-desc {{
            font-size: 9.3px;
            color: var(--text-muted);
            line-height: 1.4;
            margin-bottom: 4px;
        }}

        .proj-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 3px;
        }}

        .proj-pill {{
            font-family: var(--font-mono);
            font-size: 8px;
            font-weight: 600;
            color: var(--gold-dark);
            border: 1px solid var(--border-card);
            background: #F4F2EC;
            padding: 1.5px 5px;
            border-radius: 3px;
        }}

        .two-card-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6px;
        }}

        .info-card {{
            border: 1px solid var(--border-card);
            border-radius: 5px;
            padding: 6px 8px;
            background: #FAFAF8;
        }}

        .info-card-title {{
            font-size: 10.2px;
            font-weight: 700;
            color: #0A0A0D;
            display: flex;
            align-items: center;
            gap: 4px;
            margin-bottom: 4px;
        }}

        .bullet-line {{
            display: flex;
            align-items: flex-start;
            gap: 4px;
            font-size: 8.8px;
            color: var(--text-muted);
            line-height: 1.35;
            margin-bottom: 2.5px;
        }}

        .bullet-line svg {{
            flex-shrink: 0;
            margin-top: 1.5px;
        }}

        .bullet-circle-dot {{
            width: 4px;
            height: 4px;
            border-radius: 50%;
            border: 1px solid var(--gold-primary);
            flex-shrink: 0;
            margin-top: 4px;
            margin-right: 2px;
        }}

        .tech-comp-box {{
            border: 1px solid var(--border-card);
            border-radius: 5px;
            padding: 6px 10px;
            background: #FAFAF8;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }}

        .comp-col-title {{
            font-size: 10.2px;
            font-weight: 700;
            color: #0A0A0D;
            margin-bottom: 3px;
        }}

        @media print {{
            body {{
                background-color: transparent !important;
                padding: 0 !important;
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
                page-break-after: avoid !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- Web Navigation Toolbar -->
    <div class="web-toolbar">
        <div class="toolbar-title">
            <span>Raj Kumar &bull; Professional Resume</span>
        </div>
        <div>
            <button class="toolbar-btn" onclick="window.print()">Print / Save PDF</button>
        </div>
    </div>

    <!-- Master A4 Canvas -->
    <main class="resume-page">
        <!-- SIDEBAR -->
        <aside class="sidebar">
            <!-- Profile Photo -->
            <div class="profile-wrap">
                <div class="profile-circle">
                    <img src="data:image/jpeg;base64,{img_b64}" alt="Raj Kumar" class="profile-img">
                </div>
            </div>

            <!-- Contact -->
            <div>
                <div class="side-section-title">{svg_contact} CONTACT</div>
                <div class="contact-list">
                    <div class="contact-row">{svg_phone} <span>+91 9445437069</span></div>
                    <div class="contact-row">{svg_email} <span>vikneshvaren2@gmail.com</span></div>
                    <div class="contact-row">{svg_location} <span>Tamil Nadu, India</span></div>
                    <div class="contact-row">{svg_github} <span>github.com/vikneshvaren2007</span></div>
                </div>
            </div>

            <div class="gold-divider-node"></div>

            <!-- Core Skills -->
            <div>
                <div class="side-section-title">{svg_skills} CORE SKILLS</div>
                <div class="skill-item">
                    <div class="skill-header"><span>HTML5 / CSS3 / JavaScript</span><span>95%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" style="width: 95%;"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>Python / Flask API</span><span>90%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" style="width: 90%;"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>SQLite / Relational DB</span><span>88%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" style="width: 88%;"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>AI &amp; Gemini Flash</span><span>85%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" style="width: 85%;"></div></div>
                </div>
            </div>

            <div class="gold-divider-node"></div>

            <!-- Developer Tools -->
            <div>
                <div class="side-section-title">{svg_tool} DEVELOPER TOOLS</div>
                <div class="pill-wrap">
                    <span class="tool-pill">Git</span>
                    <span class="tool-pill">GitHub</span>
                    <span class="tool-pill">VS Code</span>
                    <span class="tool-pill">REST APIs</span>
                    <span class="tool-pill">Responsive UI</span>
                    <span class="tool-pill">Render Deploy</span>
                </div>
            </div>

            <div class="gold-divider-node"></div>

            <!-- Languages -->
            <div>
                <div class="side-section-title">{svg_lang} LANGUAGES</div>
                <div class="pill-wrap">
                    <span class="tool-pill">English (Fluent)</span>
                    <span class="tool-pill">Tamil (Native)</span>
                </div>
            </div>

            <div class="gold-divider-node"></div>

            <!-- Interests -->
            <div>
                <div class="side-section-title">{svg_star} INTERESTS</div>
                <div class="interests-grid">
                    <div class="interest-item">{svg_coding}<span class="interest-label">Coding</span></div>
                    <div class="interest-item">{svg_bot}<span class="interest-label">AI Tools</span></div>
                    <div class="interest-item">{svg_book}<span class="interest-label">Reading</span></div>
                    <div class="interest-item">{svg_plane}<span class="interest-label">Travel</span></div>
                </div>
            </div>
        </aside>

        <!-- MAIN COLUMN -->
        <section class="main-col">
            <!-- Header -->
            <div class="header-wrap">
                <h1 class="header-name">RAJ <span>KUMAR</span></h1>
                <div class="header-role">FULL-STACK WEB DEVELOPER &bull; AI SYSTEMS</div>
                <p class="header-summary">
                    Passionate Web Developer and 3rd-year B.Sc. Computer Science student with 2 years of hands-on experience building clean, responsive, and high-performance web applications. Skilled in modern JavaScript, Python/Flask backend APIs, SQLite relational databases, and intelligent AI integrations.
                </p>
            </div>

            <div class="main-divider-dot"><span></span></div>

            <!-- Education -->
            <div>
                <div class="main-section-title">{svg_edu} EDUCATION</div>
                <div class="edu-box">
                    <div>
                        <div class="edu-title">Bachelor of Science in Computer Science</div>
                        <div class="edu-sub">Government Arts College &ndash; Tamil Nadu, India</div>
                        <div class="edu-date">{svg_calendar} 2023 &ndash; 2026 (3rd Year Pursuing)</div>
                    </div>
                    <div class="edu-percent">85%</div>
                </div>
            </div>

            <!-- Featured Projects -->
            <div>
                <div class="main-section-title">{svg_proj} FEATURED PROJECTS</div>
                <div class="proj-card">
                    <div class="proj-header">{svg_sparkle} Royal Rose Milk &mdash; Luxury Brand Platform</div>
                    <p class="proj-desc">Interactive sensory web experience featuring custom ingredients visualizer, flavor-tint engine, and dynamic luxury motion design.</p>
                    <div class="proj-pills">
                        <span class="proj-pill">HTML5</span>
                        <span class="proj-pill">CSS3</span>
                        <span class="proj-pill">JavaScript ES6+</span>
                        <span class="proj-pill">Responsive UI/UX</span>
                    </div>
                </div>

                <div class="proj-card">
                    <div class="proj-header">{svg_paw} Pet Nexa &mdash; AI Pet Care Platform</div>
                    <p class="proj-desc">Full-stack pet adoption &amp; care ecosystem with automated appointment scheduling, SQLite database, and Gemini Flash AI assistance.</p>
                    <div class="proj-pills">
                        <span class="proj-pill">Python</span>
                        <span class="proj-pill">Flask</span>
                        <span class="proj-pill">SQLite</span>
                        <span class="proj-pill">Gemini AI</span>
                    </div>
                </div>
            </div>

            <!-- Achievements & Strengths -->
            <div>
                <div class="main-section-title">{svg_trophy} ACHIEVEMENTS &amp; STRENGTHS</div>
                <div class="two-card-row">
                    <div class="info-card">
                        <div class="info-card-title">{svg_sparkle} Achievements</div>
                        <div class="bullet-line">{svg_check} <span>2+ flagship full-stack web platforms deployed live.</span></div>
                        <div class="bullet-line">{svg_check} <span>Integrated Gemini Flash AI for automated smart assistance.</span></div>
                    </div>
                    <div class="info-card">
                        <div class="info-card-title">{svg_shield} Core Strengths</div>
                        <div class="bullet-line">{svg_check} <span>Clean code architecture &amp; high-performance UI.</span></div>
                        <div class="bullet-line">{svg_check} <span>Fast learner, detail-oriented &amp; proactive engineer.</span></div>
                    </div>
                </div>
            </div>

            <div class="main-divider-dot"><span></span></div>

            <!-- Technical Competencies -->
            <div>
                <div class="main-section-title">{svg_skills} TECHNICAL COMPETENCIES</div>
                <div class="tech-comp-box">
                    <div>
                        <div class="comp-col-title">Frontend</div>
                        <div class="bullet-line">{svg_check} <span>HTML5, CSS3, JavaScript (ES6+)</span></div>
                        <div class="bullet-line">{svg_check} <span>Responsive UI/UX Design</span></div>
                        <div class="bullet-line">{svg_check} <span>Tailwind CSS / Bootstrap</span></div>
                        <div class="bullet-line">{svg_check} <span>DOM Manipulation</span></div>
                    </div>
                    <div>
                        <div class="comp-col-title">Backend</div>
                        <div class="bullet-line">{svg_check} <span>Python, Flask, REST APIs</span></div>
                        <div class="bullet-line">{svg_check} <span>SQLite / Relational Databases</span></div>
                        <div class="bullet-line">{svg_check} <span>AI Integrations (Gemini Flash)</span></div>
                        <div class="bullet-line">{svg_check} <span>Authentication &amp; Security</span></div>
                    </div>
                </div>
            </div>

            <div class="main-divider-dot"><span></span></div>

            <!-- Certifications & Core Ethics -->
            <div class="two-card-row">
                <div class="info-card">
                    <div class="info-card-title">{svg_cert} CERTIFICATIONS</div>
                    <div class="bullet-line">{svg_check} <span>Python Programming &ndash; Basic to Advanced</span></div>
                    <div class="bullet-line">{svg_check} <span>Web Development &ndash; Complete Course</span></div>
                    <div class="bullet-line">{svg_check} <span>Flask &amp; REST API Development</span></div>
                    <div class="bullet-line">{svg_check} <span>AI with Gemini Flash &ndash; Integration</span></div>
                </div>
                <div class="info-card">
                    <div class="info-card-title">{svg_shield} CORE ETHICS</div>
                    <div class="bullet-line"><span class="bullet-circle-dot"></span> <span>Code with purpose &amp; precision.</span></div>
                    <div class="bullet-line"><span class="bullet-circle-dot"></span> <span>Continuous learner &amp; problem solver.</span></div>
                    <div class="bullet-line"><span class="bullet-circle-dot"></span> <span>Integrity, discipline &amp; commitment to excellence.</span></div>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
"""

# Write HTML
html_content = build_exact_reference_resume_html()
with open('resume/resume.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('[OK] resume/resume.html successfully generated!')

# Look for Chrome or Edge to export PDF
browser_candidates = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

browser_exe = None
for b in browser_candidates:
    if os.path.exists(b):
        browser_exe = b
        break

if browser_exe:
    abs_html = os.path.abspath('resume/resume.html').replace('\\', '/')
    abs_pdf = os.path.abspath('resume/Raj_Kumar_Resume.pdf')
    abs_root_pdf = os.path.abspath('Raj_Kumar_Resume.pdf')

    pdf_cmd = [
        browser_exe,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={abs_pdf}',
        f'file:///{abs_html}'
    ]
    subprocess.run(pdf_cmd, check=True)
    if os.path.exists(abs_pdf):
        shutil.copy(abs_pdf, abs_root_pdf)
        print('[OK] Raj_Kumar_Resume.pdf and resume/Raj_Kumar_Resume.pdf created successfully!')
else:
    print('Notice: Browser not found for automated PDF generation.')
