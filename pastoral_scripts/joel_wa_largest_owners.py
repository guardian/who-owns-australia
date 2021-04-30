import pandas as pd 
from paths import data_path 
pd.set_option("display.max_rows", None, "display.max_columns", None)



fillo = f"{data_path}/pastoral_joel_brand_super_merge.csv"
target = '/largest_pastoral_joel_brand_super_merge.csv'

# fillo = f"{data_path}/largest_pastoral_joel_sheet_download.csv"
# target = '/largest_pastoral_joel_sheet_merged.csv'

df = pd.read_csv(fillo)

# df['Area'] = df['Area'].str.replace(",", '')
df['Area'] = pd.to_numeric(df['Area'])
largest = df.groupby(by='Owner')['Area'].sum().reset_index()

largest = largest.sort_values(by="Area", ascending=False)

# print(largest)

with open(f"{data_path}{target}", 'w') as f:
    largest.to_csv(f, index=False, header=True)


# largest = gdf.groupby(by='Owner')['Area'].sum().reset_index()
# largest = largest.sort_values(by='Area', ascending=False)
# largest['Rank'] = largest['Area'].rank(method='first', ascending=False)

# largest['Area'] = largest['Area']/10000
# largest.rename(columns={'Area':"Hectares"}, inplace=True)

# pd.options.display.float_format = '{:.0f}'.format

# # print(largest)

# # holders = largest['Owner'].values.tolist()

# # listo = []
# # count = 0
# # def get_ratio(string1, string2):
# #     ratio = fuzz.token_sort_ratio(string1, string2)
# #     if (ratio > 85) & (string1 != string2):
# #         # print(string1, string2)
# #         listo.append((string1, string2))

# # for holder in holders:

# #     for second in holders:
# #         print(count)
# #         get_ratio(holder, second)
# #         count += 1


# # print(listo)


# # print(largest)

# # with open(f'{data_path}/final-ish/largest_pastoral_holders.csv', "w") as f:
# #     largest.to_csv(f, index=False, header=True, float_format='%f')