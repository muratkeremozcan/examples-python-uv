import geopandas as gpd
from shapely.geometry import Point, Polygon

# Layman mental model:
# - area     -> "how big is this region?"
# - centroid -> "what is its center point?"
# - distance -> "how far is it from X?"
# Use a meter-based CRS first, otherwise numbers are in degrees.

districts = gpd.GeoDataFrame(
    {"district": ["D1", "D2", "D3"]},
    geometry=[
        Polygon(
            [
                (-86.85, 36.10),
                (-86.78, 36.10),
                (-86.78, 36.18),
                (-86.85, 36.18),
                (-86.85, 36.10),
            ]
        ),
        Polygon(
            [
                (-86.78, 36.10),
                (-86.70, 36.10),
                (-86.70, 36.18),
                (-86.78, 36.18),
                (-86.78, 36.10),
            ]
        ),
        Polygon(
            [
                (-86.80, 36.18),
                (-86.72, 36.18),
                (-86.72, 36.24),
                (-86.80, 36.24),
                (-86.80, 36.18),
            ]
        ),
    ],
    crs="EPSG:4326",
)

# Convert once to a CRS with meter units.
districts_m = districts.to_crs(epsg=3857)

# 1) area in square kilometers.
m2_to_km2 = 1_000_000
area_km2 = (districts_m.geometry.area / m2_to_km2).round(2)

# 2) centroid (center point) of each district.
centers_m = districts_m.geometry.centroid
centers_lonlat = gpd.GeoSeries(centers_m, crs="EPSG:3857").to_crs(epsg=4326)

# 3) distance from each district to a downtown reference point.
downtown = (
    gpd.GeoSeries([Point(-86.775, 36.165)], crs="EPSG:4326").to_crs(epsg=3857).iloc[0]
)
distance_km = (districts_m.geometry.distance(downtown) / 1000).round(2)

print("Area (km^2) by district:")
print(area_km2)

print("\nCentroid (lon/lat) by district:")
print(centers_lonlat)

print("\nDistance from each district to downtown (km):")
print(distance_km)
