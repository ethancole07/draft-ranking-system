# Draft Ranking System

## Overview
This project implements a data-driven ranking and draft decision system for competitive leagues
with rotating roles and incomplete statistics. The system computes role-aware performance metrics,
applies participation adjustments, and outputs ranked player lists to support fair draft decisions.

The system was tested using data from a community-run football league, but is designed to be reusable
for other competitive league environments.

## How to Run
1. Install dependencies:
   pip install pandas
2. Run the ranking script:
   python src/rank.py

## Output
The program outputs a ranked leaderboard and saves results to `rankings.csv`.
