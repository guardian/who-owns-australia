import geopandas as gpd 
import pandas as pd
from paths import data_path


data_path = data_path + "/SA/"
output_path = data_path + "cleaned_data/"

# layer = f"{data_path}LandUseGeneralised2019_shp/LandUseGeneralised2019_GDA2020.shp"
layer = f"{data_path}Estate_Types/estate_types.shp"

admin_pastoral = f"{data_path}ADMIN_PastoralStations/ADMIN_PastoralStations.shp"

admin = gpd.read_file(admin_pastoral)
admin = admin.to_crs("EPSG:4326")
admin["Estate_Typ"] = "Pastoral"

land = gpd.read_file(layer)
land = land.to_crs("EPSG:4326")

difference = gpd.overlay(land, admin, how="difference")

combo = difference.append(admin)

# # Estate types: ['Fee Simple', 'Crown Lessee' 'Crown Land (Unalienated)', 'Crown Land (Alienated)']
# # Source: https://www.landservices.com.au/support-materials-and-resources/glossary-of-property-terms
# # Source: https://www.pir.sa.gov.au/primary_industry/pastoral_leases_in_sa

public = ["Crown Lessee", 'Crown Land (Unalienated)', 'Crown Land (Alienated)']
private = ["Fee Simple"]
pastoral = ['Pastoral']

combo['Ownership'] = "Public"
combo.loc[combo['Estate_Typ'].isin(private), 'Ownership'] = "Private"
combo.loc[combo['Estate_Typ'].isin(pastoral), 'Ownership'] = "Pastoral"

combo['Control'] = "Public"
combo.loc[combo['Estate_Typ'].isin(private), 'Control'] = "Private"
combo.loc[combo['Estate_Typ'].isin(pastoral), 'Control'] = "Private"

print(combo)

combo.to_file(f"{output_path}sa_pub_priv_past.shp")


# print(gdf.columns)