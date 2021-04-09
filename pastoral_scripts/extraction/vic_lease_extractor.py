import geopandas as gpd 
from paths import data_path

data_path = data_path + "/Vic/"
output_path = data_path + "cleaned_data/"

shape = f"{data_path}SDM746344/landuse_2016.shp"

gdf = gpd.read_file(shape)

pastoral = ['Mixed farming and grazing  (generally more than 20ha)', 'Livestock Production  Beef Cattle',
'Mixed farming and grazing', 'Livestock Production (Dairy Cattle)', 'Livestock Production (Sheep)', 'Piggery', 'Orchards, Groves and Plantations']

pastoral = gdf.loc[gdf['LU_DESC'].isin(pastoral)]

pastoral.to_file(f"{output_path}vic_pastoral.shp")