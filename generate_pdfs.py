from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from bidi.algorithm import get_display
import subprocess

pdfmetrics.registerFont(TTFont('ArialUnicode', '/Library/Fonts/Arial Unicode.ttf'))

def r(t): return get_display(str(t))

W, H = A4  # 595 x 842

CORAL = HexColor('#e8623a')
DARK = HexColor('#1c1c1e')
GRAY = HexColor('#6e6e73')
PURPLE = HexColor('#7b3dd5')
LIGHT_BG = HexColor('#faf9f7')
WHITE = HexColor('#ffffff')

# ─────────────────────────────────────────────
# PDF 1: user-journey-daniel.pdf
# ─────────────────────────────────────────────

def draw_step_circle(c, x, y, num, color=CORAL):
    c.setFillColor(color)
    c.circle(x, y, 14, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont('ArialUnicode', 11)
    c.drawCentredString(x, y - 4, str(num))

def draw_connector(c, x, y_top, y_bottom):
    c.setStrokeColor(GRAY)
    c.setLineWidth(1.5)
    c.setDash(3, 3)
    c.line(x, y_top - 14, x, y_bottom + 14)
    c.setDash()

def draw_header_bar(c, title, y):
    c.setFillColor(CORAL)
    c.rect(40, y - 6, W - 80, 26, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont('ArialUnicode', 13)
    c.drawRightString(W - 50, y + 4, r(title))

def draw_section_box(c, x, y, w, h, bg=LIGHT_BG, stroke_color=None):
    c.setFillColor(bg)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.roundRect(x, y, w, h, 6, fill=1, stroke=1)
    else:
        c.roundRect(x, y, w, h, 6, fill=1, stroke=0)

def page1_onboarding(c):
    # Background
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Title
    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 18)
    c.drawRightString(W - 40, H - 50, r('מסע הלקוח — First Login Experience'))
    c.setFont('ArialUnicode', 11)
    c.setFillColor(GRAY)
    c.drawRightString(W - 40, H - 70, r('CPO — דניאל · עודכן 08/04/2026'))

    # Separator
    c.setStrokeColor(CORAL)
    c.setLineWidth(2)
    c.line(40, H - 80, W - 40, H - 80)

    steps = [
        {
            'num': 1,
            'header': 'שלב 1: פנייה ראשונה',
            'copy': 'היי, כיף לראות אותך 😊 מה שמך?',
            'note': 'פנייה ידידותית — לא פורמלית. מרגישה כמו בן אדם, לא כמו טופס.',
        },
        {
            'num': 2,
            'header': 'שלב 2: הכרת הצוות + Elevator Pitch',
            'copy': 'הכר את צוות אנשי ה-AI שלך',
            'note': 'Magic moment: הרגע שבו היזם מבין שיש לו צוות שלם.',
        },
        {
            'num': 3,
            'header': 'שלב 3: Elevator Pitch — ברוך הבא',
            'copy': '[שם], ברוך הבא ל-Hub שלך. כאן כבר לא עובדים לבד יותר.',
            'note': 'Pitch מלא — ראה פירוט בעמוד זה למטה.',
        },
        {
            'num': 4,
            'header': 'שלב 4: חלל משותף',
            'copy': 'המשרד הדיגיטלי שלך — שולחן העבודה, הצוות, הספרינט.',
            'note': 'הבסיס. כאן עובדים.',
        },
        {
            'num': 5,
            'header': 'שלב 5: הגג — קהילה עתידית',
            'copy': 'מה קורה על הגג?',
            'note': 'מגיע אחרי חלל משותף — מה שמגיע כשמוכנים.',
        },
    ]

    step_y_positions = []
    start_y = H - 105
    step_height = 100
    circle_x = 70

    for i, step in enumerate(steps):
        y = start_y - i * step_height
        step_y_positions.append(y)

        # Connector line between steps
        if i > 0:
            draw_connector(c, circle_x, step_y_positions[i-1] - 16, y + 16)

        draw_step_circle(c, circle_x, y, step['num'])

        # Box
        box_x = 95
        box_w = W - 145
        draw_section_box(c, box_x, y - 28, box_w, 52, WHITE, CORAL)

        # Header
        c.setFillColor(CORAL)
        c.setFont('ArialUnicode', 10)
        c.drawRightString(W - 55, y + 14, r(step['header']))

        # Copy
        c.setFillColor(DARK)
        c.setFont('ArialUnicode', 10)
        c.drawRightString(W - 55, y, r(step['copy']))

        # Note
        c.setFillColor(GRAY)
        c.setFont('ArialUnicode', 8)
        c.drawRightString(W - 55, y - 14, r(step['note']))

    # Elevator Pitch box at bottom
    pitch_y = start_y - 5 * step_height - 10
    pitch_lines = [
        '[שם], ברוך הבא ל-Hub שלך.',
        'כאן כבר לא עובדים לבד יותר.',
        'כל רעיון שמתבשל לך בראש — הצוות שלך כאן בשבילו.',
        'הכל בשבילך — עם כל המומחיות, המקצוענות והשאיפה למצוינות שלנו.',
        'כאן יזמים ויזמות נהנים מהניסיון המצטבר שלנו ומממשים את החלומות המקצועיים,',
        'לומדים את תרבות ההייטק ועובדים בצוות לקראת עתיד של סקייל, הצלחה',
        'ועמידה בראש צוות שיכיל גם אלופים ואלופות אנושיות.',
        'כאן מקשיבים לך. נדון, נחליט, נבנה — ביחד איתך, צעד אחר צעד —',
        'עד שמה שעכשיו חי רק בראשך יהפוך לממשות.',
        'ואגב? מה שרואים כאן עכשיו הוא רק ההתחלה...',
    ]
    box_h = len(pitch_lines) * 14 + 24
    draw_section_box(c, 40, pitch_y - box_h, W - 80, box_h, WHITE, PURPLE)

    c.setFillColor(PURPLE)
    c.setFont('ArialUnicode', 10)
    c.drawRightString(W - 50, pitch_y - 14, r('טקסט מלא — Elevator Pitch (שלב 3):'))

    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 9)
    for i, line in enumerate(pitch_lines):
        ly = pitch_y - 28 - i * 14
        c.drawRightString(W - 50, ly, r(line))


def page2_daily_login(c):
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 18)
    c.drawRightString(W - 40, H - 50, r('כניסה יומית — Daily Login'))
    c.setStrokeColor(CORAL)
    c.setLineWidth(2)
    c.line(40, H - 65, W - 40, H - 65)

    col_w = (W - 100) / 2
    left_x = 40
    right_x = 40 + col_w + 20

    # Left column header
    draw_section_box(c, left_x, H - 100, col_w, 28, CORAL)
    c.setFillColor(WHITE)
    c.setFont('ArialUnicode', 11)
    c.drawRightString(left_x + col_w - 10, H - 88, r('מה המשתמש רואה'))

    # Right column header
    draw_section_box(c, right_x, H - 100, col_w, 28, DARK)
    c.setFillColor(WHITE)
    c.setFont('ArialUnicode', 11)
    c.drawRightString(right_x + col_w - 10, H - 88, r('המטרה הרגשית'))

    left_items = [
        'שלום חזרה, [שם]!',
        'הצוות שלך מחכה',
        'CTA ראשי: שאל את הצוות',
        'CTA משני: ראה מה קרה בסטארטאפ שלך',
    ]
    right_items = [
        'חזרה לעבודה — לא היכרות מחדש',
        'הצוות כבר יודע הכל מהסשן הקודם',
        'תחושה של continuity — "יש כאן מישהו שזוכר אותי"',
        'המכשיר: context management + sliding window',
    ]

    draw_section_box(c, left_x, H - 340, col_w, 230, WHITE)
    draw_section_box(c, right_x, H - 340, col_w, 230, WHITE)

    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 10)
    for i, item in enumerate(left_items):
        iy = H - 125 - i * 36
        c.setFillColor(CORAL)
        c.circle(left_x + col_w - 18, iy + 4, 4, fill=1, stroke=0)
        c.setFillColor(DARK)
        c.drawRightString(left_x + col_w - 28, iy, r(item))

    for i, item in enumerate(right_items):
        iy = H - 125 - i * 36
        c.setFillColor(PURPLE)
        c.circle(right_x + col_w - 18, iy + 4, 4, fill=1, stroke=0)
        c.setFillColor(DARK)
        c.drawRightString(right_x + col_w - 28, iy, r(item))

    # Insight box
    draw_section_box(c, 40, H - 430, W - 80, 70, HexColor('#fff3ef'), CORAL)
    c.setFillColor(CORAL)
    c.setFont('ArialUnicode', 10)
    c.drawRightString(W - 55, H - 375, r('💡 עיקרון מפתח:'))
    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 10)
    c.drawRightString(W - 55, H - 392, r('המשתמש לא אמור לחשוב — הצוות מוכן לו. הניווט הכי טוב הוא זה שלא מורגש.'))
    c.drawRightString(W - 55, H - 408, r('Daily Login = חזרה למקום מוכר, לא פתיחת אפליקציה חדשה.'))


def page3_terminology(c):
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 18)
    c.drawRightString(W - 40, H - 50, r('מינוח רשמי — HypeShow'))
    c.setStrokeColor(CORAL)
    c.setLineWidth(2)
    c.line(40, H - 65, W - 40, H - 65)

    c.setFillColor(GRAY)
    c.setFont('ArialUnicode', 10)
    c.drawRightString(W - 40, H - 82, r('המינוח שבו HypeShow משתמש — ולמה הוא חשוב'))

    # Table header
    col_widths = [155, 155, 185]
    col_headers = ['למה', 'מה אומרים', 'מה לא נאמר']
    table_x = 40
    table_y = H - 105
    row_h = 44

    # Header row
    c.setFillColor(DARK)
    c.rect(table_x, table_y - row_h + 10, W - 80, row_h - 4, fill=1, stroke=0)
    cx = W - 40
    for i, (header, cw) in enumerate(zip(col_headers, col_widths)):
        c.setFillColor(WHITE)
        c.setFont('ArialUnicode', 10)
        c.drawRightString(cx - 8, table_y - 6, r(header))
        cx -= cw

    rows = [
        ('מיליטריסטי — לא מתאים לתרבות הייטק', 'אופיסר (Officer)', 'קצין'),
        ('"סוכן" = ריגול, הוליווד — טעון שלילי', 'איש AI / אנשי AI', 'סוכן'),
        ('מוריד מהאנושיות של הצוות', 'שותף דיגיטלי / איש AI', 'בוט'),
        ('המינוח שמחזק ייחודיות HypeShow', 'אנשי ה-AI שלך', 'AI Agent'),
    ]

    for ri, row in enumerate(rows):
        ry = table_y - row_h - ri * (row_h + 4)
        bg = WHITE if ri % 2 == 0 else HexColor('#f0ede8')
        draw_section_box(c, table_x, ry - row_h + 14, W - 80, row_h, bg)

        cx = W - 40
        colors = [GRAY, CORAL, DARK]
        for ci, (cell, cw, clr) in enumerate(zip(row, col_widths, colors)):
            c.setFillColor(clr)
            c.setFont('ArialUnicode', 9)
            c.drawRightString(cx - 8, ry - 6, r(cell))
            cx -= cw

    # Bottom note
    note_y = H - 105 - (len(rows) + 1) * (row_h + 4) - 20
    draw_section_box(c, 40, note_y - 60, W - 80, 70, HexColor('#fff3ef'), CORAL)
    c.setFillColor(CORAL)
    c.setFont('ArialUnicode', 11)
    c.drawRightString(W - 55, note_y + 2, r('✦ כלל הזהב:'))
    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 10)
    c.drawRightString(W - 55, note_y - 16, r('הצוות של HypeShow מורכב מ"אנשי AI" — לא סוכנים, לא בוטים, לא קצינים.'))
    c.drawRightString(W - 55, note_y - 32, r('זהו מינוח ייחודי שמדגיש אנושיות, מקצועיות, ושייכות לצוות.'))


def page4_open_questions(c):
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 18)
    c.drawRightString(W - 40, H - 50, r('שאלות פתוחות — לדיון ב-1:1'))
    c.setStrokeColor(CORAL)
    c.setLineWidth(2)
    c.line(40, H - 65, W - 40, H - 65)

    # Note box
    draw_section_box(c, 40, H - 110, W - 80, 34, HexColor('#fff3ef'), CORAL)
    c.setFillColor(CORAL)
    c.setFont('ArialUnicode', 9)
    c.drawRightString(W - 55, H - 88, r('אלו נושאים שנדב ביקש לדון בהם ביחד — לא החלטות חד-צדדיות'))

    questions = [
        ('1', 'איך מאזנים בין חוויית First Login מלאה לטעינה מהירה?',
         'קצר ומרשים vs. מעמיק ואיטי'),
        ('2', 'UX של Team Meeting — שאלה זו התקדמה.',
         'לקבל update מסטיב על מה שנבנה.'),
        ('3', 'סדר האופיסרים בהצגה ראשונה — לפי תפקיד?',
         'לפי רלוונטיות ליזם ספציפי? רנדומלי?'),
        ('4', 'האם ה-onboarding שואל שאלות על הסטארטאפ של היזם,',
         'או מתחיל עם צוות גנרי?'),
        ('5', 'מה קורה ב-Day 7 כשהיזם חוזר —',
         'האם Onboarding מופיע שוב בגרסה מקוצרת?'),
    ]

    q_start_y = H - 140
    q_height = 90

    for i, (num, q1, q2) in enumerate(questions):
        qy = q_start_y - i * (q_height + 8)
        draw_section_box(c, 40, qy - q_height + 14, W - 80, q_height, WHITE)

        # Number circle
        c.setFillColor(CORAL)
        c.circle(W - 65, qy - 22, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('ArialUnicode', 11)
        c.drawCentredString(W - 65, qy - 26, num)

        c.setFillColor(DARK)
        c.setFont('ArialUnicode', 11)
        c.drawRightString(W - 90, qy - 12, r(q1))
        c.setFont('ArialUnicode', 10)
        c.setFillColor(GRAY)
        c.drawRightString(W - 90, qy - 28, r(q2))

        # Separator
        c.setStrokeColor(HexColor('#e0ddd8'))
        c.setLineWidth(0.5)
        c.line(60, qy - 48, W - 60, qy - 48)

        c.setFillColor(PURPLE)
        c.setFont('ArialUnicode', 8)
        c.drawRightString(W - 90, qy - 62, r('לדון ב-1:1 עם נדב'))


def page5_next_steps(c):
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(DARK)
    c.setFont('ArialUnicode', 18)
    c.drawRightString(W - 40, H - 50, r('הצעדים הבאים'))
    c.setStrokeColor(CORAL)
    c.setLineWidth(2)
    c.line(40, H - 65, W - 40, H - 65)

    items = [
        ('done',  'Team Meeting UX — נבנה (מסטיב וקלוד)'),
        ('done',  'מינוח "אנשי AI" — מאושר ומוטמע'),
        ('wip',   'עיצוב מסך Onboarding step 2 (הכרת הצוות) — Daniel'),
        ('wip',   'Copywriting לכל מסכי ה-onboarding — Daniel'),
        ('wip',   'Dev-Ready Spec לאונבורדינג — Daniel → Oded'),
        ('date',  '1:1 Nadav ↔ Daniel — שאלות פתוחות 1, 3, 4, 5'),
    ]

    item_y = H - 100
    for status, text in items:
        if status == 'done':
            icon = '✅'
            color = HexColor('#2d7a4f')
            bg = HexColor('#edf7f1')
        elif status == 'wip':
            icon = '⟳'
            color = CORAL
            bg = HexColor('#fff3ef')
        else:
            icon = '📅'
            color = PURPLE
            bg = HexColor('#f3eeff')

        draw_section_box(c, 40, item_y - 42, W - 80, 52, bg)
        c.setFillColor(color)
        c.setFont('ArialUnicode', 14)
        c.drawString(W - 70, item_y - 20, icon)
        c.setFont('ArialUnicode', 11)
        c.drawRightString(W - 90, item_y - 20, r(text))

        item_y -= 68

    # Footer
    draw_section_box(c, 40, 40, W - 80, 44, DARK)
    c.setFillColor(WHITE)
    c.setFont('ArialUnicode', 9)
    c.drawRightString(W - 55, 72, r('HypeShow — CPO Daniel · User Journey Document · 08/04/2026'))
    c.setFillColor(CORAL)
    c.drawRightString(W - 55, 55, r('סיום מסמך — Product & UX'))


def generate_user_journey():
    path = '/Users/nesher/Desktop/HypeShow/user-journey-daniel.pdf'
    c = canvas.Canvas(path, pagesize=A4)

    page1_onboarding(c)
    c.showPage()
    page2_daily_login(c)
    c.showPage()
    page3_terminology(c)
    c.showPage()
    page4_open_questions(c)
    c.showPage()
    page5_next_steps(c)
    c.showPage()

    c.save()
    print(f'Saved: {path}')
    return path


# ─────────────────────────────────────────────
# PDF 2: presentation-prompts-daniel.pdf
# ─────────────────────────────────────────────

def generate_presentation_prompts():
    path = '/Users/nesher/Desktop/HypeShow/presentation-prompts-daniel.pdf'
    c = canvas.Canvas(path, pagesize=A4)

    # ── Title page ──
    c.setFillColor(DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Decorative top bar
    c.setFillColor(CORAL)
    c.rect(0, H - 8, W, 8, fill=1, stroke=0)

    c.setFillColor(WHITE)
    c.setFont('ArialUnicode', 22)
    c.drawRightString(W - 40, H - 80, r('פרומפטים למצגת — HypeShow'))

    c.setFillColor(CORAL)
    c.setFont('ArialUnicode', 13)
    c.drawRightString(W - 40, H - 110, r('רשימת תמונות + פרומפט לכל כותרת | CPO — דניאל | 08/04/2026'))

    c.setFillColor(GRAY)
    c.setFont('ArialUnicode', 11)
    c.drawRightString(W - 40, H - 140, r('לשימוש ב-Midjourney / DALL-E 3 / Firefly'))

    # Divider
    c.setStrokeColor(CORAL)
    c.setLineWidth(1)
    c.line(40, H - 160, W - 40, H - 160)

    prompts = [
        {
            'title': 'כותרת: "הצוות שמחכה לך"',
            'prompt': 'A warm, modern digital workspace illustration showing 9 diverse professional avatars arranged in a semicircle, each with a subtle colored glow (coral, purple, blue, gold, green, pink). Minimalist flat design, white background, soft shadows. Style: clean startup UI, Figma-like aesthetic. No text. 16:9 aspect ratio.',
        },
        {
            'title': 'כותרת: "ה-Hub — המשרד הדיגיטלי שלך"',
            'prompt': 'A sleek, minimal digital office dashboard illustration. Dark sidebar on left with icon navigation, main content area showing card grid with professional profiles, warm coral accent color (#e8623a), clean typography. Isometric perspective, slight 3D feel. Style: modern SaaS product screenshot, Notion/Linear aesthetic. 16:9.',
        },
        {
            'title': 'כותרת: "שיחת 1:1 — צוות שמקשיב"',
            'prompt': 'A clean chat interface illustration showing a warm conversation between a founder and an AI executive. Speech bubbles in soft colors, one side coral (user), other side white with subtle colored border (AI officer). Modern messaging app aesthetic, minimal. No faces, just avatars with initials. Warm, professional atmosphere. 16:9.',
        },
        {
            'title': 'כותרת: "ישיבת צוות — כולם בחדר"',
            'prompt': 'A modern team meeting UI illustration showing colored circular avatars arranged around a virtual conference, each with a distinct color (coral, purple, blue, dark, gold, pink, red, gray, green). Speech bubbles showing brief messages. Timeline-style conversation flow. Clean, startup aesthetic. Coral accent color. 16:9.',
        },
        {
            'title': 'כותרת: "ספרינט לוג — ההתקדמות שלך"',
            'prompt': 'A minimal project management dashboard illustration showing a sprint log with task cards, officer assignment tags (small colored dots), progress indicators, and status badges (Done, In Progress, Upcoming). Side panel with sprint progress. Clean, Notion-like aesthetic. Coral and dark color scheme. 16:9.',
        },
        {
            'title': 'כותרת: "הגג — הקהילה שבאה"',
            'prompt': 'An aspirational rooftop scene illustration showing a modern co-working space on a rooftop at golden hour. Young entrepreneurs collaborating, city skyline in background, warm coral and amber tones. Minimal, editorial illustration style. Sense of community and belonging. No text. 16:9.',
        },
        {
            'title': 'כותרת: "First Login — הרגע הראשון"',
            'prompt': 'An onboarding welcome screen illustration. Clean white background with a large, warm greeting text area and a soft coral call-to-action button. Subtle animation effect shown as layered transparent frames. Nine small officer avatars arranged in a welcoming arc at the bottom. Modern, friendly SaaS onboarding aesthetic. 16:9.',
        },
        {
            'title': 'כותרת: "Seniority Score — הצוות שגדל איתך"',
            'prompt': 'Three building icons of ascending height (small, medium, tall) representing Junior, Senior, Partner tiers. Minimal flat illustration, coral color palette with opacity variations. Clean background. The buildings subtly glow more intensely as they get taller. Professional, aspirational feel. Square format or 16:9.',
        },
    ]

    # Draw first 3 prompts on title page
    y = H - 185
    for i, p in enumerate(prompts[:3]):
        if y < 80:
            break
        box_h = 90
        draw_section_box(c, 40, y - box_h, W - 80, box_h, HexColor('#252528'))

        c.setFillColor(CORAL)
        c.setFont('ArialUnicode', 11)
        c.drawRightString(W - 55, y - 18, r(p['title']))

        c.setFillColor(HexColor('#aaaaaa'))
        c.setFont('ArialUnicode', 8)
        # Wrap the English prompt
        words = p['prompt'].split(' ')
        line = ''
        lines_out = []
        for w in words:
            test = (line + ' ' + w).strip()
            if c.stringWidth(test, 'ArialUnicode', 8) < W - 120:
                line = test
            else:
                if line:
                    lines_out.append(line)
                line = w
        if line:
            lines_out.append(line)

        for li, ltext in enumerate(lines_out[:4]):
            c.drawString(55, y - 34 - li * 12, ltext)

        y -= box_h + 10

    c.showPage()

    # Pages for remaining prompts (4 per page, 2 pages)
    remaining = prompts[3:]
    per_page = 4
    for page_start in range(0, len(remaining), per_page):
        c.setFillColor(LIGHT_BG)
        c.rect(0, 0, W, H, fill=1, stroke=0)

        c.setFillColor(DARK)
        c.setFont('ArialUnicode', 14)
        c.drawRightString(W - 40, H - 40, r('פרומפטים למצגת — המשך'))
        c.setStrokeColor(CORAL)
        c.setLineWidth(1.5)
        c.line(40, H - 52, W - 40, H - 52)

        page_prompts = remaining[page_start:page_start + per_page]
        y = H - 75
        for p in page_prompts:
            box_h = 150
            if y - box_h < 40:
                c.showPage()
                c.setFillColor(LIGHT_BG)
                c.rect(0, 0, W, H, fill=1, stroke=0)
                y = H - 40

            draw_section_box(c, 40, y - box_h, W - 80, box_h, WHITE, CORAL)

            c.setFillColor(CORAL)
            c.setFont('ArialUnicode', 12)
            c.drawRightString(W - 55, y - 20, r(p['title']))

            # Prompt label
            c.setFillColor(GRAY)
            c.setFont('ArialUnicode', 9)
            c.drawRightString(W - 55, y - 38, r('Prompt:'))

            # Wrap English prompt
            c.setFillColor(DARK)
            c.setFont('ArialUnicode', 8.5)
            words = p['prompt'].split(' ')
            line = ''
            lines_out = []
            for w in words:
                test = (line + ' ' + w).strip()
                if c.stringWidth(test, 'ArialUnicode', 8.5) < W - 120:
                    line = test
                else:
                    if line:
                        lines_out.append(line)
                    line = w
            if line:
                lines_out.append(line)

            for li, ltext in enumerate(lines_out[:7]):
                c.drawString(55, y - 52 - li * 13, ltext)

            # Copy icon hint
            c.setFillColor(GRAY)
            c.setFont('ArialUnicode', 8)
            c.drawRightString(W - 55, y - box_h + 12, r('העתק והדבק ישירות לכלי יצירת התמונות'))

            y -= box_h + 12

        c.showPage()

    c.save()
    print(f'Saved: {path}')
    return path


if __name__ == '__main__':
    p1 = generate_user_journey()
    p2 = generate_presentation_prompts()
    subprocess.run(['open', p1])
    subprocess.run(['open', p2])
    print('Done — both PDFs opened.')
