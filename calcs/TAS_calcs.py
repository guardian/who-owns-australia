import pandas as pd 
import geopandas as gpd 
from paths import data_path

data_path = data_path + "/dissolved/"

gdf = gpd.read_file(f"{data_path}tas_piv_pub_past_dissolve.shp")
gdf = gdf.to_crs("EPSG:4326")

gdf['area'] = gdf['geometry'].area

print(gdf)

# print(data_path)

# gpd = gpd.read_file(f'{data_path}tas_piv_pub_ab.shp')

# print(gpd)

# gpd['area'] = gpd["geometry"].area

# grouped = gpd.dissolve(by='Ownership', aggfunc = "sum")

# print(grouped.crs)

# print(grouped.round())

# gpd.plot(column="Ownership")
