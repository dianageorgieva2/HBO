# INSTRUCTIONS FOR NEW YEAR FILES IMPORT, CLEANING, STANDARTISATION
# 1. Copy data_klasirane_LAST YEAR into a new py file
# 2. Import correct files from the respective folder
# 3. Replace YEAR with the year you want everywhere
# 4. Check if difference in records in the 3 klasirane and mesta and add the difference as needed
# to the highest possible
# 5. Activate the print function in the code
# 6. Run data check
# 7. Clean up data items in "Паралелка_формат" and the respective split columns "Профил_1, 2, 3, 4, 5",
# so to maintain unique records (spelling, symbol, hyphenation, etc)
import difflib

import pandas as pd
import numpy as np
import streamlit as st

pd.set_option('display.max_column', 100)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('expand_frame_repr', False)
pd.options.display.float_format = '{:,.2f}'.format


# ----------KLASIRANE 2023----------
@st.cache_data()
def klasirane_2023_combined_function():
    # Data import
    mesta_2023_3 = pd.read_csv('klasirane/2023/svobodni_mesta_za_3_etap_2023-3 (1).csv',
                               encoding='utf-8', encoding_errors='ignore')
    mesta_2023_4 = pd.read_csv('klasirane/2023/svobodni_mesta_za_4_etap_2023.csv',
                               encoding='utf-8', encoding_errors='ignore')
    mesta_2023_5 = pd.read_csv('klasirane/2023/svobodni_mesta_za_5_etap_2023-1.csv',
                               encoding='utf-8', encoding_errors='ignore')
    klasirane_2023_1 = pd.read_csv('klasirane/2023/min_maх_paralelki_1.etap_2023 (3).csv',
                                   encoding='utf-8', encoding_errors='ignore')
    klasirane_2023_2 = pd.read_csv('klasirane/2023/min_max_2_etap_2023 (1).csv',
                                   encoding='utf-8', encoding_errors='ignore')
    klasirane_2023_3 = pd.read_csv('klasirane/2023/min_max_po_paralelki_3_etap_2023 (1).csv',
                                   encoding='utf-8', encoding_errors='ignore')
    klasirane_2023_4 = pd.read_csv('klasirane/2023/min_max_po_par_4_etap_2023 (1).csv',
                                   encoding='utf-8', encoding_errors='ignore')
    kodove_2023 = pd.read_csv('klasirane/2023/Za_saita_s_kodove_baloobrazuvane_2023-12.csv',
                              encoding='utf-8', encoding_errors='ignore')

    # Clean codes model
    kodove_2023_clean = kodove_2023.rename(columns={
                               "Unnamed: 1": "Район",
                               "Unnamed: 2": "Училище",
                               "Unnamed: 3": "Код паралелка",
                               "Unnamed: 4": "Паралелка",
                               "Unnamed: 5": "Вид на паралелката",
                               "Unnamed: 6": "Балообразуване",
                               "Unnamed: 7": "Форма на обучение",
                               "Unnamed: 8": "Брой паралелки",
                               "Unnamed: 9": "Места_о",
                               "Unnamed: 10": "Места_м",
                               "Unnamed: 11": "Места_д"})
    kodove_2023_clean = kodove_2023_clean.drop(kodove_2023_clean.columns[0], axis=1)
    kodove_2023_clean = kodove_2023_clean[kodove_2023_clean["Код паралелка"].notna()]
    kodove_2023_clean = kodove_2023_clean.drop([1], axis=0)
    kodove_2023_clean[["Места_о", "Места_м", "Места_д"]] = \
        kodove_2023_clean[["Места_о", "Места_м", "Места_д"]].astype(int)
    kodove_2023_clean['Места_общ_брой'] = kodove_2023_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
    kodove_2023_clean['Места_общ_брой_м'] = kodove_2023_clean[["Места_о", "Места_м"]].sum(axis=1)
    kodove_2023_clean['Места_общ_брой_д'] = kodove_2023_clean[["Места_о", "Места_д"]].sum(axis=1)
    kodove_2023_clean["Година"] = "2023"
    kodove_2023_clean = kodove_2023_clean.sort_values(by='Код паралелка')
    kodove_2023_clean.reset_index(drop=True, inplace=True)
    basic_data_2023 = kodove_2023_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                         'Балообразуване', 'Форма на обучение', 'Брой паралелки', 'Година']]
    # print(f'Kodove: {kodove_2023_clean.shape}')

    # KLASIRANE 1
    klasirane_2023_1_clean = klasirane_2023_1.rename(columns={
                               "Unnamed: 1": "Код училище",
                               "Unnamed: 3": "Код паралелка",
                               "Unnamed: 5": "Мин_бал_о",
                               "Unnamed: 6": "Мин_бал_м",
                               "Unnamed: 7": "Мин_бал_ж",
                               "Unnamed: 8": "Макс_бал_о",
                               "Unnamed: 9": "Макс_бал_м",
                               "Unnamed: 10": "Макс_бал_ж"})
    klasirane_2023_1_clean = klasirane_2023_1_clean.drop(klasirane_2023_1_clean.columns[[0, 2, 4]], axis=1)
    klasirane_2023_1_clean = klasirane_2023_1_clean.drop([0, 1, 2, 3], axis=0)
    klasirane_2023_1_clean = klasirane_2023_1_clean[klasirane_2023_1_clean["Код паралелка"].notna()]
    klasirane_2023_1_clean = klasirane_2023_1_clean.fillna('-')  # Double check if NaN records to be - or 0.
    klasirane_2023_1_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = \
        klasirane_2023_1_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
        astype(float)
    klasirane_2023_1_clean = klasirane_2023_1_clean.sort_values(by='Код паралелка')
    klasirane_2023_1_clean.reset_index(drop=True, inplace=True)
    klasirane_2023_1_clean = pd.merge(kodove_2023_clean, klasirane_2023_1_clean, on="Код паралелка", how='outer')
    klasirane_2023_1_clean["Класиране"] = '1'
    klasirane_2023_1_clean["Класиране"] = klasirane_2023_1_clean["Класиране"].astype(int)
    klasirane_2023_1_clean = klasirane_2023_1_clean.sort_values(by='Мин_бал_о', ascending=False)
    klasirane_2023_1_clean.reset_index(drop=True, inplace=True)
    klasirane_2023_1_clean = klasirane_2023_1_clean.sort_values(by='Код паралелка')
    klasirane_2023_1_clean = klasirane_2023_1_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка',
                                                     'Вид на паралелката',
                                                    'Балообразуване', 'Форма на обучение', 'Брой паралелки',  'Година',
                                                     'Код училище', 'Места_о',
                                                     'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                     'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                     'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
    # print(f'Klasirane 1: {klasirane_2023_1_clean.shape}')

    # # Find and print items that are in kodove_set but not in klasirane_set
    # set1 = set(kodove_2023_clean["Код паралелка"])
    # set2 = set(klasirane_2023_1_clean["Код паралелка"])
    # different_items = set1 - set2
    # for k in different_items:
    #     print(k)

    # KLASIRANE 2
    klasirane_2023_2_clean = klasirane_2023_2.rename(columns={
                               "Unnamed: 1": "Код училище",
                               "Unnamed: 3": "Код паралелка",
                               "Unnamed: 6": "Мин_бал_о",
                               "Unnamed: 7": "Мин_бал_м",
                               "Unnamed: 8": "Мин_бал_ж",
                               "Unnamed: 9": "Макс_бал_о",
                               "Unnamed: 10": "Макс_бал_м",
                               "Unnamed: 11": "Макс_бал_ж"})
    klasirane_2023_2_clean = klasirane_2023_2_clean.drop(klasirane_2023_2_clean.columns[[0, 2, 4, 5]], axis=1)
    klasirane_2023_2_clean = klasirane_2023_2_clean.drop([0, 1, 2, 3], axis=0)
    klasirane_2023_2_clean = klasirane_2023_2_clean[klasirane_2023_2_clean["Код паралелка"].notna()]
    klasirane_2023_2_clean = klasirane_2023_2_clean.fillna(0)
    klasirane_2023_2_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = \
        klasirane_2023_2_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
        astype(float)
    klasirane_2023_2_clean = klasirane_2023_2_clean.sort_values(by='Код паралелка')
    klasirane_2023_2_clean.reset_index(drop=True, inplace=True)
    klasirane_2023_2_clean = pd.merge(kodove_2023_clean, klasirane_2023_2_clean, on="Код паралелка", how='outer')
    klasirane_2023_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м',
                            'Места_общ_брой_д']] = np.nan
    klasirane_2023_2_clean["Класиране"] = '2'
    klasirane_2023_2_clean["Класиране"] = klasirane_2023_2_clean["Класиране"].astype(int)
    klasirane_2023_2_clean = klasirane_2023_2_clean.sort_values(by='Код паралелка')
    klasirane_2023_2_clean.reset_index(drop=True, inplace=True)
    klasirane_2023_2_clean.index = klasirane_2023_1_clean.index
    klasirane_2023_2_clean = klasirane_2023_2_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка',
                                                     'Вид на паралелката',
                                                     'Балообразуване', 'Форма на обучение', 'Брой паралелки',  'Година',
                                                     'Код училище', 'Места_о',
                                                     'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                     'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                     'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
    # print(f'Klasirane 2: {klasirane_2023_2_clean.shape}')

    # KLASIRANE 3
    mesta_2023_3_clean = mesta_2023_3.drop(mesta_2023_3.columns[[0, 2, 4, 5]], axis=1)
    mesta_2023_3_clean = mesta_2023_3_clean.rename(columns={
                               "Unnamed: 1": "Код училище",
                               "Unnamed: 3": "Код паралелка",
                               "Unnamed: 6": "Места_о",
                               "Unnamed: 7": "Места_м",
                               "Unnamed: 8": "Места_д"})
    mesta_2023_3_clean = mesta_2023_3_clean[mesta_2023_3_clean["Код паралелка"].notna()]
    mesta_2023_3_clean = mesta_2023_3_clean.drop([2, 3], axis=0)
    mesta_2023_3_clean = mesta_2023_3_clean.fillna(0)
    mesta_2023_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_3_clean[["Места_о", "Места_м", "Места_д"]].\
        replace('-', 0)
    mesta_2023_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_3_clean[["Места_о", "Места_м", "Места_д"]].\
        astype(int)
    mesta_2023_3_clean['Места_общ_брой'] = mesta_2023_3_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
    mesta_2023_3_clean['Места_общ_брой_м'] = mesta_2023_3_clean[["Места_о", "Места_м"]].sum(axis=1)
    mesta_2023_3_clean['Места_общ_брой_д'] = mesta_2023_3_clean[["Места_о", "Места_д"]].sum(axis=1)
    mesta_2023_3_clean = pd.merge(basic_data_2023, mesta_2023_3_clean, on="Код паралелка", how='outer')
    mesta_2023_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
        mesta_2023_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м',
                            'Места_общ_брой_д']].apply(pd.to_numeric, errors='coerce').astype("Int64")
    mesta_2023_3_clean["Класиране"] = 3
    mesta_2023_3_clean["Класиране"] = mesta_2023_3_clean["Класиране"].astype(int)
    mesta_2023_3_clean = mesta_2023_3_clean.sort_values(by='Код паралелка')
    mesta_2023_3_clean.reset_index(drop=True, inplace=True)
    mesta_2023_3_clean.index = klasirane_2023_1_clean.index

    klasirane_2023_3_clean = klasirane_2023_3.rename(columns={
                               "Unnamed: 3": "Код паралелка",
                               "Unnamed: 6": "Мин_бал_о",
                               "Unnamed: 7": "Мин_бал_м",
                               "Unnamed: 8": "Мин_бал_ж",
                               "Unnamed: 9": "Макс_бал_о",
                               "Unnamed: 10": "Макс_бал_м",
                               "Unnamed: 11": "Макс_бал_ж"})
    klasirane_2023_3_clean = klasirane_2023_3_clean.drop(klasirane_2023_3_clean.columns[[0, 1, 2, 4, 5]], axis=1)
    klasirane_2023_3_clean = klasirane_2023_3_clean.drop([0, 1, 2, 3], axis=0)
    klasirane_2023_3_clean = klasirane_2023_3_clean[klasirane_2023_3_clean["Код паралелка"].notna()]
    klasirane_2023_3_clean = klasirane_2023_3_clean.fillna(0)
    klasirane_2023_3_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = \
        klasirane_2023_3_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
        astype(float)
    klasirane_2023_3_clean = klasirane_2023_3_clean.sort_values(by='Код паралелка')
    klasirane_2023_3_clean.reset_index(drop=True, inplace=True)
    klasirane_2023_3_clean = pd.merge(mesta_2023_3_clean, klasirane_2023_3_clean, on="Код паралелка", how='outer')
    klasirane_2023_3_clean = klasirane_2023_3_clean.sort_values(by='Код паралелка')
    klasirane_2023_3_clean.reset_index(drop=True, inplace=True)
    klasirane_2023_3_clean.index = klasirane_2023_1_clean.index
    # print(f'Klasirane 3: {klasirane_2023_3_clean.shape}')

    # KLASIRANE 4
    mesta_2023_4_clean = mesta_2023_4.drop(mesta_2023_4.columns[[0, 2, 4, 5]], axis=1)
    mesta_2023_4_clean = mesta_2023_4_clean.rename(columns={
                               "Unnamed: 1": "Код училище",
                               "Unnamed: 3": "Код паралелка",
                               "Unnamed: 6": "Места_о",
                               "Unnamed: 7": "Места_м",
                               "Unnamed: 8": "Места_д"})
    mesta_2023_4_clean = mesta_2023_4_clean[mesta_2023_4_clean["Код паралелка"].notna()]
    mesta_2023_4_clean = mesta_2023_4_clean.drop([2, 3], axis=0)
    mesta_2023_4_clean = mesta_2023_4_clean.fillna(0)
    mesta_2023_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_4_clean[["Места_о", "Места_м", "Места_д"]].\
        replace('-', 0)
    mesta_2023_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_4_clean[["Места_о", "Места_м", "Места_д"]].\
        astype(int)
    mesta_2023_4_clean['Места_общ_брой'] = mesta_2023_4_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
    mesta_2023_4_clean['Места_общ_брой_м'] = mesta_2023_4_clean[["Места_о", "Места_м"]].sum(axis=1)
    mesta_2023_4_clean['Места_общ_брой_д'] = mesta_2023_4_clean[["Места_о", "Места_д"]].sum(axis=1)
    mesta_2023_4_clean = mesta_2023_4_clean.sort_values(by='Код паралелка')
    mesta_2023_4_clean.reset_index(drop=True, inplace=True)
    mesta_2023_4_clean = pd.merge(basic_data_2023, mesta_2023_4_clean, on="Код паралелка", how='outer')
    mesta_2023_4_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
        mesta_2023_4_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м',
                            'Места_общ_брой_д']].apply(pd.to_numeric, errors='coerce').astype("Int64")
    mesta_2023_4_clean["Класиране"] = 4
    mesta_2023_4_clean["Класиране"] = mesta_2023_4_clean["Класиране"].astype(int)
    mesta_2023_4_clean = mesta_2023_4_clean.sort_values(by='Код паралелка')
    mesta_2023_4_clean.reset_index(drop=True, inplace=True)
    mesta_2023_4_clean.index = klasirane_2023_1_clean.index

    klasirane_2023_4_clean = klasirane_2023_4.rename(columns={
                               "Unnamed: 3": "Код паралелка",
                               "Unnamed: 6": "Мин_бал_о",
                               "Unnamed: 7": "Мин_бал_м",
                               "Unnamed: 8": "Мин_бал_ж",
                               "Unnamed: 9": "Макс_бал_о",
                               "Unnamed: 10": "Макс_бал_м",
                               "Unnamed: 11": "Макс_бал_ж"})
    klasirane_2023_4_clean = klasirane_2023_4_clean.drop(klasirane_2023_4_clean.columns[[0, 1, 2, 4, 5]], axis=1)
    klasirane_2023_4_clean = klasirane_2023_4_clean.drop([0, 1, 2, 3], axis=0)
    klasirane_2023_4_clean = klasirane_2023_4_clean[klasirane_2023_4_clean["Код паралелка"].notna()]
    klasirane_2023_4_clean = klasirane_2023_4_clean.fillna(0)
    klasirane_2023_4_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = \
        klasirane_2023_4_clean[["Мин_бал_о", "Мин_бал_м", "Мин_бал_ж", 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
        astype(float)
    klasirane_2023_4_clean = klasirane_2023_4_clean.sort_values(by='Код паралелка')
    klasirane_2023_4_clean.reset_index(drop=True, inplace=True)
    klasirane_2023_4_clean = pd.merge(mesta_2023_4_clean, klasirane_2023_4_clean, on="Код паралелка", how='outer')
    klasirane_2023_4_clean = klasirane_2023_4_clean.sort_values(by='Код паралелка')
    klasirane_2023_4_clean.reset_index(drop=True, inplace=True)
    klasirane_2023_4_clean.index = klasirane_2023_1_clean.index
    # print(f'Klasirane 4: {klasirane_2023_4_clean.shape}')

    # KLASIRANE 5
    mesta_2023_5_clean = mesta_2023_5.drop(mesta_2023_5.columns[[0, 2, 4, 5, 9]], axis=1)
    mesta_2023_5_clean = mesta_2023_5_clean.rename(columns={
                               "Unnamed: 1": "Код училище",
                               "Unnamed: 3": "Код паралелка",
                               "Unnamed: 6": "Места_о",
                               "Unnamed: 7": "Места_м",
                               "Unnamed: 8": "Места_д"})
    mesta_2023_5_clean = mesta_2023_5_clean[mesta_2023_5_clean["Код паралелка"].notna()]
    mesta_2023_5_clean = mesta_2023_5_clean.drop([2, 3], axis=0)
    mesta_2023_5_clean = mesta_2023_5_clean.fillna(0)
    mesta_2023_5_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_5_clean[["Места_о", "Места_м", "Места_д"]].\
        replace('-', 0)
    mesta_2023_5_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2023_5_clean[["Места_о", "Места_м", "Места_д"]].\
        astype(int)
    mesta_2023_5_clean['Места_общ_брой'] = mesta_2023_5_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
    mesta_2023_5_clean['Места_общ_брой_м'] = mesta_2023_5_clean[["Места_о", "Места_м"]].sum(axis=1)
    mesta_2023_5_clean['Места_общ_брой_д'] = mesta_2023_5_clean[["Места_о", "Места_д"]].sum(axis=1)
    mesta_2023_5_clean = mesta_2023_5_clean.sort_values(by='Код паралелка')
    mesta_2023_5_clean.reset_index(drop=True, inplace=True)
    mesta_2023_5_clean = pd.merge(basic_data_2023, mesta_2023_5_clean, on="Код паралелка", how='outer')
    mesta_2023_5_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
        mesta_2023_5_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м',
                            'Места_общ_брой_д']].apply(pd.to_numeric, errors='coerce').astype("Int64")
    mesta_2023_5_clean['Класиране'] = 5
    mesta_2023_5_clean["Класиране"] = mesta_2023_5_clean["Класиране"].astype(int)
    mesta_2023_5_clean = mesta_2023_5_clean.sort_values(by='Код паралелка')
    mesta_2023_5_clean.index = klasirane_2023_1_clean.index
    # print(f'Klasirane 5: {mesta_2023_5_clean.shape}')

    # Data preparation
    klasirane_2023_combined = pd.concat([klasirane_2023_1_clean.sort_index(), klasirane_2023_2_clean.sort_index(),
                                         klasirane_2023_3_clean.sort_index(), klasirane_2023_4_clean.sort_index(),
                                         mesta_2023_5_clean.sort_index()], axis=0)
    klasirane_2023_combined.reset_index(drop=True, inplace=True)

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка']
    #
    # klasirane_2023_combined.loc[klasirane_2023_combined['Профил_1'].str.startswith("Чужди езици"), 'Профил_1'] = \
    #     'Чужди езици'

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Чужди езици -АЕ интензивно, ИЕ, ГИ и ИЦ',
                'Чужди езици - АЕ интензивно, ИЕ, ГИ и ИЦ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Чужди езици АЕ интензивно, ИЕ, М, ГИ',
                'Чужди езици - АЕ интензивно, ИЕ, М, ГИ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Чужди езици - интензивно НЕ,  РЕ',
                'Чужди езици - НЕ интензивно, РЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Чужди езици -  интензивно ФЕ, РЕ',
                'Чужди езици -  ФЕ интензивно , РЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Телекомуникационни системи-АЕ',
                'Телекомуникационни системи - АЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Софтуерни и хардуени науки - АЕ интензивно, КорЕ',
                'Софтуерни и хардуерни науки - АЕ интензивно, КорЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Софтуерни и хардуерни науки /ИЕ/',
                'Софтуерни и хардуерни науки - ИЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Топлотехника - отоплителна климат. вентилационна и хладилна - АЕ (дуална)',
                'Топлотехника-отоплителна климат. вентилационна и хладилна - АЕ (дуална)')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Производство на кулинарни изделия и напитки - готвач',
                'Производство на кулинарни изделия и напитки (готвач)')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Продавач-консултант /АЕ/',
                'Продавач-консултант - АЕ ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Продавач-консултант /РЕ/',
                'Продавач-консултант - РЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Природни науки ИЕ - интензивно, АЕ, БЗО, ХООС',
                'Природни науки - ИЕ интензивно, АЕ, БЗО, ХООС')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Предприемачески - АЕ интензивно; РЕ',
                'Предприемачески - АЕ интензивно, РЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Предприемачески  - АЕ интензивно, РЕ',
                'Предприемачески - АЕ интензивно, РЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Подемно - транспортна техника монтирана на пътни транспортни средства',
                'Подемно-транспортна техника монтирана на пътни транспортни средства')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Логистика на товари и услуги /АЕ/',
                'Логистика на товари и услуги - АЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Компютърна графика- АЕ',
                'Компютърна графика - АЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Кетъринг   - ГрЕ',
                'Кетъринг - ГрЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Интериорен дизайн- НЕ',
                'Интериорен дизайн - НЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Графичен дизайн /АЕ/',
                'Графичен дизайн - АЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Български танци /АЕ/',
                'Български танци - АЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Автотранспортна техника - техник АЕ',
                'Автотранспортна техника - техник, АЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        replace('Автомобилна  мехатроника - АЕ',
                'Автомобилна мехатроника - АЕ')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        str.replace('Биология и здравно образование -', 'БЗО')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        str.replace('интензивно;',
                    'интензивно,')

    klasirane_2023_combined['Паралелка_формат'] = klasirane_2023_combined['Паралелка_формат'].\
        str.replace('разширено;',
                    'разширено,')

    klasirane_2023_combined[['Профил_1', 'Профил_1x']] = klasirane_2023_combined['Паралелка_формат'].\
        str.split(' - ', n=1, expand=True)

    klasirane_2023_combined['Профил_1'] = klasirane_2023_combined['Профил_1'].str.lstrip()
    klasirane_2023_combined['Профил_1'] = klasirane_2023_combined['Профил_1'].str.rstrip()

    klasirane_2023_combined['Профил_1x'] = klasirane_2023_combined['Профил_1x'].str.lstrip()
    klasirane_2023_combined['Профил_1x'] = klasirane_2023_combined['Профил_1x'].str.rstrip()

    klasirane_2023_combined[['Профил_2', 'Профил_3']] = klasirane_2023_combined['Профил_1x'].\
        str.split(',', n=1, expand=True)

    klasirane_2023_combined[['Профил_1x', 'Профил_2', 'Профил_3']] = \
        klasirane_2023_combined[['Профил_1x', 'Профил_2', 'Профил_3']].fillna('-')

    klasirane_2023_combined['Профил_2'] = klasirane_2023_combined['Профил_2'].str.lstrip()
    klasirane_2023_combined['Профил_2'] = klasirane_2023_combined['Профил_2'].str.rstrip()

    klasirane_2023_combined['Профил_3'] = klasirane_2023_combined['Профил_3'].str.lstrip()
    klasirane_2023_combined['Профил_3'] = klasirane_2023_combined['Профил_3'].str.rstrip()

    klasirane_2023_combined['Профил_2'] = klasirane_2023_combined['Профил_2'].\
        replace('AE интензивно',
                'АЕ интензивно')

    klasirane_2023_combined['Училище_формат'] = klasirane_2023_combined['Училище']
    klasirane_2023_combined['Училище_формат'] = klasirane_2023_combined['Училище_формат'].str.split(',', n=1).str.get(0)

    klasirane_2023_combined['Училище_формат'] = klasirane_2023_combined['Училище_формат']. \
        str.replace('\n',
                    ' ')

    klasirane_2023_combined['Училище_формат'] = klasirane_2023_combined['Училище_формат']. \
        replace('Професионална гимназия по екология и биотехнологии "Проф. д-р Асен Златаров"',
                'ПГЕБ "Проф. д-р Асен Златаров"')

    klasirane_2023_combined['Училище_формат'] = klasirane_2023_combined['Училище_формат']. \
        replace('Професионална гимназия по туризъм "Алеко Константинов"',
                'ПГ туризъм "Алеко Константинов"')

    # print(klasirane_2023_combined[['Профил_1', 'Профил_1x', 'Профил_2', 'Профил_3']])

    # Data check
    dataframes = [klasirane_2023_1_clean.sort_index(), klasirane_2023_2_clean.sort_index(),
                  klasirane_2023_3_clean.sort_index(), klasirane_2023_4_clean.sort_index(),
                  mesta_2023_5_clean.sort_index()]

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
    return klasirane_2023_combined
