import geopandas as gpd 
from paths import data_path 
import pandas as pd 
from fuzzywuzzy import fuzz

file = f'{data_path}/final-ish/pastoral_owner_dissolved_null_category.shp'

joel_path = f'{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx'

df = pd.read_excel(joel_path, sheet_name=1, skiprows=2)

df = df[['Pastoral Station', 'CCG_cat', 'CCG_owner','CCG_References']]
df.columns = ['Name', "Category", "Owner", "Source"]

additional_foreign = ['Australian Agricultural Company', 'Ruyi Group (China)', 'Ruyi Group', "Zenith (Australia) Investment Holding Pty Ltd", 'Yiang Xiang Assets', 'Clean Agriculture and International Tourism', 'Ma Xingfa', 'Cross Pacific Investment', 'Pham Nhat Vu']

foreign = df.loc[df['Category'].str.contains("Foreign")]['Owner'].values.tolist()
strayan = df.loc[(df['Category'].str.contains("Australia") | df['Category'].str.contains("Australian"))]['Owner'].values.tolist()

foreign = foreign + additional_foreign



## Calculate foreign ag %

# gdf = gpd.read_file(file)
# gdf['Area'] = gdf['geometry'].area

# total_area = gdf['Area'].sum()

# grouped = gdf.groupby(by="Category")['Area'].sum().reset_index()
# grouped['Percent'] = (grouped['Area']/total_area)*100

# print(grouped)


## Find largest pastoral holders

gdf = gpd.read_file(file)
gdf['Area'] = gdf['geometry'].area

gdf.loc[gdf['Owner'] == "Australian Agricultural Co", 'Owner'] = 'Australian Agricultural Company'
gdf.loc[gdf['Owner'] == 'Indigenous Land And Sea Corporation', 'Owner'] = 'Indigenous Land and Sea Corporation'
gdf.loc[gdf['Owner'] == 'ILC', 'Owner'] = 'Indigenous Land and Sea Corporation'

gdf.loc[gdf['Owner'] == 'S.Kidman & Co', 'Owner'] = 'S Kidman & Company'


gdf.loc[gdf['Owner'] == "Jumbuck", 'Owner'] = 'Jumbuck Pastoral Company'
gdf.loc[gdf['Owner'] == "Subsidiary of the Hu family's YK Group", 'Owner'] = 'YK Group'
gdf.loc[gdf['Owner'] == "MDH", 'Owner'] = 'MDH Pty Ltd'
gdf.loc[gdf['Owner'] == "Green??ld Pastoral Co Pty Ltd", 'Owner'] = 'Greenfield Pastoral Company Ltd'

gdf.loc[gdf['Owner'] == "Clean Agriculture & International Tourism", 'Owner'] = 'Clean Agriculture and International Tourism'

gdf.loc[gdf['Owner'] == "Heytesbury Cattle Co", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
gdf.loc[gdf['Owner'] == "Heytesbury Cattle Co.", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
gdf.loc[gdf['Owner'] == "Heytesbury Pty Ltd", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'

gdf.loc[gdf['Owner'] == 'Paraway Pastoral Co', 'Owner'] = 'Paraway Pastoral Company'


largest = gdf.groupby(by='Owner')['Area'].sum().reset_index()
largest = largest.sort_values(by='Area', ascending=False)
largest['Rank'] = largest['Area'].rank(method='first', ascending=False)

pd.options.display.float_format = '{:.0f}'.format

# print(largest)

# holders = largest['Owner'].values.tolist()

# listo = []
# count = 0
# def get_ratio(string1, string2):
#     ratio = fuzz.token_sort_ratio(string1, string2)
#     if (ratio > 85) & (string1 != string2):
#         # print(string1, string2)
#         listo.append((string1, string2))

# for holder in holders:

#     for second in holders:
#         print(count)
#         get_ratio(holder, second)
#         count += 1


# print(listo)

with open(f'{data_path}/final-ish/largest_pastoral_holders.csv', "w") as f:
    largest.to_csv(f, index=False, header=True, float_format='%f')




####### 

## Fuzzy match the pastoral holders
# from fuzzywuzzy import fuzz



# gdf = gpd.read_file(file)
# holders = gdf['Owner'].values.tolist()

# listo = []
# count = 0

# holders = gdf['Owner'].values.tolist()

# def get_ratio(string1, string2):
#     ratio = fuzz.token_sort_ratio(string1, string2)
#     if (ratio > 90) & (string1 != string2):
#         # print(string1, string2)
#         listo.append((string1, string2))

# for holder in holders:

#     for second in holders:
#         print(count)
#         get_ratio(holder, second)
#         count += 1

# print(holders)
# for i in range(0, len(holders)):
#     # print(i)
#     a = i
#     b = i + 1
#     print(a)
#     print(b)
#     get_ratio(holders[a], holders[b])

# print(listo)

# def removeDuplicates(lst):
      
#     return [t for t in (set(tuple(i) for i in lst))]

# listo = removeDuplicates(listo)

# print(listo)

# ratio = fuzz.token_sort_ratio(holders[0], holders[1])

# print(ratio)
