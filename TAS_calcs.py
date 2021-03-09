import pandas as pd 
import geopandas as gpd 
from paths import data_path

data_path = data_path + "/Tas/"

gpd = gpd.read_file(f'{data_path}tas_piv_pub_ab.shp')

print(gpd)

gpd['area'] = gpd["geometry"].area

grouped = gpd.dissolve(by='Ownership', aggfunc = "sum")

print(grouped.crs)

print(grouped.round())

gpd.plot(column="Ownership")
