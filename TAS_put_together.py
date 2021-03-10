import pandas as pd 
import geopandas as gpd 
from paths import data_path

data_path = data_path + "/Tas/"
output_path = data_path + "cleaned_data/"

land_tenure_shp = f'{data_path}LIST_LAND_TENURE_STATEWIDE/list_land_tenure_statewide.shp'
authority_shp = f'{data_path}JNichols_Authority_Land/cadastre_authority_detail.shp'

## FIRST ROUND

### LOAD AND FILTER AUTHORITY DATASET TO EXTRACT ABORIGINAL LANDS SHAPEFILE

# authority_gdf = gpd.read_file(authority_shp)
# aboriginal_gdf = authority_gdf[authority_gdf['AUTH_TYPE']=='Aboriginal Land']
# aboriginal_gdf['Ownership'] = "Aboriginal"

# aboriginal_gdf.to_file(f'{data_path}/aboriginal_land/200819TasAboriginalLand.shp')


### LOAD AND CLASSIFY LAND TENURE DATA

# land_tenure_gdf = gpd.read_file(land_tenure_shp)

def sort_tas_map(dataframe, public_listo, private_listo, other_listo, output_string):
    dataframe['Ownership'] = "Public"
    for typ in private_listo:
        dataframe.loc[dataframe['TEN_CLASS'] == typ, ['Ownership']] = "Private"
    for typ in other_listo:
        dataframe.loc[dataframe['TEN_CLASS'] == typ, ['Ownership']] = "Other"
    # print(dataframe)
    print(dataframe['Ownership'].unique())
    dataframe.to_file(output_string)


# ### THE FOLLOWING ARE BRAKDOWNS FOR CLASSIFICATION
# public_land_classification = ['Conservation Area','Game Reserve', 'Historic Site', 'National Park', 'Nature Recreation Area', 'Nature Reserve', 'Regional Reserve', 'State Reserve', 'Public Reserve', 'Permanent Timber Production Zone Land']
# # https://listdata.thelist.tas.gov.au/public/LIST_Public_Land_Classification_information.pdf

# private_land_classification = ['Private Sanctuary', 'Private Nature Reserve', 'Conservation Covenant', 'Private Freehold']
# # https://listdata.thelist.tas.gov.au/public/LIST_Private_Reserves_information.pdf

# other_gov = ['Wellington Park', 'Crown Land','Casement','Tas Irrigation','Commonwealth','Tas Water','Future Potential Production Forest (Crown)', 'Future Potential Production Forest (HEC)','Authority Crown' ,'Authority Freehold','Local Government Act Reserve','Hydro-Electric Corporation','Local Government','HEC Conservation Area','LGA Conservation Area']

# other_places = ['Inland Water']

# public_land_classification = public_land_classification + other_gov

# # sort_tas_map(land_tenure_gdf, public_land_classification, private_land_classification, other_places, f'{data_path}public_private/TasPublicPrivateLand.shp')

## SECOND ROUND

#### Combine Aboriginal and Private/Public

priv_pub = gpd.read_file(f'{data_path}public_private/TasPublicPrivateLand.shp')

priv_pub = priv_pub[['geometry', 'Ownership']]

aboriginal_gdf = gpd.read_file(f'{data_path}/aboriginal_land/200819TasAboriginalLand.shp')

aboriginal_gdf = aboriginal_gdf[['geometry', 'Ownership']]


## CUT OUT THE OVERLAP

# dissolved = priv_pub.dissolve(by="Ownership", aggfunc="last")

## APPEND THE ABORIGINAL DATASET

difference = gpd.overlay(priv_pub, aboriginal_gdf, how="difference")

appended = difference.append(aboriginal_gdf)

appended.to_file(f'{output_path}tas_piv_pub_ab.shp')

print(appended)




# Join the two datasets

# overlayed = gpd.overlay(priv_pub, aboriginal_gdf, how="union")

# print(overlayed)

# joined = gpd.sjoin(priv_pub, aboriginal_gdf, how="left")

# joined.loc[joined['Ownership_right'] == "Aboriginal", 'Ownership_left'] = "Aboriginal"

# joined = joined[["geometry","Ownership_left"]]

# print(joined["Ownership_left"].unique)

# print(joined.loc[joined["Ownership_left"] == "Aboriginal"])

# Output

# joined.to_file(f'{data_path}tas_piv_pub_ab.shp')

