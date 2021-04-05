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

 

sa_pastoral = f"{data_path}/pastoral/sa_pastoral.shp"
gdf = gpd.read_file(sa_pastoral)
gdf = gdf.dropna(subset=["NAME"])
# print(gdf)

joel_pastoral = f"{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx"

joel = pd.read_excel(joel_pastoral, sheet_name=1, skiprows=2)
joel_sa = joel.loc[joel['State'] == "SA"]
joel_sa = joel_sa[['Pastoral Station', 'CCG_owner','CCG_References']]
joel_sa.columns = ['Name', "Owner", "Source"]

extracted_pastoral = f"{data_path}/Extracted_pastoral.csv"
extra = pd.read_csv(extracted_pastoral)


extra = extra.loc[extra['State'] == "SA"]
extra = extra[['Name', 'Owner (Josh)', 'Source']]
extra.columns = ['Name', "Owner", "Source"]
extra['Name'] = extra['Name'].str.title()
# print(joel_sa)
# print(extra)

extra = fuzzy_merge(extra, joel_sa, "Name", "Name")
extra = extra.loc[pd.notna(extra['matches'])]
print(extra)

# matched = fuzzy_merge(gdf, joel_sa, "NAME", "Pastoral Station")

# combo = joel_sa.append(extra)
# combo.drop_duplicates(subset=['Name'], keep="first")


# print(combo)

# matched = fuzzy_merge(gdf, joel_sa, "NAME", "Pastoral Station")  

# print(matched)
# print(joel_sa)

# gdf = gdf.dropna(subset=["NAME"])
# print(gdf.columns)
# # CSV of pastoral properties/owners extracted from the article last year, as well as Josh research
# confirmed_pastoral = f"{data_path}/Extracted_pastoral.csv"

# # CSV of Pastoral properties extracted from SA cadastrial:
# cad_pastoral = f"{data_path}/SA/sa_pastoral_extraction.csv"

# con = pd.read_csv(confirmed_pastoral)
# con = con.loc[con['State'] == "SA"]
# con = con[['Name', 'Owner (Josh)', 'Source']]
# con['Name'] = con['Name'].str.title()

# cad = pd.read_csv(cad_pastoral)


# print(cad)
# print(cad.columns)