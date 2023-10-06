import pandas as pd
import plotly.io as pio
import textwrap

pio.templates.default = "plotly"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format

#----------KLASIRANE 2023----------
# Data import
mesta_2023_3 = pd.read_csv('klasirane/2023/svobodni_mesta_za_3_etap_2023-3 (1).csv')
mesta_2023_4 = pd.read_csv('klasirane/2023/svobodni_mesta_za_4_etap_2023.csv')
mesta_2023_5 = pd.read_csv('klasirane/2023/svobodni_mesta_za_5_etap_2023-1.csv')
klasirane_2023_1 = pd.read_csv('klasirane/2023/min_maх_paralelki_1.etap_2023 (3).csv')
klasirane_2023_2 = pd.read_csv('klasirane/2023/min_max_2_etap_2023 (1).csv')
klasirane_2023_3 = pd.read_csv('klasirane/2023/min_max_po_paralelki_3_etap_2023 (1).csv')
klasirane_2023_4 = pd.read_csv('klasirane/2023/min_max_po_par_4_etap_2023 (1).csv')
kodove_2023 = pd.read_csv('klasirane/2023/Za_saita_s_kodove_baloobrazuvane_2023-12.csv')

# Data Cleaning
klasirane_2023_1_clean = klasirane_2023_1.rename(columns={
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
klasirane_2023_1_clean = klasirane_2023_1_clean.drop(klasirane_2023_1_clean.columns[0], axis=1)
klasirane_2023_1_clean = klasirane_2023_1_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2023_1_clean = klasirane_2023_1_clean[klasirane_2023_1_clean["Код паралелка"].notna()]
klasirane_2023_1_clean = klasirane_2023_1_clean.fillna(0)
klasirane_2023_1_clean = klasirane_2023_1_clean.drop(klasirane_2023_1_clean[klasirane_2023_1_clean["Код паралелка"] == 0].index, axis=0)
klasirane_2023_1_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2023_1_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].astype(float)
klasirane_2023_1_clean["Класиране"] = '1'
klasirane_2023_1_clean["Класиране"] = klasirane_2023_1_clean["Класиране"].astype(int)
klasirane_2023_1_clean["Година"] = "2023"
klasirane_2023_1_clean = klasirane_2023_1_clean.sort_values(by='Мин_бал_о', ascending=False)
klasirane_2023_1_clean.reset_index(drop=True, inplace=True)
klasirane_2023_1_clean = klasirane_2023_1_clean.sort_values(by='Код паралелка')

klasirane_2023_2_clean = klasirane_2023_2.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 6": "Мин_бал_о",
                           "Unnamed: 7": "Мин_бал_м",
                           "Unnamed: 8": "Мин_бал_ж",
                           "Unnamed: 9": "Макс_бал_о",
                           "Unnamed: 10": "Макс_бал_м",
                           "Unnamed: 11": "Макс_бал_ж"})
klasirane_2023_2_clean = klasirane_2023_2_clean.drop([klasirane_2023_2_clean.columns[0], "Unnamed: 5"], axis=1)
klasirane_2023_2_clean = klasirane_2023_2_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2023_2_clean = klasirane_2023_2_clean[klasirane_2023_2_clean["Код паралелка"].notna()]
klasirane_2023_2_clean = klasirane_2023_2_clean.fillna(0)
klasirane_2023_2_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2023_2_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].astype(float)
klasirane_2023_2_clean["Класиране"] = '2'
klasirane_2023_2_clean["Класиране"] = klasirane_2023_2_clean["Класиране"].astype(int)
klasirane_2023_2_clean["Година"] = "2023"
klasirane_2023_2_clean = klasirane_2023_2_clean.sort_values(by='Код паралелка')
klasirane_2023_2_clean.reset_index(drop=True, inplace=True)
klasirane_2023_2_clean.index = klasirane_2023_1_clean.index

klasirane_2023_3_clean = klasirane_2023_3.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 6": "Мин_бал_о",
                           "Unnamed: 7": "Мин_бал_м",
                           "Unnamed: 8": "Мин_бал_ж",
                           "Unnamed: 9": "Макс_бал_о",
                           "Unnamed: 10": "Макс_бал_м",
                           "Unnamed: 11": "Макс_бал_ж"})
klasirane_2023_3_clean = klasirane_2023_3_clean.drop([klasirane_2023_3_clean.columns[0], "Unnamed: 5"], axis=1)
klasirane_2023_3_clean = klasirane_2023_3_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2023_3_clean = klasirane_2023_3_clean[klasirane_2023_3_clean["Код паралелка"].notna()]
klasirane_2023_3_clean = klasirane_2023_3_clean.fillna(0)
klasirane_2023_3_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2023_3_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].astype(float)
klasirane_2023_3_clean["Класиране"] = '3'
klasirane_2023_3_clean["Класиране"] = klasirane_2023_3_clean["Класиране"].astype(int)
klasirane_2023_3_clean["Година"] = "2023"
klasirane_2023_3_clean = klasirane_2023_3_clean.sort_values(by='Код паралелка')
klasirane_2023_3_clean.reset_index(drop=True, inplace=True)
klasirane_2023_3_clean.index = klasirane_2023_1_clean.index

klasirane_2023_4_clean = klasirane_2023_4.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 6": "Мин_бал_о",
                           "Unnamed: 7": "Мин_бал_м",
                           "Unnamed: 8": "Мин_бал_ж",
                           "Unnamed: 9": "Макс_бал_о",
                           "Unnamed: 10": "Макс_бал_м",
                           "Unnamed: 11": "Макс_бал_ж"})
klasirane_2023_4_clean = klasirane_2023_4_clean.drop([klasirane_2023_4_clean.columns[0], "Unnamed: 5"], axis=1)
klasirane_2023_4_clean = klasirane_2023_4_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2023_4_clean = klasirane_2023_4_clean[klasirane_2023_4_clean["Код паралелка"].notna()]
klasirane_2023_4_clean = klasirane_2023_4_clean.fillna(0)
klasirane_2023_4_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2023_4_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].astype(float)
klasirane_2023_4_clean["Класиране"] = '4'
klasirane_2023_4_clean["Класиране"] = klasirane_2023_4_clean["Класиране"].astype(int)
klasirane_2023_4_clean["Година"] = "2023"
klasirane_2023_4_clean = klasirane_2023_4_clean.sort_values(by='Код паралелка')
klasirane_2023_4_clean.reset_index(drop=True, inplace=True)
klasirane_2023_4_clean.index = klasirane_2023_1_clean.index

# For future functionalities ready to use cleaning model of the codes
# kodove_2023_cleaan = kodove_2023.rename(columns={
#                            "Unnamed: 1": "РАЙОН",
#                            "Unnamed: 2": "Училище",
#                            "Unnamed: 3": "Код паралелка",
#                            "Unnamed: 4": "Паралелка",
#                            "Unnamed: 5": "Вид на паралелката",
#                            "Unnamed: 6": "Балообразуване",
#                            "Unnamed: 7": "Форма на обучение",
#                            "Unnamed: 8": "Брой паралелки",
#                            "Unnamed: 9": "Общо основание",
#                            "Unnamed: 10": "Младежи",
#                            "Unnamed: 11": "Девойки"})
# kodove_2023_cleaan = kodove_2023_cleaan.drop(['СПИСЪК НА ПАРАЛЕЛКИТЕ С ДЪРЖАВЕН ПЛАН-ПРИЕМ В VIII КЛАС ЗА УЧЕБНАТА 2023/2024 ГОДИНА В ОБЛАСТ СОФИЯ-ГРАД \nс кодове и балообразуване'], axis=1)
# kodove_2023_cleaan = kodove_2023_cleaan[kodove_2023_cleaan["Код паралелка"].notna()]
# kodove_2023_cleaan = kodove_2023_cleaan.drop([1], axis=0)
# kodove_2023_cleaan["Година"] = "2023"
# kodove_2023_cleaan.reset_index(drop=True, inplace=True)

# Svobodni mesta data clean up
mesta_2023_3_clean = mesta_2023_3.drop([mesta_2023_3.columns[0], 'Unnamed: 5'], axis=1)
mesta_2023_3_clean = mesta_2023_3_clean.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 6": "Места_о",
                           "Unnamed: 7": "Места_м",
                           "Unnamed: 8": "Места_д",})
mesta_2023_3_clean = mesta_2023_3_clean[mesta_2023_3_clean["Код паралелка"].notna()]
mesta_2023_3_clean = mesta_2023_3_clean.drop([2, 3], axis=0)
mesta_2023_3_clean = mesta_2023_3_clean.fillna(0)
mesta_2023_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_3_clean[["Места_о", "Места_м", "Места_д"]].replace('-', 0)
mesta_2023_3_clean["Класиране"] = 3
mesta_2023_3_clean[["Места_о", "Места_м", "Места_д", "Класиране"]] = mesta_2023_3_clean[["Места_о", "Места_м", "Места_д", "Класиране"]].astype(int)
mesta_2023_3_clean['Места_общ_брой'] = mesta_2023_3_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2023_3_clean['Места_общ_брой_м'] = mesta_2023_3_clean[["Места_о", "Места_м"]].sum(axis=1)
mesta_2023_3_clean['Места_общ_брой_д'] = mesta_2023_3_clean[["Места_о", "Места_д"]].sum(axis=1)
mesta_2023_3_clean["Година"] = "2023"
mesta_2023_3_clean = mesta_2023_3_clean.sort_values(by='Код паралелка')
mesta_2023_3_clean.reset_index(drop=True, inplace=True)
mesta_2023_3_clean.index = klasirane_2023_3_clean.index
klasirane_2023_3_clean_plus = pd.concat([klasirane_2023_3_clean, mesta_2023_3_clean], axis=1, copy=False, ignore_index=False)
klasirane_2023_3_clean_plus = klasirane_2023_3_clean_plus.loc[:, ~klasirane_2023_3_clean_plus.columns.duplicated()].copy()

mesta_2023_4_clean = mesta_2023_4.drop([mesta_2023_4.columns[0], 'Unnamed: 5'], axis=1)
mesta_2023_4_clean = mesta_2023_4_clean.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 6": "Места_о",
                           "Unnamed: 7": "Места_м",
                           "Unnamed: 8": "Места_д",})
mesta_2023_4_clean = mesta_2023_4_clean[mesta_2023_4_clean["Код паралелка"].notna()]
mesta_2023_4_clean = mesta_2023_4_clean.drop([2, 3], axis=0)
mesta_2023_4_clean = mesta_2023_4_clean.fillna(0)
mesta_2023_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_4_clean[["Места_о", "Места_м", "Места_д"]].replace('-', 0)
mesta_2023_4_clean["Класиране"] = 4
mesta_2023_4_clean[["Места_о", "Места_м", "Места_д", "Класиране"]] = mesta_2023_4_clean[["Места_о", "Места_м", "Места_д", "Класиране"]].astype(int)
mesta_2023_4_clean['Места_общ_брой'] = mesta_2023_4_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2023_4_clean['Места_общ_брой_м'] = mesta_2023_4_clean[["Места_о", "Места_м"]].sum(axis=1)
mesta_2023_4_clean['Места_общ_брой_д'] = mesta_2023_4_clean[["Места_о", "Места_д"]].sum(axis=1)
mesta_2023_4_clean["Година"] = "2023"
mesta_2023_4_clean = mesta_2023_4_clean.sort_values(by='Код паралелка')
mesta_2023_4_clean.reset_index(drop=True, inplace=True)
mesta_2023_4_clean.index = klasirane_2023_4_clean.index
klasirane_2023_4_clean_plus = pd.concat([klasirane_2023_4_clean, mesta_2023_4_clean], axis=1, copy=False, ignore_index=False)
klasirane_2023_4_clean_plus = klasirane_2023_4_clean_plus.loc[:, ~klasirane_2023_4_clean_plus.columns.duplicated()].copy()

mesta_2023_5_clean = mesta_2023_5.drop([mesta_2023_5.columns[0], 'Unnamed: 5', 'Unnamed: 9'], axis=1)
mesta_2023_5_clean = mesta_2023_5_clean.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 6": "Места_о",
                           "Unnamed: 7": "Места_м",
                           "Unnamed: 8": "Места_д",})
mesta_2023_5_clean = mesta_2023_5_clean[mesta_2023_5_clean["Код паралелка"].notna()]
mesta_2023_5_clean = mesta_2023_5_clean.drop([2, 3], axis=0)
# df = mesta_2023_5_clean[mesta_2023_5_clean['Код паралелка'].isin(klasirane_2023_1_clean['Код паралелка']) == False]
# print(df) #Paraalaka kod 0374 and 3191 are only in the last file and will be removed for the moment.
mesta_2023_5_clean = mesta_2023_5_clean[mesta_2023_5_clean['Код паралелка'].isin(klasirane_2023_1_clean['Код паралелка'])]
mesta_2023_5_clean = mesta_2023_5_clean.fillna(0)
mesta_2023_5_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_5_clean[["Места_о", "Места_м", "Места_д"]].replace('-', 0)
mesta_2023_5_clean["Класиране"] = 5
mesta_2023_5_clean[["Места_о", "Места_м", "Места_д", "Класиране"]] = mesta_2023_5_clean[["Места_о", "Места_м", "Места_д", "Класиране"]].astype(int)
mesta_2023_5_clean['Места_общ_брой'] = mesta_2023_5_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2023_5_clean['Места_общ_брой_м'] = mesta_2023_5_clean[["Места_о", "Места_м"]].sum(axis=1)
mesta_2023_5_clean['Места_общ_брой_д'] = mesta_2023_5_clean[["Места_о", "Места_д"]].sum(axis=1)
mesta_2023_5_clean["Година"] = "2023"
mesta_2023_5_clean = mesta_2023_5_clean.sort_values(by='Код паралелка')
mesta_2023_5_clean.reset_index(drop=True, inplace=True)
mesta_2023_5_clean.index = klasirane_2023_1_clean.index
mesta_2023_5_clean_ordered = pd.concat([klasirane_2023_1_clean, mesta_2023_5_clean], axis=1, copy=False, ignore_index=False)
mesta_2023_5_clean_ordered = mesta_2023_5_clean_ordered.sort_index()
mesta_2023_5_clean_ordered = mesta_2023_5_clean_ordered.loc[:, ~mesta_2023_5_clean_ordered.columns.duplicated()].copy()
mesta_2023_5_clean_ordered = mesta_2023_5_clean_ordered.drop(['Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж'], axis=1)
mesta_2023_5_clean_ordered['Класиране'] = 5

# Data preparation
klasirane_2023_combined = pd.concat([klasirane_2023_1_clean.sort_index(), klasirane_2023_2_clean.sort_index(), klasirane_2023_3_clean_plus.sort_index(), klasirane_2023_4_clean_plus.sort_index(), mesta_2023_5_clean_ordered.sort_index()], axis=0)
klasirane_2023_combined.reset_index(drop=True, inplace=True)

code_to_uchilishte_map = dict(klasirane_2023_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
code_to_paral_map = dict(zip(klasirane_2023_combined['Код паралелка'], klasirane_2023_combined['Паралелка']))

yticks_text2_2023 = [
    f"{code}-{'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=25))}"
    for code in klasirane_2023_combined['Код паралелка'].unique()
]

yticks_text2_2023_mobile = [
    f"{code}"
    for code in klasirane_2023_combined['Код паралелка'].unique()
]

# yticks_text2 = [
#     f"{code}<br>{code_to_paral_map[code][:45]}<br>{code_to_uchilishte_map[code][:45]}..."
#     for code in klasirane_2023_combined['Код паралелка'].unique()
# ]

# yticks_text2 = [
#     f"{code}<br>{code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
#     for code in klasirane_2023_combined['Код паралелка'].unique()
# ]

# yticks_text2 = [
#     f"{code} - {code_to_paral_map[code]:<40}..."  # Adjust the width as needed
#     for code in klasirane_2023_combined['Код паралелка'].unique()
# ]


