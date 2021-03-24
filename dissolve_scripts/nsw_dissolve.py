import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/NSW/"

gdf = gpd.read_file(f"{data_path}nsw_pub_priv.shp")

print("read")

dissolved = gdf.dissolve(by="Ownership")

print(dissolved)

dissolved.to_file(f"{data_path}nsw_pp_dissolved.shp")