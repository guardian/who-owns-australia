import geopandas as gpd 
import matplotlib.pyplot as plt
from paths import data_path

data_path = data_path + "/NSW/"

capd = f'{data_path}CAPAD2018_terrestrial/CAPAD2018_terrestrial.shp'

# print(capd)

# index = ['PA_ID', 'PA_PID', 'NAME', 'TYPE', 'TYPE_ABBR', 'IUCN', 'NRS_PA',
#        'GAZ_AREA', 'GIS_AREA', 'GAZ_DATE', 'LATEST_GAZ', 'STATE', 'AUTHORITY',
#        'DATASOURCE', 'GOVERNANCE', 'COMMENTS', 'ENVIRON', 'OVERLAP',
#        'MGT_PLAN', 'RES_NUMBER', 'EPBC', 'LONGITUDE', 'LATITUDE', 'SHAPE_AREA',
#        'SHAPE_LEN', 'geometry']



# types = ['Nature Reserve' 'Botanic Gardens (Commonwealth)' 'National Park'
#  'CCA Zone 1 National Park' 'Wilderness Zone' 'Aboriginal Area'
#  'Conservation Reserve' 'Flora Reserve'
#  'CCA Zone 3 State Conservation Area' 'Indigenous Protected Area'
#  'Historic Site' 'Karst Conservation Reserve' 'Nature Park'
#  'Conservation Park' 'NRS Addition - Gazettal in Progress'
#  'Other Conservation Area' 'Coordinated Conservation Area'
#  'Forest Reserve' 'Other Conservation Area or Nature Park'
#  'Private Nature Reserve'
#  'Proposed National Parks Act park or park addition'
#  'National Park (Commonwealth)' 'Natural Catchment Area'
#  'State Conservation Area' 'Botanic Gardens' 'Coastal Reserve'
#  'Conservation Area' 'Conservation Covenant' 'Permanent Park Preserve'
#  'Protected Area' 'Historical Reserve' 'Hunting Reserve'
#  'Management Agreement Area' 'Management Area' 'Regional Park'
#  'Nature Refuge' 'Resources Reserve' 'National Park (Scientific)'
#  'National Park Aboriginal' 'Heritage Agreement' 'Recreation Park'
#  'Game Reserve' 'Regional Reserve' 'Wilderness Protection Area'
#  'Nature Recreation Area' 'Private Sanctuary' 'Other' 'State Reserve'
#  'Natural Features Reserve' 'Heritage River'
#  'National Parks Act Schedule 4 park or reserve'
#  'Nature Conservation Reserve' 'State Park' '5(1)(h) Reserve'
#  'Reference Area' 'Wilderness Park' '5(1)(g) Reserve'
#  'Remote and Natural Area - not scheduled under Nat Parks Act'
#  'Remote and Natural Area - Schedule 6, National Parks Act'
#  'Antarctic Specially Managed Area' 'Antarctic Specially Protected Area']

aboriginal_lands = ['Aboriginal Area', 'Indigenous Protected Area', 'National Park Aboriginal']

gdf = gpd.read_file(capd)

aboriginal_land_gdf = gdf[(gdf['TYPE'] == 'Aboriginal Area') | (gdf['TYPE'] == 'Indigenous Protected Area') | (gdf['TYPE'] == 'National Park Aboriginal')]

fig, ax = plt.subplots(1, figsize=(14,8))
aboriginal_land_gdf.plot(column='TYPE', categorical=True, cmap='Spectral', linewidth=.6, edgecolor='0.2',
    legend=True, legend_kwds={'bbox_to_anchor':(.3, 1.05),'fontsize':16,'frameon':False}, ax=ax)

plt.show()

# print(gdf[(gdf['TYPE'] == 'Aboriginal Area') | (gdf['TYPE'] == 'Indigenous Protected Area') | (gdf['TYPE'] == 'National Park Aboriginal')])

# print(gdf.columns)
# print(gdf['TYPE'].unique())