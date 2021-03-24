import geopandas as gpd 
import pandas as pd 
from paths import data_path
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
# pd.set_option("display.max_rows", None, "display.max_columns", None)

# CSV of pastoral properties/owners extracted from the article last year, as well as Josh research
confirmed_pastoral = f"{data_path}/Extracted_pastoral.csv"

# CSV of Pastoral properties extracted from SA cadastrial:
cad_pastoral = f"{data_path}/SA/sa_pastoral_extraction.csv"

con = pd.read_csv(confirmed_pastoral)
con = con.loc[con['State'] == "SA"]
con = con[['Name', 'Owner (Josh)', 'Source']]
con['Name'] = con['Name'].str.title()

cad = pd.read_csv(cad_pastoral)


print(cad)
print(cad.columns)