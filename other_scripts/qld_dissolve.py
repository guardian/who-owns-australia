import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/QLD/"

gdf = gpd.read_file(f"{data_path}qld_pub_priv.shp")

print(gdf)

dissolved = gdf.dissolve(by="Ownership")

print(dissolved)

dissolved.to_file(f"{data_path}qld_pp_dissolved.shp")