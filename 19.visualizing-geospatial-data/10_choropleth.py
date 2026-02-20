import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Polygon

# Layman core idea:
# - Raw count = "how many total".
# - Density = "how concentrated per area".
# - Choropleth should usually color by density, not raw count.

# 1) Region polygons (council districts).
# Why: a choropleth colors regions, so we need region geometry first.
council_districts = gpd.GeoDataFrame(
    {"district": ["D1", "D2", "D3"]},
    geometry=[
        Polygon(
            [
                (-86.82, 36.12),
                (-86.76, 36.12),
                (-86.76, 36.20),
                (-86.82, 36.20),
                (-86.82, 36.12),
            ]
        ),
        Polygon(
            [
                (-86.76, 36.12),
                (-86.70, 36.12),
                (-86.70, 36.18),
                (-86.76, 36.18),
                (-86.76, 36.12),
            ]
        ),
        Polygon(
            [
                (-86.76, 36.18),
                (-86.68, 36.18),
                (-86.68, 36.25),
                (-86.76, 36.25),
                (-86.76, 36.18),
            ]
        ),
    ],
    crs="EPSG:4326",
)

# 2) Compute district area in square kilometers.
# Why: we need area to normalize counts into fair density.
council_districts = council_districts.to_crs(epsg=3857)  # meter-based CRS
sqm_to_sqkm = 10**6
council_districts["area"] = council_districts.area / sqm_to_sqkm
council_districts = council_districts.to_crs(epsg=4326)  # back to lon/lat for plotting

# 3) Point events (building permits).
# Why: these are the events we summarize by district.
permits = pd.DataFrame(
    {
        "permit_id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "lng": [-86.80, -86.79, -86.77, -86.74, -86.73, -86.72, -86.71, -86.75, -86.69],
        "lat": [36.14, 36.18, 36.13, 36.13, 36.15, 36.17, 36.19, 36.22, 36.23],
    }
)
permits["geometry"] = gpd.points_from_xy(permits.lng, permits.lat)
permits_geo = gpd.GeoDataFrame(
    permits, crs=council_districts.crs, geometry=permits.geometry
)

# 4) Spatially join permits to districts.
# Why: this adds a district label to each permit point.
permits_by_district = gpd.sjoin(permits_geo, council_districts, predicate="within")

# 5) Count permits per district.
# Why: choropleth needs one numeric value per region.
permit_counts = permits_by_district.groupby("district").size()
counts_df = permit_counts.to_frame().reset_index()  # Series -> 2-column DataFrame
counts_df.columns = ["district", "bldg_permits"]

# 6) Merge counts into district polygons.
# Why: geometry + metric must be in one GeoDataFrame before plotting.
districts_and_permits = council_districts.merge(counts_df, on="district", how="left")
districts_and_permits["bldg_permits"] = districts_and_permits["bldg_permits"].fillna(0)

# 7) Normalize counts by area.
# Why: big districts should not look important just because they are large.
districts_and_permits["permit_density"] = districts_and_permits.apply(
    lambda row: row.bldg_permits / row.area, axis=1
)

print(type(districts_and_permits))
print(districts_and_permits[["district", "bldg_permits", "area", "permit_density"]])

# 8) Polished choropleth (exercise-style).
# Why: this is the final communication view.
districts_and_permits.plot(
    column="permit_density",
    cmap="BuGn",
    edgecolor="black",
    legend=True,
)
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.xticks(rotation="vertical")
plt.title("2017 Building Project Density by Council District")
plt.show()
