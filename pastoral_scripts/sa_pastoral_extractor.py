import geopandas as gpd 
import pandas as pd 
from paths import data_path

data_path = data_path + "/SA/"
output_path = data_path + "cleaned_data/"

admin = f"{data_path}ADMIN_PastoralStations/ADMIN_PastoralStations.shp"
leases = f"{data_path}Pastoral_Leases/Pastoral_Leases.shp"

admin = gpd.read_file(admin)
admin = admin.to_crs("EPSG:4326")

leases = gpd.read_file(leases)
leases = leases.to_crs("EPSG:4326")

difference = gpd.overlay(leases, admin, how="difference")

combo = difference.append(admin)

exclude = ['OTHER', 'NPWSA']

combo = combo.loc[~combo['PROPERTYTY'].isin(exclude)]

combo.to_file(f"{output_path}sa_pastoral.shp")