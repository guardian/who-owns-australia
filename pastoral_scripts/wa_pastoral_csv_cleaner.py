import pandas as pd 
from paths import data_path
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
import geopandas as gpd 
# pd.set_option("display.max_rows", None, "display.max_columns", None)


def fuzzy_merge(df_1, df_2, key1, key2, threshold=90, limit=1):
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

# List of Pastoral properties extracted from Cadastrial, including areas
# wacv = f"{data_path}/WA/WA_second_extraction.csv"
# wa = pd.read_csv(wacv)
# # wa = wa[['property_n', 'Shape_Leng', 'Shape_Area']]
# wa['Owner'] = wa['Owner'].str.title()
# wa['Source'] = "WA brand directory"

# wa = wa.drop_duplicates(subset="Station", keep="last")


wa_pastoral = f"{data_path}/pastoral/wa_pastoral.shp"
gdf = gpd.read_file(wa_pastoral)
gdf = gdf.dropna(subset=["PROPERTY_N"])
gdf = gdf.loc[gdf['Pastoral_L'] != "Mining"]


# CSV of pastoral properties/owners extracted from the article last year, as well as Josh research
extracted_pastoral = f"{data_path}/Extracted_pastoral.csv"

# CSV of WA Pastoral properties/ owners scraped from the WA Brand Registry
wa_brand_scraped = f"{data_path}/WA/WA_second_extraction.csv"


extra = pd.read_csv(extracted_pastoral)
extra = extra.loc[extra['State'] == "WA"]
extra = extra[['Name', 'Owner (Josh)', 'Source']]
extra.columns = ['Name', "Owner", "Source"]
extra['Name'] = extra['Name'].str.title()


bran_df = pd.read_csv(wa_brand_scraped)
bran_df['Name'] = bran_df['Station'].str.title()
bran_df = bran_df.drop_duplicates(subset="Station", keep="last")
# bran_df.rename(columns={"Owner":"Brands owner"}, inplace=True)
bran_df['Owner'] = bran_df['Owner'].str.title()
bran_df['Source'] = "WA brand directory"


# Work out which ones in brand are also in extra
bran_df = fuzzy_merge(bran_df, extra, "Name", "Name")
bran_df = bran_df.loc[bran_df['matches'] == '']
bran_df = bran_df[['Name', 'Owner', 'Source']]

combo = extra.append(bran_df)
combo = combo.dropna(subset=["Owner"])




matched = fuzzy_merge(combo, gdf, "Name", "PROPERTY_N")


matches = matched[['matches', 'Owner', "Source"]]

# print(matches)
matches.columns = ['Station', 'Owner', "Source"]

# print(matches)

# # matches['Station'] = matches['Station'].str.split(",")[0]

with open(f"{data_path}/WA/WA_second_extraction_cleaned.csv", 'w') as f:
    matches.to_csv(f, index=False, header=True)


