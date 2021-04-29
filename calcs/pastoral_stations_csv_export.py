import geopandas as gpd 
from paths import data_path 
import pandas as pd 

# df = pd.read_csv(f'{data_path}/final-ish/largest_pastoral_holders.csv')

# gdf = gpd.read_file(f'{data_path}/final-ish/pastoral_owner_dissolved_null_category.shp')
gdf = gpd.read_file(f'{data_path}/final-ish/pastoral_owner_dissolved_null.shp')

gdf = gdf.to_crs("EPSG:3577")


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

# print(gdf['Owner'].unique())

# print(gdf.loc[gdf['Owner'].isna()])

gdf.loc[gdf['Owner'].isna(), 'NAME'] = "Unknown"
gdf.loc[gdf['Owner'].isna(), 'Owner'] = "Unknown"
gdf.loc[gdf['Source'].isna(), 'Source'] = "Unknown"


print(gdf.loc[gdf['Owner'] == 'Unknown'])

gdf['Area'] = gdf['geometry'].area

gdf = gdf[['NAME', 'Owner', 'Source', 'Area']]

print(gdf.shape)
# gdf = gdf.drop_duplicates(subset=['NAME', 'Area'])
# print(gdf.shape)

merged = gdf.groupby(by= ['NAME', 'Owner', 'Source']).sum().reset_index()

print(merged.shape)

with open(f'{data_path}/final-ish/pastoral_stations_area.csv', 'w') as f:
    merged.to_csv(f, index=False, header=True)

# # grouped.to_file(f'{data_path}/final-ish/pastoral_owner_dissolved_null_category_ranked.shp')


# # print(gdf)
# # print(gdf.columns)
