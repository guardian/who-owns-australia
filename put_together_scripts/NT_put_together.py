import geopandas as gpd
from paths import data_path

data_path = data_path + "/NT/"
output_path = data_path + "cleaned_data/"

half_cad = f"{data_path}/NT_LandTenureData/Cadastre_Excluding_Freehold_and_VCL.shp"
indig = f"{data_path}/NT_LandTenureData/NT_Aboriginal_Land_Trusts.shp"

gdf = gpd.read_file(half_cad)
gdf = gdf.to_crs("EPSG:4326")

gdf['Ownership'] = "Public"
gdf.loc[gdf['TEN_DESC'] == 'Perpetual Pastoral Lease', "Ownership"] = "Pastoral"
gdf.loc[gdf['TEN_DESC'] == 'Pastoral Lease', "Ownership"] = "Pastoral"
gdf['Control'] = "Public"
gdf.loc[gdf['TEN_DESC'] == 'Perpetual Pastoral Lease', "Control"] = "Private"
gdf.loc[gdf['TEN_DESC'] == 'Pastoral Lease', "Control"] = "Private"

gdf = gdf.dissolve(by="Ownership")

# public = gdf.copy()
# public['Ownership'] = "Public"
# public['Control'] = 'Public'
# # public = public.dissolve(by="Ownership")

# pastoral_list = ['Perpetual Pastoral Lease', 'Pastoral Lease']
# pastoral = gdf.loc[gdf['TEN_DESC'].isin(pastoral_list)].copy()
# pastoral['Ownership'] = 'Pastoral'
# pastoral['Control'] = "Private"

# print("Assigned")

# gdf = gpd.overlay(public, pastoral, how="difference")

# gdf = gdf.append(pastoral)

# print("First difference")

# ## gdf = gdf.loc[gdf['geometry'].geom_type == 'LineString']

gdf.to_file(f"{output_path}nt_pub_past_dissolved.shp")

# ind = gpd.read_file(indig)
# ind = ind.to_crs("EPSG:4326")

# ind['Ownership'] = "Indigenous"
# ind['Control'] = "Indigenous"

# print("Second one read")


# difference = gpd.overlay(ind, gdf, how="difference")
# combo = difference.append(gdf)

# print("Differenced")

# combo.to_file(f"{output_path}nt_pub_past.shp")

# gdf = gdf.loc[gdf['geometry'].geom_type != 'LineString']

# gdf.to_file(f"{output_path}nt_pub_past.shp")