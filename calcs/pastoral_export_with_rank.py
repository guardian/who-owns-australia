import geopandas as gpd 
from paths import data_path 
import pandas as pd 

df = pd.read_csv(f'{data_path}/final-ish/largest_pastoral_holders.csv')

gdf = gpd.read_file(f'{data_path}/final-ish/pastoral_owner_dissolved_null_category.shp')

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

gdf.loc[gdf['Owner'] == 'Cleveland Agriculture (Harris family)', 'Owner'] = 'Cleveland Agriculture'

merged = gdf.merge(df, on='Owner', how='left')

merged = merged[['NAME', 'Owner', 'Source', 'Category', 'geometry', 'Area', 'Rank']]

merged.columns = ['Name', 'Owner', 'Source', 'Category', 'geometry', 'Owner area', 'Owner rank']

# merged.to_file(f'{data_path}/final-ish/pastoral_owner_dissolved_null_category_ranked.shp')

# print(merged.loc[merged['Owner'] == 'North Australian Pastoral Company'])

print(merged)



# grouped = gdf.dissolve(by="Owner").reset_index()

# grouped['Area'] = grouped['geometry'].area

# grouped = grouped.sort_values(by='Area', ascending=False)

# grouped['Rank'] = grouped['Area'].rank(method='first', ascending=False)

# grouped = grouped[['Owner', 'Source', 'Category', 'geometry', 'Area', 'Rank']]

# grouped.to_file(f'{data_path}/final-ish/pastoral_owner_dissolved_null_category_ranked.shp')

# print(grouped)

# print(grouped.columns)