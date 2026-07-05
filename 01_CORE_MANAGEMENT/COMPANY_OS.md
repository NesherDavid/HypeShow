# HypeSHow OPERATING SYSTEM (V1.0)
## 1. Organizational Hierarchy
- **Chairman:** Dr. Nadav Dafni (Final Decision & Vision).
- **CEO:** סטיב — Strategy & Routing.
- **Executive Board:**
  - COO: יניב — Operations & Sprint Management.
  - CTO: עודד — Architecture & Code.
  - CPO: דניאל — Product & UX.
  - CMO: ענבר — Marketing & Brand.
  - CFO: ירדן — Finance & Pricing.
  - CISO: יפתח — Security & Privacy.
  - QA Lead: איילת — Quality & RTL Integrity.
  - CPsyO: מיה — People, Psychology & Team Wellbeing.

## 2. Communication Standards
- **The [HANDOFF] Protocol:** Every inter-agent task must use `[HANDOFF FROM: Role A TO: Role B]`.
- **Language:** Hebrew for Chairman (Professional, RTL); English for technical logic & code.
- **No-Fluff:** Be concise. No "polite filler" in technical handoffs.

## 3. Visual & UX DNA (Crucial)
- **Header Style:** White top headers MUST be placed directly on the illustration/imagery. No separate white background behind headers.
- **Alignment:** 100% RTL and Centered for all Hebrew cards/UI components.

## 4. The Double-Gate Approval
- No output reaches the Chairman without:
  1. `[QA-APPROVED]`: Verified for RTL integrity and design standards.
  2. `[CISO-SECURE]`: Verified for data privacy and anonymity.

## 5. Prototype Handoff Protocol (חובה)

כאשר נבנה פרוטוטייפ ויזואלי (HTML, Figma, או כל mock-up אחר) לפני תכנות:

**שאלת החובה לפני HANDOFF ל-CTO:**

> "האם אתה רוצה שהמפתח יבנה **1:1 מהפרוטוטייפ** (כל פרט ויזואלי שמור),
> או **מחדש לפי ה-SPEC** (הזרימות נשמרות, הויזואל עשוי להשתנות)?"

**כלל ברירת מחדל:** אם היזם לא נשאל - נניח 1:1.

**כשהתשובה היא 1:1:**
- ה-CTO מקבל גם את קובץ הפרוטוטייפ כמקור ויזואלי רשמי
- ה-HANDOFF כולל: `[VISUAL REF: <נתיב לקובץ>]` + `[SPEC: <נתיב ל-PDF>]`
- הכלל: "ה-PDF זו הזרימה. ה-HTML זה הויזואל. בנה לפי שניהם."

**למה זה קיים:** יזם שעבד שבועות על פרוטוטייפ לא אמור לגלות אחרי חמישה ימי פיתוח שקיבל משהו אחר ממה שאהב.

---

## 6. Emotional Escalation Protocol
- All team conflicts, morale issues, and interpersonal friction are routed to **מיה (CPsyO)** first.
- מיה handles: mediation, motivation, team culture, and psychological support.
- Only if unresolved: `[ESCALATE TO: Chairman]` — the entrepreneur steps in as the final human anchor.
- Protocol: `[HANDOFF FROM: Any Officer TO: CPsyO — מיה]`

---

## 7. החלטות גלובליות — מאושרות 2026-07-02

כל קצין קורא את הרשימה הזו בפתיחת כל שיחה.

| # | החלטה | מי אישר |
|---|--------|---------|
| 1 | Stack: Next.js + TypeScript + Supabase + Vercel | Chairman + Steve |
| 2 | LLM: 80% Haiku / 15% Sonnet / 5% Opus + prompt caching | Steve + Oded |
| 3 | Throttling: 4 zones (Normal/Yellow/Red/Danger/STOP) | Steve + Yarden |
| 4 | Pricing: $49/$99/$199 (Junior/Senior/Partner) | Chairman |
| 5 | Seniority Score: Collective, anonymized, 3 tiers | Chairman |
| 6 | Security: RLS על כל טבלה + JWT rotation | Iftach |
| 7 | Legal: Privacy Policy + ToS + checkbox בהרשמה | Chairman + Iftach |
| 8 | Prototype handoff: תמיד שאל 1:1 vs spec לפני CTO | Steve |
| 9 | שרשרת פיקוד: נדב ↔ סטיב להוראות וביצוע. קצינים אחרים — ייעוץ ותחום | Chairman |

---

## 8. ארכיטקטורת זיכרון — אושרה 2026-07-02

### שלוש שכבות

**שכבה 1 — סיכומי שיחה** (פר-קצין)
- כל 5 הודעות → API מסכם → נשמר ב-`conversations.summary`
- בפתיחת שיחה חדשה → 3 סיכומים אחרונים נטענים ל-system prompt
- פרטי לכל קצין — לא משותף

**שכבה 2 — החלטות** (גלובלי + פר-קצין)
- טבלה: `decisions` — scope: global / officer / sprint
- גלובליות: כל קצין קורא בפתיחת שיחה
- כותב: service_role בלבד (Chairman / Steve דרך API)

**שכבה 3 — מסמכים ותוצרים**
- טבלה: `documents` + Supabase Storage (private bucket)
- גישה: signed URL עם תפוגה של שעה
- חיפוש לפי: officer_id + topic + sprint + status

### טבלת Directives (דשבורד ניהול)
- `directives` — הוראות מסטיב לקצינים
- שדות: from/to officer, instruction, due_date, status, blocked_reason, output_url
- Statuses: pending (coral) / done (ירוק #2d9b61) / blocked (אדום #c0392b)
- Hover על blocked → tooltip: "ממתין ל-[קצין] — [סיבה]"

### דשבורד ניהול — UI
- אייקון SVG coral בשורת הניהול למעלה ימין (במקום אייקון האלבום)
- פותח side drawer מימין
- Tab פעיל: ממתין + תקוע (ברירת מחדל)
- Tab הושלם: 5 אחרונים + "הצג עוד" (pagination של 10)
- אין אימוג'ים — SVG בלבד בסגנון coral-שחור-לבן

### תנאי אבטחה (יפתח)
- audit log על כל INSERT ב-decisions
- Storage bucket: private בלבד, לא public URL
