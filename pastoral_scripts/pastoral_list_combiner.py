import pandas as pd 
from paths import data_path
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 

# List of pastoral properties (and owners) from Joel
xcel = f"{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx"
joel = pd.read_excel(xcel, sheet_name="1. Pastoral Station Ownership", skiprows=2)

# List of Pastoral properties (and owners) from Weekly Times and Josh research
wt = f"{data_path}/Extracted_pastoral.csv"
wt = pd.read_csv(wt)
wt = wt[['Name', 'State', 'Owner (Josh)', 'Source']]