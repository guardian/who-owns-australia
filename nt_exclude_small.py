import geopandas as gpd 
from paths import data_path

fillo = f"{data_path}/final-ish/nt-diff-multi.shp"

gdf = gpd.read_file(fillo)
gdf = gdf.to_crs("EPSG:4326")


gdf = gdf[['name', 'name_alt', 'name_local','latitude', 'longitude', 'geometry']]

gdf['area'] = gdf['geometry'].area

# gdf.to_file(f"{data_path}/final-ish/nt-diff-multi-area-included.shp")

# print(gdf)

sorted = gdf.sort_values(by="area", ascending=False)
print(sorted)