import geopandas as gpd 
from paths import data_path 
import pandas as pd 

file = f'{data_path}/final-ish/pastoral_owner_dissolved_null.shp'
joel_path = f'{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx'

df = pd.read_excel(joel_path, sheet_name=1, skiprows=2)

df = df[['Pastoral Station', 'CCG_cat', 'CCG_owner','CCG_References']]
df.columns = ['Name', "Category", "Owner", "Source"]

additional_foreign = ['Australian Agricultural Company', 'Ruyi Group (China)', 'Ruyi Group', "Zenith (Australia) Investment Holding Pty Ltd", 'Yiang Xiang Assets', 'Clean Agriculture and International Tourism', 'Ma Xingfa', 'Cross Pacific Investment', 'Pham Nhat Vu']

foreign = df.loc[df['Category'].str.contains("Foreign")]['Owner'].values.tolist()
strayan = df.loc[(df['Category'].str.contains("Australia") | df['Category'].str.contains("Australian"))]['Owner'].values.tolist()

foreign = foreign + additional_foreign

gdf = gpd.read_file(file)
gdf.loc[gdf['Owner'] == "Jumbuck", 'Owner'] = 'Jumbuck Pastoral Company'
gdf.loc[gdf['Owner'] == "Subsidiary of the Hu family's YK Group", 'Owner'] = 'YK Group'
gdf.loc[gdf['Owner'] == "MDH", 'Owner'] = 'MDH Pty Ltd'
gdf.loc[gdf['Owner'] == "Green??ld Pastoral Co Pty Ltd", 'Owner'] = 'Greenfield Pastoral Company Ltd'

gdf.loc[gdf['Owner'] == "Clean Agriculture & International Tourism", 'Owner'] = 'Clean Agriculture and International Tourism'

gdf.loc[gdf['Owner'] == "Heytesbury Cattle Co", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
gdf.loc[gdf['Owner'] == "Heytesbury Cattle Co.", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
gdf.loc[gdf['Owner'] == "Heytesbury Pty Ltd", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'



gdf['Category'] = 'Unknown'

gdf.loc[gdf['Owner'].isin(foreign), 'Category'] = "Foreign"
gdf.loc[gdf['Owner'].isin(strayan), 'Category'] = "Australian"


# large = ['Anna Creek', 'Cubbie', 'Alexandria',  'Davenport Downs',  'Home Valley Station', 'Wave Hill' , 'Marion Downs',
# 'Lake Nash', 'Brunette Downs','Macumba',  'Andado', 'Newcastle Waters', 'Helen Springs', 'Rawlinna Station', 'Headingly' 
# 'Commonwealth Hill' , 'Walhallow' ,'Rugby','Anthony Lagoon','Eva Downs','Strathmore','Durham Downs','Victoria River Downs'
# 'Adria Downs' ,'Nockatunga','Tanbar','Dunbar'  ]

# largers = gdf.loc[gdf['NAME'].isin(large)].head(100)


gdf.to_file(f'{data_path}/final-ish/pastoral_owner_dissolved_null_category.shp')




