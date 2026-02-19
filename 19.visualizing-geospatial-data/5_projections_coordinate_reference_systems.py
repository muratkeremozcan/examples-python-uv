import geopandas as gpd
import pandas as pd

# GeoDataFrame = pandas DataFrame + a real map column ("geometry") + map metadata coordinate reference systems (CRS).
# You care because that is what lets you plot maps, do spatial joins/overlays, and measure distances correctly.

# A GeoDataFrame needs geometry + coordinate reference systems (CRS).
# CRS tells geopandas how to interpret coordinates and units.
# EPSG:4326 uses lon/lat in degrees.
# EPSG:3857 uses projected x/y in meters (better for web maps and meter distances).

# Start with a normal DataFrame (lon/lat columns only).
schools = pd.DataFrame(
    {
        "school": ["North HS", "East HS", "West HS"],
        "Longitude": [-86.79, -86.73, -86.84],
        "Latitude": [36.17, 36.19, 36.15],
    }
)
print("DataFrame:")
print(schools)
print("Type:", type(schools))

# points_from_xy creates shapely Point geometry from x=lon, y=lat.
schools["geometry"] = gpd.points_from_xy(schools["Longitude"], schools["Latitude"])

# Build GeoDataFrame:
# - geometry: which column contains Point/Line/Polygon objects
# - crs="EPSG:4326": coordinates are lon/lat degrees (WGS84)
schools_geo = gpd.GeoDataFrame(schools, geometry="geometry", crs="EPSG:4326")
print("\nGeoDataFrame in EPSG:4326 (degrees):")
print(schools_geo.head())
print("Type:", type(schools_geo))

# Convert geometry to a projected CRS in meters.
# to_crs only transforms geometry values; original lon/lat columns stay unchanged.
schools_geo_3857 = schools_geo.to_crs(epsg=3857)
print("\nGeoDataFrame in EPSG:3857 (meters):")
print(schools_geo_3857[["school", "geometry"]].head())

# Side-by-side first point to show unit change.
print("\nFirst school geometry comparison:")
print("4326 geometry (degrees):", schools_geo.loc[0, "geometry"])
print("3857 geometry (meters):", schools_geo_3857.loc[0, "geometry"])
