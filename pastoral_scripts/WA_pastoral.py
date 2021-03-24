import geopandas as gpd 
import pandas as pd 
from paths import data_path
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
# pd.set_option("display.max_rows", None, "display.max_columns", None)

# CSV of pastoral properties/owners extracted from the article last year, as well as Josh research
confirmed_pastoral_list = f"{data_path}/Extracted_pastoral.csv"

# CSV of WA Pastoral properties/ owners scraped from the WA Brand Registry
wa_brand_scraped = f"{data_path}/WA/WA_second_extraction.csv"

# List of Pastoral properties extracted from Cadastrial, including areas
previous = f"{data_path}/WA/WApastoral.csv"

# Pub/Private shape file
wa_shp = f"{data_path}/WA/cleaned_data/wa_pub_priv.shp"


## WORK OUT LARGEST FARM OWNERS

con_df = pd.read_csv(confirmed_pastoral_list)
con_df = con_df.loc[con_df['State'] == "WA"]
con_df = con_df[['Name', 'Owner (Josh)', 'Source']]
con_df['Name'] = con_df['Name'].str.title()

bran_df = pd.read_csv(wa_brand_scraped)
bran_df['Station'] = bran_df['Station'].str.title()
bran_df = bran_df.drop_duplicates(subset="Station", keep="last")
bran_df.rename(columns={"Owner":"Brands owner"}, inplace=True)

wa_off = pd.read_csv(previous)
wa_off['property_n'] = wa_off['property_n'].str.title()

wa_uniques = wa_off['property_n'].unique()
print(f"WA Pastoral CSV unique propertiess: {wa_uniques.size}")

def fuzzy_merge(df_1, df_2, key1, key2, threshold=90, limit=2):
    """
    :param df_1: the left table to join
    :param df_2: the right table to join
    :param key1: key column of the left table
    :param key2: key column of the right table
    :param threshold: how close the matches should be to return a match, based on Levenshtein distance
    :param limit: the amount of matches that will get returned, these are sorted high to low
    :return: dataframe with boths keys and matches
    """
    s = df_2[key2].tolist()
    
    m = df_1[key1].apply(lambda x: process.extract(x, s, limit=limit))    
    df_1['matches'] = m
    
    m2 = df_1['matches'].apply(lambda x: ', '.join([i[0] for i in x if i[1] >= threshold]))
    df_1['matches'] = m2
    
    return df_1

# first_match = fuzzy_merge(wa_off, bran_df, "property_n", "Station")

# first_match = pd.merge(first_match, bran_df, left_on="matches", right_on="Station", how="left")
# first_match.drop(columns=['property_t', "matches", "Station"], inplace=True)

# fuzzied = fuzzy_merge(first_match, con_df, "property_n", "Name")

# merged = pd.merge(fuzzied, con_df, left_on="matches", right_on="Name", how="left")
# merged = merged[['property_n', 'Shape_Area', 'Brands owner', 'Owner (Josh)', 'Source']]

# grouped = merged.groupby(by=['Brands owner'])['Shape_Area'].sum().reset_index()

# sortie = grouped.sort_values(by = 'Shape_Area', ascending=False)

# sortie['Shape_Area'] = sortie['Shape_Area'].apply(lambda x: '%.5f' % x)

# print(sortie.head(10))





#### JOIN PASTORAL PROPERTIES TO SPATIAL





gdf = gpd.read_file(wa_shp)

gdf = gdf.loc[gdf['Tenure_Cat'] == 'Pastoral Lease']
uniques = gdf['PROPERTY_N'].unique()
print(f"Unique property leases: {uniques.size}")

event_props = wa_uniques.tolist()
shape_props = uniques.tolist()

event_props = [x.lower() for x in event_props]
shape_props = [x.lower() for x in shape_props]

combined = [x for x in shape_props if x in event_props]

print(combined)
print(f"Combined length: {len(combined)}")

# df = 

# merged = gdf.merge()

# print(gdf)

# print(gdf['PROPERTY_N'].unique())
# print(gdf['Tenure_Cat'].unique())

# print(gdf['ID2'].unique())

# print(f"oid_1: {gdf.loc[gdf['ID2'] == 1903695]}")
# print(f"property_i: {gdf.loc[gdf['ID2'] == 1493780]}")


# ['DBCA Legislated' 'DBCA Interest' 'DBCA Legislated_Ag_Area'
#  'DBCA Interest_Ag_Area' 'Reserve' 'Indigenous Reserve' 'Reserve_Ag_Area'
#  'VCL' 'General and Special Lease' 'VCL_Ag_Area' 'Pastoral Lease'
#  'State Government' 'Agricultural area' 'Commonwealth' 'Water' 'Freehold'
#  'Road' 'DEC' 'Forest' 'DEC_Ag_Area' None]

# con_df = pd.read_csv(confirmed_pastoral_list)
# con_df = con_df[['Name', 'State', 'Owner (WT)', 'WT Source', 'Owner (Josh)', 'Source']]

# brands_df = pd.read_csv(wa_brand_scraped)
# brands_df.rename(columns={"Owner": "Brand_owner"}, inplace=True)

# off_df = pd.read_csv(wa_official)