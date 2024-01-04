# INSTRUCTIONS FOR NEW YEAR FILES IMPORT, CLEANING, STANDARTISATION
# 1. Copy data_klasirane_LAST YEAR into a new py file
# 2. Import correct files from the respective folder
# 3. Replace YEAR with the year you want everywhere
# 4. Check if difference in records in the 3 klasirane and mesta and add the difference as needed
# to the highest possible
# 5. Run data check and specifically check orders, numbers, types

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_colwidth', None)

# ----------KLASIRANE 2021----------
# Data import
mesta_2021_3 = pd.read_csv('klasirane/2021/Свободни_места_трети_етап-1.csv')
mesta_2021_4 = pd.read_csv('klasirane/2021/svobodni_mesta_za_4_etap_2021.csv')
mesta_2021_5 = pd.read_csv('klasirane/2021/Справка-свободни-места-към-03.09.21.csv')
klasirane_2021_1 = pd.read_csv('klasirane/2021/За_СайтаСправка_за_мин_мак_по_паралелки_сорт_мин_3rtf (1).csv')
klasirane_2021_2 = pd.read_csv('klasirane/2021/Spravka_min_max_par_2_klasirane_21_22.csv')
klasirane_2021_3 = pd.read_csv('klasirane/2021/spravka_min_max_3_klasirane.csv')
kodove_2021 = pd.read_csv('klasirane/2021/za_saita_s_kodove_22_06.csv')

# DATA STRUCTURING
# Clean model for codes
kodove_2021_clean = kodove_2021.rename(columns={
                           "Unnamed: 1": "Район",
                           "Unnamed: 2": "Код училище",
                           "Unnamed: 3": "Училище",
                           "Unnamed: 4": "Код паралелка",
                           "Unnamed: 5": "Паралелка",
                           "Unnamed: 6": "Вид на паралелката",
                           "Unnamed: 7": "Балообразуване",
                           "Unnamed: 8": "Брой паралелки",
                           "Unnamed: 9": "Места_о",
                           "Unnamed: 10": "Места_м",
                           "Unnamed: 11": "Места_д"})
kodove_2021_clean = kodove_2021_clean.drop(kodove_2021_clean.columns[0], axis=1)
kodove_2021_clean = kodove_2021_clean[kodove_2021_clean["Код паралелка"].notna()]
kodove_2021_clean = kodove_2021_clean.drop([1], axis=0)
kodove_2021_clean[["Места_о", "Места_м", "Места_д"]] = kodove_2021_clean[["Места_о", "Места_м", "Места_д"]].astype(int)
kodove_2021_clean['Места_общ_брой'] = kodove_2021_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
kodove_2021_clean['Места_общ_брой_м'] = kodove_2021_clean[["Места_о", "Места_м"]].sum(axis=1)
kodove_2021_clean['Места_общ_брой_д'] = kodove_2021_clean[["Места_о", "Места_д"]].sum(axis=1)
kodove_2021_clean["Година"] = "2021"
kodove_2021_clean = kodove_2021_clean.sort_values(by='Код паралелка')
kodove_2021_clean.reset_index(drop=True, inplace=True)
# print(f'Kodove: {kodove_2021_clean.shape}')

# KLASIRANE 1
klasirane_2021_1_clean = klasirane_2021_1.drop("№ по ред", axis=1)
klasirane_2021_1_clean[['Код училище', 'Име училище']] = klasirane_2021_1['Училище'].str.split(' ', n=1, expand=True)
klasirane_2021_1_clean[['Код паралелка', 'Име паралелка']] = klasirane_2021_1['Паралелка'].\
    str.split(' ', n=1, expand=True)
klasirane_2021_1_clean = klasirane_2021_1_clean.drop(['Училище', 'Паралелка'], axis=1)
klasirane_2021_1_clean["Мин_бал_о"] = 0
klasirane_2021_1_clean["Мин_бал_м"] = 0
klasirane_2021_1_clean["Мин_бал_ж"] = 0
klasirane_2021_1_clean.loc[klasirane_2021_1_clean['Пол'] == 'без квоти', 'Мин_бал_о'] = \
    klasirane_2021_1_clean['Минимален бал']
klasirane_2021_1_clean.loc[klasirane_2021_1_clean['Пол'] == 'младежи', 'Мин_бал_м'] = \
    klasirane_2021_1_clean['Минимален бал']
klasirane_2021_1_clean.loc[klasirane_2021_1_clean['Пол'] == 'девойки', 'Мин_бал_ж'] = \
    klasirane_2021_1_clean['Минимален бал']
klasirane_2021_1_clean["Макс_бал_о"] = 0
klasirane_2021_1_clean["Макс_бал_м"] = 0
klasirane_2021_1_clean["Макс_бал_ж"] = 0
klasirane_2021_1_clean.loc[klasirane_2021_1_clean['Пол'] == 'без квоти', 'Макс_бал_о'] = \
    klasirane_2021_1_clean['Максимален бал']
klasirane_2021_1_clean.loc[klasirane_2021_1_clean['Пол'] == 'младежи', 'Макс_бал_м'] = \
    klasirane_2021_1_clean['Максимален бал']
klasirane_2021_1_clean.loc[klasirane_2021_1_clean['Пол'] == 'девойки', 'Макс_бал_ж'] = \
    klasirane_2021_1_clean['Максимален бал']
klasirane_2021_1_clean = klasirane_2021_1_clean.groupby('Код паралелка', as_index=False).sum()
klasirane_2021_1_clean["Мин_бал_о"] = klasirane_2021_1_clean.apply(
    lambda row: min(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_о"] == 0 else row["Мин_бал_о"], axis=1)
klasirane_2021_1_clean["Макс_бал_о"] = klasirane_2021_1_clean.apply(
    lambda row: max(row["Макс_бал_м"], row["Макс_бал_ж"]) if row["Макс_бал_о"] == 0 else row["Макс_бал_о"], axis=1)
klasirane_2021_1_clean = klasirane_2021_1_clean.sort_values(by='Код паралелка')
klasirane_2021_1_clean.reset_index(drop=True, inplace=True)
klasirane_2021_1_clean = pd.merge(kodove_2021_clean, klasirane_2021_1_clean, on="Код паралелка", how='outer')
klasirane_2021_1_clean["Класиране"] = 1
klasirane_2021_1_clean = klasirane_2021_1_clean.sort_values(by='Мин_бал_о', ascending=False)
klasirane_2021_1_clean.reset_index(drop=True, inplace=True)
klasirane_2021_1_clean = klasirane_2021_1_clean.sort_values(by='Код паралелка')
klasirane_2021_1_clean['Код училище'] = klasirane_2021_1_clean['Код училище_x']
klasirane_2021_1_clean = klasirane_2021_1_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                                'Балообразуване', 'Брой паралелки',  'Година', 'Код училище', 'Места_о',
                                                 'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                 'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
basic_data_2021 = klasirane_2021_1_clean[['Район', 'Училище',  'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                          'Балообразуване', 'Брой паралелки', 'Година', 'Код училище']]
# print(f'Klasirane 1: {klasirane_2021_1_clean.shape}')

# # Find and print items that are in kodove_set but not in klasirane_set
# set1 = set(kodove_2021_clean["Код паралелка"])
# set2 = set(klasirane_2021_1_clean["Код паралелка"])
# different_items = set1 - set2
# for k in different_items:
#     print(k)

# KLASIRANE 2
klasirane_2021_2_clean = klasirane_2021_2.drop("№ по ред", axis=1)
klasirane_2021_2_clean[['Код паралелка', 'Име паралелка']] = klasirane_2021_2['Паралелка'].\
    str.split(' ', n=1, expand=True)
klasirane_2021_2_clean = klasirane_2021_2_clean.drop(['Училище', 'Паралелка'], axis=1)
klasirane_2021_2_clean["Мин_бал_о"] = 0
klasirane_2021_2_clean["Мин_бал_м"] = 0
klasirane_2021_2_clean["Мин_бал_ж"] = 0
klasirane_2021_2_clean.loc[klasirane_2021_2_clean['Пол'] == 'без квоти', 'Мин_бал_о'] = \
    klasirane_2021_2_clean['Минимален бал']
klasirane_2021_2_clean.loc[klasirane_2021_2_clean['Пол'] == 'младежи', 'Мин_бал_м'] = \
    klasirane_2021_2_clean['Минимален бал']
klasirane_2021_2_clean.loc[klasirane_2021_2_clean['Пол'] == 'девойки', 'Мин_бал_ж'] = \
    klasirane_2021_2_clean['Минимален бал']
klasirane_2021_2_clean["Макс_бал_о"] = 0
klasirane_2021_2_clean["Макс_бал_м"] = 0
klasirane_2021_2_clean["Макс_бал_ж"] = 0
klasirane_2021_2_clean.loc[klasirane_2021_2_clean['Пол'] == 'без квоти', 'Макс_бал_о'] = \
    klasirane_2021_2_clean['Максимален бал']
klasirane_2021_2_clean.loc[klasirane_2021_2_clean['Пол'] == 'младежи', 'Макс_бал_м'] = \
    klasirane_2021_2_clean['Максимален бал']
klasirane_2021_2_clean.loc[klasirane_2021_2_clean['Пол'] == 'девойки', 'Макс_бал_ж'] = \
    klasirane_2021_2_clean['Максимален бал']
klasirane_2021_2_clean = klasirane_2021_2_clean.groupby('Код паралелка', as_index=False).sum()
klasirane_2021_2_clean["Мин_бал_о"] = klasirane_2021_2_clean.apply(
    lambda row: min(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_о"] == 0 else row["Мин_бал_о"], axis=1)
klasirane_2021_2_clean["Макс_бал_о"] = klasirane_2021_2_clean.apply(
    lambda row: max(row["Макс_бал_м"], row["Макс_бал_ж"]) if row["Макс_бал_о"] == 0 else row["Макс_бал_о"], axis=1)
klasirane_2021_2_clean = klasirane_2021_2_clean.sort_values(by='Код паралелка')
klasirane_2021_2_clean.reset_index(drop=True, inplace=True)
klasirane_2021_2_clean = pd.merge(basic_data_2021, klasirane_2021_2_clean, on="Код паралелка", how='outer')
klasirane_2021_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
    np.nan
klasirane_2021_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
    klasirane_2021_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м',
                            'Места_общ_брой_д']].apply(pd.to_numeric, errors='coerce').astype("Int64")
klasirane_2021_2_clean["Класиране"] = 2
klasirane_2021_2_clean = klasirane_2021_2_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                                'Балообразуване', 'Брой паралелки',  'Година', 'Код училище', 'Места_о',
                                                 'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                 'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
klasirane_2021_2_clean.index = klasirane_2021_1_clean.index
# print(f'Klasirane 2: {klasirane_2021_2_clean.shape}')

# KLASIRANE 3
mesta_2021_3_clean = mesta_2021_3.drop(mesta_2021_3.columns[[0, 3, 4, 5]], axis=1)
mesta_2021_3_clean = mesta_2021_3_clean.rename(columns={
                           "Unnamed: 2": "Код паралелка",
                           "Unnamed: 6": "Места_о",
                           "Unnamed: 7": "Места_м",
                           "Unnamed: 8": "Места_д"})
mesta_2021_3_clean = mesta_2021_3_clean[mesta_2021_3_clean["Код паралелка"].notna()]
mesta_2021_3_clean = mesta_2021_3_clean.drop(0, axis=0)
mesta_2021_3_clean = mesta_2021_3_clean.fillna(0)
mesta_2021_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2021_3_clean[["Места_о", "Места_м", "Места_д"]].\
    replace('-', 0)
mesta_2021_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2021_3_clean[["Места_о", "Места_м", "Места_д"]].\
    astype(int)
mesta_2021_3_clean['Места_общ_брой'] = mesta_2021_3_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2021_3_clean['Места_общ_брой_м'] = mesta_2021_3_clean[["Места_о", "Места_м"]].sum(axis=1)
mesta_2021_3_clean['Места_общ_брой_д'] = mesta_2021_3_clean[["Места_о", "Места_д"]].sum(axis=1)
mesta_2021_3_clean = pd.merge(basic_data_2021, mesta_2021_3_clean, on="Код паралелка", how='outer')
mesta_2021_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
    mesta_2021_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']].\
    apply(pd.to_numeric, errors='coerce').astype("Int64")
mesta_2021_3_clean["Класиране"] = 3
mesta_2021_3_clean = mesta_2021_3_clean.sort_values(by='Код паралелка')
mesta_2021_3_clean.reset_index(drop=True, inplace=True)
mesta_2021_3_clean.index = klasirane_2021_1_clean.index

klasirane_2021_3_clean = klasirane_2021_3.drop("№ по ред", axis=1)
klasirane_2021_3_clean[['Код паралелка', 'Име паралелка']] = klasirane_2021_3['Паралелка'].\
    str.split(' ', n=1, expand=True)
klasirane_2021_3_clean = klasirane_2021_3_clean.drop(['Училище', 'Паралелка'], axis=1)
klasirane_2021_3_clean["Мин_бал_о"] = 0
klasirane_2021_3_clean["Мин_бал_м"] = 0
klasirane_2021_3_clean["Мин_бал_ж"] = 0
klasirane_2021_3_clean.loc[klasirane_2021_3_clean['Пол'] == 'без квоти', 'Мин_бал_о'] = \
    klasirane_2021_3_clean['Минимален бал']
klasirane_2021_3_clean.loc[klasirane_2021_3_clean['Пол'] == 'младежи', 'Мин_бал_м'] = \
    klasirane_2021_3_clean['Минимален бал']
klasirane_2021_3_clean.loc[klasirane_2021_3_clean['Пол'] == 'девойки', 'Мин_бал_ж'] = \
    klasirane_2021_3_clean['Минимален бал']
klasirane_2021_3_clean["Макс_бал_о"] = 0
klasirane_2021_3_clean["Макс_бал_м"] = 0
klasirane_2021_3_clean["Макс_бал_ж"] = 0
klasirane_2021_3_clean.loc[klasirane_2021_3_clean['Пол'] == 'без квоти', 'Макс_бал_о'] = \
    klasirane_2021_3_clean['Максимален бал']
klasirane_2021_3_clean.loc[klasirane_2021_3_clean['Пол'] == 'младежи', 'Макс_бал_м'] = \
    klasirane_2021_3_clean['Максимален бал']
klasirane_2021_3_clean.loc[klasirane_2021_3_clean['Пол'] == 'девойки', 'Макс_бал_ж'] = \
    klasirane_2021_3_clean['Максимален бал']
klasirane_2021_3_clean = klasirane_2021_3_clean.groupby('Код паралелка', as_index=False).sum()
klasirane_2021_3_clean["Мин_бал_о"] = klasirane_2021_3_clean.apply(
    lambda row: min(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_о"] == 0 else row["Мин_бал_о"], axis=1)
klasirane_2021_3_clean["Макс_бал_о"] = klasirane_2021_3_clean.apply(
    lambda row: max(row["Макс_бал_м"], row["Макс_бал_ж"]) if row["Макс_бал_о"] == 0 else row["Макс_бал_о"], axis=1)
klasirane_2021_3_clean = klasirane_2021_3_clean.sort_values(by='Код паралелка')
klasirane_2021_3_clean.reset_index(drop=True, inplace=True)
klasirane_2021_3_clean = pd.merge(mesta_2021_3_clean, klasirane_2021_3_clean, on="Код паралелка", how='outer')
klasirane_2021_3_clean["Класиране"] = 3
klasirane_2021_3_clean = klasirane_2021_3_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                                'Балообразуване', 'Брой паралелки',  'Година', 'Код училище', 'Места_о',
                                                 'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                 'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
klasirane_2021_3_clean.index = klasirane_2021_1_clean.index
# print(f'Klasirane 3: {klasirane_2021_3_clean.shape}')

# KLASIRANE 4
mesta_2021_4_clean = mesta_2021_4.drop(mesta_2021_4.columns[[0, 2, 3, 4]], axis=1)
mesta_2021_4_clean = mesta_2021_4_clean.rename(columns={
                           "Unnamed: 1": "Код паралелка",
                           "Unnamed: 5": "Места_о",
                           "Unnamed: 6": "Места_м",
                           "Unnamed: 7": "Места_д"})
mesta_2021_4_clean = mesta_2021_4_clean[mesta_2021_4_clean["Код паралелка"].notna()]
mesta_2021_4_clean = mesta_2021_4_clean.drop([0], axis=0)
mesta_2021_4_clean = mesta_2021_4_clean.fillna(0)
mesta_2021_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2021_4_clean[["Места_о", "Места_м", "Места_д"]].\
    replace('-', 0)
mesta_2021_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2021_4_clean[["Места_о", "Места_м", "Места_д"]].\
    astype(int)
mesta_2021_4_clean['Места_общ_брой'] = mesta_2021_4_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2021_4_clean['Места_общ_брой_м'] = mesta_2021_4_clean[["Места_о", "Места_м"]].sum(axis=1)
mesta_2021_4_clean['Места_общ_брой_д'] = mesta_2021_4_clean[["Места_о", "Места_д"]].sum(axis=1)
mesta_2021_4_clean = mesta_2021_4_clean.sort_values(by='Код паралелка')
mesta_2021_4_clean.reset_index(drop=True, inplace=True)
mesta_2021_4_clean = pd.merge(basic_data_2021, mesta_2021_4_clean, on="Код паралелка", how='outer')
mesta_2021_4_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
    mesta_2021_4_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']].\
    apply(pd.to_numeric, errors='coerce').astype("Int64")
mesta_2021_4_clean["Класиране"] = 4
mesta_2021_4_clean = mesta_2021_4_clean.sort_values(by='Код паралелка')
mesta_2021_4_clean.reset_index(drop=True, inplace=True)
mesta_2021_4_clean.index = klasirane_2021_1_clean.index
# print(f'Klasirane 4: {mesta_2021_4_clean.shape}')

# Data preparation
klasirane_2021_combined = pd.concat([klasirane_2021_1_clean.sort_index(), klasirane_2021_2_clean.sort_index(),
                                     klasirane_2021_3_clean.sort_index(), mesta_2021_4_clean.sort_index()], axis=0)
klasirane_2021_combined.reset_index(drop=True, inplace=True)

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка']
#
# klasirane_2021_combined.loc[klasirane_2021_combined['Профил_1'].str.startswith("Чужди езици"), 'Профил_1'] = \
#     'Чужди езици'

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Чужди езици -АЕ интензивно, ИЕ, ГИ и ИЦ',
            'Чужди езици - АЕ интензивно, ИЕ, ГИ и ИЦ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Чужди езици АЕ интензивно, ИЕ, М, ГИ',
            'Чужди езици - АЕ интензивно, ИЕ, М, ГИ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Чужди езици - интензивно НЕ,  РЕ',
            'Чужди езици - НЕ интензивно, РЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Чужди езици -  интензивно ФЕ, РЕ',
            'Чужди езици -  ФЕ интензивно , РЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Телекомуникационни системи-АЕ',
            'Телекомуникационни системи - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Софтуерни и хардуени науки - АЕ интензивно, КорЕ',
            'Софтуерни и хардуерни науки - АЕ интензивно, КорЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Софтуерни и хардуерни науки /ИЕ/',
            'Софтуерни и хардуерни науки - ИЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Топлотехника - отоплителна климат. вентилационна и хладилна - АЕ (дуална)',
            'Топлотехника-отоплителна климат. вентилационна и хладилна - АЕ (дуална)')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Производство на кулинарни изделия и напитки - готвач',
            'Производство на кулинарни изделия и напитки (готвач)')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Продавач-консултант /АЕ/',
            'Продавач-консултант - АЕ ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Продавач-консултант /РЕ/',
            'Продавач-консултант - РЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Природни науки ИЕ - интензивно, АЕ, БЗО, ХООС',
            'Природни науки - ИЕ интензивно, АЕ, БЗО, ХООС')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Предприемачески - АЕ интензивно; РЕ',
            'Предприемачески - АЕ интензивно, РЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Предприемачески  - АЕ интензивно, РЕ',
            'Предприемачески - АЕ интензивно, РЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Подемно - транспортна техника монтирана на пътни транспортни средства',
            'Подемно-транспортна техника монтирана на пътни транспортни средства')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Логистика на товари и услуги /АЕ/',
            'Логистика на товари и услуги - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Компютърна графика- АЕ',
            'Компютърна графика - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Кетъринг   - ГрЕ',
            'Кетъринг - ГрЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Интериорен дизайн- НЕ',
            'Интериорен дизайн - НЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Графичен дизайн /АЕ/',
            'Графичен дизайн - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Български танци /АЕ/',
            'Български танци - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Автотранспортна техника - техник АЕ',
            'Автотранспортна техника - техник, АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Автомобилна  мехатроника - АЕ',
            'Автомобилна мехатроника - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Интериорен дизайн- НЕ, АЕ',
            'Интериорен дизайн - НЕ, АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Графичен дизайн /',
            'Графичен дизайн')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Логистика на товари и услуги /НЕ/',
            'Логистика на товари и услуги - НЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Логистика на товари и услуги - куриер /АЕ/',
            'Логистика на товари и услуги - куриер АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Логистика на товари и услуги - куриер /РЕ/',
            'Логистика на товари и услуги - куриер РЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace(r'\s*/\s*', ', ', regex=True)


klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Автомобилна  мехатроника - АЕ (дуална)',
            'Автомобилна мехатроника - АЕ (дуална)')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Организация на хотелиерството -  АЕ',
            'Организация на хотелиерството - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Предприемачество - АЕ интензивно, НЕ',
            'Предприемачески - АЕ интензивно, НЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Производство на месо месни продукти и риба - АЕ',
            'Производство на месо, месни продукти и риба - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Хумантарни науки - АЕ интензивно, НЕ',
            'Хуманитарни науки - АЕ интензивно, НЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Чужди езици - АЕ интензивно  ИЕ',
            'Чужди езици - АЕ интензивно, ИЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    replace('Софтуерни и хардуери науки - АЕ',
            'Софтуерни и хардуерни науки - АЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    str.replace('Биология и здравно образование -', 'БЗО')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    str.replace('Топлотехника - отоплителна климат. вентилационна и хладилна - АЕ (дуална), РЕ, НЕ',
                'Топлотехника-отоплителна климат. вентилационна и хладилна - АЕ (дуална), РЕ, НЕ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].\
    str.replace('интензивно ',
                'интензивно, ')

klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].str.lstrip()
klasirane_2021_combined['Паралелка_формат'] = klasirane_2021_combined['Паралелка_формат'].str.rstrip()

klasirane_2021_combined[['Профил_1', 'Профил_1x']] = klasirane_2021_combined['Паралелка_формат'].\
    str.split(' - ', n=1, expand=True)

klasirane_2021_combined['Профил_1'] = klasirane_2021_combined['Профил_1'].str.lstrip()
klasirane_2021_combined['Профил_1'] = klasirane_2021_combined['Профил_1'].str.rstrip()

klasirane_2021_combined['Профил_1x'] = klasirane_2021_combined['Профил_1x'].str.lstrip()
klasirane_2021_combined['Профил_1x'] = klasirane_2021_combined['Профил_1x'].str.rstrip()

klasirane_2021_combined[['Профил_2', 'Профил_3']] = klasirane_2021_combined['Профил_1x'].\
    str.split(',', n=1, expand=True)

klasirane_2021_combined[['Профил_1x', 'Профил_2', 'Профил_3']] = klasirane_2021_combined[['Профил_1x', 'Профил_2', 'Профил_3']].fillna('-')

klasirane_2021_combined['Профил_2'] = klasirane_2021_combined['Профил_2'].str.lstrip()
klasirane_2021_combined['Профил_2'] = klasirane_2021_combined['Профил_2'].str.rstrip()

klasirane_2021_combined['Профил_3'] = klasirane_2021_combined['Профил_3'].str.lstrip()
klasirane_2021_combined['Профил_3'] = klasirane_2021_combined['Профил_3'].str.rstrip()

klasirane_2021_combined['Профил_2'] = klasirane_2021_combined['Профил_2'].\
    replace('AE интензивно',
            'АЕ интензивно')

# unique_values = klasirane_2021_combined['Профил_1x'].sort_values().unique()
# for value in unique_values:
#     print(value)
# print(klasirane_2021_combined.loc[klasirane_2021_combined['Паралелка_формат'].str.startswith('Топлотехника'), 'Паралелка_формат'])


# print(klasirane_2021_combined[['Профил_1', 'Профил_1x', 'Профил_2', 'Профил_3']])

# Data check
dataframes = [klasirane_2021_1_clean.sort_index(), klasirane_2021_2_clean.sort_index(),
              klasirane_2021_3_clean.sort_index(), mesta_2021_4_clean.sort_index()]

all_data_check = []
for df in dataframes:
    data_check = []
    for col in df.columns:
        col_info = {
            'Columns': col,
            'Records': df[col].count(),
            'DType': df[col].dtype
        }
        data_check.append(col_info)
    check_df = pd.DataFrame(data_check)
    all_data_check.append(check_df)

# Concatenate all the DataFrames vertically
result = pd.concat(all_data_check, axis=1, ignore_index=True)
# print(result)
