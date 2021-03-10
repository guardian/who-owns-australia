import geopandas as gpd 
from paths import data_path

data_path = data_path + "/Qld/"
output_path = data_path + "cleaned_data/"

private = ['Freehold']
public = ['Easement', 'Lands Lease', 'Reserve', 'National Park',
'State Land', 'State Forest', 'Profit à Prendre', 'Main Road', 'Forest Reserve',
 'Housing Land', 'Port and Harbours Boards', 'Railway' ,
'Commonwealth Acquisition', 'Mines Tenure', 'Water Resource',
'Timber Reserve', 'Industrial Estates', 'Boat Harbours']
leave_out = ["Covenant", 'Below the Depth Plans', 'Carbon Abatement Interest']
# Source: https://docs.google.com/spreadsheets/d/1mwOMKzcr957ZSrPr6qHyBhCOHzNXwtODs6BMNNs8XoU/edit#gid=0

data = f"{data_path}DP_QLD_DCDB_WOS_CUR.gdb"


gdf = gpd.read_file(data, layer = "QLD_CADASTRE_DCDB")

gdf = gdf.loc[~gdf['TENURE'].isin(leave_out)]

gdf.loc[gdf['TENURE'].isin(public), 'Ownership'] = "Public"
gdf.loc[gdf['TENURE'].isin(private), 'Ownership'] = "Private"

gdf = gdf[['geometry', 'Ownership']]

gdf.to_file(f"{output_path}qld_pub_priv.shp")