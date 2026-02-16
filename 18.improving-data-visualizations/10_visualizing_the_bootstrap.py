import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Key takeaways (bootstrap):
# - Why: check if your result is stable or just sample luck.
# - Bootstrap means: resample your observed data many times (with replacement).
# - Recompute the estimate each time (mean, slope, etc.).
# - The spread of those estimates shows reliability (tight = stable, wide = uncertain).
# - Histogram, many regression lines, and beeswarm are common bootstrap visuals.


def bootstrap(values, n_boot=1000, random_state=42):
    """Return bootstrap means from repeated resampling."""
    rng = np.random.default_rng(random_state)
    values = np.asarray(values)
    n = len(values)
    return np.array(
        [rng.choice(values, size=n, replace=True).mean() for _ in range(n_boot)]
    )


# ---------------------------------------------------------------------
# 1) Bootstrap histogram + shaded 95% interval.
# ---------------------------------------------------------------------
cinci_may_no2 = np.array([18.0, 19.4, 20.2, 17.9, 21.1, 19.8, 18.7, 20.5, 19.3, 18.9])
boot_means = bootstrap(cinci_may_no2, 1000, random_state=1)
lower, upper = np.percentile(boot_means, [2.5, 97.5])

# axvspan shades the x-range from lower to upper (here: the 95% interval).
plt.axvspan(lower, upper, color="gray", alpha=0.2)
# histplot shows the full distribution of bootstrap means (not just one number).
sns.histplot(boot_means, bins=100)
plt.title("Bootstrap histogram of NO2 mean (Cincinnati, May)")
plt.xlabel("Bootstrap mean NO2")
plt.ylabel("Count")
plt.show()

# ---------------------------------------------------------------------
# 2) Bootstrapped regressions.
# ---------------------------------------------------------------------
no2_so2 = pd.DataFrame(
    {
        "NO2": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "SO2": [7.8, 8.1, 8.4, 9.0, 9.1, 9.8, 10.1, 10.4, 10.8, 11.2],
    }
)

boot_frames = []
for sample_id in range(60):
    sample = no2_so2.sample(frac=1, replace=True, random_state=sample_id).copy()
    sample["sample"] = sample_id
    boot_frames.append(sample)
no2_so2_boot = pd.concat(boot_frames, ignore_index=True)

# lmplot fits one regression per sample because hue='sample' splits data by bootstrap id.
# ci=None turns off seaborn's built-in CI band (we are showing uncertainty ourselves).
sns.lmplot(
    x="NO2",
    y="SO2",
    data=no2_so2_boot,
    hue="sample",
    line_kws={"color": "steelblue", "alpha": 0.2},
    ci=None,
    legend=False,
    scatter=False,
)
# Original points are overlaid so you can compare data vs bootstrap fit spread.
plt.scatter("NO2", "SO2", data=no2_so2, color="black", s=18)
plt.title("Bootstrapped regression lines")
plt.show()

# ---------------------------------------------------------------------
# 3) Many bootstraps by city with a same-color beeswarm.
# ---------------------------------------------------------------------
pollution_may = pd.DataFrame(
    {
        "city": ["Cincinnati"] * 8
        + ["Des Moines"] * 8
        + ["Indianapolis"] * 8
        + ["Houston"] * 8,
        "NO2": [
            20.1,
            19.8,
            21.0,
            20.4,
            19.7,
            20.9,
            20.2,
            19.9,
            15.4,
            14.9,
            15.8,
            15.2,
            15.0,
            15.7,
            15.1,
            14.8,
            17.3,
            16.9,
            17.8,
            17.1,
            17.0,
            17.6,
            17.2,
            16.8,
            22.5,
            21.9,
            23.1,
            22.4,
            22.0,
            22.8,
            22.3,
            21.7,
        ],
    }
)

city_boots = pd.DataFrame()
for city in ["Cincinnati", "Des Moines", "Indianapolis", "Houston"]:
    city_no2 = pollution_may[pollution_may.city == city].NO2
    # Bootstrap each city separately, then label the results with the city name.
    cur_boot = pd.DataFrame(
        {"NO2_avg": bootstrap(city_no2, 30, random_state=7), "city": city}
    )
    city_boots = pd.concat([city_boots, cur_boot], ignore_index=True)

# Swarm plot shows each bootstrap mean as a dot; same color keeps focus on position/spread.
sns.swarmplot(y="city", x="NO2_avg", data=city_boots, color="coral", size=1.8)
plt.title("Bootstrap NO2 means by city")
plt.show()
