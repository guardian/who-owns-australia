import geopandas as gpd 
from paths import data_path 
import pandas as pd 

# file = f"{data_path}/final_merged/final.shp"

# gdf = gpd.read_file(file)
# gdf = gdf.to_crs("EPSG:3577")

# gdf['area'] = gdf["geometry"].area

# grouped = gdf.dissolve(by='Ownership', aggfunc = "sum")

# print(grouped.round())

# gdf.to_file(f"{data_path}/final_merged/final_with_area.shp")


areas_cv = f"{data_path}/area.csv"

df = pd.read_csv(areas_cv)

# Group by state and ownership type



# grouped = df.groupby(by=['State', "Ownership"])['area'].sum().reset_index()
# states = ['ACT', 'NSW', 'NT', "QLD", 'SA', "TAS", 'VIC', 'WA']

# listo = []
# for state in states:
#     init_state = grouped.loc[grouped['State'] == state].copy()
#     init_total = init_state['area'].sum()
#     init_state['Percentages'] = (init_state['area'] / init_total)*100
#     listo.append(init_state)


# final = pd.concat(listo)
# print(final.round())


## Group by ownership type

total_oz = df['area'].sum()
grouped = df.groupby(by=["Ownership"])['area'].sum().reset_index()
grouped['percentages'] = (grouped['area'] / total_oz)*100

grouped['area'] = round(grouped['area'])

print(grouped.round())