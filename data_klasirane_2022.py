import pandas as pd
import plotly.io as pio
import textwrap

pio.templates.default = "plotly"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format

#----------KLASIRANE 2022----------
# Data import
mesta_2022_3 = pd.read_csv('klasirane/2022/free_IIIetap_sait (7).csv')
mesta_2022_4 = pd.read_csv('klasirane/2022/svobodni_mesta_sled_IIIetap_2022 (2).csv')
klasirane_2022_1 = pd.read_csv('klasirane/2022/po_bal_sait (5).csv')
klasirane_2022_2 = pd.read_csv('klasirane/2022/min_max_2_etap_2022 (5).csv')
klasirane_2022_3 = pd.read_csv('klasirane/2022/min_max_III_etap (3).csv')


# Data Cleaning
klasirane_2022_1_clean = klasirane_2022_1.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 5": "Мин_бал_о",
                           "Unnamed: 6": "Мин_бал_м",
                           "Unnamed: 7": "Мин_бал_ж",
                           "Unnamed: 8": "Макс_бал_о",
                           "Unnamed: 9": "Макс_бал_м",
                           "Unnamed: 10": "Макс_бал_ж"})
klasirane_2022_1_clean = klasirane_2022_1_clean.drop(klasirane_2022_1_clean.columns[0], axis=1)
klasirane_2022_1_clean = klasirane_2022_1_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2022_1_clean = klasirane_2022_1_clean[klasirane_2022_1_clean["Код паралелка"].notna()]
klasirane_2022_1_clean = klasirane_2022_1_clean.fillna(0)
klasirane_2022_1_clean = klasirane_2022_1_clean.drop(klasirane_2022_1_clean[klasirane_2022_1_clean["Код паралелка"] == 0].index, axis=0)
klasirane_2022_1_clean = klasirane_2022_1_clean[~klasirane_2022_1_clean['Код паралелка'].isin(['0374', '3191'])] # Those 2 are removed in 2023 as well as the approach for the exam is different
klasirane_2022_1_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2022_1_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].astype(float)
klasirane_2022_1_clean["Класиране"] = '1'
klasirane_2022_1_clean["Класиране"] = klasirane_2022_1_clean["Класиране"].astype(int)
klasirane_2022_1_clean["Година"] = "2022"
klasirane_2022_1_clean = klasirane_2022_1_clean.sort_values(by='Мин_бал_о', ascending=False)
klasirane_2022_1_clean.reset_index(drop=True, inplace=True)
klasirane_2022_1_clean = klasirane_2022_1_clean.sort_values(by='Код паралелка')

klasirane_2022_2_clean = klasirane_2022_2.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 5": "Мин_бал_о",
                           "Unnamed: 6": "Мин_бал_м",
                           "Unnamed: 7": "Мин_бал_ж",
                           "Unnamed: 8": "Макс_бал_о",
                           "Unnamed: 9": "Макс_бал_м",
                           "Unnamed: 10": "Макс_бал_ж"})
klasirane_2022_2_clean = klasirane_2022_2_clean.drop(klasirane_2022_2_clean.columns[0], axis=1)
klasirane_2022_2_clean = klasirane_2022_2_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2022_2_clean = klasirane_2022_2_clean[klasirane_2022_2_clean["Код паралелка"].notna()]
difference_2022_2 = klasirane_2022_1_clean[~klasirane_2022_1_clean['Код паралелка'].isin(klasirane_2022_2_clean['Код паралелка'])] # The difference between klasirane 1 and 2 is cleaned by adding the items in klasirane 2, but assuming 0 scores for (nobody was accepted in those, as nobody wanted them)
difference_2022_2 = difference_2022_2[["Код училище", "Училище", "Код паралелка", "Паралелка"]]
klasirane_2022_2_clean = pd.concat([klasirane_2022_2_clean, difference_2022_2], axis=0)
klasirane_2022_2_clean = klasirane_2022_2_clean.fillna(0)
klasirane_2022_2_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2022_2_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].astype(float)
klasirane_2022_2_clean["Класиране"] = '2'
klasirane_2022_2_clean["Класиране"] = klasirane_2022_2_clean["Класиране"].astype(int)
klasirane_2022_2_clean["Година"] = "2022"
klasirane_2022_2_clean = klasirane_2022_2_clean.sort_values(by='Код паралелка')
klasirane_2022_2_clean.reset_index(drop=True, inplace=True)
klasirane_2022_2_clean.index = klasirane_2022_1_clean.index

klasirane_2022_3_clean = klasirane_2022_3.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 5": "Мин_бал_о",
                           "Unnamed: 6": "Мин_бал_м",
                           "Unnamed: 7": "Мин_бал_ж",
                           "Unnamed: 8": "Макс_бал_о",
                           "Unnamed: 9": "Макс_бал_м",
                           "Unnamed: 10": "Макс_бал_ж"})
klasirane_2022_3_clean = klasirane_2022_3_clean.drop(klasirane_2022_3_clean.columns[0], axis=1)
klasirane_2022_3_clean = klasirane_2022_3_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2022_3_clean = klasirane_2022_3_clean[klasirane_2022_3_clean["Код паралелка"].notna()]
difference_2022_3 = klasirane_2022_1_clean[~klasirane_2022_1_clean['Код паралелка'].isin(klasirane_2022_3_clean['Код паралелка'])] # The difference between klasirane 1 and 3 is cleaned by adding the items in klasirane 3, but assuming 0 scores for (nobody was accepted in those, as nobody wanted them)
difference_2022_3 = difference_2022_3[["Код училище", "Училище", "Код паралелка", "Паралелка"]]
klasirane_2022_3_clean = pd.concat([klasirane_2022_3_clean, difference_2022_3], axis=0)
klasirane_2022_3_clean = klasirane_2022_3_clean.fillna(0)
klasirane_2022_3_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2022_3_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].astype(float)
klasirane_2022_3_clean["Класиране"] = '3'
klasirane_2022_3_clean["Класиране"] = klasirane_2022_3_clean["Класиране"].astype(int)
klasirane_2022_3_clean["Година"] = "2022"
klasirane_2022_3_clean = klasirane_2022_3_clean.sort_values(by='Код паралелка')
klasirane_2022_3_clean.reset_index(drop=True, inplace=True)
klasirane_2022_3_clean.index = klasirane_2022_1_clean.index

# Svobodni mesta data clean up
mesta_2022_3_clean = mesta_2022_3.drop(mesta_2022_3.columns[0], axis=1)
mesta_2022_3_clean = mesta_2022_3_clean.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 5": "Места_о",
                           "Unnamed: 6": "Места_м",
                           "Unnamed: 7": "Места_д",})
mesta_2022_3_clean = mesta_2022_3_clean[mesta_2022_3_clean["Код паралелка"].notna()]
mesta_2022_3_clean = mesta_2022_3_clean.drop([2, 3], axis=0)
mesta_2022_3_clean = pd.concat([mesta_2022_3_clean, difference_2022_3], axis=0)
mesta_2022_3_clean = mesta_2022_3_clean.fillna(0)
mesta_2022_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2022_3_clean[["Места_о", "Места_м", "Места_д"]].replace('-', 0)
mesta_2022_3_clean["Класиране"] = 3
mesta_2022_3_clean[["Места_о", "Места_м", "Места_д", "Класиране"]] = mesta_2022_3_clean[["Места_о", "Места_м", "Места_д", "Класиране"]].astype(int)
mesta_2022_3_clean['Места_общ_брой'] = mesta_2022_3_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2022_3_clean["Година"] = "2022"
mesta_2022_3_clean = mesta_2022_3_clean.sort_values(by='Код паралелка')
mesta_2022_3_clean.reset_index(drop=True, inplace=True)
mesta_2022_3_clean.index = klasirane_2022_3_clean.index
klasirane_2022_3_clean_plus = pd.concat([klasirane_2022_3_clean, mesta_2022_3_clean], axis=1, copy=False, ignore_index=False)
klasirane_2022_3_clean_plus = klasirane_2022_3_clean_plus.loc[:, ~klasirane_2022_3_clean_plus.columns.duplicated()].copy()

mesta_2022_4_clean = mesta_2022_4.drop(mesta_2022_4.columns[0], axis=1)
mesta_2022_4_clean = mesta_2022_4_clean.rename(columns={
                           "Unnamed: 1": "Училище",
                           "Unnamed: 2": "Код паралелка",
                           "Unnamed: 3": "Паралелка",
                           "Unnamed: 4": "Места_о",
                           "Unnamed: 5": "Места_м",
                           "Unnamed: 6": "Места_д",})
mesta_2022_4_clean = mesta_2022_4_clean[mesta_2022_4_clean["Код паралелка"].notna()]
mesta_2022_4_clean = mesta_2022_4_clean.drop([0], axis=0)
difference_2022_4 = klasirane_2022_1_clean[~klasirane_2022_1_clean['Код паралелка'].isin(mesta_2022_4_clean['Код паралелка'])] # The difference between klasirane 1 and mesta for klasirane 4 is cleaned by adding the items in mesta 4, but assuming 0 scores for (nobody was accepted in those, as nobody wanted them)
difference_2022_4 = difference_2022_4[["Код училище", "Училище", "Код паралелка", "Паралелка"]]
mesta_2022_4_clean = mesta_2022_4_clean[~mesta_2022_4_clean['Код паралелка'].isin(['0374', '3191'])] # Those 2 are removed in 2023 as well as the approach for the exam is different
mesta_2022_4_clean = pd.concat([mesta_2022_4_clean, difference_2022_4], axis=0)
mesta_2022_4_clean = mesta_2022_4_clean.fillna(0)
mesta_2022_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2022_4_clean[["Места_о", "Места_м", "Места_д"]].replace('-', 0)
mesta_2022_4_clean["Класиране"] = 4
mesta_2022_4_clean[["Места_о", "Места_м", "Места_д", "Класиране"]] = mesta_2022_4_clean[["Места_о", "Места_м", "Места_д", "Класиране"]].astype(int)
mesta_2022_4_clean['Места_общ_брой'] = mesta_2022_4_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2022_4_clean["Година"] = "2022"
mesta_2022_4_clean = mesta_2022_4_clean.sort_values(by='Код паралелка')
mesta_2022_4_clean["Код училище"] = mesta_2022_3_clean["Код училище"]
mesta_2022_4_clean.reset_index(drop=True, inplace=True)
mesta_2022_4_clean.index = klasirane_2022_1_clean.index

# Data preparation
klasirane_2022_combined = pd.concat([klasirane_2022_1_clean.sort_index(), klasirane_2022_2_clean.sort_index(), klasirane_2022_3_clean_plus.sort_index(), mesta_2022_4_clean.sort_index()], axis=0)
klasirane_2022_combined.reset_index(drop=True, inplace=True)

code_to_uchilishte_map = dict(klasirane_2022_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
code_to_paral_map = dict(zip(klasirane_2022_combined['Код паралелка'], klasirane_2022_combined['Паралелка']))

yticks_text2_2022 = [
    f"{code}-{'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=25))}"
    for code in klasirane_2022_combined['Код паралелка'].unique()
]

# yticks_text2 = [
#     f"{code}"
#     for code in klasirane_2022_combined['Код паралелка'].unique()
# ]

# yticks_text2 = [
#     f"{code}<br>{code_to_paral_map[code][:45]}<br>{code_to_uchilishte_map[code][:45]}..."
#     for code in klasirane_2022_combined['Код паралелка'].unique()
# ]

# yticks_text2 = [
#     f"{code}<br>{code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
#     for code in klasirane_2022_combined['Код паралелка'].unique()
# ]

# yticks_text2 = [
#     f"{code} - {code_to_paral_map[code]:<40}..."  # Adjust the width as needed
#     for code in klasirane_2022_combined['Код паралелка'].unique()
# ]
#  Steps to perform for every year update:
# 1. Copy data_klasirane_LAST YEAR into a new file
# 2. Import correct files from the respective folder
# 3. Replace YEAR with the year you want everywhere
# 4. Change the name of the 1st column for every file
# 5. Check if difference in records in the 3 klasirane and mesta and add the difference ass needed (done for 2022)