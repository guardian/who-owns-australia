import pandas as pd 
import geopandas as gpd 
from paths import data_path

data_path = data_path + "/QLD/"
output_path = data_path + "cleaned_data/"


lease_type_cad_csv = f'{data_path}qld_joel/qldcadLEASETYPEJOIN.csv'
rural_properties_shp = f'{data_path}QSC_Extracted_Data_20200804_111134877000-31036/Rural_Properties.shp'
lease_type_cad_shp = f'{data_path}qld_joel/PROP.QLD.CADASTRE_DCDB_Join_Leasedtype.shp'

# lease_columns = ['LOT', 'PLAN', 'LOTPLAN', 'SEG_NUM', 'PAR_NUM', 'SEGPAR', 'PAR_IND',
#        'LOT_AREA', 'EXCL_AREA', 'LOT_VOLUME', 'SURV_IND', 'TENURE', 'PRC',
#        'PARISH', 'COUNTY', 'LAC', 'SHIRE_NAME', 'FEAT_NAME', 'ALIAS_NAME',
#        'LOC', 'LOCALITY', 'PARCEL_TYP', 'COVER_TYP', 'ACC_CODE', 'CA_AREA_SQ',
#        'SMIS_MAP', 'OBJECTID', 'O_SHAPE_Le', 'O_SHAPE_Ar', 'OBJECTID_1',
#        'TITLE_REF', 'LOTPLAN_1', 'PLAN_NUMBE', 'PLAN_TYPE', 'PLAN_NO',
#        'LOT_NO', 'COMMENCE_D', 'EXPIRE_DAT', 'GAZETTAL', 'TENURE_TYP',
#        'TENURE_DES', 'LOCAL_GOVT', 'LEASE_AREA', 'LEASE_PURP', 'LEASE_SUBP',
#        'TRUSTEE', 'GIVEN_NAME', 'geometry']
# lease_tenure_types = ['PH' 'GHPL' None 'NCL' 'RL' 'TL' 'PO' 'SL' 'PLS' 'PPL' 'OL' 'PPH' 'PDH'
#  'AF' 'GHFL' 'FL' 'SH' 'SHPTL' 'WHPTL' 'SLPF']


# rural_properties_gdf = gpd.read_file(rural_properties_shp)
# # print(len(rural_properties_gdf['NAME'].unique().tolist()))
# # 21120 unique names in this dataset

# lease_gdf = gpd.read_file(lease_type_cad_shp)

from paths import data_path

# List of pastoral properties (and owners) from Joel
xcel = f"{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx"
joel = pd.read_excel(xcel, sheet_name="1. Pastoral Station Ownership", skiprows=2)

# List of Pastoral properties (and owners) from Weekly Times and Josh research
wt = f"{data_path}/Extracted_pastoral.csv"
wt = pd.read_csv(wt)
wt = wt[['Name', 'State', 'Owner (Josh)', 'Source']]
print(wt)
print(joel)
print(joel.columns)

### SORTING INTO NON PASTORAL AND PASTORAL BASED ON JOEL'S GRAPHIC

# lease_gdf['Pastoral_classificiation'] = "Non-pastoral"

# lease_gdf.loc[lease_gdf['TENURE_TYP'] == 'PH', ['Pastoral_classificiation']] = "Pastoral"
# lease_gdf.loc[lease_gdf['TENURE_TYP'] == 'GHPL', ['Pastoral_classificiation']] = "Pastoral"
# lease_gdf.loc[lease_gdf['TENURE_TYP'] == 'PDH', ['Pastoral_classificiation']] = "Pastoral"
# lease_gdf.loc[lease_gdf['TENURE_TYP'] == 'PPH', ['Pastoral_classificiation']] = "Pastoral"
# lease_gdf.loc[lease_gdf['TENURE_TYP'] == 'SH', ['Pastoral_classificiation']] = "Pastoral"
# lease_gdf.loc[lease_gdf['TENURE_TYP'] == 'TL', ['Pastoral_classificiation']] = "Pastoral"

# ## SPATIAL JOIN

# combined_gdf = gpd.sjoin(rural_properties_gdf, lease_gdf, how='left')

# ## SELECT JUST PASTORAL PROPERTIES FROM TENURE TYPE RECLASSIFICATION

# pastoral_properties = combined_gdf[combined_gdf['Pastoral_classificiation'] == "Pastoral"]

# pastoral_properties.to_file(f"{data_path}pastoral/qld_pastoral.shp")
