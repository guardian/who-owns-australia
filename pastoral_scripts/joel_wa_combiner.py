import pandas as pd 
from paths import data_path
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 

# List of pastoral properties (and owners) from Joel
# xcel = f"{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx"
# joel = pd.read_excel(xcel, sheet_name="1. Pastoral Station Ownership", skiprows=2)
xcel = f"{data_path}/joel_pastoral.csv"
joel = pd.read_csv(xcel)


foreign_list = joel.loc[joel['CCG_cat'].str.contains("Foreign")]['CCG_owner'].values.tolist()

additional_foreign = ["Zenith (Australia) Investment Holding Pty Ltd", 'Australian Agricultural Company', 'Ruyi Group (China)', 'Ruyi Group', "Zenith (Australia) Investment Holding Pty Ltd", 'Yiang Xiang Assets', 'Clean Agriculture and International Tourism', 'Ma Xingfa', 'Cross Pacific Investment', 'Pham Nhat Vu']

foreign_list = foreign_list + additional_foreign

additional_oz = ['Harvest Road Group', "S Kidman & Company", 'S.Kidman & Co', 'Jumbuck Pastoral Company', "Jumbuck", 'Hancock Prospecting', 'Forrest & Forrest Pty Ltd']

oz_list = joel.loc[(joel['CCG_cat'].str.contains("Australia") | joel['CCG_cat'].str.contains("Australian"))]['CCG_owner'].values.tolist()

oz_list = oz_list + additional_oz

joel['Category'] = "Unknown"
joel.loc[joel['CCG_cat'].str.contains("Foreign"),'Category' ] = "Foreign"
joel.loc[joel['CCG_owner'].isin(additional_foreign), 'Category' ] = "Foreign"

joel.loc[(joel['CCG_cat'].str.contains("Australia") | joel['CCG_cat'].str.contains("Australian")), 'Category'] = "Australian"
joel.loc[joel['CCG_owner'].isin(additional_oz), 'Category' ] = "Australian"


joel = joel[['Pastoral Station', 'State', 'CCG_owner', 'Category', 'Area (Ha)', 'CCG_References']]

joel.columns = ["Station", "State", "Owner", "Category", "Area", "Source"]

# wacv = f"{data_path}/WA/qgis_wa_export_three.csv"
wacv = f"{data_path}/WA/qgis_wa_export_four.csv"
wa = pd.read_csv(wacv)

# wa['Area'] = wa['Area']/10000

wa['PROPERTY_N'] = wa['PROPERTY_N'].str.title()
wa.rename(columns={"hectares":"Area"}, inplace=True)

wa = wa[['PROPERTY_N', 'Area', 'WA_second_extraction_cleaned_Owner', 'WA_second_extraction_cleaned_Source']]

combined = wa.groupby(by=['PROPERTY_N', 'WA_second_extraction_cleaned_Owner', 'WA_second_extraction_cleaned_Source']).sum().reset_index()

combined = combined.sort_values(by='Area', ascending=False)

combined['State'] = 'WA'

combined['Category'] = "Unknown"

combined.loc[combined['WA_second_extraction_cleaned_Owner'].isin(foreign_list), 'Category' ] = "Foreign"
combined.loc[combined['WA_second_extraction_cleaned_Owner'].isin(oz_list), 'Category' ] = "Australian"

combined = combined[['PROPERTY_N', 'State', 'WA_second_extraction_cleaned_Owner',
         'Category', 'Area', 'WA_second_extraction_cleaned_Source']]

combined.columns = ["Station", "State", "Owner", "Category", "Area", "Source"]


merged = joel.append(combined)

sorted = merged.sort_values(by="Area", ascending=False)

sorted.loc[sorted['Owner'] == "Australian Agricultural Co", 'Owner'] = 'Australian Agricultural Company'
sorted.loc[sorted['Owner'] == 'Indigenous Land And Sea Corporation', 'Owner'] = 'Indigenous Land and Sea Corporation'
sorted.loc[sorted['Owner'] == 'ILC', 'Owner'] = 'Indigenous Land and Sea Corporation'

sorted.loc[sorted['Owner'] == 'S.Kidman & Co', 'Owner'] = 'S Kidman & Company'
sorted.loc[sorted['Station'] == 'Killarney', 'Source'] = 'https://jumbuck.com.au/killarney/'
sorted.loc[sorted['Station'] == 'Killarney', 'State'] = 'QLD'

sorted.loc[sorted['Owner'] == "Jumbuck ", 'Owner'] = 'Jumbuck Pastoral Company'
sorted.loc[sorted['Owner'] == "Jumbuck", 'Owner'] = 'Jumbuck Pastoral Company'
sorted.loc[sorted['Owner'] == "Subsidiary of the Hu family's YK Group", 'Owner'] = 'YK Group'
sorted.loc[sorted['Owner'] == "MDH", 'Owner'] = 'MDH Pty Ltd'
sorted.loc[sorted['Owner'] == "Green??ld Pastoral Co Pty Ltd", 'Owner'] = 'Greenfield Pastoral Company Ltd'
sorted.loc[sorted['Owner'] == "Green铿乪ld Pastoral Co Pty Ltd", 'Owner'] = 'Greenfield Pastoral Company Ltd'



sorted.loc[sorted['Owner'] == "Clean Agriculture & International Tourism", 'Owner'] = 'Clean Agriculture and International Tourism'

sorted.loc[sorted['Owner'] == "Heytesbury Cattle Co", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
sorted.loc[sorted['Owner'] == "Heytesbury Cattle Co.", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'
sorted.loc[sorted['Owner'] == "Heytesbury Pty Ltd", 'Owner'] = 'Heytesbury Cattle Company Pty Ltd'

sorted.loc[sorted['Owner'] == 'Paraway Pastoral Co', 'Owner'] = 'Paraway Pastoral Company'
sorted.loc[sorted['Owner'] == 'Cleveland Agriculture (Harris family)', 'Owner'] = 'Cleveland Agriculture'

sorted = sorted.groupby(by=['Station', "State", 'Owner',"Category", 'Source']).sum().reset_index()


# print(sorted)

# print(sorted.loc[sorted['Owner'] == "Hancock Prospecting"])

innaminckha = pd.DataFrame.from_records([{"Station": "Innamincka Station", "State": "SA",
 "Owner": "S Kidman & Company", "Category":"Australian", "Area":"1355000", 
 "Source":"https://www.kidman.com.au/locations/innamincka/"}])

# print(innaminckha)

sorted = sorted.append(innaminckha)

# print(sorted)



# sorted = sorted.sort_values(by="Area", ascending=False)

sorted = sorted[["Station", "State", "Owner", "Category", "Area", "Source"]]

print(sorted.loc[sorted['Owner'] == "Jumbuck "])

sorted["Area"] = pd.to_numeric(sorted["Area"])

sorted = sorted.sort_values(by="Area", ascending=False)

with open(f"{data_path}/pastoral_joel_brand_super_merge.csv", 'w') as f:
    sorted.to_csv(f, index=False, header=True)

