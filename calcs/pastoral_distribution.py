from paths import data_path 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 


## Find what percentage of Pastoral Land is owned by top X landowners

df = pd.read_csv(f'{data_path}/final-ish/largest_pastoral_holders.csv')

total_pastoral = df['Area'].sum()

df['Percentage'] = (df['Area']/total_pastoral) * 100

print(df.loc[df['Rank'] <= 20])
print(df.loc[df['Rank'] <= 20]['Percentage'].sum())

# print(df)

# sns.lineplot(data = df, x = 'Rank', y="Area")
# plt.show()

# print(df)



# ## Find how much of pastoral land is foreign owned

# joel_path = f'{data_path}/Pastoral_ownership_data_2020_08_18_noWA.xlsx'

# df = pd.read_excel(joel_path, sheet_name=1, skiprows=2)

# df = df[['Pastoral Station', 'CCG_cat', 'CCG_owner','CCG_References']]
# df.columns = ['Name', "Category", "Owner", "Source"]

# additional_foreign = ['Australian Agricultural Company', 'Ruyi Group (China)', 'Ruyi Group', "Zenith (Australia) Investment Holding Pty Ltd", 'Yiang Xiang Assets', 'Clean Agriculture and International Tourism', 'Ma Xingfa', 'Cross Pacific Investment', 'Pham Nhat Vu']

# foreign = df.loc[df['Category'].str.contains("Foreign")]['Owner'].values.tolist()
# strayan = df.loc[(df['Category'].str.contains("Australia") | df['Category'].str.contains("Australian"))]['Owner'].values.tolist()

# foreign = foreign + additional_foreign

# largest =  pd.read_csv(f'{data_path}/final-ish/largest_pastoral_holders.csv')

# print(largest.loc[largest['Owner'].isin(foreign)])