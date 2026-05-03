# HypeShow — Venture Data Schema (v1.0)

**Status:** Approved | **Date:** 2026-04-30
**Owners:** Oded (CTO) + Daniel (CPO) + Iftach (CISO) + Gemini (Advisor)

---

## Schema — 16 Fields

| Field Name | Type | Enum/Options | Max Length | Required | Validation Rule |
|---|---|---|---|---|---|
| companyName | text | — | 100 | ✅ | No special chars |
| pitch | text | — | 500 | ✅ | No URLs |
| targetAudience | enum | SMB, Enterprise, Consumer | — | ✅ | Strict enum |
| industryCategory | enum | See list below | — | ✅ | Strict enum |
| fundingStage | enum | Seed, Series-A, Series-B, Growth | — | ✅ | Strict enum |
| businessModel | enum | SaaS, B2B, B2C, Marketplace, Fintech, Other | — | ✅ | Strict enum |
| primaryChallenge | enum | Fundraising, Product_Launch, Customer_Acquisition, Scalability, Strategy | — | ✅ | Strict enum |
| uniqueValueProp | text | — | 150 | ✅ | No URLs |
| competitors | text | — | 250 | ❌ | Free text |
| targetGeo | enum | Global, US, Europe, Israel, Asia | — | ✅ | Strict enum |
| productStage | enum | Concept, Prototype, MVP, Revenue_Generating, Scaling | — | ✅ | Strict enum |
| revenueModel | enum | Subscription, Transactional, Ad-based, Licensing, Freemium | — | ✅ | Strict enum |
| brandVoice | enum | Professional, Disruptive, Bold, Trustworthy, Friendly | — | ✅ | Strict enum |
| teamSize | enum | Solo_Founder, 2-5, 6-15, 16-50, 50+ | — | ✅ | Strict enum |
| techStack | text | — | 200 | ❌ | Keywords only |
| immediateGoal | text | — | 300 | ✅ | Free text |

---

## industryCategory — Full Enum (Iftach, CISO)

```
Cybersecurity, AI/ML, FinTech, HealthTech, E-commerce,
Cloud Infrastructure, SaaS, EdTech, Blockchain/Web3,
MarketplacesTech, IoT, Biotech, CleanTech, InsurTech,
Supply Chain, Logistics, HR/Recruiting, Travel/Hospitality,
Media/Entertainment, Other
```

**Security note (Iftach):** Cybersecurity + HealthTech + FinTech = elevated compliance logging.

---

## PII Masking Rules (Iftach, CISO)

Fields sent to Gemini API: all [REDACTED] per regex:
- CC numbers → [REDACTED_CARD_****XXXX]
- SSN/ID → [REDACTED_ID]
- API keys → [REDACTED_KEY]
- Bank accounts → [REDACTED_ACCOUNT]

LocalStorage: raw (founder sees own data only).
Audit log: 90 days, layered visibility.

---

## Onboarding — 4-Step Flow (Daniel, CPO)

**Step 1 — מי אתה?** (4 fields)
companyName, pitch, targetAudience, teamSize

**Step 2 — מה אתה בונה?** (5 fields)
businessModel, revenueModel, productStage, fundingStage, techStack

**Step 3 — מה הדרך?** (5 fields)
primaryChallenge, immediateGoal, uniqueValueProp, competitors, targetGeo

**Step 4 — מה הסגנון שלך?** (2 fields)
industryCategory, brandVoice

---

## Security Sign-off

- **Iftach (CISO):** Approved 2026-04-30
- **Layer 3:** Active in all officer prompts
- **Luhn validation:** Required for CC detection
- **Audit log:** 90 days, Nadav sees all, officers see metadata only
