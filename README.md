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
- **Modular**
