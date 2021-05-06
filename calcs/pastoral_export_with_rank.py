import geopandas as gpd 
from paths import data_path 
import pandas as pd 

df = pd.read_csv(f'{data_path}/final-ish/largest_pastoral_holders.csv')

gdf = gpd.read_file(f'{data_path}/final-ish/pastoral_owner_dissolved_null_category.shp')

# print(gdf)
# print(gdf.columns)

merged = gdf.merge(df, on='Owner', how='left')


merged.loc[merged['Owner'] == "Australian Agricultural Co", 'Owner'] = 'Australian Agricultural Company'
merged.loc[merged['Owner'] == 'Indigenous Land And Sea Corporation', 'Owner'] = 'Indigenous Land and Sea Corporation'
merged.loc[merged['Owner'] == 'ILC', 'Owner'] = 'Indigenous Land and Sea Corporation'

merged.loc[merged['Owner'] == 'S.Kidman & Co', 'Owner'] = 'S Kidman & Company'

merged.loc[merged['Owner'] == "Jumbuck", 'Owner'] = 'Jumbuck Pastoral Company'
merged.loc[merged['Owner'] == "Subsidiary of the Hu family's YK Group", 'Owner'] = 'YK Group'
merged.loc[merged['Owner'] == "MDH", 'Owner'] = 'MDH Pty Ltd'
merged.loc[merged['Owner'] == "Green??ld Pastoral Co Pty Ltd", 'Owner'] = 'Greenfield Pastoral Company Ltd'

merged.loc[merged['Owner'] == "Clean Agriculture & International Tourism", 'Owner'] = 'Clean Agriculture and International Tourism'

merged.loc[merged['Owner'] == "Heytesbury Cattle Co", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
merged.loc[merged['Owner'] == "Heytesbury Cattle Co.", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
merged.loc[merged['Owner'] == "Heytesbury Pty Ltd", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'

merged.loc[merged['Owner'] == 'Paragdfy Pastoral Co', 'Owner'] = 'Paragdfy Pastoral Company'

merged.loc[merged['Owner'] == 'Cleveland Agriculture (Harris family)', 'Owner'] = 'Cleveland Agriculture'



merged.loc[merged['Owner'] == "Australian Agricultural Co", 'Owner'] = 'Australian Agricultural Company'
merged.loc[merged['Owner'] == 'Indigenous Land And Sea Corporation', 'Owner'] = 'Indigenous Land and Sea Corporation'
merged.loc[merged['Owner'] == 'ILC', 'Owner'] = 'Indigenous Land and Sea Corporation'

merged.loc[merged['Owner'] == 'S.Kidman & Co', 'Owner'] = 'S Kidman & Company'

merged.loc[merged['Owner'] == "Jumbuck ", 'Owner'] = 'Jumbuck Pastoral Company'
merged.loc[merged['Owner'] == "Jumbuck", 'Owner'] = 'Jumbuck Pastoral Company'
merged.loc[merged['Owner'] == "Subsidiary of the Hu family's YK Group", 'Owner'] = 'YK Group'
merged.loc[merged['Owner'] == "MDH", 'Owner'] = 'MDH Pty Ltd'
merged.loc[merged['Owner'] == "Green??ld Pastoral Co Pty Ltd", 'Owner'] = 'Greenfield Pastoral Company Ltd'
merged.loc[merged['Owner'] == "Green铿乪ld Pastoral Co Pty Ltd", 'Owner'] = 'Greenfield Pastoral Company Ltd'



merged.loc[merged['Owner'] == "Clean Agriculture & International Tourism", 'Owner'] = 'Clean Agriculture and International Tourism'

merged.loc[merged['Owner'] == "Heytesbury Cattle Co", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
merged.loc[merged['Owner'] == "Heytesbury Cattle Co.", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
merged.loc[merged['Owner'] == "Heytesbury Pty Ltd", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'

merged.loc[merged['Owner'] == 'Paragdfy Pastoral Co', 'Owner'] = 'Paragdfy Pastoral Company'
merged.loc[merged['Owner'] == 'Cleveland Agriculture (Harris family)', 'Owner'] = 'Cleveland Agriculture'


merged.loc[merged['NAME'] == 'Carranya Station', 'Owner'] = 'Indigenous Land and Sea Corporation'

merged.loc[merged['NAME'] == 'MULGA DOWNS STATION', 'Owner'] = 'Hancock Prospecting'
merged.loc[merged['NAME'] == 'Mulga Downs Station', 'Owner'] = 'Hancock Prospecting'


merged = merged[['NAME', 'Owner', 'Source', 'Category', 'geometry']]

merged.columns = ['Name', 'Owner', 'Source', 'Category', 'geometry']

merged.loc[merged['Owner'] == 'Indigenous Land And Sea Corporation', 'Category'] = "Australian"
merged.loc[merged['Owner'] == 'Kurtijar People', 'Category'] = "Australian"
merged.loc[merged['Owner'] == 'Waanyi people', 'Category'] = "Australian"
merged.loc[merged['Owner'] == 'Traditional owners', 'Category'] = "Australian"

listor = ['Indigenous Land And Sea Corporation', 'Kurtijar People', 'Waanyi people', 
'Traditional owners', 'North Australian Pastoral Company', 'Crown Point Pastoral Company', 
'Williams Cattle Company', 'Jumbuck Pastoral Company', 'Australian Agricultural Company', 
'Australian Outback Beef', 'Brook Pastoral Company', 'Hancock Prospecting', 'MDH Pty Ltd', 
'Heytesbury Cattle Company Pty Ltd', 'Western Grazing', 'Australian Wildlife Conservancy', 
'S Kidman & Company', 'Australian Country Choice', 'Paraway Pastoral Company', 
'Brett Blundy, Adrian and Emma Brown', 'Kimberley Agriculture']

merged.loc[merged['Owner'].isin(listor), 'Category'] = "Australian"
print(merged.loc[merged['Owner'].isin(listor)])

merged.to_file(f'{data_path}/210503final_final/pastoral_owner_dissolved_null_category.shp')

# print(merged.loc[merged['Owner'] == 'North Australian Pastoral Company'])

# print(merged)



print(merged.loc[merged['Owner'].isin(listor)])

grouped = merged.dissolve(by="Owner").reset_index()

grouped['Area'] = grouped['geometry'].area

grouped = grouped.sort_values(by='Area', ascending=False)

grouped['Rank'] = grouped['Area'].rank(method='first', ascending=False)

grouped = grouped[['Owner', 'Source', 'Category', 'geometry', 'Area', 'Rank']]

grouped.to_file(f'{data_path}/210503final_final/pastoral_owner_dissolved_null_category_ranked.shp')

print(grouped)

print(grouped.columns)