import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/WA/"
output_path = data_path + "cleaned_data/"

data = f"{data_path}WA_Land_Tenure_2019/WA_Land_Tenure_2019.shp"

public = ['DBCA Legislated', 'DBCA Interest', 'DBCA Legislated_Ag_Area','DBCA Interest_Ag_Area',
'Reserve', 'Indigenous Reserve', 'Reserve_Ag_Area','VCL', 'General and Special Lease',
 'VCL_Ag_Area', 'State Government', 'DEC', 'Forest', 'DEC_Ag_Area', 'Commonwealth', 'Agricultural area']
private = ['Freehold']
other = ["Road", "Water"]
pastoral = ['Pastoral Lease']

gdf = gpd.read_file(data)

print("Read")

gdf.loc[gdf['Tenure_Cat'].isin(public), 'Ownership'] = "Public"
gdf.loc[gdf['Tenure_Cat'].isin(private), 'Ownership'] = "Private"
gdf.loc[gdf['Tenure_Cat'].isin(other), 'Ownership'] = "Other"
gdf.loc[gdf['Tenure_Cat'].isin(pastoral), 'Ownership'] = "Pastoral"


gdf.loc[gdf['Tenure_Cat'].isin(public), 'Control'] = "Public"
gdf.loc[gdf['Tenure_Cat'].isin(private), 'Control'] = "Private"
gdf.loc[gdf['Tenure_Cat'].isin(pastoral), 'Control'] = "Private"

print("Assigned")

# gdf = gdf[['geometry', 'Ownership']]

gdf.to_file(f"{output_path}wa_pub_priv_past.shp")