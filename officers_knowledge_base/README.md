# Officers Knowledge Base

Cross-venture knowledge management system for HypeShow officers.

## Structure

```
officers_knowledge_base/
├── _universal/                    # Knowledge across ALL ventures
│   ├── ceo_expertise.md           # Aggregated CEO learnings (SUPER_CEO)
│   ├── cto_expertise.md           # Aggregated CTO learnings (SUPER_CTO)
│   ├── cpo_expertise.md           # Aggregated CPO learnings
│   ├── cmo_expertise.md           # Aggregated CMO learnings
│   ├── cfo_expertise.md           # Aggregated CFO learnings
│   ├── ciso_expertise.md          # Aggregated CISO learnings
│   ├── coo_expertise.md           # Aggregated COO learnings
│   ├── cpsycho_expertise.md       # Aggregated CPsyO learnings
│   ├── qa_expertise.md            # Aggregated QA learnings
│   ├── security_playbook.md       # Common threats + fixes
│   └── officer_templates.md       # System prompts that work
│
└── ventures/
    └── HYP_001/                   # Venture-specific (anonymized ID)
        ├── officer_ceo_role.md    # CEO behavior for this venture
        ├── officer_cto_role.md
        ├── officer_cpo_role.md
        ├── officer_cmo_role.md
        ├── officer_cfo_role.md
        ├── officer_ciso_role.md
        ├── officer_coo_role.md
        ├── officer_cpsycho_role.md
        ├── officer_qa_role.md
        ├── founder_profile.md     # Anonymized founder context
        ├── venture_state.md       # Sprint, blockers, decisions
        └── officer_learnings.md   # Daily extracts from conversations
```

## Naming Convention

- **No first names** in any file (security through obscurity)
- Venture IDs: `HYP_NNN` format (HYP_001, HYP_002, etc.)
- Officer references: role-based only (`officer_ceo_role.md`, NOT `officer_steve.md`)

## Knowledge Flow

1. **Onboarding new venture (Day 1):**
   - Officer reads `_universal/<role>_expertise.md` → 50 ventures of wisdom
   - Officer reads `ventures/HYP_NNN/founder_profile.md` → knows founder
   - Officer reads `ventures/HYP_NNN/officer_<role>_role.md` → role behavior

2. **During conversation:**
   - Officer logs to `ventures/HYP_NNN/officer_learnings.md`

3. **Weekly synthesis (content editor):**
   - Editor reads all `ventures/*/officer_learnings.md`
   - Extracts patterns → `_universal/<role>_expertise.md`
   - Founder/Ayelet review + approve

4. **Future automation:**
   - AI extracts learnings from conversation logs
   - Weekly synthesis → human review → universal base
