import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Key takeaways (continuous palettes):
# - Use continuous palettes when a variable moves smoothly across values.
# - `light_palette()` makes low values light; `dark_palette()` makes low values dark.
# - Use a diverging palette when zero (or another midpoint) has special meaning.
# - `cmap` picks colors, `center` defines the neutral value, `vmin`/`vmax` fix range.
# - Use a dark-centered palette when plotting on dark backgrounds.

# Palette previews.
light_blues = sns.light_palette("blue", as_cmap=False)
dark_reds = sns.dark_palette("red", as_cmap=False)
# palplot draws color swatches so you can inspect a palette quickly.
sns.palplot(light_blues)
plt.title("light_palette('blue')")
plt.show()

sns.palplot(dark_reds)
plt.title("dark_palette('red')")
plt.show()

# Heatmap example: values above/below 0 split around a neutral center.
data = np.random.normal(0, 1, (6, 12))
sns.heatmap(
    data,
    cmap=sns.diverging_palette(220, 20, as_cmap=True),
    center=0,
    vmin=-3,
    vmax=3,
)
plt.title("Heatmap with diverging palette (centered at 0)")
plt.show()

# Dark background version: neutral values should not look bright.
plt.style.use("dark_background")
dark_center = sns.diverging_palette(250, 0, center="dark", as_cmap=True)
sns.heatmap(data, cmap=dark_center, center=0, vmin=-3, vmax=3)
plt.title("Diverging palette with dark center (dark background)")
plt.show()
plt.style.use("default")

# Bar chart with values above/below zero.
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
# axhline adds a visual baseline at y=0.
plt.axhline(0, color="gray", linewidth=1)
plt.title("Diverging palette for values around 0")
plt.show()

# Compare palette choices on light vs dark backgrounds.
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
