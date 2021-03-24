import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/SA/"

gdf = gpd.read_file(f"{data_path}sa_pub_private.shp")

print(gdf)

dissolved = gdf.dissolve(by="Ownership")

print(dissolved)

dissolved.to_file(f"{data_path}sa_pp_dissolved.shp")