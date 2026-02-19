from pprint import pprint

import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon

# Layman workflow used in the exercises:
# 1) Pick one neighborhood polygon.
# 2) Find its center point.
# 3) Keep only points inside that neighborhood.
# 4) Measure distance from each point to the center.

# One neighborhood polygon.
urban_residents = gpd.GeoDataFrame(
    {"neighborhood": ["Urban Residents"]},
    geometry=[
        Polygon(
            [
                (-86.82, 36.12),
                (-86.74, 36.12),
                (-86.74, 36.20),
                (-86.82, 36.20),
                (-86.82, 36.12),
            ]
        )
    ],
    crs="EPSG:4326",
).to_crs(epsg=3857)

center_point = urban_residents.geometry.centroid.iloc[0]

# "Art" points: 3 inside, 1 outside.
art = pd.DataFrame(
    {
        "title": ["Sun Wall", "River Arc", "Steel Loop", "Far Mural"],
        "lon": [-86.80, -86.78, -86.76, -86.70],
        "lat": [36.15, 36.18, 36.13, 36.16],
    }
)

# Build GeoDataFrame in degrees, then convert to meters.
art_dist_meters = gpd.GeoDataFrame(
    art, geometry=gpd.points_from_xy(art["lon"], art["lat"]), crs="epsg:4326"
).to_crs(epsg=3857)

# Keep only art points that are inside the neighborhood.
art_inside = gpd.sjoin(
    art_dist_meters, urban_residents[["neighborhood", "geometry"]], predicate="within"
).copy()

# Add same center point to every row (same pattern as DataCamp exercise).
art_inside["center"] = center_point

# Build title -> distance_in_meters dictionary.
art_distances = {}
for _, row in art_inside.iterrows():
    art_distances[row["title"]] = round(row["geometry"].distance(row["center"]), 1)

print("Art points inside neighborhood:", art_inside.shape[0])
print("Distances to neighborhood center (meters):")
pprint(art_distances)
