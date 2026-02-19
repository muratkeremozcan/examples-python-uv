import geopandas as gpd
from shapely.geometry import Polygon

# Layman mental model:
# - Normal join: "match by ID/text".
# - Spatial join: "match by where shapes are on the map".
# - within / contains / intersects are the 3 core checks.

# School districts (big polygons).
school_districts = gpd.GeoDataFrame(
    {"school_district": ["S1", "S2"]},
    geometry=[
        Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]),
        Polygon([(10, 0), (20, 0), (20, 10), (10, 10), (10, 0)]),
    ],
    crs="EPSG:4326",
)

# Council districts (smaller polygons).
council_districts = gpd.GeoDataFrame(
    {"council_district": ["C1", "C2", "C3"]},
    geometry=[
        Polygon([(1, 1), (4, 1), (4, 4), (1, 4), (1, 1)]),  # fully inside S1
        Polygon([(8, 2), (12, 2), (12, 6), (8, 6), (8, 2)]),  # overlaps S1 and S2
        Polygon([(13, 2), (18, 2), (18, 8), (13, 8), (13, 2)]),  # fully inside S2
    ],
    crs="EPSG:4326",
)

# 1) Council polygons fully inside school polygons.
within_gdf = gpd.sjoin(council_districts, school_districts, predicate="within")

# 2) Any overlap/touch.
intersects_gdf = gpd.sjoin(council_districts, school_districts, predicate="intersects")

# 3) Same relationship as "within", just reversed order.
contains_gdf = gpd.sjoin(school_districts, council_districts, predicate="contains")

print("Counts:")
print("within    ->", len(within_gdf))
print("intersects->", len(intersects_gdf))
print("contains  ->", len(contains_gdf))

print("\nwithin pairs (left council, right school):")
print(within_gdf[["council_district", "school_district"]])

print("\nintersects pairs (C2 appears twice because it touches two school districts):")
print(intersects_gdf[["council_district", "school_district"]])

# Quick aggregation: how many council districts are fully inside each school district?
summary = (
    within_gdf.groupby("school_district", as_index=False)
    .agg(council_count=("council_district", "count"))
    .sort_values("council_count", ascending=False)
)
print("\nCouncil districts fully inside each school district:")
print(summary)
