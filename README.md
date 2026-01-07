# Draft Ranking System

## Overview
This project builds a ranking system for a competitive league where players rotate roles and stats are incomplete.
It ingests player box-score data, computes role-aware performance metrics, applies participation adjustments,
and outputs ranked player lists to support draft decisions.

## Features (current / planned)
- Data model for players and game stats
- Offensive / defensive / special teams scoring functions
- Participation factor to reduce small-sample noise
- Composite ranking output (CSV + printed leaderboard)

## How to run
1. Install dependencies:
   pip install -r requirements.txt
2. Run ranking:
   python -m src.rank
