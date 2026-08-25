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
svg_phone = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
svg_email = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>'
svg_location = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>'
svg_globe = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'
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
svg_check = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
svg_sparkles = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>'
svg_calendar = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>'

# Interests SVGs
svg_coding = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'
svg_gym = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6.5 6.5 11 11"></path><path d="m21 21-1-1"></path><path d="m3 3 1 1"></path><path d="m18 22 4-4"></path><path d="m2 6 4-4"></path><path d="m3 10 7-7"></path><path d="m14 21 7-7"></path></svg>'
svg_camera = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"></path><circle cx="12" cy="13" r="3"></circle></svg>'
svg_music = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>'


def generate_html_content(theme="gold_white"):
    if theme == "gold_white":
        theme_vars = """
            --bg-midnight: #FFFFFF;
            --bg-sidebar: #0D0D12;
            --bg-deep-emerald: #14141C;
            --bg-dark-forest: #0D0D12;
            --bg-surface: #FFFFFF;
            --bg-surface-elevated: #F8F7F3;
            
            --copper-main: #B8860B;
            --copper-light: #D4AF37;
            --copper-glow: rgba(184, 134, 11, 0.35);
            --copper-subtle: rgba(184, 134, 11, 0.12);
            --copper-deep: #8C6200;
            
            --ivory-warm: #FFFFFF;
            --cream-soft: #F6F4EE;
            --gray-muted: #575762;
            --gray-dim: #71717A;
            
            --text-dark: #121216;
            --text-heading: #0A0A0D;
            --text-body: #24242C;
            --text-muted: #575762;
            --sidebar-text: #FBFBFC;
            --sidebar-muted: #A1A1AA;
            
            --bg-main-col: #FFFFFF;
            --bg-card: #FAF9F5;
            --bg-card-alt: #F4F2EC;
            --border-color: #E2DDD5;
            --border-subtle: #EDEAE4;
            --tag-bg: #F5F2EB;
            --page-bg: #EAE8E2;
        """
        theme_title = "Golden &amp; White Edition"
    else:
        theme_vars = """
            --bg-midnight: #08080A;
            --bg-sidebar: #0B0B0F;
            --bg-deep-emerald: #121218;
            --bg-dark-forest: #08080A;
            --bg-surface: #121218;
            --bg-surface-elevated: #181822;
            
            --copper-main: #D4AF37;
            --copper-light: #F3E5AB;
            --copper-glow: rgba(212, 175, 55, 0.4);
            --copper-subtle: rgba(212, 175, 55, 0.15);
            --copper-deep: #9A7428;
            
            --ivory-warm: #FBFBFC;
            --cream-soft: #EDE8DF;
            --gray-muted: #A1A1AA;
            --gray-dim: #71717A;
            
            --text-dark: #FBFBFC;
            --text-heading: #FFFFFF;
            --text-body: #D4D4DF;
            --text-muted: #A1A1AA;
            --sidebar-text: #FBFBFC;
            --sidebar-muted: #A1A1AA;
            
            --bg-main-col: #0A0A0E;
            --bg-card: #121218;
            --bg-card-alt: #161620;
            --border-color: #272734;
            --border-subtle: #1E1E28;
            --tag-bg: #1A1A24;
            --page-bg: #050507;
        """
        theme_title = "Golden &amp; Obsidian Black Edition"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raj Kumar — Professional Full-Stack Developer Resume ({theme_title})</title>
    <meta name="description" content="Raj Kumar - Full Stack Developer Resume (B.Sc Computer Science, Python, Flask, JavaScript, SQLite, AI Systems)">
    
    <!-- Google Fonts: Inter & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {{
            {theme_vars}
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
            background-color: var(--page-bg);
            color: var(--text-dark);
            line-height: 1.42;
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
            background: #0A0A0E;
            padding: 12px 24px;
            border-radius: 8px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.5);
            border: 1px solid rgba(212, 175, 55, 0.35);
        }}

        .toolbar-title {{
            color: #FFFFFF;
            font-size: 13.5px;
            font-weight: 600;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .toolbar-actions {{
            display: flex;
            gap: 12px;
        }}

        .toolbar-btn {{
            background: #181822;
            color: #FFFFFF;
            border: 1px solid rgba(212, 175, 55, 0.4);
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
            background: var(--copper-main);
            color: #0A0A0D;
            transform: translateY(-1px);
        }}

        .toolbar-btn-primary {{
            background: var(--copper-main);
            color: #0A0A0D;
            font-weight: 700;
        }}

        /* Strict A4 Document Canvas */
        .resume-page {{
            width: 210mm;
            min-height: 297mm;
            height: 297mm;
            display: grid;
            grid-template-columns: 74mm 136mm;
            background-color: var(--bg-main-col);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4);
            border-radius: 2px;
            overflow: hidden;
            position: relative;
        }}

        /* LEFT SIDEBAR (Dark Luxury Onyx & Gold) */
        .sidebar {{
            background: var(--bg-sidebar);
            color: var(--sidebar-text);
            padding: 24px 18px 20px 20px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            border-right: 1.5px solid var(--border-color);
            position: relative;
        }}

        .profile-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            position: relative;
        }}

        .profile-img-wrap {{
            width: 104px;
            height: 104px;
            border-radius: 50%;
            padding: 3px;
            background: linear-gradient(135deg, var(--copper-light), var(--copper-main), var(--copper-deep));
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
            margin-bottom: 12px;
        }}

        .profile-img {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            background-color: #121217;
            display: block;
        }}

        .contact-list {{
            display: flex;
            flex-direction: column;
            gap: 7px;
            width: 100%;
            background: rgba(255, 255, 255, 0.03);
            padding: 10px 12px;
            border-radius: 6px;
            border: 1px solid rgba(212, 175, 55, 0.2);
        }}

        .contact-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 10.2px;
            color: var(--sidebar-text);
            text-decoration: none;
            word-break: break-all;
        }}

        .contact-icon {{
            color: var(--copper-main);
            flex-shrink: 0;
            display: flex;
            align-items: center;
        }}

        .sidebar-title {{
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--copper-light);
            border-bottom: 1px solid rgba(212, 175, 55, 0.3);
            padding-bottom: 3.5px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .skills-group {{
            display: flex;
            flex-direction: column;
            gap: 6.5px;
        }}

        .skill-item {{
            display: flex;
            flex-direction: column;
            gap: 2.5px;
        }}

        .skill-header {{
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            font-weight: 600;
            color: var(--sidebar-text);
        }}

        .skill-bar-bg {{
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 2px;
            overflow: hidden;
        }}

        .skill-bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--copper-main), var(--copper-light));
            border-radius: 2px;
        }}

        .pill-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
        }}

        .pill-tag {{
            font-family: var(--font-mono);
            font-size: 9px;
            background: rgba(212, 175, 55, 0.1);
            color: var(--copper-light);
            border: 1px solid rgba(212, 175, 55, 0.25);
            padding: 2.5px 7px;
            border-radius: 3px;
            font-weight: 600;
        }}

        /* RIGHT MAIN COLUMN */
        .main-column {{
            padding: 24px 24px 20px 24px;
            display: flex;
            flex-direction: column;
            gap: 13px;
            background-color: var(--bg-main-col);
        }}

        .header-block {{
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 10px;
        }}

        .name-row {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }}

        .candidate-name {{
            font-size: 26px;
            font-weight: 900;
            color: var(--text-heading);
            letter-spacing: -0.5px;
        }}

        .candidate-name span {{
            color: var(--copper-main);
        }}

        .candidate-role {{
            font-family: var(--font-mono);
            font-size: 11.5px;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: var(--copper-main);
            text-transform: uppercase;
            margin-top: 2px;
        }}

        .summary-text {{
            font-size: 10.4px;
            color: var(--text-body);
            line-height: 1.55;
            margin-top: 6px;
        }}

        .section-header {{
            display: flex;
            align-items: center;
            gap: 7.5px;
            font-size: 12.5px;
            font-weight: 800;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            color: var(--text-heading);
            border-bottom: 1.8px solid var(--border-color);
            padding-bottom: 3.5px;
        }}

        .section-header svg {{
            color: var(--copper-main);
        }}

        .education-card {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-left: 4px solid var(--copper-main);
            border-radius: 6px;
            padding: 9px 14px;
        }}

        .edu-degree {{
            font-size: 12.2px;
            font-weight: 700;
            color: var(--text-heading);
        }}

        .edu-institution {{
            font-size: 10.8px;
            color: var(--text-muted);
        }}

        .edu-meta {{
            font-family: var(--font-mono);
            font-size: 9.5px;
            color: var(--copper-main);
            font-weight: 600;
            margin-top: 2px;
        }}

        .score-val {{
            font-size: 20px;
            font-weight: 800;
            color: var(--copper-main);
        }}

        .project-item {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 9px 12px;
            display: flex;
            flex-direction: column;
            gap: 3px;
        }}

        .project-title {{
            font-size: 12px;
            font-weight: 700;
            color: var(--copper-main);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .project-desc {{
            font-size: 10px;
            color: var(--text-body);
            line-height: 1.48;
        }}

        .tech-tag {{
            font-family: var(--font-mono);
            font-size: 8.5px;
            font-weight: 600;
            background: var(--tag-bg);
            color: var(--copper-main);
            border: 1px solid var(--border-color);
            padding: 2px 6px;
            border-radius: 3px;
        }}

        .bottom-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }}

        .bottom-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 8px 12px;
        }}

        .bottom-heading {{
            font-size: 10.5px;
            font-weight: 700;
            color: var(--text-heading);
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 5px;
        }}

        .bottom-heading svg {{
            color: var(--copper-main);
        }}

        .bullet-item {{
            display: flex;
            align-items: flex-start;
            gap: 6px;
            font-size: 9.8px;
            color: var(--text-body);
            line-height: 1.42;
            margin-bottom: 3px;
        }}

        .bullet-item svg {{
            color: var(--copper-main);
            flex-shrink: 0;
            margin-top: 2px;
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
                margin: 0 !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- Web Navigation Toolbar -->
    <div class="web-toolbar">
        <div class="toolbar-title">
            <span>Raj Kumar &bull; Resume ({theme_title})</span>
        </div>
        <div class="toolbar-actions">
            <button class="toolbar-btn toolbar-btn-primary" onclick="window.print()">
                Print / Save PDF
            </button>
            <a href="../index.html" class="toolbar-btn">Back to Portfolio</a>
        </div>
    </div>

    <!-- Master A4 Canvas -->
    <main class="resume-page">
        <!-- SIDEBAR -->
        <aside class="sidebar">
            <div class="profile-container">
                <div class="profile-img-wrap">
                    <img src="data:image/jpeg;base64,{img_b64}" alt="Raj Kumar" class="profile-img">
                </div>
            </div>

            <!-- Contact Information -->
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
                    <span>github.com/vikneshvaren2007</span>
                </div>
            </div>

            <!-- Technical Proficiency -->
            <div class="skills-group">
                <div class="sidebar-title">{svg_skills} Core Skills</div>
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

            <!-- Developer Tools -->
            <div class="skills-group">
                <div class="sidebar-title">{svg_tool} Developer Tools</div>
                <div class="pill-grid">
                    <span class="pill-tag">Git</span>
                    <span class="pill-tag">GitHub</span>
                    <span class="pill-tag">VS Code</span>
                    <span class="pill-tag">REST APIs</span>
                    <span class="pill-tag">Responsive UX</span>
                    <span class="pill-tag">Render Deploy</span>
                </div>
            </div>

            <!-- Languages -->
            <div class="skills-group">
                <div class="sidebar-title">{svg_lang} Languages</div>
                <div class="pill-grid">
                    <span class="pill-tag">English (Fluent)</span>
                    <span class="pill-tag">Tamil (Native)</span>
                </div>
            </div>
        </aside>

        <!-- MAIN COLUMN -->
        <section class="main-column">
            <!-- Header -->
            <div class="header-block">
                <div class="name-row">
                    <h1 class="candidate-name">RAJ <span>KUMAR</span></h1>
                </div>
                <div class="candidate-role">Full-Stack Web Developer &bull; AI Systems</div>
                <p class="summary-text">
                    Passionate Web Developer and 3rd-year B.Sc. Computer Science student with 2 years of hands-on experience building clean, responsive, and high-performance web applications. Skilled in modern JavaScript, Python/Flask backend APIs, SQLite relational databases, and intelligent AI integrations.
                </p>
            </div>

            <!-- Education -->
            <div class="section-block">
                <div class="section-header">{svg_edu} Education</div>
                <div class="education-card">
                    <div class="edu-details">
                        <div class="edu-degree">Bachelor of Science in Computer Science</div>
                        <div class="edu-institution">Government Arts College &bull; Tamil Nadu, India</div>
                        <div class="edu-meta">{svg_calendar} 2023 &ndash; 2026 (3rd Year Pursuing)</div>
                    </div>
                    <div class="score-val">85%</div>
                </div>
            </div>

            <!-- Flagship Projects -->
            <div class="section-block">
                <div class="section-header">{svg_proj} Featured Projects</div>
                <div class="project-item">
                    <div class="project-title">{svg_sparkles} Royal Rose Milk — Luxury Brand Platform</div>
                    <p class="project-desc">Interactive sensory web experience featuring custom ingredients visualizer, flavor-tint engine, and dynamic luxury motion design.</p>
                    <div class="tech-tags">
                        <span class="tech-tag">HTML5</span>
                        <span class="tech-tag">CSS3</span>
                        <span class="tech-tag">JavaScript ES6+</span>
                        <span class="tech-tag">Responsive UX</span>
                    </div>
                </div>

                <div class="project-item">
                    <div class="project-title">{svg_sparkles} Pet Nexa — AI Pet Care Platform</div>
                    <p class="project-desc">Full-stack pet adoption &amp; care ecosystem with automated appointment scheduling, SQLite database, and Gemini Flash AI assistance.</p>
                    <div class="tech-tags">
                        <span class="tech-tag">Python</span>
                        <span class="tech-tag">Flask</span>
                        <span class="tech-tag">SQLite</span>
                        <span class="tech-tag">Gemini AI</span>
                    </div>
                </div>
            </div>

            <!-- Strengths & Focus -->
            <div class="bottom-grid">
                <div class="bottom-card">
                    <div class="bottom-heading">{svg_trophy} Achievements</div>
                    <div class="bullet-item">{svg_check} <span>2+ flagship full-stack web platforms deployed live.</span></div>
                    <div class="bullet-item">{svg_check} <span>Integrated Gemini Flash AI for automated smart assistance.</span></div>
                </div>
                <div class="bottom-card">
                    <div class="bottom-heading">{svg_sparkles} Core Strengths</div>
                    <div class="bullet-item">{svg_check} <span>Clean code architecture &amp; high-performance UI.</span></div>
                    <div class="bullet-item">{svg_check} <span>Fast learner, detail-oriented &amp; proactive engineer.</span></div>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
"""

# Generate HTML files
html_white = generate_html_content("gold_white")
html_black = generate_html_content("gold_black")

with open('resume/resume_gold_white.html', 'w', encoding='utf-8') as f:
    f.write(html_white)

with open('resume/resume_gold_black.html', 'w', encoding='utf-8') as f:
    f.write(html_black)

with open('resume/resume.html', 'w', encoding='utf-8') as f:
    f.write(html_black)

print('[OK] HTML resume templates generated successfully!')

# Look for Chrome or Edge
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
    # 1. Gold & White PDF
    abs_white_html = os.path.abspath('resume/resume_gold_white.html').replace('\\', '/')
    abs_white_pdf = os.path.abspath('resume/Raj_Kumar_Resume_Gold_White.pdf')
    abs_root_white_pdf = os.path.abspath('Raj_Kumar_Resume_Gold_White.pdf')
    
    subprocess.run([
        browser_exe, '--headless', '--disable-gpu', '--no-pdf-header-footer',
        f'--print-to-pdf={abs_white_pdf}', f'file:///{abs_white_html}'
    ], check=True)
    if os.path.exists(abs_white_pdf):
        shutil.copy(abs_white_pdf, abs_root_white_pdf)
        print('[OK] Raj_Kumar_Resume_Gold_White.pdf created!')

    # 2. Gold & Black PDF
    abs_black_html = os.path.abspath('resume/resume_gold_black.html').replace('\\', '/')
    abs_black_pdf = os.path.abspath('resume/Raj_Kumar_Resume_Gold_Black.pdf')
    abs_root_black_pdf = os.path.abspath('Raj_Kumar_Resume_Gold_Black.pdf')
    
    subprocess.run([
        browser_exe, '--headless', '--disable-gpu', '--no-pdf-header-footer',
        f'--print-to-pdf={abs_black_pdf}', f'file:///{abs_black_html}'
    ], check=True)
    if os.path.exists(abs_black_pdf):
        shutil.copy(abs_black_pdf, abs_root_black_pdf)
        print('[OK] Raj_Kumar_Resume_Gold_Black.pdf created!')

    # 3. Default Raj_Kumar_Resume.pdf (Gold & Black)
    abs_default_pdf = os.path.abspath('resume/Raj_Kumar_Resume.pdf')
    abs_root_default_pdf = os.path.abspath('Raj_Kumar_Resume.pdf')
    shutil.copy(abs_black_pdf, abs_default_pdf)
    shutil.copy(abs_black_pdf, abs_root_default_pdf)
    print('[OK] Default Raj_Kumar_Resume.pdf created!')
else:
    print('Notice: Browser not found for automated PDF generation.')
