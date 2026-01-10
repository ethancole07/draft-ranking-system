# Draft Ranking System

## Overview
This project implements a data-driven player ranking and draft decision system designed for competitive leagues with rotating roles, incomplete statistics, and unequal participation. The system computes role-aware performance metrics, applies participation-based adjustments, and produces composite rankings to support fair and informed draft decisions.

While the system is general-purpose and reusable across league formats, it was tested and demonstrated using data from a community-run football league on Roblox.

---

## Key Features
- **Role-aware scoring** for offense, defense, and special teams
- **Participation factor** to mitigate small-sample and availability bias
- **Eligibility rules** for specialized roles (e.g., quarterback, kicker)
- **Automatic weight tuning** using MVP outcomes as a proxy for player impact
- **Modular scoring design** allowing metrics and weights to be adjusted without changing core logic

---

## Methodology
Each player’s overall value is computed as a weighted combination of:
- Offensive contribution
- Defensive contribution
- Special teams contribution

Scores are scaled by a participation factor to account for uneven games played. Feature weights are automatically tuned via grid search to maximize alignment between top-ranked players and observed MVP outcomes, producing rankings that better reflect real in-game impact.

---

## How to Run
1. Open the notebook:
