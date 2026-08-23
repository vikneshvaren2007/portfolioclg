import os
import base64

os.makedirs('resume', exist_ok=True)

img_b64 = ""
profile_path = 'images/profile.jpg'
if os.path.exists(profile_path):
    with open(profile_path, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode('utf-8')

# High quality SVG icons definitions for guaranteed offline vector sharpness
svg_phone = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
svg_email = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>'
svg_location = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>'
svg_globe = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'
svg_linkedin = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect width="4" height="12" x="2" y="9"></rect><circle cx="4" cy="4" r="2"></circle></svg>'
svg_github = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>'

svg_skills = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 16 4-4-4-4"></path><path d="m6 8-4 4 4 4"></path><path d="m14.5 4-5 16"></path></svg>'
svg_server = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="8" x="2" y="2" rx="2" ry="2"></rect><rect width="20" height="8" x="2" y="14" rx="2" ry="2"></rect><line x1="6" x2="6.01" y1="6" y2="6"></line><line x1="6" x2="6.01" y1="18" y2="18"></line></svg>'
svg_code = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'
svg_tool = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>'
svg_lang = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 8 6 6"></path><path d="m4 14 6-6 2-3"></path><path d="M2 5h12"></path><path d="M7 2h1"></path><path d="m22 22-5-10-5 10"></path><path d="M14 18h6"></path></svg>'
svg_heart = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></svg>'

svg_edu = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"></path><path d="M22 10v6"></path><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"></path></svg>'
svg_proj = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13.381h20M8.6 21v-3.722a2.28 2.28 0 0 1 2.28-2.278h2.24a2.28 2.28 0 0 1 2.28 2.278V21M2 8.5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v10.5a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2zM9 6.5V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2.5"></path></svg>'
svg_briefcase = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>'
svg_trophy = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.45 1-1 1H7v2h10v-2h-2c-.55 0-1-.45-1-1v-2.34c3.48-.63 6-3.66 6-7.32V4H4v5.34c0 3.66 2.52 6.69 6 7.32z"></path></svg>'
svg_cert = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"></rect><path d="m9 12 2 2 4-4"></path></svg>'
svg_check = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#DC2626" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
svg_award = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#DC2626" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"></circle><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"></path></svg>'
svg_brain = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 4.44-5.04z"></path><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-4.44-5.04z"></path></svg>'

# Interests SVGs
svg_coding = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'
svg_gym = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6.5 6.5 11 11"></path><path d="m21 21-1-1"></path><path d="m3 3 1 1"></path><path d="m18 22 4-4"></path><path d="m2 6 4-4"></path><path d="m3 10 7-7"></path><path d="m14 21 7-7"></path></svg>'
svg_camera = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"></path><circle cx="12" cy="13" r="3"></circle></svg>'
svg_music = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>'

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raj Kumar — Professional Resume</title>
    <meta name="description" content="Raj Kumar - Full Stack Developer Resume (B.Sc Computer Science, Python, Flask, AI Systems)">
    
    <!-- Google Fonts: Inter & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {{
            --navy-dark: #060B18;
            --navy-mid: #0C1630;
            --navy-light: #142244;
            --crimson: #DC2626;
            --crimson-light: #EF4444;
            --crimson-glow: rgba(220, 38, 38, 0.25);
            --text-dark: #0F172A;
            --text-body: #334155;
            --text-muted: #64748B;
            --text-light: #F8FAFC;
            --sidebar-text: #E2E8F0;
            --sidebar-muted: #94A3B8;
            --bg-light: #FFFFFF;
            --bg-alt: #F8FAFC;
            --border-color: #E2E8F0;
            --border-subtle: #F1F5F9;
            --tag-bg: #F1F5F9;
            --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            --font-mono: 'JetBrains Mono', 'Courier New', monospace;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
            color-adjust: exact !important;
        }}

        body {{
            font-family: var(--font-main);
            background-color: #1e293b;
            color: var(--text-dark);
            line-height: 1.45;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 24px 0 40px 0;
            min-height: 100vh;
        }}

        /* Web Action Toolbar */
        .web-toolbar {{
            width: 210mm;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
            background: #0f172a;
            padding: 12px 24px;
            border-radius: 8px;
            box-shadow: 0 6px 24px rgba(0,0,0,0.4);
            border: 1px solid #334155;
        }}

        .toolbar-title {{
            color: #f8fafc;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .toolbar-title svg {{
            color: var(--crimson-light);
        }}

        .toolbar-actions {{
            display: flex;
            gap: 12px;
        }}

        .toolbar-btn {{
            background: #1e293b;
            color: #ffffff;
            border: 1px solid #475569;
            padding: 8px 18px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
            transition: all 0.2s ease;
        }}

        .toolbar-btn:hover {{
            background: var(--crimson);
            border-color: var(--crimson);
            color: #ffffff;
        }}

        .toolbar-btn-primary {{
            background: var(--crimson);
            border-color: var(--crimson);
            box-shadow: 0 3px 12px rgba(220, 38, 38, 0.4);
        }}

        .toolbar-btn-primary:hover {{
            background: #b91c1c;
            border-color: #b91c1c;
        }}

        /* A4 Page Container */
        .resume-page {{
            width: 210mm;
            height: 297mm;
            min-height: 297mm;
            max-height: 297mm;
            background: var(--bg-light);
            display: flex;
            position: relative;
            box-shadow: 0 16px 48px rgba(0,0,0,0.5);
            overflow: hidden;
            border-radius: 0px;
        }}

        /* ================= SIDEBAR (LEFT) ================= */
        .sidebar {{
            width: 76mm;
            height: 100%;
            background: linear-gradient(180deg, var(--navy-dark) 0%, var(--navy-mid) 50%, #050812 100%);
            color: var(--sidebar-text);
            padding: 30px 22px 28px 22px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border-right: 3px solid var(--crimson);
            position: relative;
            z-index: 2;
        }}

        /* Profile Photo Container */
        .profile-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            position: relative;
            margin-bottom: 4px;
        }}

        .profile-frame {{
            width: 136px;
            height: 136px;
            border-radius: 50%;
            padding: 4px;
            background: linear-gradient(135deg, var(--crimson) 0%, #ffffff 50%, var(--crimson) 100%);
            box-shadow: 0 8px 28px rgba(220, 38, 38, 0.55);
            position: relative;
        }}

        .profile-img {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            object-position: center top;
            display: block;
            background-color: var(--navy-mid);
        }}

        /* Sidebar Section Titles */
        .sidebar-heading {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1.6px;
            text-transform: uppercase;
            color: #FFFFFF;
            padding-bottom: 5px;
            border-bottom: 1.8px solid rgba(220, 38, 38, 0.85);
            margin-bottom: 11px;
        }}

        .sidebar-heading svg {{
            color: var(--crimson-light);
        }}

        /* Contact Items */
        .contact-list {{
            display: flex;
            flex-direction: column;
            gap: 10.5px;
        }}

        .contact-item {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 10.5px;
            color: var(--sidebar-text);
            text-decoration: none;
            transition: color 0.15s ease;
        }}

        a.contact-item:hover {{
            color: #FFFFFF;
            text-decoration: underline;
        }}

        .contact-icon {{
            width: 26px;
            height: 26px;
            border-radius: 5px;
            background: rgba(220, 38, 38, 0.25);
            border: 1px solid rgba(220, 38, 38, 0.5);
            color: #F87171;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }}

        .contact-text {{
            word-break: break-all;
            line-height: 1.3;
            font-weight: 400;
        }}

        /* Skills Groups */
        .skills-group-title {{
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #F87171;
            margin: 10px 0 6px 0;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .skills-group-title:first-child {{
            margin-top: 0;
        }}

        .skills-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 5.5px;
        }}

        .skill-pill {{
            font-family: var(--font-mono);
            font-size: 9.5px;
            font-weight: 500;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #F1F5F9;
            padding: 3.5px 8.5px;
            border-radius: 4px;
            line-height: 1.25;
        }}

        /* Languages */
        .lang-list {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .lang-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11px;
        }}

        .lang-name {{
            font-weight: 600;
            color: #FFFFFF;
        }}

        .lang-level {{
            font-size: 9.6px;
            color: var(--sidebar-muted);
            background: rgba(255,255,255,0.08);
            padding: 2.5px 8px;
            border-radius: 4px;
            border: 1px solid rgba(255,255,255,0.12);
        }}

        /* Interests */
        .interests-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 6px;
            text-align: center;
        }}

        .interest-card {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.14);
            border-radius: 5px;
            padding: 9px 2px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
        }}

        .interest-card svg {{
            color: #F87171;
        }}

        .interest-card span {{
            font-size: 8.5px;
            font-weight: 600;
            color: #E2E8F0;
            text-transform: uppercase;
        }}

        /* ================= MAIN CONTENT (RIGHT) ================= */
        .main-content {{
            width: 134mm;
            height: 100%;
            background: #FFFFFF;
            padding: 30px 24px 28px 24px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* Header block */
        .header-block {{
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 14px;
        }}

        .name-wrapper {{
            display: flex;
            align-items: baseline;
            gap: 10px;
        }}

        .name-raj {{
            font-size: 38px;
            font-weight: 900;
            color: var(--navy-dark);
            letter-spacing: 1.2px;
            line-height: 1;
        }}

        .name-kumar {{
            font-size: 38px;
            font-weight: 900;
            color: var(--crimson);
            letter-spacing: 1.2px;
            line-height: 1;
        }}

        .role-title {{
            font-family: var(--font-mono);
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 3px;
            color: var(--navy-mid);
            text-transform: uppercase;
            margin-top: 6px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .role-title::after {{
            content: "";
            flex: 1;
            height: 2px;
            background: linear-gradient(90deg, var(--crimson) 0%, transparent 100%);
        }}

        .summary-text {{
            font-size: 10.8px;
            color: var(--text-body);
            line-height: 1.65;
            margin-top: 9px;
            text-align: justify;
        }}

        /* Section Styling */
        .section-block {{
            display: flex;
            flex-direction: column;
            gap: 9px;
        }}

        .section-header {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13.5px;
            font-weight: 800;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            color: var(--navy-dark);
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 4.5px;
        }}

        .section-header svg {{
            color: var(--crimson);
        }}

        /* Education Card */
        .education-card {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--bg-alt);
            border: 1px solid var(--border-color);
            border-left: 5px solid var(--crimson);
            border-radius: 6px;
            padding: 13px 20px;
        }}

        .edu-details {{
            display: flex;
            flex-direction: column;
            gap: 3.5px;
        }}

        .edu-degree {{
            font-size: 13.5px;
            font-weight: 700;
            color: var(--navy-dark);
        }}

        .edu-institution {{
            font-size: 11.5px;
            font-style: italic;
            color: var(--text-muted);
        }}

        .edu-meta {{
            font-family: var(--font-mono);
            font-size: 10.2px;
            color: var(--crimson);
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
            margin-top: 2px;
        }}

        .score-box {{
            text-align: right;
            padding-left: 20px;
            border-left: 1.5px solid var(--border-color);
        }}

        .score-label {{
            font-size: 9.5px;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .score-val {{
            font-size: 23px;
            font-weight: 800;
            color: var(--crimson);
            line-height: 1.1;
        }}

        /* Projects Section */
        .projects-wrapper {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .project-item {{
            background: #FFFFFF;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 11px 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
            gap: 4.5px;
        }}

        .project-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .project-title {{
            font-size: 12.5px;
            font-weight: 700;
            color: var(--crimson);
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 7px;
        }}

        .project-desc {{
            font-size: 10.6px;
            color: var(--text-body);
            line-height: 1.55;
        }}

        .tech-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 5.5px;
            margin-top: 3.5px;
        }}

        .tech-tag {{
            font-family: var(--font-mono);
            font-size: 9.5px;
            font-weight: 600;
            background: var(--tag-bg);
            border: 1px solid #CBD5E1;
            color: var(--navy-dark);
            padding: 2.5px 8px;
            border-radius: 4px;
        }}

        .tech-tag.ai-tag {{
            background: #EFF6FF;
            border-color: #93C5FD;
            color: #1E40AF;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        /* Experience Section */
        .exp-container {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .exp-item {{
            position: relative;
            padding-left: 16px;
            border-left: 2px solid var(--border-color);
            margin-left: 6px;
            display: flex;
            flex-direction: column;
            gap: 3.5px;
        }}

        .exp-item::before {{
            content: "";
            position: absolute;
            left: -6px;
            top: 3.5px;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--crimson);
            border: 2px solid #FFFFFF;
            box-shadow: 0 0 0 1.5px var(--crimson);
        }}

        .exp-top {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }}

        .exp-title {{
            font-size: 12.2px;
            font-weight: 700;
            color: var(--navy-dark);
        }}

        .exp-date {{
            font-family: var(--font-mono);
            font-size: 10px;
            font-weight: 600;
            color: var(--crimson);
        }}

        .exp-bullets {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 3px;
        }}

        .exp-bullet {{
            font-size: 10.2px;
            color: var(--text-body);
            display: flex;
            align-items: flex-start;
            gap: 7px;
            line-height: 1.5;
        }}

        .exp-bullet::before {{
            content: "•";
            color: var(--crimson);
            font-weight: 800;
            font-size: 13px;
            line-height: 1;
        }}

        /* Two Column Layout for Achievements & Certifications */
        .bottom-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
        }}

        .bottom-card {{
            background: var(--bg-alt);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 12px 14px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .bottom-heading {{
            font-size: 11.2px;
            font-weight: 700;
            color: var(--navy-dark);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
            border-bottom: 1.5px solid var(--border-color);
            padding-bottom: 4px;
        }}

        .bottom-heading svg {{
            color: var(--crimson);
        }}

        .bullet-list {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 4.5px;
        }}

        .bullet-item {{
            font-size: 9.8px;
            color: var(--text-body);
            line-height: 1.45;
            display: flex;
            align-items: flex-start;
            gap: 6px;
        }}

        .bullet-item svg {{
            flex-shrink: 0;
            margin-top: 2.5px;
        }}

        /* Print media query */
        @media print {{
            body {{
                background: none !important;
                padding: 0 !important;
                margin: 0 !important;
            }}
            .web-toolbar {{
                display: none !important;
            }}
            .resume-page {{
                box-shadow: none !important;
                margin: 0 !important;
                width: 210mm !important;
                height: 297mm !important;
                max-height: 297mm !important;
                page-break-after: avoid !important;
                page-break-inside: avoid !important;
            }}
            @page {{
                size: A4 portrait;
                margin: 0mm !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- Web Action Toolbar for Interactive Browsing -->
    <div class="web-toolbar">
        <div class="toolbar-title">
            {svg_edu}
            <span>Raj Kumar &bull; Executive Resume (A4 Ready)</span>
        </div>
        <div class="toolbar-actions">
            <a href="Raj_Kumar_Resume.pdf" download="Raj_Kumar_Resume.pdf" class="toolbar-btn toolbar-btn-primary">
                {svg_briefcase} Download PDF
            </a>
            <button onclick="window.print()" class="toolbar-btn" type="button">
                {svg_code} Print / Save
            </button>
            <a href="../index.html" class="toolbar-btn">
                Back to Portfolio
            </a>
        </div>
    </div>

    <!-- Main A4 Resume Document Container -->
    <main class="resume-page" id="resumeDocument">

        <!-- ================= LEFT SIDEBAR ================= -->
        <aside class="sidebar">

            <!-- Profile Photo -->
            <div class="profile-container">
                <div class="profile-frame">
                    <img src="data:image/jpeg;base64,{img_b64}" alt="Raj Kumar" class="profile-img">
                </div>
            </div>

            <!-- Contact Information -->
            <div class="sidebar-section">
                <div class="sidebar-heading">
                    {svg_phone} Contact
                </div>
                <div class="contact-list">
                    <a href="tel:+919445437069" class="contact-item">
                        <span class="contact-icon">{svg_phone}</span>
                        <span class="contact-text">+91 94454 37069</span>
                    </a>
                    <a href="mailto:vikneshvaren2@gmail.com" class="contact-item">
                        <span class="contact-icon">{svg_email}</span>
                        <span class="contact-text">vikneshvaren2@gmail.com</span>
                    </a>
                    <div class="contact-item">
                        <span class="contact-icon">{svg_location}</span>
                        <span class="contact-text">Tamil Nadu, India</span>
                    </div>
                    <a href="https://www.rajkumarportfolio.dev" target="_blank" rel="noopener noreferrer" class="contact-item">
                        <span class="contact-icon">{svg_globe}</span>
                        <span class="contact-text">rajkumarportfolio.dev</span>
                    </a>
                    <a href="https://linkedin.com/in/rajkumar2007" target="_blank" rel="noopener noreferrer" class="contact-item">
                        <span class="contact-icon">{svg_linkedin}</span>
                        <span class="contact-text">linkedin.com/in/rajkumar2007</span>
                    </a>
                    <a href="https://github.com/rajkumar2007" target="_blank" rel="noopener noreferrer" class="contact-item">
                        <span class="contact-icon">{svg_github}</span>
                        <span class="contact-text">github.com/rajkumar2007</span>
                    </a>
                </div>
            </div>

            <!-- Technical Skills -->
            <div class="sidebar-section">
                <div class="sidebar-heading">
                    {svg_skills} Technical Skills
                </div>

                <div class="skills-group-title">{svg_code} Frontend Development</div>
                <div class="skills-pills">
                    <span class="skill-pill">HTML5</span>
                    <span class="skill-pill">CSS3</span>
                    <span class="skill-pill">JavaScript (ES6+)</span>
                    <span class="skill-pill">Responsive Design</span>
                    <span class="skill-pill">Bootstrap</span>
                    <span class="skill-pill">Swiper.js</span>
                </div>

                <div class="skills-group-title">{svg_server} Backend Development</div>
                <div class="skills-pills">
                    <span class="skill-pill">Python</span>
                    <span class="skill-pill">Flask</span>
                    <span class="skill-pill">SQLite</span>
                </div>

                <div class="skills-group-title">{svg_tool} Tools &amp; Workflow</div>
                <div class="skills-pills">
                    <span class="skill-pill">VS Code</span>
                    <span class="skill-pill">Git &amp; GitHub</span>
                    <span class="skill-pill">Figma</span>
                    <span class="skill-pill">Postman</span>
                </div>
            </div>

            <!-- Languages -->
            <div class="sidebar-section">
                <div class="sidebar-heading">
                    {svg_lang} Languages
                </div>
                <div class="lang-list">
                    <div class="lang-row">
                        <span class="lang-name">Tamil</span>
                        <span class="lang-level">Native</span>
                    </div>
                    <div class="lang-row">
                        <span class="lang-name">English</span>
                        <span class="lang-level">Professional</span>
                    </div>
                    <div class="lang-row">
                        <span class="lang-name">Hindi</span>
                        <span class="lang-level">Conversational</span>
                    </div>
                </div>
            </div>

            <!-- Interests -->
            <div class="sidebar-section">
                <div class="sidebar-heading">
                    {svg_heart} Interests
                </div>
                <div class="interests-grid">
                    <div class="interest-card">
                        {svg_coding}
                        <span>Coding</span>
                    </div>
                    <div class="interest-card">
                        {svg_gym}
                        <span>Fitness</span>
                    </div>
                    <div class="interest-card">
                        {svg_camera}
                        <span>Photo</span>
                    </div>
                    <div class="interest-card">
                        {svg_music}
                        <span>Music</span>
                    </div>
                </div>
            </div>

        </aside>

        <!-- ================= RIGHT MAIN CONTENT ================= -->
        <section class="main-content">

            <!-- Header & Summary -->
            <header class="header-block">
                <div class="name-wrapper">
                    <span class="name-raj">RAJ</span>
                    <span class="name-kumar">KUMAR</span>
                </div>
                <div class="role-title">FULL STACK DEVELOPER</div>
                <p class="summary-text">
                    Motivated and detail-oriented Full Stack Developer with hands-on experience in building responsive websites and web applications using modern technologies. Passionate about clean code, problem-solving, and creating great user experiences.
                </p>
            </header>

            <!-- Education -->
            <div class="section-block">
                <div class="section-header">
                    {svg_edu} Education
                </div>
                <div class="education-card">
                    <div class="edu-details">
                        <div class="edu-degree">B.Sc Computer Science</div>
                        <div class="edu-institution">Manonmaniam University</div>
                        <div class="edu-meta">{svg_cert} 2024 – 2027 | Pursuing</div>
                    </div>
                    <div class="score-box">
                        <div class="score-label">Current Percentage</div>
                        <div class="score-val">81%</div>
                    </div>
                </div>
            </div>

            <!-- Featured Projects -->
            <div class="section-block">
                <div class="section-header">
                    {svg_proj} Projects
                </div>

                <div class="projects-wrapper">
                    <!-- Project 1: Royal Rose Milk -->
                    <div class="project-item">
                        <div class="project-top">
                            <span class="project-title">{svg_code} ROYAL ROSE MILK</span>
                        </div>
                        <p class="project-desc">
                            A complete product website for “Royal Rose Milk” with cinematic UI/UX, product showcase, booking system, and WhatsApp integration.
                        </p>
                        <div class="tech-tags">
                            <span class="tech-tag">HTML</span>
                            <span class="tech-tag">CSS</span>
                            <span class="tech-tag">JavaScript</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Flask</span>
                            <span class="tech-tag">SQLite</span>
                        </div>
                    </div>

                    <!-- Project 2: Pet Nexa -->
                    <div class="project-item">
                        <div class="project-top">
                            <span class="project-title">{svg_code} PET NEXA</span>
                        </div>
                        <p class="project-desc">
                            A pet care and grooming website with booking system, AI assistant, shop, and admin dashboard.
                        </p>
                        <div class="tech-tags">
                            <span class="tech-tag">HTML</span>
                            <span class="tech-tag">CSS</span>
                            <span class="tech-tag">JavaScript</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Flask</span>
                            <span class="tech-tag">SQLite</span>
                            <span class="tech-tag ai-tag">{svg_brain} AI (Ollama)</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Work Experience -->
            <div class="section-block">
                <div class="section-header">
                    {svg_briefcase} Experience
                </div>

                <div class="exp-container">
                    <div class="exp-item">
                        <div class="exp-top">
                            <span class="exp-title">Freelance Web Developer</span>
                            <span class="exp-date">2024 – Present</span>
                        </div>
                        <ul class="exp-bullets">
                            <li class="exp-bullet">Building responsive websites and web applications.</li>
                            <li class="exp-bullet">Working with clients to understand requirements and deliver quality solutions.</li>
                            <li class="exp-bullet">Integrating backend, database, and payment systems.</li>
                        </ul>
                    </div>

                    <div class="exp-item">
                        <div class="exp-top">
                            <span class="exp-title">Personal Projects &amp; Learning</span>
                            <span class="exp-date">2023 – 2024</span>
                        </div>
                        <ul class="exp-bullets">
                            <li class="exp-bullet">Developed multiple projects to improve skills.</li>
                            <li class="exp-bullet">Explored AI integration in web applications.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Two-column grid for Achievements & Certifications -->
            <div class="bottom-grid">
                <!-- Achievements -->
                <div class="bottom-card">
                    <div class="bottom-heading">
                        {svg_trophy} Achievements
                    </div>
                    <ul class="bullet-list">
                        <li class="bullet-item">
                            {svg_check}
                            <span>Built &amp; deployed multiple full-stack web projects.</span>
                        </li>
                        <li class="bullet-item">
                            {svg_check}
                            <span>Integrated Email &amp; WhatsApp automation in booking systems.</span>
                        </li>
                        <li class="bullet-item">
                            {svg_check}
                            <span>Continuously improving skills in Web Development and AI.</span>
                        </li>
                    </ul>
                </div>

                <!-- Certifications -->
                <div class="bottom-card">
                    <div class="bottom-heading">
                        {svg_cert} Certifications
                    </div>
                    <ul class="bullet-list">
                        <li class="bullet-item">
                            {svg_award}
                            <span>Python for Everybody – Coursera</span>
                        </li>
                        <li class="bullet-item">
                            {svg_award}
                            <span>Responsive Web Design – freeCodeCamp</span>
                        </li>
                        <li class="bullet-item">
                            {svg_award}
                            <span>Flask Web Development – Udemy (In Progress)</span>
                        </li>
                    </ul>
                </div>
            </div>

        </section>
    </main>

</body>
</html>
'''

with open('resume/resume.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('resume/resume.html successfully updated and balanced!')
