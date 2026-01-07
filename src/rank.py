from __future__ import annotations

import pandas as pd


DATA_PATH = "data/sample_players.csv"


def participation_factor(games_played: int, cap: int = 6) -> float:
    """Scale down small sample sizes. Maxes out at 1.0 once cap games are reached."""
    if games_played <= 0:
        return 0.0
    return min(1.0, games_played / cap)


def simple_offense_score(row: pd.Series) -> float:
    """
    Baby-step offense score:
    - Passing efficiency: yards/attempt
    - Passing TD rate: TDs/attempt
    - Penalty for INT rate: INTs/attempt
    - Receiving efficiency: rec_yards/target + TD rate
    This is NOT final — just enough to generate reasonable rankings.
    """
    pass_attempts = row["pass_attempts"]
    targets = row["targets"]

    pass_eff = (row["pass_yards"] / pass_attempts) if pass_attempts > 0 else 0.0
    pass_td_rate = (row["pass_tds"] / pass_attempts) if pass_attempts > 0 else 0.0
    pass_int_rate = (row["pass_ints"] / pass_attempts) if pass_attempts > 0 else 0.0

    rec_eff = (row["rec_yards"] / targets) if targets > 0 else 0.0
    rec_td_rate = (row["rec_tds"] / targets) if targets > 0 else 0.0

    # weights are arbitrary for now; we'll tune later
    return (0.7 * pass_eff) + (20 * pass_td_rate) - (15 * pass_int_rate) + (0.5 * rec_eff) + (20 * rec_td_rate)


def simple_defense_score(row: pd.Series) -> float:
    """Baby-step defense score per game with simple weights."""
    gp = row["games_played"]
    if gp <= 0:
        return 0.0
    return (3.0 * row["sacks"] / gp) + (0.5 * row["tackles"] / gp) + (6.0 * row["def_ints"] / gp) + (10.0 * row["safeties"] / gp)


def simple_special_teams_score(row: pd.Series) -> float:
    """Baby-step kicking score with eligibility threshold."""
    gp = row["games_played"]
    att = row["fg_attempts"]
    if gp <= 0 or att < 5:
        return 0.0
    accuracy = (row["fg_made"] / att) if att > 0 else 0.0
    range_bonus = max(0.0, row["long_fg"] - 30.0) * 0.05
    return (10.0 * accuracy) + (row["fg_made"] / gp) + range_bonus


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    # Compute component scores
    df["offense"] = df.apply(simple_offense_score, axis=1)
    df["defense"] = df.apply(simple_defense_score, axis=1)
    df["special_teams"] = df.apply(simple_special_teams_score, axis=1)

    # Participation adjustment
    df["pf"] = df["games_played"].apply(participation_factor)

    # Composite score (weights can be tuned later)
    df["score"] = df["pf"] * (df["offense"] + df["defense"] + df["special_teams"])

    # Sort and display top players
    ranked = df.sort_values("score", ascending=False)[
        ["player", "games_played", "score", "offense", "defense", "special_teams", "pf"]
    ]

    print("\nTop players (sample data):")
    print(ranked.head(10).to_string(index=False))

    # Save output
    ranked.to_csv("rankings.csv", index=False)
    print("\nSaved rankings.csv")


if __name__ == "__main__":
    main()
