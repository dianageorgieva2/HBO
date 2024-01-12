# INSTRUCTIONS FOR NEW YEAR FILES IMPORT, CLEANING, STANDARTISATION
# 1. Copy data_klasirane_LAST YEAR into a new py file
# 2. Import correct files from the respective folder
# 3. Replace YEAR with the year you want everywhere
# 4. Check if difference in records in the 3 klasirane and mesta and add the difference as
# needed to the highest possible
# 5. Run data check and specifically check orders, numbers, types

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_colwidth', None)

# ----------KLASIRANE 2022----------
# Data import
mesta_2022_3 = pd.read_csv('klasirane/2022/free_IIIetap_sait (7).csv')
mesta_2022_4 = pd.read_csv('klasirane/2022/svobodni_mesta_sled_IIIetap_2022 (2).csv')
klasirane_2022_1 = pd.read_csv('klasirane/2022/po_bal_sait (5).csv')
klasirane_2022_2 = pd.read_csv('klasirane/2022/min_max_2_etap_2022 (5).csv')
klasirane_2022_3 = pd.read_csv('klasirane/2022/min_max_III_etap (3).csv')
kodove_2022 = pd.read_csv('klasirane/2022/Za_saita_s_kodove_i_baloobrazuvane_2022.csv')

# DATA STRUCTURING

# Clean model for codes
kodove_2022_clean = kodove_2022.rename(columns={
                           "Unnamed: 1": "Район",
                           "Unnamed: 2": "Училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 4": "Паралелка",
                           "Unnamed: 5": "Вид на паралелката",
                           "Unnamed: 6": "Балообразуване",
                           "Unnamed: 7": "Брой паралелки",
                           "Unnamed: 8": "Места_о",
                           "Unnamed: 9": "Места_м",
                           "Unnamed: 10": "Места_д"})
kodove_2022_clean = kodove_2022_clean.drop(kodove_2022_clean.columns[0], axis=1)
kodove_2022_clean = kodove_2022_clean[kodove_2022_clean["Код паралелка"].notna()]
kodove_2022_clean["Код паралелка"] = kodove_2022_clean["Код паралелка"].str.zfill(4)  # Adds leading 0 to 3dig records
kodove_2022_clean = kodove_2022_clean.drop([2], axis=0)
kodove_2022_clean[["Места_о", "Места_м", "Места_д"]] = kodove_2022_clean[["Места_о", "Места_м", "Места_д"]].astype(int)
kodove_2022_clean['Места_общ_брой'] = kodove_2022_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
kodove_2022_clean['Места_общ_брой_м'] = kodove_2022_clean[["Места_о", "Места_м"]].sum(axis=1)
kodove_2022_clean['Места_общ_брой_д'] = kodove_2022_clean[["Места_о", "Места_д"]].sum(axis=1)
kodove_2022_clean["Година"] = "2022"
kodove_2022_clean = kodove_2022_clean.sort_values(by='Код паралелка')
kodove_2022_clean.reset_index(drop=True, inplace=True)
# print(f'Kodove: {kodove_2022_clean.shape}')

# KLASIRANE 1
klasirane_2022_1_clean = klasirane_2022_1.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 5": "Мин_бал_о",
                           "Unnamed: 6": "Мин_бал_м",
                           "Unnamed: 7": "Мин_бал_ж",
                           "Unnamed: 8": "Макс_бал_о",
                           "Unnamed: 9": "Макс_бал_м",
                           "Unnamed: 10": "Макс_бал_ж"})
klasirane_2022_1_clean = klasirane_2022_1_clean.drop(klasirane_2022_1_clean.columns[[0, 2, 4]], axis=1)
klasirane_2022_1_clean = klasirane_2022_1_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2022_1_clean = klasirane_2022_1_clean[klasirane_2022_1_clean["Код паралелка"].notna()]
klasirane_2022_1_clean = klasirane_2022_1_clean.fillna('-')  # Check whether it is correct the NaN records to be - or 0.
klasirane_2022_1_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = \
    klasirane_2022_1_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
    astype(float)
klasirane_2022_1_clean = klasirane_2022_1_clean.sort_values(by='Код паралелка')
klasirane_2022_1_clean.reset_index(drop=True, inplace=True)
klasirane_2022_1_clean = pd.merge(kodove_2022_clean, klasirane_2022_1_clean, on="Код паралелка", how='outer')
klasirane_2022_1_clean["Класиране"] = '1'
klasirane_2022_1_clean["Класиране"] = klasirane_2022_1_clean["Класиране"].astype(int)
klasirane_2022_1_clean = klasirane_2022_1_clean.sort_values(by='Мин_бал_о', ascending=False)
klasirane_2022_1_clean.reset_index(drop=True, inplace=True)
klasirane_2022_1_clean = klasirane_2022_1_clean.sort_values(by='Код паралелка')
klasirane_2022_1_clean = klasirane_2022_1_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                                'Балообразуване', 'Брой паралелки',  'Година', 'Код училище', 'Места_о',
                                                 'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                 'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
basic_data_2022 = klasirane_2022_1_clean[['Район', 'Училище',  'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                          'Балообразуване', 'Брой паралелки', 'Година']]
# print(f'Klasirane 1: {klasirane_2022_1_clean.shape}')

# # Find and print items that are in kodove_set but not in klasirane_set
# set1 = set(kodove_2022_clean["Код паралелка"])
# set2 = set(klasirane_2022_1_clean["Код паралелка"])
# different_items = set1 - set2
# for k in different_items:
#     print(k)

# KLASIRANE 2
klasirane_2022_2_clean = klasirane_2022_2.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 5": "Мин_бал_о",
                           "Unnamed: 6": "Мин_бал_м",
                           "Unnamed: 7": "Мин_бал_ж",
                           "Unnamed: 8": "Макс_бал_о",
                           "Unnamed: 9": "Макс_бал_м",
                           "Unnamed: 10": "Макс_бал_ж"})
klasirane_2022_2_clean = klasirane_2022_2_clean.drop(klasirane_2022_2_clean.columns[[0, 2, 4]], axis=1)
klasirane_2022_2_clean = klasirane_2022_2_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2022_2_clean = klasirane_2022_2_clean[klasirane_2022_2_clean["Код паралелка"].notna()]
klasirane_2022_2_clean = klasirane_2022_2_clean.fillna(0)
klasirane_2022_2_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = \
    klasirane_2022_2_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
    astype(float)
klasirane_2022_2_clean = klasirane_2022_2_clean.sort_values(by='Код паралелка')
klasirane_2022_2_clean.reset_index(drop=True, inplace=True)
klasirane_2022_2_clean = pd.merge(basic_data_2022, klasirane_2022_2_clean, on="Код паралелка", how='outer')
klasirane_2022_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
    np.nan
klasirane_2022_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
    klasirane_2022_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м',
                            'Места_общ_брой_д']].apply(pd.to_numeric, errors='coerce').astype("Int64")
klasirane_2022_2_clean["Класиране"] = '2'
klasirane_2022_2_clean["Класиране"] = klasirane_2022_2_clean["Класиране"].astype(int)
klasirane_2022_2_clean = klasirane_2022_2_clean.sort_values(by='Код паралелка')
klasirane_2022_2_clean.reset_index(drop=True, inplace=True)
klasirane_2022_2_clean.index = klasirane_2022_1_clean.index
klasirane_2022_2_clean = klasirane_2022_2_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                                'Балообразуване', 'Брой паралелки',  'Година', 'Код училище', 'Места_о',
                                                 'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                 'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
# print(f'Klasirane 2: {klasirane_2022_2_clean.shape}')

# KLASIRANE 3
mesta_2022_3_clean = mesta_2022_3.drop(mesta_2022_3.columns[[0, 2, 4]], axis=1)
mesta_2022_3_clean = mesta_2022_3_clean.rename(columns={
                           "Unnamed: 1": "Код училище",
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 5": "Места_о",
                           "Unnamed: 6": "Места_м",
                           "Unnamed: 7": "Места_д"})
mesta_2022_3_clean = mesta_2022_3_clean[mesta_2022_3_clean["Код паралелка"].notna()]
mesta_2022_3_clean = mesta_2022_3_clean.drop([2, 3], axis=0)
mesta_2022_3_clean = mesta_2022_3_clean.fillna(0)
mesta_2022_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2022_3_clean[["Места_о", "Места_м", "Места_д"]].\
    replace('-', 0)
mesta_2022_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2022_3_clean[["Места_о", "Места_м", "Места_д"]].\
    astype(int)
mesta_2022_3_clean['Места_общ_брой'] = mesta_2022_3_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2022_3_clean['Места_общ_брой_м'] = mesta_2022_3_clean[["Места_о", "Места_м"]].sum(axis=1)
mesta_2022_3_clean['Места_общ_брой_д'] = mesta_2022_3_clean[["Места_о", "Места_д"]].sum(axis=1)
mesta_2022_3_clean = pd.merge(basic_data_2022, mesta_2022_3_clean, on="Код паралелка", how='outer')
mesta_2022_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
    mesta_2022_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']].\
    apply(pd.to_numeric, errors='coerce').astype("Int64")
mesta_2022_3_clean["Класиране"] = 3
mesta_2022_3_clean["Класиране"] = mesta_2022_3_clean["Класиране"].astype(int)
mesta_2022_3_clean = mesta_2022_3_clean.sort_values(by='Код паралелка')
mesta_2022_3_clean.reset_index(drop=True, inplace=True)
mesta_2022_3_clean.index = klasirane_2022_1_clean.index

klasirane_2022_3_clean = klasirane_2022_3.rename(columns={
                           "Unnamed: 3": "Код паралелка",
                           "Unnamed: 5": "Мин_бал_о",
                           "Unnamed: 6": "Мин_бал_м",
                           "Unnamed: 7": "Мин_бал_ж",
                           "Unnamed: 8": "Макс_бал_о",
                           "Unnamed: 9": "Макс_бал_м",
                           "Unnamed: 10": "Макс_бал_ж"})
klasirane_2022_3_clean = klasirane_2022_3_clean.drop(klasirane_2022_3_clean.columns[[0, 1, 2, 4]], axis=1)
klasirane_2022_3_clean = klasirane_2022_3_clean.drop([0, 1, 2, 3], axis=0)
klasirane_2022_3_clean = klasirane_2022_3_clean[klasirane_2022_3_clean["Код паралелка"].notna()]
klasirane_2022_3_clean = klasirane_2022_3_clean.fillna(0)
klasirane_2022_3_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = \
    klasirane_2022_3_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
    astype(float)
klasirane_2022_3_clean = klasirane_2022_3_clean.sort_values(by='Код паралелка')
klasirane_2022_3_clean.reset_index(drop=True, inplace=True)
klasirane_2022_3_clean = pd.merge(mesta_2022_3_clean, klasirane_2022_3_clean, on="Код паралелка", how='outer')
klasirane_2022_3_clean = klasirane_2022_3_clean.sort_values(by='Код паралелка')
klasirane_2022_3_clean.reset_index(drop=True, inplace=True)
klasirane_2022_3_clean.index = klasirane_2022_1_clean.index
# print(f'Klasirane 3: {klasirane_2022_3_clean.shape}')

# KLASIRANE 4
mesta_2022_4_clean = mesta_2022_4.drop(mesta_2022_4.columns[[0, 1, 3]], axis=1)
mesta_2022_4_clean = mesta_2022_4_clean.rename(columns={
                            "Unnamed: 2": "Код паралелка",
                            "Unnamed: 4": "Места_о",
                            "Unnamed: 5": "Места_м",
                            "Unnamed: 6": "Места_д"})

mesta_2022_4_clean = mesta_2022_4_clean[mesta_2022_4_clean["Код паралелка"].notna()]
mesta_2022_4_clean = mesta_2022_4_clean.drop([0], axis=0)
mesta_2022_4_clean = mesta_2022_4_clean.fillna(0)
mesta_2022_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2022_4_clean[["Места_о", "Места_м", "Места_д"]].\
    replace('-', 0)
mesta_2022_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2022_4_clean[["Места_о", "Места_м", "Места_д"]].\
    astype(int)
mesta_2022_4_clean['Места_общ_брой'] = mesta_2022_4_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
mesta_2022_4_clean['Места_общ_брой_м'] = mesta_2022_4_clean[["Места_о", "Места_м"]].sum(axis=1)
mesta_2022_4_clean['Места_общ_брой_д'] = mesta_2022_4_clean[["Места_о", "Места_д"]].sum(axis=1)
mesta_2022_4_clean = mesta_2022_4_clean.sort_values(by='Код паралелка')
mesta_2022_4_clean.reset_index(drop=True, inplace=True)
mesta_2022_4_clean = pd.merge(basic_data_2022, mesta_2022_4_clean, on="Код паралелка", how='outer')
mesta_2022_4_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
    mesta_2022_4_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']].\
    apply(pd.to_numeric, errors='coerce').astype("Int64")
mesta_2022_4_clean["Класиране"] = 4
mesta_2022_4_clean["Класиране"] = mesta_2022_4_clean["Класиране"].astype(int)

for paralelka_kod in klasirane_2022_1_clean["Код паралелка"]:
    if paralelka_kod in mesta_2022_4_clean["Код паралелка"].values:
        mesta_2022_4_clean.loc[mesta_2022_4_clean["Код паралелка"] == paralelka_kod, "Код училище"] = \
            klasirane_2022_1_clean.loc[klasirane_2022_1_clean["Код паралелка"] == paralelka_kod, "Код училище"].values[0]

mesta_2022_4_clean = mesta_2022_4_clean.sort_values(by='Код паралелка')
mesta_2022_4_clean.reset_index(drop=True, inplace=True)
mesta_2022_4_clean.index = klasirane_2022_1_clean.index
# print(f'Klasirane 4: {mesta_2022_4_clean.shape}')

# Data preparation
klasirane_2022_combined = pd.concat([klasirane_2022_1_clean.sort_index(), klasirane_2022_2_clean.sort_index(),
                                     klasirane_2022_3_clean.sort_index(), mesta_2022_4_clean.sort_index()], axis=0)
klasirane_2022_combined.reset_index(drop=True, inplace=True)

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка']
#
# klasirane_2022_combined.loc[klasirane_2022_combined['Профил_1'].str.startswith("Чужди езици"), 'Профил_1'] = \
#     'Чужди езици'

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Чужди езици -АЕ интензивно, ИЕ, ГИ и ИЦ',
            'Чужди езици - АЕ интензивно, ИЕ, ГИ и ИЦ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Чужди езици АЕ интензивно, ИЕ, М, ГИ',
            'Чужди езици - АЕ интензивно, ИЕ, М, ГИ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Чужди езици - интензивно НЕ,  РЕ',
            'Чужди езици - НЕ интензивно, РЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Чужди езици -  интензивно ФЕ, РЕ',
            'Чужди езици -  ФЕ интензивно , РЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Телекомуникационни системи-АЕ',
            'Телекомуникационни системи - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Софтуерни и хардуени науки - АЕ интензивно, КорЕ',
            'Софтуерни и хардуерни науки - АЕ интензивно, КорЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Софтуерни и хардуерни науки /ИЕ/',
            'Софтуерни и хардуерни науки - ИЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Топлотехника - отоплителна климат. вентилационна и хладилна - АЕ (дуална)',
            'Топлотехника-отоплителна климат. вентилационна и хладилна - АЕ (дуална)')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Производство на кулинарни изделия и напитки - готвач',
            'Производство на кулинарни изделия и напитки (готвач)')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Продавач-консултант /АЕ/',
            'Продавач-консултант - АЕ ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Продавач-консултант /РЕ/',
            'Продавач-консултант - РЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Природни науки ИЕ - интензивно, АЕ, БЗО, ХООС',
            'Природни науки - ИЕ интензивно, АЕ, БЗО, ХООС')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Предприемачески - АЕ интензивно; РЕ',
            'Предприемачески - АЕ интензивно, РЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Предприемачески  - АЕ интензивно, РЕ',
            'Предприемачески - АЕ интензивно, РЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Подемно - транспортна техника монтирана на пътни транспортни средства',
            'Подемно-транспортна техника монтирана на пътни транспортни средства')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Логистика на товари и услуги /АЕ/',
            'Логистика на товари и услуги - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Компютърна графика- АЕ',
            'Компютърна графика - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Кетъринг   - ГрЕ',
            'Кетъринг - ГрЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Интериорен дизайн- НЕ',
            'Интериорен дизайн - НЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Графичен дизайн /АЕ/',
            'Графичен дизайн - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Български танци /АЕ/',
            'Български танци - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Автотранспортна техника - техник АЕ',
            'Автотранспортна техника - техник, АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Автомобилна  мехатроника - АЕ',
            'Автомобилна мехатроника - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Интериорен дизайн- НЕ, АЕ',
            'Интериорен дизайн - НЕ, АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Графичен дизайн /',
            'Графичен дизайн')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Логистика на товари и услуги /НЕ/',
            'Логистика на товари и услуги - НЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Логистика на товари и услуги - куриер /АЕ/',
            'Логистика на товари и услуги - куриер АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Логистика на товари и услуги - куриер /РЕ/',
            'Логистика на товари и услуги - куриер РЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace(r'\s*/\s*', ', ', regex=True)


klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Автомобилна  мехатроника - АЕ (дуална)',
            'Автомобилна мехатроника - АЕ (дуална)')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Организация на хотелиерството -  АЕ',
            'Организация на хотелиерството - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Предприемачество - АЕ интензивно, НЕ',
            'Предприемачески - АЕ интензивно, НЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Производство на месо месни продукти и риба - АЕ',
            'Производство на месо, месни продукти и риба - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Хумантарни науки - АЕ интензивно, НЕ',
            'Хуманитарни науки - АЕ интензивно, НЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Чужди езици - АЕ интензивно  ИЕ',
            'Чужди езици - АЕ интензивно, ИЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    replace('Софтуерни и хардуери науки - АЕ',
            'Софтуерни и хардуерни науки - АЕ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    str.replace('Биология и здравно образование -', 'БЗО')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].\
    str.replace('интензивно ',
                'интензивно, ')

klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].str.lstrip()
klasirane_2022_combined['Паралелка_формат'] = klasirane_2022_combined['Паралелка_формат'].str.rstrip()

klasirane_2022_combined[['Профил_1', 'Профил_1x']] = klasirane_2022_combined['Паралелка_формат'].\
    str.split(' - ', n=1, expand=True)

klasirane_2022_combined['Профил_1'] = klasirane_2022_combined['Профил_1'].str.lstrip()
klasirane_2022_combined['Профил_1'] = klasirane_2022_combined['Профил_1'].str.rstrip()

klasirane_2022_combined['Профил_1x'] = klasirane_2022_combined['Профил_1x'].str.lstrip()
klasirane_2022_combined['Профил_1x'] = klasirane_2022_combined['Профил_1x'].str.rstrip()

klasirane_2022_combined[['Профил_2', 'Профил_3']] = klasirane_2022_combined['Профил_1x'].\
    str.split(',', n=1, expand=True)

klasirane_2022_combined[['Профил_1x', 'Профил_2', 'Профил_3']] = klasirane_2022_combined[['Профил_1x', 'Профил_2', 'Профил_3']].fillna('-')

klasirane_2022_combined['Профил_2'] = klasirane_2022_combined['Профил_2'].str.lstrip()
klasirane_2022_combined['Профил_2'] = klasirane_2022_combined['Профил_2'].str.rstrip()

klasirane_2022_combined['Профил_3'] = klasirane_2022_combined['Профил_3'].str.lstrip()
klasirane_2022_combined['Профил_3'] = klasirane_2022_combined['Профил_3'].str.rstrip()

klasirane_2022_combined['Профил_2'] = klasirane_2022_combined['Профил_2'].\
    replace('AE интензивно',
            'АЕ интензивно')

klasirane_2022_combined['Училище_формат'] = klasirane_2022_combined['Училище']
klasirane_2022_combined['Училище_формат'] = klasirane_2022_combined['Училище_формат'].str.split(',', n=1).str.get(0)

klasirane_2022_combined['Училище_формат'] = klasirane_2022_combined['Училище_формат']. \
    str.replace('\n',
                ' ')

klasirane_2022_combined['Училище_формат'] = klasirane_2022_combined['Училище_формат']. \
    replace('Професионална гимназия по екология и биотехнологии "Проф. д-р Асен Златаров"',
            'ПГЕБ "Проф. д-р Асен Златаров"')

klasirane_2022_combined['Училище_формат'] = klasirane_2022_combined['Училище_формат']. \
    replace('Професионална гимназия по туризъм "Алеко Константинов"',
            'ПГ туризъм "Алеко Константинов"')

# unique_values = klasirane_2022_combined['Профил_1x'].sort_values().unique()
# for value in unique_values:
#     print(value)

# print(klasirane_2022_combined[['Профил_1', 'Профил_1x', 'Профил_2', 'Профил_3']])

# Data check
dataframes = [klasirane_2022_1_clean.sort_index(), klasirane_2022_2_clean.sort_index(),
              klasirane_2022_3_clean.sort_index(), mesta_2022_4_clean.sort_index()]

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
