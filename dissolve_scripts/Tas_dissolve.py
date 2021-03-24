import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/Tas/"

gdf = gpd.read_file(f"{data_path}TasPublicPrivateLand.shp")

print(gdf)

dissolved = gdf.dissolve(by="Ownership")

print(dissolved)

dissolved.to_file(f"{data_path}tas_pp_dissolved.shp")


#### Combine Aboriginal and Private/Public

# priv_pub = gpd.read_file(f'{data_path}public_private/TasPublicPrivateLand.shp')

# priv_pub = priv_pub[['geometry', 'Ownership']]

# aboriginal_gdf = gpd.read_file(f'{data_path}/aboriginal_land/200819TasAboriginalLand.shp')

# aboriginal_gdf = aboriginal_gdf[['geometry', 'Ownership']]


# ## CUT OUT THE OVERLAP

# # dissolved = priv_pub.dissolve(by="Ownership", aggfunc="last")

# ## APPEND THE ABORIGINAL DATASET

# difference = gpd.overlay(priv_pub, aboriginal_gdf, how="difference")

# appended = difference.append(aboriginal_gdf)

# appended.to_file(f'{output_path}tas_piv_pub_ab.shp')

# print(appended)