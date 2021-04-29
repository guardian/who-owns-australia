import pandas as pd 
from paths import data_path 
pd.set_option("display.max_rows", None, "display.max_columns", None)

cv = f"{data_path}/largest_pastoral_joel_sheet_merged.csv"

df = pd.read_csv(cv)


Australia = 768828700
# https://www.ga.gov.au/scientific-topics/national-location-information/dimensions/area-of-australia-states-and-territories

rinehart = ['Australian Outback Beef', 'S Kidman & Company', 'Hancock Prospecting']
forrest = ['Harvest Road Group', 'Forrest & Forrest Pty Ltd', 'Red Sky Stations Pty Ltd']

df.loc[df['Owner'].isin(rinehart), 'Owner'] = "Gina Rinehart"
df.loc[df['Owner'].isin(forrest), 'Owner'] = "Forrest"

grouped = df.groupby(by="Owner").sum().reset_index()
grouped = grouped.sort_values(by="Area", ascending=False)
grouped['Rank'] = grouped['Area'].rank(ascending=False)

top_20 = grouped[:20]
top_55 = grouped[:55]
top_100 = grouped[:100]

top_20_sum = top_20['Area'].sum()
top_55_sum = top_55['Area'].sum()
top_100_sum = top_100['Area'].sum()

total = df['Area'].sum()

new = [{"Cat": "Australia", "Area": Australia}, {"Cat": "Pastoral we have", "Area": total},
 {"Cat": "Top 20", "Area": top_20_sum}, {"Cat": "Top 55", "Area": top_55_sum}, 
 {"Cat": "Top 100", "Area": top_100_sum}]

# # total 

new = pd.DataFrame.from_records(new)
new["Percent of Oz"] = (new['Area']/Australia)*100
print(new)

# top_twenty 

# # innaminckha = pd.DataFrame.from_records([{"Station": "Innamincka Station", "State": "SA",
# #  "Owner": "S Kidman & Company", "Category":"Australian", "Area":"1355000", 
# #  "Source":"https://www.kidman.com.au/locations/innamincka/"}])