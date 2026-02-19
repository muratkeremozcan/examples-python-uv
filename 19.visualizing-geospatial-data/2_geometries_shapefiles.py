import matplotlib.pyplot as plt

try:
    import geopandas as gpd
    from shapely.geometry import Point, Polygon
except ModuleNotFoundError:
    print(
        "This lesson needs geopandas + shapely. Install with:\n"
        "uv add geopandas shapely pyproj fiona"
    )
    raise SystemExit(0)

# Key takeaways (geometries + shapefiles):
# - Shapefiles store geometry so regions/lines/points can be mapped.
# - .shp is the geometry file, and it must live with matching .shx + .dbf files.
# - geopandas.read_file(...) loads shapefiles into a GeoDataFrame.
# - GeoDataFrame supports familiar pandas-like access (head, loc, iloc, plot).

# How you'd read a real shapefile:
# service_districts = gpd.read_file("data/service_districts/service_districts.shp")
# print(service_districts.head())

# Reproducible demo GeoDataFrame with two polygons (districts).
urban_poly = Polygon(
    [
        (-86.82, 36.13),
        (-86.74, 36.13),
        (-86.74, 36.20),
        (-86.82, 36.20),
        (-86.82, 36.13),
    ]
)
general_poly = Polygon(
    [
        (-86.90, 36.08),
        (-86.66, 36.08),
        (-86.66, 36.27),
        (-86.90, 36.27),
        (-86.90, 36.08),
    ]
)

service_districts = gpd.GeoDataFrame(
    {
        "district": ["Urban Services District", "General Services District"],
        "tax_level": ["higher", "lower"],
    },
    geometry=[urban_poly, general_poly],
    crs="EPSG:4326",
)

print(service_districts.head())

# Inspect one geometry with loc/iloc (same result, different access style).
geom_loc = service_districts.loc[0, "geometry"]
geom_iloc = service_districts.iloc[0, service_districts.columns.get_loc("geometry")]
print("\nGeometry via loc:")
print(geom_loc)
print("\nGeometry via iloc:")
print(geom_iloc)

# Plot GeoDataFrame and color polygons by a column.
ax = service_districts.plot(
    column="district",
    legend=True,
    edgecolor="black",
    alpha=0.35,
    figsize=(7, 5),
)

# Add sample point geometries for context.
chicken_points = gpd.GeoDataFrame(
    {"permit_id": [101, 102, 103]},
    geometry=[
        Point(-86.78, 36.16),
        Point(-86.76, 36.18),
        Point(-86.80, 36.15),
    ],
    crs="EPSG:4326",
)
chicken_points.plot(ax=ax, color="orangered", markersize=28, label="Chicken permits")

ax.set_title("District polygons with point data")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.show()
