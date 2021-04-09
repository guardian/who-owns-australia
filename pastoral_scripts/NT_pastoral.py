import geopandas as gpd 
import pandas as pd 
from paths import data_path
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
# pd.set_option("display.max_rows", None, "display.max_columns", None)

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


sa_pastoral = f"{data_path}/pastoral/nt_pastoral.shp"
gdf = gpd.read_file(sa_pastoral)
gdf = gdf.dropna(subset=["PROPERTY_N"])


joel_pastoral = f"{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx"

joel = pd.read_excel(joel_pastoral, sheet_name=1, skiprows=2)
joel_nt = joel.loc[joel['State'] == "NT"]
joel_nt = joel_nt[['Pastoral Station', 'CCG_owner','CCG_References']]
joel_nt.columns = ['Name', "Owner", "Source"]



extracted_pastoral = f"{data_path}/Extracted_pastoral.csv"
extra = pd.read_csv(extracted_pastoral)

extra = extra.loc[extra['State'] == "NT"]
extra = extra[['Name', 'Owner (Josh)', 'Source']]
extra.columns = ['Name', "Owner", "Source"]
extra['Name'] = extra['Name'].str.title()

# # Only select the pastoral properties in extra that aren't in Joel's
extra = fuzzy_merge(extra, joel_nt, "Name", "Name")
extra = extra.loc[extra['matches'] == '']

extra = extra[['Name', 'Owner', 'Source']]

combo = joel_nt.append(extra)
combo.drop_duplicates(subset=['Name'], keep="first")

matched = fuzzy_merge(gdf, combo, "PROPERTY_N", "Name")  

joined = matched.merge(combo, left_on="matches", right_on="Name", how="left")

joined.to_file(f"{data_path}/pastoral_owned/nt_pastoral_ownership.shp")