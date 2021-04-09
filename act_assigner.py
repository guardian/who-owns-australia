import geopandas as gpd 

from paths import data_path

act_file = f'{data_path}/final-ish/act.shp'

gdf = gpd.read_file(act_file)
gdf = gdf.to_crs("EPSG:4326")

gdf = gdf[['name', 'latitude', 'longitude', 'geometry']]

gdf['Ownership'] = "Public"

gdf.to_file(act_file)


