import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/NSW/"
output_path = data_path + "cleaned_data/"

data = f"{data_path}STATE_cadastral_2020-08-01.gdb"

gdf = gpd.read_file(data, layer="Lot")
gdf2 = gpd.read_file(data, layer="NPWSReserve")
gdf3 = gpd.read_file(data, layer="StateForest")

private = ['FREEHOLD']
unknown = ['UNKNOWN']
public = ['CROWN', "LOCAL GOVERNMENT AUTHORITY", "SHARED CROWN / COUNCIL", "NSW GOVERNMENT", "AUSTRALIAN GOVERNEMENT"]

gdf.loc[gdf['controllingauthorityoid'].isin(public), 'Ownership'] = "Public"
gdf.loc[gdf['controllingauthorityoid'].isin(private), 'Ownership'] = "Private"
gdf.loc[gdf['controllingauthorityoid'].isin(unknown), 'Ownership'] = "Unknown"

gdf2['Ownership'] = "Public"
gdf3['Ownership'] = "Public"

gdf = gpd.overlay(gdf, gdf2, how="difference")

gdf = gdf.append(gdf2)

gdf = gpd.overlay(gdf, gdf3, how="difference")

gdf = gdf.append(gdf3)

# gdf = gdf[['geometry', 'Ownership']]

gdf.to_file(f"{output_path}nsw_pub_priv.shp")





# ### CLASSIFYING CADASTRIAL TENURE TYPES BASED ON DATA DICTIONARY AND TALKING TO JOEL

# private_land_classification = ['FREEHOLD' ]
# public_land_classification = ['CROWN', 'UNKNOWN', 'LOCAL GOVERNMENT AUTHORITY', 'SHARED CROWN / COUNCIL', 'NSW GOVERNMENT', 'AUSTRALIAN GOVERNEMENT']

# def sort_nsw_map(dataframe, public_listo, private_listo, output_string):
#     dataframe['Ownership'] = "Public"
#     for typ in private_listo:
#         dataframe.loc[dataframe['controllingauthorityoid'] == typ, ['Ownership']] = "Private"
#     print(dataframe)
#     print(dataframe['Ownership'].unique())
#     # dataframe.to_file(output_string)
#     with open(output_string, 'w') as f:
#         dataframe.to_csv(f, header=True, index=False)


# sort_nsw_map(df, public_land_classification, private_land_classification, '/Users/josh_nicholas/WOA/NSW/Final_putting_together/200819NSW_PrivatePublic.csv')

