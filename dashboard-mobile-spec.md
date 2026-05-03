# HypeShow Dashboard — Mobile Spec

**Priority**: High  
**Sprint**: Day 12  
**Owner**: Oded (CTO)  

---

## Overview

Build mobile-responsive dashboard layout. Desktop version intact — mobile is **separate build in same file with media query** `@media (max-width: 768px)`.

## Critical Rules

1. **BACKUP FIRST** — Full backup of `dashboard/index.html` before ANY changes
2. **Use desktop SVG icons exactly** — Copy from current `dashboard/index.html` topbar icons (meetings, notifications)
3. **Settings icon** — Copy gear icon from desktop, apply same orange color as other icons
4. **No hardcoded emoji**
5. **RTL maintained** — Text flows right-to-left, header direction LTR

---

## Mobile Header

**Location**: Fixed, top 0, height 56px

**Layout (LTR inside RTL doc)**:
- LEFT: HypeShow logo (from landing page) + text "HypeShow"
- RIGHT: 3 icon buttons (meetings, notifications, settings)

**Icons**: 
- Copy SVG code directly from desktop topbar (`topbar-right` section)
- Keep circular background + border styling
- ALL icons: coral color (#e8623a)
- Settings: Same gear icon as desktop, coral colored

---

## Card Layout

**Width**: 100% (full screen minus 16px padding each side)

**Stack**: Vertical (one per row)

**RTL**: Avatar on RIGHT side (use `flex-direction: row-reverse`)

---

## Reference Mockup

**http://localhost:8765/dashboard-mobile-mockup.html**

(Icons are placeholder — you'll copy actual SVGs from desktop dashboard)

---

## Files to Modify

- `dashboard/index.html` — Add mobile CSS + mobile header, keep desktop untouched

---

## Timeline

4 days remaining in sprint. Start backup → icon copy → media query → test on device.

