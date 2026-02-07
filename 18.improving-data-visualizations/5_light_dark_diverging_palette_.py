import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Key takeaways (continuous palettes):
# - Use continuous palettes for continuous data; keep them simple for readability.
# - `light_palette()` maps low values to light; `dark_palette()` maps low to dark.
# - Diverging palettes (e.g., `diverging_palette`) are best when data has a meaningful midpoint.
# - Color encodes magnitude but is less precise than position/length.
# - `cmap` is the colormap used by heatmap; `center` sets the neutral value.
# - `vmin`/`vmax` fix the color scale range (useful for symmetric legends).
# - `plt.style.use("dark_background")` switches the whole figure to a dark theme.

# Simple palette previews.
light_blues = sns.light_palette("blue", as_cmap=False)
dark_reds = sns.dark_palette("red", as_cmap=False)
# palplot: quick visual preview of a palette (color swatches).
sns.palplot(light_blues)
plt.title("light_palette('blue')")
plt.show()

sns.palplot(dark_reds)
plt.title("dark_palette('red')")
plt.show()

# Heatmap with a diverging palette centered at 0.
data = np.random.normal(0, 1, (6, 12))
# heatmap: color-encoded grid for 2D numeric data.
# center/vmin/vmax: set the neutral midpoint and symmetric color limits.
sns.heatmap(
    data,
    cmap=sns.diverging_palette(220, 20, as_cmap=True),
    center=0,
    vmin=-3,
    vmax=3,
)
plt.title("Heatmap with diverging palette (centered at 0)")
plt.show()

# Dark background example: use a dark-centered diverging palette.
plt.style.use("dark_background")
dark_center = sns.diverging_palette(250, 0, center="dark", as_cmap=True)
sns.heatmap(data, cmap=dark_center, center=0, vmin=-3, vmax=3)
plt.title("Diverging palette with dark center (dark background)")
plt.show()
plt.style.use("default")

# Diverging palette for data centered at 0.
df = pd.DataFrame(
    {
        "city": ["Denver", "LA", "Houston", "Fairbanks"],
        "z_score": [-0.6, 0.2, 1.1, -0.3],
    }
)
sns.barplot(
    data=df,
    x="city",
    y="z_score",
    palette=sns.diverging_palette(220, 20, as_cmap=False),
)
# axhline: draw a horizontal reference line across the axes (here at y=0).
plt.axhline(0, color="gray", linewidth=1)
plt.title("Diverging palette for values around 0")
plt.show()

# Light vs dark palette for different backgrounds.
sns.set_style("white")
sns.scatterplot(
    data=df,
    x="city",
    y="z_score",
    hue="z_score",
    palette=sns.light_palette("orangered", as_cmap=False),
)
plt.title("Light palette on white background")
plt.show()

sns.set_style("dark")
sns.scatterplot(
    data=df,
    x="city",
    y="z_score",
    hue="z_score",
    palette=sns.dark_palette("orangered", as_cmap=False),
)
plt.title("Dark palette on dark background")
plt.show()
