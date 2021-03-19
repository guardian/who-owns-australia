import pandas as pd 
from paths import data_path
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 

# List of pastoral properties (and owners) from Joel
xcel = f"{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx"
joel = pd.read_excel(xcel, sheet_name="1. Pastoral Station Ownership", skiprows=2)

# List of Pastoral properties (and owners) from Weekly Times and Josh research
wt = f"{data_path}/Extracted_pastoral.csv"
wt = pd.read_csv(wt)
wt = wt[['Name', 'State', 'Owner (Josh)', 'Source']]

# List of Pastoral properties extracted from Cadastrial, including areas
wacv = f"{data_path}/WA/WApastoral.csv"
wa = pd.read_csv(wacv)
wa = wa[['property_n', 'Shape_Leng', 'Shape_Area']]
wa['property_n'] = wa['property_n'].str.title()




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

# wt = fuzzy_merge(wt, joel, "Name", "Pastoral Station", threshold=90, limit=2)

# combo = pd.merge(wt, joel, left_on="matches", right_on="Pastoral Station", how="left")

# test = combo.loc[~combo['Pastoral Station'].isna()]
# print(test)



