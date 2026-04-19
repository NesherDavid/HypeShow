# HypeSHow STRATEGY: THE COLLECTIVE INTELLIGENCE BOARD

## 1. Core Vision
Scaling solopreneurs by providing a "Senior Executive Suite" that learns and adapts.
HypeSHow serves a dual purpose:
- **Technological:** Provides expert executive guidance for building and growing a venture.
- **Educational:** Prepares the entrepreneur to eventually hire and manage real human employees — learning management, organizational culture, and leadership by doing, not by reading.

## 2. Competitive Moat: Collective Wisdom Engine
Every interaction refines the agents' professional methodology. When one agent learns, the entire HypeSHow fleet gets smarter for all future users (Methodology-only, no PII leakage).
Strategy: be first to market, accumulate expertise advantage from day one. A competitor who arrives later cannot buy this knowledge — it must be earned over time and projects.

## 3. Business Model
Experience-based SaaS. Pricing is driven by the 'Seniority' of the agents, which grows with every project they complete.

### Seniority Score Model (Approved: 2026-04-05)
- **Model:** Collective (cross-platform) — expertise accumulated across all customers benefits every new customer. Anonymized. No PII transfer.
- **Scoring:** Points per action (project completion, Chairman approval, LEARNINGS_LOG entry, on-time HANDOFF).
- **Tiers:** Junior Suite (0–150pts / $49mo) → Senior Suite (151–500pts / $99mo) → Partner Suite (501+pts / $199mo).
- **Visibility:** Seniority Score shown as ★ progress bar on every officer card — drives organic upgrade desire.

## 4. Customer Experience North Star

### The 4 Milestones
| רגע | מה הלקוח חווה | מה אנחנו עושים |
| :--- | :--- | :--- |
| **יום 1** | קל להתחיל, עוצמתי לחוות, אמיתי לגמרי — תחושת "ביום הראשון בעבודה עם צוות שכבר מחכה לי" | Onboarding מרגש: שמות, תפקידים, ברכת צוות, Sprint ראשון נפתח |
| **יום 7** | "הם עוזרים לי לקבל החלטות שלא ידעתי לקבל לבד" | החלטה ראשונה משמעותית שהלקוח מוביל בעצמו |
| **יום 14** | "אני כבר חושב אחרת — כמו מנהל" | הלקוח מנתב, מחליט, מבקר — לא רק שואל |
| **יום 30** | "אני חייב לספר לחבר שלי על זה" | רגע ה-NPS — הלקוח ממליץ כי הוא גאה בעצמו, לא רק במוצר |

### מטרת העל
> הלקוח מרגיש שההצלחה היא שלו. אנחנו הצוות שלו — לא הכלי שלו.

## 5. Approved Tech Decisions (2026-04-05)
- **Frontend:** Next.js (SSR, RTL-native, `dir="rtl"` at root layout)
- **CSS:** CSS Logical Properties only — no `padding-left`, no `margin-right`
- **Language:** TypeScript throughout
- **Backend:** Node.js + Express (MVP) → Python Microservice added later for AI Engine only
- **Database:** Supabase (PostgreSQL + Auth + RLS + Real-time) — replaces plain PostgreSQL. Free tier → Pro $25/mo.
- **Hosting:** Vercel (MVP) → AWS when scaling

## 6. LLM Cost Architecture (Approved: 2026-04-06)

Three-layer protection — allows "unlimited" UX while maintaining healthy margins:

### Layer 1: Model Routing
- 80% Haiku (simple queries) / 15% Sonnet (complex) / 5% Opus (strategic)
- User never knows which model responded
- Savings: ~60% vs. Sonnet-only

### Layer 2: Prompt Caching
- Each officer system prompt (~2,500 tokens) cached via Anthropic API flag
- Cache reads cost 10% of normal input price (90% discount)
- One line of code — immediate ROI, scales automatically

### Layer 3: Soft Throttling (4-Zone System)
Track `daily_tokens_used` per user in Supabase. Resets at midnight.

| Zone | Threshold | Response Delay | UX Behavior |
| :--- | :--- | :--- | :--- |
| Normal | 0–70% | 0s | Full speed |
| Yellow | 70–90% | 12s | "מעבד..." spinner shown |
| Red | 90–100% | 30s | Officer: "יש המון מה לעבד — תן לי רגע לחשוב על זה" |
| Danger | 100–110% | 60s | Officer: "זו שאלה מורכבת, אני רוצה לענות לך טוב מחר" |
| STOP | >110% | Full stop | Same message + conversation ends |

- All throttle messages come from the officer persona — never a system error
- Yellow zone requires "מעבד..." UI indicator (prevents "app crashed" perception)
- Legal: "fair use policy" clause required in Terms of Service (CISO: יפתח)

### Cost Model — Pessimistic Scenario (5 conversations/day/user)
| Scale | API Cost/User/Month | Revenue ($99×N) | Gross Margin |
| :--- | :--- | :--- | :--- |
| 20 users | $37.50 | $1,980 | ~58% |
| 200 users | $32 | $19,800 | ~67% |
| 2,000 users | $26 | $198,000 | ~73% |

Margin improves at scale: caching efficiency increases, infra costs amortize. At $50K+/month API → Anthropic Enterprise tier (custom pricing).

### Scaling Infrastructure
| Users | Vercel | Supabase | Redis | Total Infra |
| :--- | :--- | :--- | :--- | :--- |
| 20 | $20 | $0 | — | $20 |
| 200 | $50 | $25 | — | $75 |
| 500+ | $100 | $25 | $80 | $205 |
| 2,000 | $200 | $100 | $80 | $380 |

Redis added at ~500 users for concurrent session cache (~1 week Oded's time, not a rebuild).
