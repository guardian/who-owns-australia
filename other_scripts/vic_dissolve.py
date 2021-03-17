import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/Vic/"

gdf = gpd.read_file(f"{data_path}vic_pub_private.shp")

# gdf = gdf.dropna(subset=['geometry'])

# print(gdf['Ownership'].unique())

print(gdf)

dissolved = gdf.dissolve(by="Ownership")

print(dissolved)

dissolved.to_file(f"{data_path}vic_pp_dissolved.shp")