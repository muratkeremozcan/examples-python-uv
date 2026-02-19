import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from shapely.geometry import Point, Polygon

# Key takeaways (scatter + polygons):
# - A map is often built in layers.
# - Plot polygons first as the base context.
# - Then add location points on top.
# - This makes it easier to answer "where is this point relative to boundaries?"

# Two district polygons (simple sample geometry).
service_districts = gpd.GeoDataFrame(
    {"district": ["Urban Services District", "General Services District"]},
    geometry=[
        Polygon(
            [
                (-86.82, 36.13),
                (-86.74, 36.13),
                (-86.74, 36.20),
                (-86.82, 36.20),
                (-86.82, 36.13),
            ]
        ),
        Polygon(
            [
                (-86.90, 36.08),
                (-86.66, 36.08),
                (-86.66, 36.27),
                (-86.90, 36.27),
                (-86.90, 36.08),
            ]
        ),
    ],
    crs="EPSG:4326",
)

# Chicken permit points (longitude, latitude).
chickens = pd.DataFrame(
    {
        "permit_id": [201, 202, 203, 204, 205],
        "lon": [-86.79, -86.77, -86.75, -86.81, -86.71],
        "lat": [36.16, 36.18, 36.14, 36.19, 36.12],
    }
)

# 1) Points only (no boundaries yet).
sns.scatterplot(data=chickens, x="lon", y="lat", color="orangered", s=60)
plt.title("Chicken locations only")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(alpha=0.2)
plt.show()

# 2) District polygons only.
service_districts.plot(column="district", legend=True, alpha=0.35, edgecolor="black")
plt.title("Service district boundaries")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# 3) Final layered map: polygons first, then points.
ax = service_districts.plot(
    column="district",
    legend=True,
    alpha=0.35,
    edgecolor="black",
    figsize=(8, 6),
)

chicken_points = gpd.GeoDataFrame(
    chickens,
    geometry=[Point(xy) for xy in zip(chickens["lon"], chickens["lat"])],
    crs="EPSG:4326",
)
chicken_points.plot(ax=ax, color="orangered", markersize=35)

ax.set_title("Chicken locations by service district")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.show()
