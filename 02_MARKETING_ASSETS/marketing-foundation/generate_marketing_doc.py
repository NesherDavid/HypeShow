import subprocess
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from bidi.algorithm import get_display

pdfmetrics.registerFont(TTFont('ArialUnicode', '/Library/Fonts/Arial Unicode.ttf'))
pdfmetrics.registerFont(TTFont('ArialUnicodeBold', '/Library/Fonts/Arial Unicode.ttf'))

CORAL = colors.HexColor('#e8623a')
DARK = colors.HexColor('#1c1c1e')
GRAY = colors.HexColor('#6e6e73')
WHITE = colors.white
LIGHT_BG = colors.HexColor('#f5f5f7')

def r(t):
    return get_display(t)

OUTPUT_PATH = '/Users/nesher/Desktop/HypeShow/02_MARKETING_ASSETS/marketing-foundation/marketing-foundation-inbar.pdf'

doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm,
)

# Styles
title_style = ParagraphStyle(
    'Title',
    fontName='ArialUnicode',
    fontSize=28,
    textColor=WHITE,
    alignment=TA_RIGHT,
    spaceAfter=6,
    leading=36,
)
subtitle_style = ParagraphStyle(
    'Subtitle',
    fontName='ArialUnicode',
    fontSize=13,
    textColor=colors.HexColor('#f0c4b4'),
    alignment=TA_RIGHT,
    spaceAfter=4,
    leading=18,
)
chapter_style = ParagraphStyle(
    'Chapter',
    fontName='ArialUnicode',
    fontSize=17,
    textColor=CORAL,
    alignment=TA_RIGHT,
    spaceBefore=18,
    spaceAfter=8,
    leading=24,
)
body_style = ParagraphStyle(
    'Body',
    fontName='ArialUnicode',
    fontSize=11,
    textColor=DARK,
    alignment=TA_RIGHT,
    spaceAfter=6,
    leading=18,
)
bullet_style = ParagraphStyle(
    'Bullet',
    fontName='ArialUnicode',
    fontSize=11,
    textColor=DARK,
    alignment=TA_RIGHT,
    spaceAfter=4,
    leading=17,
    rightIndent=12,
)
highlight_style = ParagraphStyle(
    'Highlight',
    fontName='ArialUnicode',
    fontSize=12,
    textColor=CORAL,
    alignment=TA_RIGHT,
    spaceAfter=6,
    leading=19,
)
caption_style = ParagraphStyle(
    'Caption',
    fontName='ArialUnicode',
    fontSize=9,
    textColor=GRAY,
    alignment=TA_RIGHT,
    spaceAfter=4,
    leading=14,
)
tag_style = ParagraphStyle(
    'Tag',
    fontName='ArialUnicode',
    fontSize=10,
    textColor=WHITE,
    alignment=TA_CENTER,
    leading=14,
)

story = []

# ── HEADER BLOCK ──────────────────────────────────────────────────────────────
header_data = [[
    Paragraph(r('יסודות השיווק — מסמך עבודה'), title_style),
    Paragraph(r('HYPESHOW'), ParagraphStyle('HS', fontName='ArialUnicode', fontSize=32, textColor=CORAL, alignment=TA_CENTER, leading=40)),
]]
header_table = Table(header_data, colWidths=[12*cm, 5*cm])
header_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), DARK),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 18),
    ('BOTTOMPADDING', (0,0), (-1,-1), 18),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ('ROUNDEDCORNERS', (0,0), (-1,-1), [8,8,8,8]),
]))
story.append(header_table)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(r('מסמך פנימי | ענבר, CMO | אפריל 2026'), caption_style))
story.append(Spacer(1, 0.4*cm))
story.append(HRFlowable(width="100%", thickness=1.5, color=CORAL))
story.append(Spacer(1, 0.5*cm))

# ── CHAPTER 1 ─────────────────────────────────────────────────────────────────
story.append(Paragraph(r('פרק 1 — מי אנחנו באמת'), chapter_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph(r('לא "AI לעסקים". לא "כלי אוטומציה". לא "צ\'אטבוט חכם".'), highlight_style))
story.append(Paragraph(r('HypeShow הוא הצוות שמחכה לך — מקצועי, זמין, ומכיר את העסק שלך.'), body_style))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(r('כמו WeWork שנתן ליזם קטן תשתית של תאגיד — HypeShow נותן ליזם בודד חדר מנהלים שלם. לא כלי — חוויה. לא אוטומציה — שותפות.'), body_style))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(r('9 קצינים. כל אחד עם תחום, אישיות, וניסיון מצטבר. כולם עובדים בשבילך.'), body_style))

story.append(Spacer(1, 0.5*cm))

# ── CHAPTER 2 ─────────────────────────────────────────────────────────────────
story.append(Paragraph(r('פרק 2 — למי אנחנו מדברים'), chapter_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph(r('היזם הבודד — הפרופיל שלנו:'), highlight_style))
bullets2 = [
    r('חלום גדול. ידיים בודדות. שעות ספורות ביום.'),
    r('יודע מה הוא רוצה לבנות — לא תמיד יודע איך.'),
    r('מחפש להתחיל להרוויח, לגייס, לגדול — בסדר הנכון.'),
    r('לא מחפש להחליף אנשים — מחפש להיות מוכן לקראתם.'),
    r('מעדיף ללמוד תוך כדי תנועה, לא מקורסים.'),
]
for b in bullets2:
    story.append(Paragraph('← ' + b, bullet_style))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(r('HypeShow לא פונה ליזם שמחפש פרצה — הוא פונה ליזם שמחפש בסיס.'), body_style))

story.append(Spacer(1, 0.5*cm))

# ── CHAPTER 3 ─────────────────────────────────────────────────────────────────
story.append(Paragraph(r('פרק 3 — למה HypeShow ולא אחר'), chapter_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
story.append(Spacer(1, 0.3*cm))

compare_data = [
    [Paragraph(r('HypeShow'), ParagraphStyle('CH', fontName='ArialUnicode', fontSize=11, textColor=CORAL, alignment=TA_RIGHT, leading=16)),
     Paragraph(r('האלטרנטיבות'), ParagraphStyle('CA', fontName='ArialUnicode', fontSize=11, textColor=GRAY, alignment=TA_RIGHT, leading=16))],
    [Paragraph(r('מקצוענים עם ניסיון יזמי'), body_style),
     Paragraph(r('שותפים שלעיתים חסרי ניסיון'), body_style)],
    [Paragraph(r('זמין 24/7, ללא אגו'), body_style),
     Paragraph(r('כלים גנריים ללא אישיות'), body_style)],
    [Paragraph(r('מכינים אותך לצוות אנושי בריא'), body_style),
     Paragraph(r('מחליפים עובדים לצמיתות'), body_style)],
    [Paragraph(r('מצטברים ומשתפרים איתך'), body_style),
     Paragraph(r('מתחילים מאפס בכל פרויקט'), body_style)],
]
compare_table = Table(compare_data, colWidths=[8.5*cm, 8.5*cm])
compare_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK),
    ('BACKGROUND', (0,1), (-1,-1), LIGHT_BG),
    ('GRID', (0,0), (-1,-1), 0.5, GRAY),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, LIGHT_BG]),
]))
story.append(compare_table)

story.append(Spacer(1, 0.5*cm))

# ── CHAPTER 4 ─────────────────────────────────────────────────────────────────
story.append(Paragraph(r('פרק 4 — ה-MOAT בשפה שיווקית'), chapter_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph(r('Collective Wisdom Engine — מנוע הידע המשותף'), highlight_style))
story.append(Paragraph(r('כל יזם שעובד עם HypeShow לא רק מקבל — הוא גם תורם. כל החלטה, כל ספרינט, כל שגיאה ולמידה — מחזקים את הקצינים עבור כולם.'), body_style))
story.append(Spacer(1, 0.2*cm))

moat_bullets = [
    r('מתחרה יכול להעתיק פרומפט — לא יכול להעתיק שנים של ניסיון אמיתי.'),
    r('כל יזם שמצטרף הופך את המערכת לחכמה יותר עבור הבא אחריו.'),
    r('ה-MOAT לא נבנה בקוד — הוא נבנה בזמן ובהחלטות אמיתיות.'),
]
for b in moat_bullets:
    story.append(Paragraph('← ' + b, bullet_style))

story.append(Spacer(1, 0.5*cm))

# ── CHAPTER 5 ─────────────────────────────────────────────────────────────────
story.append(Paragraph(r('פרק 5 — Consistency Intelligence'), chapter_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph(r('מה שלמדת עם אופיסר אחד — עובד אותו אופן עם כל השאר.'), highlight_style))
story.append(Paragraph(r('כל פיצ\'ר שנוסף ל-HypeShow עובר בדיקת עקביות: האם הוא מתנהג כמו כל השאר? האם שפת הממשק, חוויית המשתמש, ודפוסי האינטראקציה — עקביים ברמה שמרגישה טבעית מהיום הראשון?'), body_style))
story.append(Spacer(1, 0.2*cm))

ci_bullets = [
    r('לחיצה על שם אופיסר — תמיד מסננת לפי אותו אופיסר, בכל מסך.'),
    r('סגירת חלון שיחה — לא מאפסת. ממשיכים מאותה נקודה.'),
    r('כותרת שיחה — נקבעת תמיד בשאלה פתיחה, בכל סוג שיחה.'),
    r('ה-pattern החדש הופך לתקן — ויושם בכל מקום.'),
]
for b in ci_bullets:
    story.append(Paragraph('← ' + b, bullet_style))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(r('זו האינטליגנציה השקטה של HypeShow — לא רואים אותה, אבל מרגישים אותה בכל אינטראקציה.'), body_style))

story.append(Spacer(1, 0.5*cm))

# ── CHAPTER 6 ─────────────────────────────────────────────────────────────────
story.append(Paragraph(r('פרק 6 — מסע 30 יום: הגיבור הוא היזם'), chapter_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
story.append(Spacer(1, 0.3*cm))

journey_data = [
    [Paragraph(r('מה היזם מרגיש'), ParagraphStyle('JH', fontName='ArialUnicode', fontSize=11, textColor=CORAL, alignment=TA_RIGHT, leading=16)),
     Paragraph(r('יום'), ParagraphStyle('JD', fontName='ArialUnicode', fontSize=11, textColor=CORAL, alignment=TA_CENTER, leading=16))],
    [Paragraph(r('"הצוות מחכה לי — זה מרגיש כמו יום ראשון בעבודה חדשה"'), body_style),
     Paragraph(r('יום 1'), ParagraphStyle('JN', fontName='ArialUnicode', fontSize=12, textColor=DARK, alignment=TA_CENTER, leading=18))],
    [Paragraph(r('"הם עזרו לי להחליט מה שלא יכולתי לבד"'), body_style),
     Paragraph(r('יום 7'), ParagraphStyle('JN', fontName='ArialUnicode', fontSize=12, textColor=DARK, alignment=TA_CENTER, leading=18))],
    [Paragraph(r('"אני כבר חושב כמו מנהל — מנתב, מחליט, בודק"'), body_style),
     Paragraph(r('יום 14'), ParagraphStyle('JN', fontName='ArialUnicode', fontSize=12, textColor=DARK, alignment=TA_CENTER, leading=18))],
    [Paragraph(r('"חייב לספר לחבר — ההצלחה מרגישה שלי"'), body_style),
     Paragraph(r('יום 30'), ParagraphStyle('JN', fontName='ArialUnicode', fontSize=12, textColor=DARK, alignment=TA_CENTER, leading=18))],
]
journey_table = Table(journey_data, colWidths=[13*cm, 4*cm])
journey_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK),
    ('GRID', (0,0), (-1,-1), 0.5, GRAY),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, LIGHT_BG]),
    ('BACKGROUND', (1,1), (1,1), colors.HexColor('#fff0eb')),
    ('BACKGROUND', (1,2), (1,2), colors.HexColor('#ffe4d6')),
    ('BACKGROUND', (1,3), (1,3), colors.HexColor('#ffd0bb')),
    ('BACKGROUND', (1,4), (1,4), colors.HexColor('#e8623a')),
    ('TEXTCOLOR', (1,4), (1,4), WHITE),
]))
story.append(journey_table)
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(r('HypeShow הוא הצוות. ההצלחה — תמיד של היזם.'), highlight_style))

story.append(Spacer(1, 0.5*cm))

# ── CHAPTER 7 ─────────────────────────────────────────────────────────────────
story.append(Paragraph(r('פרק 7 — הדרך קדימה: אקוסיסטם שגדל איתך'), chapter_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
story.append(Spacer(1, 0.3*cm))

eco_data = [
    [Paragraph(r('מה זה'), ParagraphStyle('EH', fontName='ArialUnicode', fontSize=11, textColor=CORAL, alignment=TA_RIGHT, leading=16)),
     Paragraph(r('שלב'), ParagraphStyle('ES', fontName='ArialUnicode', fontSize=11, textColor=CORAL, alignment=TA_CENTER, leading=16)),
     Paragraph(r('רכיב'), ParagraphStyle('EN', fontName='ArialUnicode', fontSize=11, textColor=CORAL, alignment=TA_RIGHT, leading=16))],
    [Paragraph(r('9 קצינים עם ניסיון מצטבר, ספרינטים, שיחות מתמשכות'), body_style),
     Paragraph(r('MVP'), ParagraphStyle('EV', fontName='ArialUnicode', fontSize=11, textColor=DARK, alignment=TA_CENTER, leading=16)),
     Paragraph(r('AI Executive Suite'), body_style)],
    [Paragraph(r('לומדים יזמות תוך כדי עשייה — לקצינים, לא מקורסים'), body_style),
     Paragraph(r('ספרינט 3-4'), ParagraphStyle('EV', fontName='ArialUnicode', fontSize=11, textColor=DARK, alignment=TA_CENTER, leading=16)),
     Paragraph(r('Entrepreneur School'), body_style)],
    [Paragraph(r('עצמאיים מאומנים שנשארים באקוסיסטם'), body_style),
     Paragraph(r('Post-MVP'), ParagraphStyle('EV', fontName='ArialUnicode', fontSize=11, textColor=DARK, alignment=TA_CENTER, leading=16)),
     Paragraph(r('Freelancer Marketplace'), body_style)],
]
eco_table = Table(eco_data, colWidths=[8*cm, 3*cm, 6*cm])
eco_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK),
    ('GRID', (0,0), (-1,-1), 0.5, GRAY),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, LIGHT_BG]),
]))
story.append(eco_table)

story.append(Spacer(1, 0.5*cm))

# ── FOOTER ────────────────────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=1.5, color=CORAL))
story.append(Spacer(1, 0.2*cm))
footer_data = [[
    Paragraph(r('מסמך עבודה פנימי — לא להפצה'), caption_style),
    Paragraph(r('HypeShow © 2026'), ParagraphStyle('FC', fontName='ArialUnicode', fontSize=9, textColor=CORAL, alignment=TA_CENTER, leading=14)),
    Paragraph(r('ענבר | CMO'), caption_style),
]]
footer_table = Table(footer_data, colWidths=[6*cm, 5*cm, 6*cm])
footer_table.setStyle(TableStyle([
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(footer_table)

doc.build(story)
print(f"PDF נוצר: {OUTPUT_PATH}")
subprocess.run(['open', OUTPUT_PATH])
