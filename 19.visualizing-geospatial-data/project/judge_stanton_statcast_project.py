from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Layman roadmap:
# 1) Count what happened in 2017 for each player.
# 2) Compare HR quality (hard + low) with launch_speed/launch_angle.
# 3) Compare pitch speed they hit HRs off (release_speed median).
# 4) Build strike-zone heatmaps for HR locations.
#


# Expected outputs for DataCamp-style checks:
# - judge_events_2017, stanton_events_2017 (Series)
# - fig1, ax1 (HR scatterplots)
# - player_hr, player_fast (single-word conclusions)
# - judge_strike_hr, stanton_strike_hr with zone_x/zone_y columns


# Reusable template (if you do not care about baseball):
# 1) Compare category frequencies across two groups.
# 2) Compare quality metrics with scatterplots.
# 3) Compare context metrics with median + boxplot.
# 4) Compare concentration patterns with 2D heatmaps.


def assign_x_coord(row):
    """
    Assign x position for Statcast strike-zone bins.
    Zones 11-14 are intentionally ignored for simpler plotting.
    """
    if row.zone in [1, 4, 7]:
        return 1
    if row.zone in [2, 5, 8]:
        return 2
    if row.zone in [3, 6, 9]:
        return 3
    return None


def assign_y_coord(row):
    """
    Assign y position for Statcast strike-zone bins.
    Zones 11-14 are intentionally ignored for simpler plotting.
    """
    if row.zone in [1, 2, 3]:
        return 3
    if row.zone in [4, 5, 6]:
        return 2
    if row.zone in [7, 8, 9]:
        return 1
    return None


def load_player_csv(path: Path, fallback_url: str) -> pd.DataFrame:
    """Load local file if present, otherwise fetch once and cache it locally."""
    if path.exists():
        return pd.read_csv(path)

    df = pd.read_csv(fallback_url)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return df


# Data source setup.
# DataCamp context:
# - In the project notebook, `judge.csv` and `stanton.csv` are preloaded in the working dir.
# - Outside DataCamp, you need to provide those files yourself.
# - This script handles both: local file first, URL fallback second.
project_dir = Path(__file__).resolve().parent
judge_path = project_dir / "judge.csv"
stanton_path = project_dir / "stanton.csv"

judge = load_player_csv(
    judge_path,
    "https://raw.githubusercontent.com/Suraj-Patro/Baseball_Data_Analysis/main/datasets/judge.csv",
)
stanton = load_player_csv(
    stanton_path,
    "https://raw.githubusercontent.com/Suraj-Patro/Baseball_Data_Analysis/main/datasets/stanton.csv",
)

# -------------------------------------------------------------------
# 1) Event counts in 2017 (required Series outputs).
# -------------------------------------------------------------------
# Template step 1 applied here: frequency comparison across the two groups.
# Why: this answers "How many of each event did each player have in 2017?"
# Why this matters: it gives a baseline profile before we focus only on home runs.
judge_events_2017 = judge.loc[judge["game_year"] == 2017, "events"].value_counts()
stanton_events_2017 = stanton.loc[stanton["game_year"] == 2017, "events"].value_counts()

# -------------------------------------------------------------------
# 2) Who hits HRs lower + harder? (launch angle vs launch speed).
# -------------------------------------------------------------------
# Template step 2 applied here: quality comparison via scatterplots + medians.
# Why: lower angle + higher speed usually means a harder "line-drive style" HR profile.
# Why this matters: "home run count" says volume; these metrics say HR quality/style.
judge_hr = judge.loc[judge["events"] == "home_run"].copy()
stanton_hr = stanton.loc[stanton["events"] == "home_run"].copy()

# Two side-by-side plots make visual comparison quick.
fig1, ax1 = plt.subplots(1, 2, figsize=(12, 5), sharex=True, sharey=True)

sns.scatterplot(
    data=judge_hr,
    x="launch_angle",
    y="launch_speed",
    color="tab:blue",
    alpha=0.6,
    ax=ax1[0],
)
ax1[0].set_title("Aaron Judge home runs")
ax1[0].set_xlabel("launch_angle")
ax1[0].set_ylabel("launch_speed")

sns.scatterplot(
    data=stanton_hr,
    x="launch_angle",
    y="launch_speed",
    color="tab:orange",
    alpha=0.6,
    ax=ax1[1],
)
ax1[1].set_title("Giancarlo Stanton home runs")
ax1[1].set_xlabel("launch_angle")
ax1[1].set_ylabel("launch_speed")
fig1.suptitle("Home run profile: launch speed vs launch angle", y=1.02)
fig1.tight_layout()

judge_med_speed = judge_hr["launch_speed"].median()
judge_med_angle = judge_hr["launch_angle"].median()
stanton_med_speed = stanton_hr["launch_speed"].median()
stanton_med_angle = stanton_hr["launch_angle"].median()

# Decision rule for this question:
# - "harder" -> higher median launch_speed
# - "lower"  -> lower median launch_angle
player_hr = (
    "Stanton"
    if (stanton_med_speed > judge_med_speed and stanton_med_angle < judge_med_angle)
    else "Judge"
)

# -------------------------------------------------------------------
# 3) Who hits HRs off faster pitches? (release_speed median).
# -------------------------------------------------------------------
# Template step 3 applied here: context comparison via median + boxplot.
# Why median: less sensitive to outliers than mean.
# Why this matters: shows whether one player succeeds against tougher pitch velocity.
release_compare = pd.concat(
    [
        judge_hr[["release_speed"]].assign(player="Judge"),
        stanton_hr[["release_speed"]].assign(player="Stanton"),
    ],
    ignore_index=True,
)

fig2, ax2 = plt.subplots(figsize=(7, 4))
sns.boxplot(data=release_compare, x="player", y="release_speed", ax=ax2)
ax2.set_title("Pitch speed (release_speed) for home runs")
ax2.set_xlabel("Player")
ax2.set_ylabel("release_speed")
fig2.tight_layout()

player_fast = release_compare.groupby("player")["release_speed"].median().idxmax()

# -------------------------------------------------------------------
# 4) 2D histogram of strike zones for home runs (zones 1-9 only).
# -------------------------------------------------------------------
# Template step 4 applied here: concentration pattern comparison via 2D heatmaps.
# Why drop 11-14: they are not in the simple 3x3 strike-zone grid used here.
# Why this matters: shows where in/around the zone each player does damage on HRs.
judge_strike_hr = judge_hr.loc[
    judge_hr["zone"].isin([1, 2, 3, 4, 5, 6, 7, 8, 9])
].copy()
stanton_strike_hr = stanton_hr.loc[
    stanton_hr["zone"].isin([1, 2, 3, 4, 5, 6, 7, 8, 9])
].copy()

# Convert Statcast zone id -> simple x/y grid so we can plot a heatmap.
judge_strike_hr["zone_x"] = judge_strike_hr.apply(assign_x_coord, axis=1)
judge_strike_hr["zone_y"] = judge_strike_hr.apply(assign_y_coord, axis=1)
stanton_strike_hr["zone_x"] = stanton_strike_hr.apply(assign_x_coord, axis=1)
stanton_strike_hr["zone_y"] = stanton_strike_hr.apply(assign_y_coord, axis=1)

fig3, ax3 = plt.subplots(1, 2, figsize=(10, 4), sharex=True, sharey=True)

sns.histplot(
    data=judge_strike_hr,
    x="zone_x",
    y="zone_y",
    bins=(3, 3),
    cbar=True,
    cmap="Blues",
    ax=ax3[0],
)
ax3[0].set_title("Judge HR strike-zone heatmap")
ax3[0].set_xlabel("Zone X")
ax3[0].set_ylabel("Zone Y")

sns.histplot(
    data=stanton_strike_hr,
    x="zone_x",
    y="zone_y",
    bins=(3, 3),
    cbar=True,
    cmap="Oranges",
    ax=ax3[1],
)
ax3[1].set_title("Stanton HR strike-zone heatmap")
ax3[1].set_xlabel("Zone X")
ax3[1].set_ylabel("Zone Y")
fig3.tight_layout()

print("judge_events_2017 (top):")
print(judge_events_2017.head())
print("\nstanton_events_2017 (top):")
print(stanton_events_2017.head())
print("\nplayer_hr:", player_hr)
print("player_fast:", player_fast)

plt.show()
