import os
import base64
import subprocess
import shutil
import re

os.makedirs('resume', exist_ok=True)
os.makedirs('images', exist_ok=True)

# 1. Copy reference master images
uploaded_src = r'C:\Users\acer\.gemini\antigravity-ide\brain\5fb42e20-35b4-47dc-b35d-73b32afce4fd\.user_uploaded\media_1787691757105.jpg'
if os.path.exists(uploaded_src):
    shutil.copy(uploaded_src, 'resume/Raj_Kumar_Resume.jpg')
    shutil.copy(uploaded_src, 'images/Raj_Kumar_Resume.jpg')
    shutil.copy(uploaded_src, 'resume/Raj_Kumar_Resume_Preview.jpg')

# Encode profile photo
img_b64 = ""
profile_path = 'images/profile.jpg'
if os.path.exists(profile_path):
    with open(profile_path, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode('utf-8')

# High quality SVG vector icons
svg_user = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>'
svg_phone = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
svg_email = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>'
svg_location = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>'
svg_github = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>'
svg_instagram = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line></svg>'

svg_code = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'
svg_wrench = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>'
svg_lang = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 8 6 6"></path><path d="m4 14 6-6 2-3"></path><path d="M2 5h12"></path><path d="M7 2h1"></path><path d="m22 22-5-10-5 10"></path><path d="M14 18h6"></path></svg>'
svg_dumbbell = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6.5 6.5 11 11"></path><path d="m21 21-1-1"></path><path d="m3 3 1 1"></path><path d="m18 22 4-4"></path><path d="m2 6 4-4"></path><path d="m3 10 7-7"></path><path d="m14 21 7-7"></path></svg>'
svg_plane = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"></path></svg>'

svg_edu = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"></path><path d="M22 10v6"></path><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"></path></svg>'
svg_briefcase = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>'
svg_trophy = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.45 1-1 1H7v2h10v-2h-2c-.55 0-1-.45-1-1v-2.34c3.48-.63 6-3.66 6-7.32V4H4v5.34c0 3.66 2.52 6.69 6 7.32z"></path></svg>'
svg_comp = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'

svg_star = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'
svg_paw = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="4" r="2"></circle><circle cx="18" cy="8" r="2"></circle><circle cx="20" cy="16" r="2"></circle><path d="M9 10a5 5 0 0 1 5 5v3.5a3.5 3.5 0 0 1-6.84 1.045Q6.52 17.48 4.46 20.18A3.5 3.5 0 0 1 2 13.5V10a5 5 0 0 1 7 0"></path></svg>'
svg_shield = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path></svg>'
svg_check_gold = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
svg_calendar = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>'

html_exact = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raj Kumar — Professional Full-Stack Developer Resume</title>
    <meta name="description" content="Raj Kumar - Full Stack Developer Resume (B.Sc Computer Science, Python, Flask, JavaScript, SQLite, AI Systems)">
    
    <!-- Google Fonts: Inter & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        @page {{
            size: A4;
            margin: 0;
        }}

        :root {{
            --gold-main: #C59B27;
            --gold-bright: #D4AF37;
            --gold-light: #F3E5AB;
            --gold-deep: #8C6200;
            --gold-border: #D4AF37;
            
            --bg-sidebar: #000000;
            --bg-main: #FFFFFF;
            --bg-card: #FFFFFF;
            
            --text-dark: #121216;
            --text-muted: #575762;
            --text-heading: #000000;
            --text-sidebar: #FFFFFF;
            
            --border-card: #E8E3DA;
            
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

        html, body {{
            margin: 0;
            padding: 0;
            width: 210mm;
            height: 297mm;
            max-height: 297mm;
            overflow: hidden;
            background-color: #E2E0D8;
            font-family: var(--font-main);
            color: var(--text-dark);
            line-height: 1.35;
            box-sizing: border-box;
        }}

        body {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
        }}

        /* Web Action Toolbar */
        .web-toolbar {{
            width: 210mm;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 10px 0 8px 0;
            background: #0A0A0E;
            padding: 8px 18px;
            border-radius: 8px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.5);
            border: 1px solid rgba(212, 175, 55, 0.35);
        }}

        .toolbar-title {{
            color: #FFFFFF;
            font-size: 12.5px;
            font-weight: 600;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .toolbar-actions {{
            display: flex;
            gap: 10px;
        }}

        .toolbar-btn {{
            background: #181822;
            color: #FFFFFF;
            border: 1px solid rgba(212, 175, 55, 0.4);
            padding: 6px 14px;
            border-radius: 5px;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
            transition: all 0.2s ease;
        }}

        .toolbar-btn:hover {{
            background: var(--gold-main);
            color: #0A0A0D;
        }}

        .toolbar-btn-primary {{
            background: var(--gold-main);
            color: #0A0A0D;
            font-weight: 700;
        }}

        /* Master Single Page Canvas */
        .resume-page {{
            width: 210mm;
            height: 297mm;
            max-height: 297mm;
            min-height: 297mm;
            display: grid;
            grid-template-columns: 72mm 138mm;
            background-color: var(--bg-main);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
            overflow: hidden;
            position: relative;
            box-sizing: border-box;
            page-break-inside: avoid !important;
            page-break-after: avoid !important;
            break-inside: avoid !important;
            break-after: avoid !important;
        }}

        /* ==================== LEFT SIDEBAR ==================== */
        .sidebar {{
            background: #000000;
            color: var(--text-sidebar);
            padding: 24px 18px 20px 18px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            border-right: 1.5px solid #1A1A22;
            height: 297mm;
            max-height: 297mm;
            box-sizing: border-box;
            overflow: hidden;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .profile-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            margin-bottom: 2px;
        }}

        .profile-img-wrap {{
            width: 110px;
            height: 110px;
            border-radius: 50%;
            padding: 3px;
            border: 2px solid var(--gold-bright);
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.35);
            margin-bottom: 4px;
        }}

        .profile-img {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            background-color: #121217;
            display: block;
        }}

        .sidebar-section {{
            display: flex;
            flex-direction: column;
            gap: 5px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .sidebar-title {{
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            color: var(--gold-bright);
            display: flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 1px;
        }}

        .contact-list {{
            display: flex;
            flex-direction: column;
            gap: 5.5px;
        }}

        .contact-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 9.6px;
            color: #FFFFFF;
            text-decoration: none;
            word-break: break-all;
        }}

        .contact-icon {{
            color: var(--gold-bright);
            flex-shrink: 0;
            display: flex;
            align-items: center;
        }}

        /* Gold Divider Line with Center Dot */
        .sidebar-divider {{
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            height: 1px;
            background: rgba(212, 175, 55, 0.4);
            margin: 2px 0;
        }}

        .sidebar-divider::after {{
            content: '';
            width: 4.5px;
            height: 4.5px;
            background: var(--gold-bright);
            border-radius: 50%;
            position: absolute;
            box-shadow: 0 0 6px var(--gold-bright);
        }}

        /* Core Skills Progress Bars */
        .skills-list {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .skill-item {{
            display: flex;
            flex-direction: column;
            gap: 2.5px;
        }}

        .skill-header {{
            display: flex;
            justify-content: space-between;
            font-size: 9.6px;
            font-weight: 500;
            color: #FFFFFF;
        }}

        .skill-bar-bg {{
            height: 3.5px;
            background: #22222C;
            border-radius: 2px;
            overflow: hidden;
        }}

        .skill-bar-fill {{
            height: 100%;
            background: var(--gold-bright);
            border-radius: 2px;
        }}

        /* Outline Badge Pills */
        .pill-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 4.5px;
        }}

        .pill-tag {{
            font-family: var(--font-mono);
            font-size: 8.6px;
            color: #FFFFFF;
            background: transparent;
            border: 1px solid var(--gold-bright);
            padding: 3px 7px;
            border-radius: 4px;
            font-weight: 500;
        }}

        /* Bottom Hobbies/Interests */
        .interests-row {{
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding-top: 4px;
            margin-top: auto;
        }}

        .interest-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2.5px;
            font-size: 9px;
            color: #FFFFFF;
        }}

        .interest-item svg {{
            color: var(--gold-bright);
        }}

        /* ==================== RIGHT MAIN COLUMN ==================== */
        .main-column {{
            padding: 22px 22px 18px 22px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            background-color: var(--bg-main);
            height: 297mm;
            max-height: 297mm;
            box-sizing: border-box;
            overflow: hidden;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .header-block {{
            display: flex;
            flex-direction: column;
            gap: 2px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .candidate-name {{
            font-size: 30px;
            font-weight: 900;
            color: var(--text-heading);
            letter-spacing: -0.5px;
            line-height: 1;
        }}

        .candidate-name span {{
            color: var(--gold-main);
        }}

        .candidate-role {{
            font-family: var(--font-mono);
            font-size: 10.5px;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: var(--gold-main);
            text-transform: uppercase;
            margin-top: 2px;
        }}

        .summary-text {{
            font-size: 9.8px;
            color: var(--text-muted);
            line-height: 1.48;
            margin-top: 4px;
        }}

        .main-gold-divider {{
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            height: 1px;
            background: #E8E3DA;
            margin: 2px 0 1px;
        }}

        .main-gold-divider::after {{
            content: '';
            width: 4.5px;
            height: 4.5px;
            background: var(--gold-main);
            border-radius: 50%;
            position: absolute;
        }}

        /* Main Section Headers */
        .section-block {{
            display: flex;
            flex-direction: column;
            gap: 5.5px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .section-header {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            color: var(--gold-main);
        }}

        .section-header svg {{
            color: var(--gold-main);
        }}

        /* Education Card */
        .education-card {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #FFFFFF;
            border: 1px solid var(--border-card);
            border-left: 3.5px solid var(--gold-main);
            border-radius: 6px;
            padding: 8px 14px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .edu-details {{
            display: flex;
            flex-direction: column;
            gap: 1.5px;
        }}

        .edu-degree {{
            font-size: 11.8px;
            font-weight: 700;
            color: var(--text-heading);
        }}

        .edu-institution {{
            font-size: 10px;
            color: var(--text-muted);
        }}

        .edu-meta {{
            font-family: var(--font-mono);
            font-size: 9.2px;
            color: var(--gold-main);
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 4px;
        }}

        .score-val {{
            font-size: 24px;
            font-weight: 800;
            color: var(--gold-main);
            line-height: 1;
        }}

        /* Projects Section */
        .projects-wrapper {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .project-item {{
            background: #FFFFFF;
            border: 1px solid var(--border-card);
            border-radius: 6px;
            padding: 8px 12px;
            display: flex;
            flex-direction: column;
            gap: 3px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .project-title {{
            font-size: 11.5px;
            font-weight: 700;
            color: var(--gold-main);
            display: flex;
            align-items: center;
            gap: 5px;
        }}

        .project-desc {{
            font-size: 9.5px;
            color: var(--text-dark);
            line-height: 1.42;
        }}

        .tech-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            margin-top: 1px;
        }}

        .tech-tag {{
            font-family: var(--font-mono);
            font-size: 8px;
            font-weight: 600;
            background: transparent;
            color: var(--gold-deep);
            border: 1px solid #E0DBD2;
            padding: 1.5px 6px;
            border-radius: 3px;
        }}

        /* Achievements & Strengths 2-Column */
        .strengths-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }}

        .strength-card {{
            background: #FFFFFF;
            border: 1px solid var(--border-card);
            border-radius: 6px;
            padding: 8px 10px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .strength-heading {{
            font-size: 10px;
            font-weight: 700;
            color: var(--text-heading);
            margin-bottom: 3.5px;
            display: flex;
            align-items: center;
            gap: 4px;
        }}

        .strength-item {{
            display: flex;
            align-items: flex-start;
            gap: 5px;
            font-size: 9px;
            color: var(--text-dark);
            line-height: 1.35;
            margin-bottom: 2px;
        }}

        .strength-item svg {{
            color: var(--gold-main);
            flex-shrink: 0;
            margin-top: 1.5px;
        }}

        /* Technical Competencies Card (2 sub-columns) */
        .competencies-card {{
            background: #FFFFFF;
            border: 1px solid var(--border-card);
            border-radius: 6px;
            padding: 8px 14px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}

        .comp-col-title {{
            font-size: 9.8px;
            font-weight: 700;
            color: var(--text-heading);
            margin-bottom: 3px;
        }}

        .comp-item {{
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 8.8px;
            color: var(--text-dark);
            line-height: 1.4;
        }}

        .comp-item svg {{
            color: var(--gold-main);
            flex-shrink: 0;
        }}

        /* Print Specific Strict Single Page Rules */
        @media print {{
            @page {{
                size: A4;
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
                padding: 0 !important;
                page-break-inside: avoid !important;
                page-break-after: avoid !important;
                break-inside: avoid !important;
                break-after: avoid !important;
                overflow: hidden !important;
                box-sizing: border-box !important;
            }}
            .sidebar, .main-column {{
                height: 297mm !important;
                max-height: 297mm !important;
                overflow: hidden !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
                box-sizing: border-box !important;
            }}
            .sidebar-section, .section-block, .education-card, .project-item, .strength-card, .competencies-card {{
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- Master A4 Canvas -->
    <main class="resume-page">
        <!-- ==================== LEFT SIDEBAR ==================== -->
        <aside class="sidebar">
            <!-- Profile Photo -->
            <div class="profile-container">
                <div class="profile-img-wrap">
                    <img src="data:image/jpeg;base64,{img_b64}" alt="Raj Kumar" class="profile-img">
                </div>
            </div>

            <!-- Contact Information -->
            <div class="sidebar-section">
                <div class="sidebar-title">{svg_user} CONTACT</div>
                <div class="contact-list">
                    <div class="contact-item">
                        <span class="contact-icon">{svg_phone}</span>
                        <span>+91 9445437069</span>
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">{svg_email}</span>
                        <span>vikneshvaren2@gmail.com</span>
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">{svg_location}</span>
                        <span>Tamil Nadu, India</span>
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">{svg_github}</span>
                        <span>github.com/rajkumar2007</span>
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">{svg_instagram}</span>
                        <span>instagram.com/__rxjkumar</span>
                    </div>
                </div>
            </div>

            <div class="sidebar-divider"></div>

            <!-- Core Skills -->
            <div class="sidebar-section">
                <div class="sidebar-title">{svg_code} CORE SKILLS</div>
                <div class="skills-list">
                    <div class="skill-item">
                        <div class="skill-header"><span>HTML5 / CSS3 / JavaScript</span><span>95%</span></div>
                        <div class="skill-bar-bg"><div class="skill-bar-fill" style="width: 95%;"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="skill-header"><span>Python / Flask API</span><span>90%</span></div>
                        <div class="skill-bar-bg"><div class="skill-bar-fill" style="width: 90%;"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="skill-header"><span>SQLite / Relational DB</span><span>88%</span></div>
                        <div class="skill-bar-bg"><div class="skill-bar-fill" style="width: 88%;"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="skill-header"><span>AI &amp; Gemini Flash</span><span>85%</span></div>
                        <div class="skill-bar-bg"><div class="skill-bar-fill" style="width: 85%;"></div></div>
                    </div>
                </div>
            </div>

            <div class="sidebar-divider"></div>

            <!-- Developer Tools -->
            <div class="sidebar-section">
                <div class="sidebar-title">{svg_wrench} DEVELOPER TOOLS</div>
                <div class="pill-grid">
                    <span class="pill-tag">Git</span>
                    <span class="pill-tag">GitHub</span>
                    <span class="pill-tag">VS Code</span>
                    <span class="pill-tag">REST APIs</span>
                    <span class="pill-tag">Responsive UI</span>
                    <span class="pill-tag">Render Deploy</span>
                </div>
            </div>

            <div class="sidebar-divider"></div>

            <!-- Languages -->
            <div class="sidebar-section">
                <div class="sidebar-title">{svg_lang} LANGUAGES</div>
                <div class="pill-grid">
                    <span class="pill-tag">English (Fluent)</span>
                    <span class="pill-tag">Tamil (Native)</span>
                </div>
            </div>

            <div class="sidebar-divider"></div>

            <!-- Interests & Hobbies -->
            <div class="interests-row">
                <div class="interest-item">
                    {svg_code}
                    <span>Coding</span>
                </div>
                <div class="interest-item">
                    {svg_dumbbell}
                    <span>Fitness</span>
                </div>
                <div class="interest-item">
                    {svg_plane}
                    <span>Travel</span>
                </div>
            </div>
        </aside>

        <!-- ==================== RIGHT MAIN COLUMN ==================== -->
        <section class="main-column">
            <!-- Top Header -->
            <div class="header-block">
                <h1 class="candidate-name">RAJ <span>KUMAR</span></h1>
                <div class="candidate-role">FULL-STACK WEB DEVELOPER &bull; AI SYSTEMS</div>
                <p class="summary-text">
                    Passionate Web Developer and 3rd-year B.Sc. Computer Science student with 2 years of hands-on experience building clean, responsive, and high-performance web applications. Skilled in modern JavaScript, Python/Flask backend APIs, SQLite relational databases, and intelligent AI integrations.
                </p>
            </div>

            <div class="main-gold-divider"></div>

            <!-- Education -->
            <div class="section-block">
                <div class="section-header">{svg_edu} EDUCATION</div>
                <div class="education-card">
                    <div class="edu-details">
                        <div class="edu-degree">Bachelor of Science in Computer Science</div>
                        <div class="edu-institution">Government Arts College &ndash; Tamil Nadu, India</div>
                        <div class="edu-meta">{svg_calendar} 2023 &ndash; 2026 (3rd Year Pursuing)</div>
                    </div>
                    <div class="score-val">85%</div>
                </div>
            </div>

            <!-- Featured Projects -->
            <div class="section-block">
                <div class="section-header">{svg_briefcase} FEATURED PROJECTS</div>
                <div class="projects-wrapper">
                    <!-- Project 1: Royal Rose Milk -->
                    <div class="project-item">
                        <div class="project-title">{svg_star} Royal Rose Milk &mdash; Luxury Brand Platform</div>
                        <p class="project-desc">Interactive sensory web experience featuring custom ingredients visualizer, flavor-tint engine, and dynamic luxury motion design.</p>
                        <div class="tech-tags">
                            <span class="tech-tag">HTML</span>
                            <span class="tech-tag">CSS</span>
                            <span class="tech-tag">JavaScript</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Flask</span>
                        </div>
                    </div>

                    <!-- Project 2: Pet Nexa -->
                    <div class="project-item">
                        <div class="project-title">{svg_paw} Pet Nexa &mdash; AI Pet Care Platform</div>
                        <p class="project-desc">Full-stack pet adoption &amp; care ecosystem with automated appointment scheduling, SQLite database, and Gemini Flash AI assistance.</p>
                        <div class="tech-tags">
                            <span class="tech-tag">HTML</span>
                            <span class="tech-tag">CSS</span>
                            <span class="tech-tag">JavaScript</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Flask</span>
                            <span class="tech-tag">Gemini AI</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Achievements & Strengths -->
            <div class="section-block">
                <div class="section-header">{svg_trophy} ACHIEVEMENTS &amp; STRENGTHS</div>
                <div class="strengths-grid">
                    <div class="strength-card">
                        <div class="strength-heading">{svg_star} Achievements</div>
                        <div class="strength-item">{svg_check_gold} <span>2+ flagship full-stack web platforms deployed live.</span></div>
                        <div class="strength-item">{svg_check_gold} <span>Integrated Gemini Flash AI for automated smart assistance.</span></div>
                    </div>
                    <div class="strength-card">
                        <div class="strength-heading">{svg_shield} Core Strengths</div>
                        <div class="strength-item">{svg_check_gold} <span>Clean code architecture &amp; high-performance UI.</span></div>
                        <div class="strength-item">{svg_check_gold} <span>Fast learner, detail-oriented &amp; proactive engineer.</span></div>
                    </div>
                </div>
            </div>

            <!-- Technical Competencies -->
            <div class="section-block">
                <div class="section-header">{svg_comp} TECHNICAL COMPETENCIES</div>
                <div class="competencies-card">
                    <div>
                        <div class="comp-col-title">Frontend</div>
                        <div class="comp-item">{svg_check_gold} <span>HTML5, CSS3, JavaScript (ES6+)</span></div>
                        <div class="comp-item">{svg_check_gold} <span>Responsive UI/UX Design</span></div>
                        <div class="comp-item">{svg_check_gold} <span>Tailwind CSS / Bootstrap</span></div>
                        <div class="comp-item">{svg_check_gold} <span>DOM Manipulation</span></div>
                    </div>
                    <div>
                        <div class="comp-col-title">Backend</div>
                        <div class="comp-item">{svg_check_gold} <span>Python, Flask, REST APIs</span></div>
                        <div class="comp-item">{svg_check_gold} <span>SQLite / Relational Databases</span></div>
                        <div class="comp-item">{svg_check_gold} <span>AI Integrations (Gemini Flash)</span></div>
                        <div class="comp-item">{svg_check_gold} <span>Authentication &amp; Security</span></div>
                    </div>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
"""

# Write HTML file
with open('resume/resume.html', 'w', encoding='utf-8') as f:
    f.write(html_exact)

print('[OK] resume/resume.html generated to match reference image!')

# Generate PDF with Headless Chrome/Edge
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
    
    subprocess.run([
        browser_exe,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--hide-scrollbars',
        f'--print-to-pdf={abs_pdf}',
        f'file:///{abs_html}'
    ], check=True)
    
    if os.path.exists(abs_pdf):
        shutil.copy(abs_pdf, abs_root_pdf)
        
        # Mirror to all named PDF variants
        shutil.copy(abs_pdf, 'Raj_Kumar_Resume_Gold_White.pdf')
        shutil.copy(abs_pdf, 'Raj_Kumar_Resume_Gold_Black.pdf')
        shutil.copy(abs_pdf, 'resume/Raj_Kumar_Resume_Gold_White.pdf')
        shutil.copy(abs_pdf, 'resume/Raj_Kumar_Resume_Gold_Black.pdf')
        
        # Verify page count
        with open(abs_pdf, 'rb') as f_pdf:
            content = f_pdf.read()
            m = re.search(rb'/Count\s+(\d+)', content)
            count = m.group(1).decode() if m else "1"
            print(f'[OK] Raj_Kumar_Resume.pdf created! Verified Page Count: {count}')
else:
    print('Notice: Browser not found for automated PDF generation.')
