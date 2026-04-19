# ACTIVE LOG — Current Sprint
## Sprint: MVP Foundation | 2026-03-31 → 2026-04-19 (הוארך)

| Task | Owner | Deadline | Status |
| :--- | :--- | :--- | :--- |
| Executive Suite Onboarding | CEO | 2026-03-31 | ✅ Complete |
| Tech Stack Decision | CTO | 2026-04-03 | ✅ Complete |
| Agent Routing Architecture | CTO | 2026-04-06 | ✅ Complete |
| LLM Cost Architecture (routing + caching + throttling) | CFO + CTO | 2026-04-06 | ✅ Decided |
| Database: Supabase (replaces Vercel Postgres) | CTO + CISO | 2026-04-06 | ✅ Decided |
| Soft Throttling — 4-Zone System | CFO + CISO | 2026-04-06 | ✅ Decided |
| CISO Threat Model — Learning Pipeline | CISO | 2026-04-06 | ✅ Complete (v1.1 — 05_LEGAL/) |
| User Journey Definition | CPO | 2026-04-05 | ✅ Complete (04_DOCUMENTS/) |
| Dashboard — Design Handoff & Dev-Ready Spec | CPO | 2026-04-07 | ✅ Complete (04_DOCUMENTS/) |
| Seniority Score Definition | CPO + CFO | 2026-04-04 | ✅ Complete |
| Design System | CPO | 2026-04-10 | 🔜 Pending |
| Supabase Setup + Schema + RLS | CTO (עודד) | 2026-04-07 | 🔜 Pending |
| Prompt Caching Implementation | CTO (עודד) | 2026-04-08 | 🔜 Pending |
| Soft Throttling Middleware (4-zone) | CTO (עודד) | 2026-04-09 | 🔜 Pending |
| Vibe Coding Security Review (videos) | CISO (יפתח) | 2026-04-07 | 🔄 In Progress (סרטונים נשלחו ע"י Chairman ב-2026-04-06) |
| LEARNINGS_LOG Sync Mechanism | CTO (עודד) | 2026-04-09 | 🔜 Pending |
| Oded + Iftach Green Light Meeting | CTO + CISO | 2026-04-16 | ✅ התקיים — Green Light ניתן |
| MVP Environment Ready | CTO (עודד) | 2026-04-19 10:00 | 🔄 In Progress (Green Light ניתן ב-16.04) |
| Legal Pages — Privacy Policy + Terms of Service | CTO (עודד) + תמר | 2026-04-19 | 🔜 Pending |
| Chairman Prototype Review | CPO | 2026-04-19 | 🔜 Pending |
| Legal Review Session — ישיבה משפטית | Chairman + תמר + Steve | 2026-04-13 | 🗓️ מתוזמן (יום שני)
| Landing Page i18n — TRANSLATIONS JS (10 שפות) | CPO (דניאל) | 2026-04-17 | 🔜 Pending — HTML tags בוצעו, JS חסר |
| Weekly — Entrepreneur School Brainstorm | Steve (מנחה) + כל הצוות | 2026-04-17 | 🗓️ מתוזמן (מחר)

## 📋 הערות פיתוח — עודד

### דפים משפטיים (Legal Pages)
- יש ליצור שני דפים סטטיים: `/privacy` ו-/terms`
- מקום בממשק: **Footer** — מופיע בכל דף, קישורים בולטים
- Footer יכלול: "מדיניות פרטיות | תנאי שימוש | © 2026 נדב דפני בע"מ"
- הקישורים חייבים להיות נגישים **לפני** סיום תהליך ההרשמה (מסך אחרון של onboarding)
- בנוסף: בדף ההרשמה — checkbox מפורש: "קראתי ואני מסכים לתנאי השימוש ולמדיניות הפרטיות" — **חובה לסימון לפני המשך**
- מקור המסמכים: `05_LEGAL/` בתיקיית הפרויקט
