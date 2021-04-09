import geopandas as gpd
from paths import data_path

data_path = data_path + "/NT/"
output_path = data_path + "cleaned_data/"

half_cad = f"{data_path}/NT_LandTenureData/Cadastre_Excluding_Freehold_and_VCL.shp"
indig = f"{data_path}/NT_LandTenureData/NT_Aboriginal_Land_Trusts.shp"

gdf = gpd.read_file(half_cad)
gdf = gdf.to_crs("EPSG:4326")

print("Read")

leases = ['Perpetual Pastoral Lease', 'Pastoral Lease']

pastoral = gdf.loc[gdf['TEN_DESC'].isin(leases)]

print("Cut down")

pastoral.to_file(f"{output_path}nt_pastoral.shp")

print("Saved")

