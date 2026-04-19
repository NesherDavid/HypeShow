# HypeShow — הגדרות עבודה

## Plan Mode
בplan mode: מאה מילים או פחות, צעדים ממוספרים, בלי הסברים — אלא אם נדב מבקש אחרי זה.

## שפת עבודה
נדב עובד בעברית עם ערבוב אנגלי. כל תוצרים כתובים ב-RTL.

## כלל מסמכים: תוצר מפורט = PDF בלבד

**מתי:** כשיש תכנית, רעיון מפורט, מסע לקוח, ארכיטקטורה, סיכום ישיבה, או כל תוצר שמיועד לקריאה — **אל תציג markdown בצ'אט**.

**איך:**
1. צור PDF עם Python + reportlab
2. פונט: **Arial Unicode** (`/Library/Fonts/Arial Unicode.ttf`) — תומך עברית + אנגלית + מספרים
3. כיוון: **RTL** — יישור ימין, `get_display()` מ-bidi על כל מחרוזת
4. שמור ב: `/Users/nesher/Desktop/HypeShow/<שם-קובץ>.pdf`
5. פתח אוטומטית עם `open`

**קוד בסיסי לשימוש חוזר:**
```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from bidi.algorithm import get_display

pdfmetrics.registerFont(TTFont('ArialUnicode', '/Library/Fonts/Arial Unicode.ttf'))

def r(t): return get_display(t)  # RTL conversion
```

**צבעי HypeShow:**
- Coral: `#e8623a`
- Dark: `#1c1c1e`
- Gray: `#6e6e73`
- Purple (Daniel): `#7b3dd5`

**שמות קבצים:** `<נושא>-<קצין>.pdf` — לדוגמה: `user-journey-daniel.pdf`, `threat-model-iftach.pdf`

---

## כלל גיבויים — חובה לפני כל עריכה

**לפני נגיעה בכל קובץ קיים:**
1. שמור עותק עם timestamp: `שם-קובץ-backup-YYYY-MM-DD.ext`
2. מיקום: אותה תיקייה, או `_backups/` לידה

**3 רמות גרסאות (naming convention):**
- `draft` — עבודה בתהליך
- `review` — הוצג לנדב / ממתין לאישור
- `release` — אושר ויצא לאוויר

פורמט: `hypeshow-landing-v1.2-release.html`

---

## GitHub — כלל עבודה

- כל milestone משמעותי = commit מ-Oded עם הודעה ברורה
- אין עבודה "בחלל" ללא גיבוי מרכזי ב-Repository
- Repository נמצא ב-GitHub תחת פרויקט HypeShow

---

## כלל תרגומים — אל תתרגמו בעצמכם

כשמשתמש מבקש תרגום חומרים — **אל תתרגמו**. הפנו לפרילאנסר מתמחה (Gemini Translation Agent או שירות חיצוני). קצינים אינם מומחי תרגום — הזמן והטוקנים יקרים מדי לכך.

---

## תרגומי דף הנחיתה — ארכיטקטורה

- קבצי תרגום: `/Users/nesher/Desktop/HypeShow/Languages/<lang>.json`
- פורמט שמות: `en.json`, `es.json`, `he.json` וכו'
- הדף טוען תרגום דינמית עם `fetch('../../Languages/' + lang + '.json')`
- **לא** מוטמעים inline ב-HTML
