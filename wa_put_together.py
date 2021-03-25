import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/WA/"
output_path = data_path + "cleaned_data/"

data = f"{data_path}WA_Land_Tenure_2019/WA_Land_Tenure_2019.shp"

public = ['DBCA Legislated', 'DBCA Interest', 'DBCA Legislated_Ag_Area','DBCA Interest_Ag_Area',
'Reserve', 'Indigenous Reserve', 'Reserve_Ag_Area','VCL', 
'VCL_Ag_Area', 'State Government', 'DEC', 'Forest', 'DEC_Ag_Area', 'Commonwealth']
private = ['Freehold', 'Agricultural area']
other = ["Road", "Water"]
leases = ['Pastoral Lease', 'General and Special Lease']

gdf = gpd.read_file(data)
# gdf = gdf.dropna(subset=['geometry'])
gdf = gdf.to_crs("EPSG:4326")

# print("Read")

gdf.loc[gdf['Tenure_Cat'].isin(public), 'Ownership'] = "Public"
gdf.loc[gdf['Tenure_Cat'].isin(private), 'Ownership'] = "Private"
gdf.loc[gdf['Tenure_Cat'].isin(other), 'Ownership'] = "Other"
gdf.loc[gdf['Tenure_Cat'].isin(leases), 'Ownership'] = "Pastoral"

gdf.loc[gdf['Tenure_Cat'].isin(public), 'Control'] = "Public"
gdf.loc[gdf['Tenure_Cat'].isin(private), 'Control'] = "Private"
gdf.loc[gdf['Tenure_Cat'].isin(leases), 'Control'] = "Private"

gdf = gdf.loc[gdf['Ownership'] != "Other"]

# public = gdf.copy()
# # public = gdf.loc[gdf['Tenure_Cat'].isin(public)].copy()

# public['Ownership'] = "Public"
# public['Control'] = 'Public'
# public = public.dissolve(by="Ownership")

# private = gdf.loc[gdf['Tenure_Cat'].isin(private)].copy()
# private['Ownership'] = "Private"
# private['Control'] = "Private"

# pastoral = gdf.loc[gdf['Tenure_Cat'].isin(pastoral)].copy()
# pastoral['Ownership'] = "Pastoral"
# pastoral['Control'] = "Private"

# print("Assigned")

# gdf = gpd.overlay(public, private, how="difference")

# gdf = gdf.append(private)

# print("First difference")

# gdf = gpd.overlay(gdf, pastoral, how="difference")

# gdf = gdf.append(pastoral)

# print("Second difference")

gdf.to_file(f"{output_path}wa_pub_priv_past_two.shp")