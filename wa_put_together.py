import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/WA/"
output_path = data_path + "cleaned_data/"

data = f"{data_path}WA_Land_Tenure_2019/WA_Land_Tenure_2019.shp"

public = ['DBCA Legislated', 'DBCA Interest', 'DBCA Legislated_Ag_Area','DBCA Interest_Ag_Area',
'Reserve', 'Indigenous Reserve', 'Reserve_Ag_Area','VCL', 'General and Special Lease',
 'VCL_Ag_Area', 'Pastoral Lease','State Government', 'DEC', 'Forest', 'DEC_Ag_Area', 'Commonwealth', 'Agricultural area']
private = ['Freehold']
other = ["Road", "Water"]

gdf = gpd.read_file(data)

gdf.loc[gdf['Tenure_Cat'].isin(public), 'Ownership'] = "Public"
gdf.loc[gdf['Tenure_Cat'].isin(private), 'Ownership'] = "Private"
gdf.loc[gdf['Tenure_Cat'].isin(other), 'Ownership'] = "Other"

# gdf = gdf[['geometry', 'Ownership']]

gdf.to_file(f"{output_path}wa_pub_priv.shp")