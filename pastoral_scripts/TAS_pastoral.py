import geopandas as gpd 
import pandas as pd 
from paths import data_path
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
# pd.set_option("display.max_rows", None, "display.max_columns", None)

# CSV of pastoral properties/owners extracted from the article last year, as well as Josh research
confirmed_pastoral_list = f"{data_path}/Extracted_pastoral.csv"

## WORK OUT LARGEST FARM OWNERS

con_df = pd.read_csv(confirmed_pastoral_list)
con_df = con_df.loc[con_df['State'] == "TAS"]
con_df = con_df[['Name', 'Owner (Josh)', 'Source']]
con_df['Name'] = con_df['Name'].str.title()

print(con_df)