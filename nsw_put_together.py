import geopandas as gpd 
import pandas as pd
from paths import data_path

data_path = data_path + "/NSW/"
output_path = data_path + "cleaned_data/"

data = f"{data_path}DP_QLD_DCDB_WOS_CUR.gdb"

gdf = gpd.read_file(data, layer="Lot")

private = ["Freehold"]
public = ["Crown", "Unknown", "Local Government Authority", "Shared Crown/ Council", "NSW Government", "Australian Government"]

gdf.loc[gdf['controllingauthorityoid'].isin(public), 'Ownership'] = "Public"
gdf.loc[gdf['controllingauthorityoid'].isin(private), 'Ownership'] = "Private"

gdf = gdf[['geometry', 'Ownership']]

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

