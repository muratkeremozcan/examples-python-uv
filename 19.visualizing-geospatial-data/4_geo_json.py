import tempfile
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import MultiPolygon, Polygon

# Key takeaways (GeoJSON):
# - GeoJSON is one file, so it is easier to move/share than shapefile bundles.
# - geopandas.read_file(...) loads GeoJSON into a GeoDataFrame.
# - Use qualitative colormaps (like Set2) for non-numeric categories.
# - legend_kwds lets you position/style the legend for cleaner layouts.

# Build a tiny neighborhood-like GeoDataFrame.
neighborhoods = gpd.GeoDataFrame(
    {
        "name": ["Downtown", "Midtown", "East Side"],
        "group": ["core", "core", "residential"],
        "district": ["D1", "D2", "D3"],
    },
    geometry=[
        Polygon(
            [
                (-86.81, 36.15),
                (-86.77, 36.15),
                (-86.77, 36.18),
                (-86.81, 36.18),
                (-86.81, 36.15),
            ]
        ),
        # MultiPolygon example: one neighborhood made of two disconnected pieces.
        MultiPolygon(
            [
                Polygon(
                    [
                        (-86.77, 36.16),
                        (-86.74, 36.16),
                        (-86.74, 36.18),
                        (-86.77, 36.18),
                        (-86.77, 36.16),
                    ]
                ),
                Polygon(
                    [
                        (-86.76, 36.14),
                        (-86.75, 36.14),
                        (-86.75, 36.15),
                        (-86.76, 36.15),
                        (-86.76, 36.14),
                    ]
                ),
            ]
        ),
        Polygon(
            [
                (-86.74, 36.14),
                (-86.70, 36.14),
                (-86.70, 36.18),
                (-86.74, 36.18),
                (-86.74, 36.14),
            ]
        ),
    ],
    crs="EPSG:4326",
)

# Write to a temp GeoJSON, then read it back (same flow as downloaded GeoJSON files).
with tempfile.TemporaryDirectory() as tmp_dir:
    geojson_path = Path(tmp_dir) / "neighborhoods_sample.geojson"
    neighborhoods.to_file(geojson_path, driver="GeoJSON")
    geo = gpd.read_file(geojson_path)

print(geo.head())
#        name        group district                                           geometry
# 0  Downtown         core       D1  POLYGON ((-86.81 36.15, -86.77 36.15, -86.77 3...
# ...

# 1) Color by a categorical column using a qualitative colormap.
ax1 = geo.plot(
    column="district", cmap="Set2", legend=True, edgecolor="black", alpha=0.6
)
ax1.set_title("GeoJSON plot colored by district (Set2)")
ax1.set_xlabel("Longitude")
ax1.set_ylabel("Latitude")
plt.show()

# 2) If you set cmap without column, regions still get colors, but not data-driven.
ax2 = geo.plot(cmap="Set2", edgecolor="black", alpha=0.6)
ax2.set_title("GeoJSON plot with cmap only (not tied to any column)")
ax2.set_xlabel("Longitude")
ax2.set_ylabel("Latitude")
plt.show()

# 3) Legend styling with legend_kwds.
# legend_kwds passes options to the legend:
# - bbox_to_anchor=(1.02, 1.0): move legend to the right of the plot.
# - ncol=1: keep legend entries in one vertical column.
# - title="Neighborhood": text shown at the top of the legend.
ax3 = geo.plot(
    column="name",
    cmap="Set2",
    legend=True,
    edgecolor="black",
    alpha=0.6,
    legend_kwds={"bbox_to_anchor": (1.02, 1.0), "ncol": 1, "title": "Neighborhood"},
)
ax3.set_title("Legend styling with legend_kwds")
ax3.set_xlabel("Longitude")
ax3.set_ylabel("Latitude")
plt.tight_layout()
plt.show()
