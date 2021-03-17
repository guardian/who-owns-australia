import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/WA/"

gdf = gpd.read_file(f"{data_path}wa_pub_priv.shp")

gdf = gdf.dropna(subset=['geometry'])

print(gdf)

dissolved = gdf.dissolve(by="Ownership")

print(dissolved)

dissolved.to_file(f"{data_path}wa_pp_dissolved.shp")