import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/WA/"
output_path = data_path + "cleaned_data/"

data = f"{data_path}WA_Land_Tenure_2019/WA_Land_Tenure_2019.shp"

pastoral = ['Pastoral Lease']

gdf = gpd.read_file(data)

print("read")

gdf = gdf.loc[gdf['Tenure_Cat'].isin(pastoral)]

print("cut down")

# gdf = gdf[['geometry', 'Ownership']]

print(gdf)

gdf.to_file(f"{output_path}wa_pastoral.shp")

# print("saved")