from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon

# Key message:
# - Build folium location as [latitude, longitude].
# - Create folium.Map(...), then add polygon with folium.GeoJson(...).add_to(...).

urban_polygon = gpd.GeoDataFrame(
    {"name": ["Urban Residents"]},
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
)

# Create a center column (project first so center math is more reliable).
urban_polygon["center"] = urban_polygon.to_crs(epsg=3857).geometry.centroid.to_crs(
    epsg=4326
)

print(urban_polygon.head())

urban_center = urban_polygon["center"].iloc[0]
print("urban_center:", urban_center)

urban_location = [urban_center.y, urban_center.x]
print("urban_location:", urban_location)

# Keep this alias name so it matches DataCamp examples.
nashville = urban_location

downtown_map = folium.Map(location=nashville, zoom_start=15)

# Make polygon styling explicit so the overlay is easy to see.
folium.GeoJson(
    urban_polygon[["name", "geometry"]].__geo_interface__,
    style_function=lambda _: {
        "color": "red",
        "weight": 4,
        "fillColor": "red",
        "fillOpacity": 0.15,
    },
).add_to(downtown_map)

# Add the computed center as a marker for quick visual confirmation.
folium.Marker(location=nashville, popup="Urban center").add_to(downtown_map)

# optional:Fit map bounds to polygon so overlay is always in view.
# minx, miny, maxx, maxy = urban_polygon.total_bounds
# downtown_map.fit_bounds([[miny, minx], [maxy, maxx]])

# Sample public art points for marker + popup demo.
urban_art = pd.DataFrame(
    {
        "title": ["Sun Wall", 'River "Arc"', "Steel Loop"],
        "lat": [36.155, 36.182, 36.140],
        "lng": [-86.800, -86.772, -86.755],
    }
)

# DataCamp-style loop: build location + popup, then add marker each iteration.
for row in urban_art.iterrows():
    row_values = row[1]
    location = [row_values["lat"], row_values["lng"]]  # folium: [lat, lon]
    popup = str(row_values["title"]).replace('"', "")
    marker = folium.Marker(location=location, popup=popup)
    marker.add_to(downtown_map)

# In scripts, save to HTML and open in browser.
out_path = Path("19.visualizing-geospatial-data/folium_downtown_map.html")
downtown_map.save(out_path)
print("Saved:", out_path)
