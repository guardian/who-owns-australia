import pandas as pd 
from paths import data_path
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time 
from random import randint 

official = f"{data_path}/WA/WApastoral.csv"
df = pd.read_csv(official)

names = df['property_n'].values.tolist()
names = [x.title() for x in names]



start = 324
end = 443


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# driver = webdriver.Chrome(ChromeDriverManager().install())

start_url = "https://spatial.agric.wa.gov.au/brands/scripts/QueryProperty.asp"

test_val = 'MOWANJUM STATION'
grand_list = []

for proper in names[start:]:
    print(proper)
    try:
        driver.get(start_url)

        prop_input = driver.find_element_by_name("P_PropName").send_keys(proper)

        button = driver.find_element_by_name("PropQuery").click()

        time.sleep(1)

        table = pd.read_html(driver.page_source)[0]

        owners = table.loc[table[0] == "Owner Name"][1].values.tolist()

        

        init_listo = []
        for thing in owners:
            init_listo.append({"Station": proper, "Owner": thing})

        init_df = pd.DataFrame(init_listo)
        grand_list.append(init_df)

        time.sleep(randint(3,7))

    except Exception as e:

        print(e)
        time.sleep(3)

        continue

driver.close()
df = pd.concat(grand_list)

old_df = pd.read_csv(f"{data_path}/WA/WA_second_extraction.csv")

comboed = old_df.append(df)

df = comboed.drop_duplicates(subset=["Station", "Owner"])

df = df[['Station', 'Owner']]

with open(f"{data_path}/WA/WA_second_extraction.csv", "w") as f:
    df.to_csv(f, index=False, header=True)

print(df)
print(f"Total number in csv: {len(names)}\n")
print(f"Going from {start} to {end}\n")
# driver.quit()


