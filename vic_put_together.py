import geopandas as gpd 
from paths import data_path

data_path = data_path + "/Vic/"
output_path = data_path + "cleaned_data/"

shape = f"{data_path}SDM746344/landuse_2016.shp"

gdf = gpd.read_file(shape)

gdf.loc[gdf['TENURE'] == "PUBLIC", "Ownership"] = "Public"
gdf.loc[gdf['TENURE'] == "PRIVATE", "Ownership"] = "Private"


# gdf = gdf[['Ownership', 'geometry']]

gdf.to_file(f"{output_path}vic_pub_private.shp")

# print(shape)

# df = pd.read_csv('/Users/josh_nicholas/WOA/VIC/victorianlandtenure2016.csv')

# df['Ownership'] = 'Public'
# df.loc[df['TENURE'] == 'PRIVATE', ['Ownership']] = 'Private'

# with open('/Users/josh_nicholas/WOA/VIC/Final_putting_together/200819Vic_publicprivate.csv', 'w') as f:
#     df.to_csv(f, index=False, header=True)

    