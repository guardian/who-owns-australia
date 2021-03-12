import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/SA/"
output_path = data_path + "cleaned_data/"

# layer = f"{data_path}LandUseGeneralised2019_shp/LandUseGeneralised2019_GDA2020.shp"
layer = f"{data_path}Estate_Types/estate_types.shp"

gdf = gpd.read_file(layer)


# Estate types: ['Fee Simple', 'Crown Lessee' 'Crown Land (Unalienated)', 'Crown Land (Alienated)']
# Source: https://www.landservices.com.au/support-materials-and-resources/glossary-of-property-terms
# Source: https://www.pir.sa.gov.au/primary_industry/pastoral_leases_in_sa

public = ["Crown Lessee", 'Crown Land (Unalienated)', 'Crown Land (Alienated)']
private = ["Fee Simple"]

gdf['Ownership'] = "Private"

for thing in public:
    gdf.loc[gdf['Estate_Typ'] == thing, "Ownership"] = "Public"

print(gdf)

# gdf = gdf[['Ownership', 'geometry']]

gdf.to_file(f"{output_path}sa_pub_private.shp")


# print(gdf.columns)