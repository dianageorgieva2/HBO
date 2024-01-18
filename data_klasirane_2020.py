# INSTRUCTIONS FOR NEW YEAR FILES IMPORT, CLEANING, STANDARTISATION
# 1. Copy data_klasirane_LAST YEAR into a new py file
# 2. Import correct files from the respective folder
# 3. Replace YEAR with the year you want everywhere
# 4. Check if difference in records in the 3 klasirane and mesta and add the difference as needed
# to the highest possible
# 5. Run data check and specifically check orders, numbers, types

import pandas as pd
import numpy as np
import streamlit as st

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_colwidth', None)


# ----------KLASIRANE 2020----------
@st.cache_data()
def klasirane_2020_combined_function():
    # Data import
    mesta_2020_3 = pd.read_csv('klasirane/2020/свободни-места-за-3-етап-2020_.csv', encoding='utf-8', encoding_errors='ignore')
    mesta_2020_4 = pd.read_csv('klasirane/2020/Свободни-места-за-4-етап-2020.csv', encoding='utf-8', encoding_errors='ignore')
    mesta_2020_5 = pd.read_csv('klasirane/2020/SVOBODNI_MESTA_08_09_2020.csv', encoding='utf-8', encoding_errors='ignore')
    klasirane_2020_1 = pd.read_csv('klasirane/2020/min_max_1_etap.csv', encoding='utf-8', encoding_errors='ignore')
    klasirane_2020_2 = pd.read_csv('klasirane/2020/min_maх_paralelki_2_etap-2020.csv', encoding='utf-8', encoding_errors='ignore')
    klasirane_2020_3 = pd.read_csv('klasirane/2020/min_max_po_paralelki_3kl.csv', encoding='utf-8', encoding_errors='ignore')
    kodove_2020 = pd.read_csv('klasirane/2020/Паралелки-кодове-2020_.csv', encoding='utf-8', encoding_errors='ignore')

    # DATA STRUCTURING
    # Clean model for codes
    kodove_2020_clean = kodove_2020.drop("№\nпо\nред", axis=1)
    kodove_2020_clean = kodove_2020_clean.rename(columns={
                               "Код": "Код паралелка",
                               "Тип": "Вид на паралелката"})
    kodove_2020_clean[["Места_о", "Места_м", "Места_д"]] = kodove_2020_clean['Места:\nобщо/\nмъже/\nжени'].\
        str.split('/', n=2, expand=True)
    kodove_2020_clean = kodove_2020_clean.drop('Места:\nобщо/\nмъже/\nжени', axis=1)
    kodove_2020_clean[["Места_о", "Места_м", "Места_д"]] = kodove_2020_clean[["Места_о", "Места_м", "Места_д"]].\
        replace('-', 0)
    kodove_2020_clean = kodove_2020_clean[kodove_2020_clean["Код паралелка"].notna()]
    kodove_2020_clean[["Места_о", "Места_м", "Места_д"]] = kodove_2020_clean[["Места_о", "Места_м", "Места_д"]].\
        astype(int)
    kodove_2020_clean['Места_общ_брой'] = kodove_2020_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
    kodove_2020_clean['Места_общ_брой_м'] = kodove_2020_clean[["Места_о", "Места_м"]].sum(axis=1)
    kodove_2020_clean['Места_общ_брой_д'] = kodove_2020_clean[["Места_о", "Места_д"]].sum(axis=1)
    kodove_2020_clean["Година"] = "2020"
    kodove_2020_clean["Код паралелка"] = kodove_2020_clean["Код паралелка"].astype(str)
    kodove_2020_clean["Код паралелка"] = kodove_2020_clean["Код паралелка"].str.zfill(4)
    kodove_2020_clean = kodove_2020_clean.sort_values(by='Код паралелка')
    kodove_2020_clean.reset_index(drop=True, inplace=True)
    # print(f'Kodove: {kodove_2020_clean.shape}')

    # KLASIRANE 1
    klasirane_2020_1_clean = klasirane_2020_1.drop(['СПРАВКА'], axis=1)
    klasirane_2020_1_clean = klasirane_2020_1_clean.rename(columns={
                               "Unnamed: 1": "Училище",
                               "Unnamed: 2": "Паралелка",
                               "Unnamed: 3": "Минимален бал",
                               "Unnamed: 4": "Максимален бал",
                               "Unnamed: 5": "Пол"})
    klasirane_2020_1_clean = klasirane_2020_1_clean.drop([0, 1, 2, 3, 4], axis=0)
    klasirane_2020_1_clean[['Код училище', 'Име училище']] = klasirane_2020_1_clean['Училище'].str.split(' ', n=1, expand=True)

    klasirane_2020_1_clean[['Код паралелка', 'Име паралелка']] = klasirane_2020_1_clean['Паралелка'].\
        str.split(' ', n=1, expand=True)
    klasirane_2020_1_clean = klasirane_2020_1_clean.drop(['Училище', 'Паралелка'], axis=1)
    klasirane_2020_1_clean["Мин_бал_о"] = 0
    klasirane_2020_1_clean["Мин_бал_м"] = 0
    klasirane_2020_1_clean["Мин_бал_ж"] = 0
    klasirane_2020_1_clean.loc[klasirane_2020_1_clean['Пол'] == 'без квоти', 'Мин_бал_о'] = \
        klasirane_2020_1_clean['Минимален бал']
    klasirane_2020_1_clean.loc[klasirane_2020_1_clean['Пол'] == 'младежи', 'Мин_бал_м'] = \
        klasirane_2020_1_clean['Минимален бал']
    klasirane_2020_1_clean.loc[klasirane_2020_1_clean['Пол'] == 'девойки', 'Мин_бал_ж'] = \
        klasirane_2020_1_clean['Минимален бал']
    klasirane_2020_1_clean["Макс_бал_о"] = 0
    klasirane_2020_1_clean["Макс_бал_м"] = 0
    klasirane_2020_1_clean["Макс_бал_ж"] = 0
    klasirane_2020_1_clean.loc[klasirane_2020_1_clean['Пол'] == 'без квоти', 'Макс_бал_о'] = \
        klasirane_2020_1_clean['Максимален бал']
    klasirane_2020_1_clean.loc[klasirane_2020_1_clean['Пол'] == 'младежи', 'Макс_бал_м'] = \
        klasirane_2020_1_clean['Максимален бал']
    klasirane_2020_1_clean.loc[klasirane_2020_1_clean['Пол'] == 'девойки', 'Макс_бал_ж'] = \
        klasirane_2020_1_clean['Максимален бал']
    klasirane_2020_1_clean[['Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2020_1_clean[['Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
        apply(pd.to_numeric, errors='coerce').astype("float")

    klasirane_2020_1_clean = klasirane_2020_1_clean.groupby('Код паралелка', as_index=False).agg({
        'Минимален бал': 'min',
        'Максимален бал': 'max',
        'Пол': lambda x: None,
        'Код училище': 'first',
        'Име училище': 'first',
        'Име паралелка': 'first',
        'Мин_бал_о': 'sum',
        'Мин_бал_м': 'sum',
        'Мин_бал_ж': 'sum',
        'Макс_бал_о': 'sum',
        'Макс_бал_м': 'sum',
        'Макс_бал_ж': 'sum'
    })

    klasirane_2020_1_clean["Мин_бал_о"] = klasirane_2020_1_clean.apply(
        lambda row: min(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_о"] == 0 and row["Мин_бал_м"] != 0 and row["Мин_бал_ж"] != 0
        else max(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_м"] == 0 or row["Мин_бал_ж"] == 0 and row["Мин_бал_о"] == 0
        else row["Мин_бал_о"], axis=1)
    klasirane_2020_1_clean["Макс_бал_о"] = klasirane_2020_1_clean.apply(
        lambda row: max(row["Макс_бал_м"], row["Макс_бал_ж"]) if row["Макс_бал_о"] == 0 else row["Макс_бал_о"], axis=1)
    klasirane_2020_1_clean = klasirane_2020_1_clean.sort_values(by='Код паралелка')
    klasirane_2020_1_clean.reset_index(drop=True, inplace=True)
    klasirane_2020_1_clean = pd.merge(kodove_2020_clean, klasirane_2020_1_clean, on="Код паралелка", how='outer')
    klasirane_2020_1_clean["Класиране"] = 1
    klasirane_2020_1_clean = klasirane_2020_1_clean.sort_values(by='Мин_бал_о', ascending=False)
    klasirane_2020_1_clean.reset_index(drop=True, inplace=True)
    klasirane_2020_1_clean = klasirane_2020_1_clean.sort_values(by='Код паралелка')
    klasirane_2020_1_clean = klasirane_2020_1_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                                    'Балообразуване',  'Година', 'Код училище', 'Места_о',
                                                     'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                     'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                     'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
    basic_data_2020 = klasirane_2020_1_clean[['Район', 'Училище',  'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                              'Балообразуване', 'Година', 'Код училище']]
    # print(f'Klasirane 1: {klasirane_2020_1_clean.shape}')

    # # Find and print items that are in kodove_set but not in klasirane_set
    # set1 = set(kodove_2020_clean["Код паралелка"])
    # set2 = set(klasirane_2020_1_clean["Код паралелка"])
    # different_items = set1 - set2
    # for k in different_items:
    #     print(k)

    # KLASIRANE 2
    klasirane_2020_2_clean = klasirane_2020_2.drop(['СПРАВКА'], axis=1)
    klasirane_2020_2_clean = klasirane_2020_2_clean.rename(columns={
                               "Unnamed: 1": "Училище",
                               "Unnamed: 2": "Паралелка",
                               "Unnamed: 3": "Минимален бал",
                               "Unnamed: 4": "Максимален бал",
                               "Unnamed: 5": "Пол"})
    klasirane_2020_2_clean = klasirane_2020_2_clean.drop([0, 1, 2, 3, 4], axis=0)
    klasirane_2020_2_clean[['Код паралелка', 'Име паралелка']] = klasirane_2020_2_clean['Паралелка'].\
        str.split(' ', n=1, expand=True)
    klasirane_2020_2_clean = klasirane_2020_2_clean.drop(['Училище', 'Паралелка'], axis=1)
    klasirane_2020_2_clean["Мин_бал_о"] = 0
    klasirane_2020_2_clean["Мин_бал_м"] = 0
    klasirane_2020_2_clean["Мин_бал_ж"] = 0
    klasirane_2020_2_clean.loc[klasirane_2020_2_clean['Пол'] == 'без квоти', 'Мин_бал_о'] = \
        klasirane_2020_2_clean['Минимален бал']
    klasirane_2020_2_clean.loc[klasirane_2020_2_clean['Пол'] == 'младежи', 'Мин_бал_м'] = \
        klasirane_2020_2_clean['Минимален бал']
    klasirane_2020_2_clean.loc[klasirane_2020_2_clean['Пол'] == 'девойки', 'Мин_бал_ж'] = \
        klasirane_2020_2_clean['Минимален бал']
    klasirane_2020_2_clean["Макс_бал_о"] = 0
    klasirane_2020_2_clean["Макс_бал_м"] = 0
    klasirane_2020_2_clean["Макс_бал_ж"] = 0
    klasirane_2020_2_clean.loc[klasirane_2020_2_clean['Пол'] == 'без квоти', 'Макс_бал_о'] = \
        klasirane_2020_2_clean['Максимален бал']
    klasirane_2020_2_clean.loc[klasirane_2020_2_clean['Пол'] == 'младежи', 'Макс_бал_м'] = \
        klasirane_2020_2_clean['Максимален бал']
    klasirane_2020_2_clean.loc[klasirane_2020_2_clean['Пол'] == 'девойки', 'Макс_бал_ж'] = \
        klasirane_2020_2_clean['Максимален бал']
    klasirane_2020_2_clean[['Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2020_2_clean[['Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
        apply(pd.to_numeric, errors='coerce').astype("float")
    klasirane_2020_2_clean = klasirane_2020_2_clean.groupby('Код паралелка', as_index=False).agg({
        'Минимален бал': 'min',
        'Максимален бал': 'max',
        'Пол': lambda x: None,
        'Име паралелка': 'first',
        'Мин_бал_о': 'sum',
        'Мин_бал_м': 'sum',
        'Мин_бал_ж': 'sum',
        'Макс_бал_о': 'sum',
        'Макс_бал_м': 'sum',
        'Макс_бал_ж': 'sum'})

    klasirane_2020_2_clean["Мин_бал_о"] = klasirane_2020_2_clean.apply(
        lambda row: min(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_о"] == 0 and row["Мин_бал_м"] != 0 and row["Мин_бал_ж"] != 0
        else max(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_м"] == 0 or row["Мин_бал_ж"] == 0 and row["Мин_бал_о"] == 0
        else row["Мин_бал_о"], axis=1)
    klasirane_2020_2_clean["Макс_бал_о"] = klasirane_2020_2_clean.apply(
        lambda row: max(row["Макс_бал_м"], row["Макс_бал_ж"]) if row["Макс_бал_о"] == 0 else row["Макс_бал_о"], axis=1)
    klasirane_2020_2_clean = klasirane_2020_2_clean.sort_values(by='Код паралелка')
    klasirane_2020_2_clean.reset_index(drop=True, inplace=True)
    klasirane_2020_2_clean = pd.merge(basic_data_2020, klasirane_2020_2_clean, on="Код паралелка", how='outer')
    klasirane_2020_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
        np.nan
    klasirane_2020_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
        klasirane_2020_2_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м',
                                'Места_общ_брой_д']].apply(pd.to_numeric, errors='coerce').astype("Int64")
    klasirane_2020_2_clean["Класиране"] = 2
    klasirane_2020_2_clean = klasirane_2020_2_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                                    'Балообразуване',  'Година', 'Код училище', 'Места_о',
                                                     'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                     'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                     'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
    klasirane_2020_2_clean.index = klasirane_2020_1_clean.index
    # print(f'Klasirane 2: {klasirane_2020_2_clean.shape}')

    # KLASIRANE 3
    mesta_2020_3_clean = mesta_2020_3.drop(mesta_2020_3.columns[[0, 1, 2, 3, 5]], axis=1)
    mesta_2020_3_clean = mesta_2020_3_clean.rename(columns={
                               "Unnamed: 4": "Код паралелка",
                               "Unnamed: 6": "Места_о",
                               "Unnamed: 7": "Места_м",
                               "Unnamed: 8": "Места_д"})
    mesta_2020_3_clean = mesta_2020_3_clean[mesta_2020_3_clean["Код паралелка"].notna()]
    mesta_2020_3_clean = mesta_2020_3_clean.drop(1, axis=0)
    mesta_2020_3_clean = mesta_2020_3_clean.fillna(0)
    mesta_2020_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2020_3_clean[["Места_о", "Места_м", "Места_д"]].\
        replace('-', 0)
    mesta_2020_3_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2020_3_clean[["Места_о", "Места_м", "Места_д"]].\
        astype(int)
    mesta_2020_3_clean['Места_общ_брой'] = mesta_2020_3_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
    mesta_2020_3_clean['Места_общ_брой_м'] = mesta_2020_3_clean[["Места_о", "Места_м"]].sum(axis=1)
    mesta_2020_3_clean['Места_общ_брой_д'] = mesta_2020_3_clean[["Места_о", "Места_д"]].sum(axis=1)
    mesta_2020_3_clean = pd.merge(basic_data_2020, mesta_2020_3_clean, on="Код паралелка", how='outer')
    mesta_2020_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
        mesta_2020_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']].\
        apply(pd.to_numeric, errors='coerce').astype("Int64")
    mesta_2020_3_clean["Класиране"] = 3
    mesta_2020_3_clean = mesta_2020_3_clean.sort_values(by='Код паралелка')
    mesta_2020_3_clean.reset_index(drop=True, inplace=True)
    mesta_2020_3_clean.index = klasirane_2020_1_clean.index

    klasirane_2020_3_clean = klasirane_2020_3.drop(['СПРАВКА'], axis=1)
    klasirane_2020_3_clean = klasirane_2020_3_clean.rename(columns={
                               "Unnamed: 1": "Училище",
                               "Unnamed: 2": "Паралелка",
                               "Unnamed: 3": "Минимален бал",
                               "Unnamed: 4": "Максимален бал",
                               "Unnamed: 5": "Пол"})
    klasirane_2020_3_clean = klasirane_2020_3_clean.drop([0, 1, 2, 3, 4], axis=0)
    klasirane_2020_3_clean[['Код паралелка', 'Име паралелка']] = klasirane_2020_3_clean['Паралелка'].\
        str.split(' ', n=1, expand=True)
    klasirane_2020_3_clean = klasirane_2020_3_clean[klasirane_2020_3_clean["Код паралелка"].notna()]
    klasirane_2020_3_clean = klasirane_2020_3_clean.drop(['Училище', 'Паралелка', 'Име паралелка'], axis=1)
    klasirane_2020_3_clean["Мин_бал_о"] = 0
    klasirane_2020_3_clean["Мин_бал_м"] = 0
    klasirane_2020_3_clean["Мин_бал_ж"] = 0
    klasirane_2020_3_clean.loc[klasirane_2020_3_clean['Пол'] == 'без квоти', 'Мин_бал_о'] = \
        klasirane_2020_3_clean['Минимален бал']
    klasirane_2020_3_clean.loc[klasirane_2020_3_clean['Пол'] == 'младежи', 'Мин_бал_м'] = \
        klasirane_2020_3_clean['Минимален бал']
    klasirane_2020_3_clean.loc[klasirane_2020_3_clean['Пол'] == 'девойки', 'Мин_бал_ж'] = \
        klasirane_2020_3_clean['Минимален бал']
    klasirane_2020_3_clean["Макс_бал_о"] = 0
    klasirane_2020_3_clean["Макс_бал_м"] = 0
    klasirane_2020_3_clean["Макс_бал_ж"] = 0
    klasirane_2020_3_clean.loc[klasirane_2020_3_clean['Пол'] == 'без квоти', 'Макс_бал_о'] = \
        klasirane_2020_3_clean['Максимален бал']
    klasirane_2020_3_clean.loc[klasirane_2020_3_clean['Пол'] == 'младежи', 'Макс_бал_м'] = \
        klasirane_2020_3_clean['Максимален бал']
    klasirane_2020_3_clean.loc[klasirane_2020_3_clean['Пол'] == 'девойки', 'Макс_бал_ж'] = \
        klasirane_2020_3_clean['Максимален бал']
    klasirane_2020_3_clean[['Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']] = klasirane_2020_3_clean[['Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']].\
        apply(pd.to_numeric, errors='coerce').astype("float")
    klasirane_2020_3_clean = klasirane_2020_3_clean.groupby('Код паралелка', as_index=False).agg({
        'Минимален бал': 'min',
        'Максимален бал': 'max',
        'Пол': lambda x: None,
        'Мин_бал_о': 'sum',
        'Мин_бал_м': 'sum',
        'Мин_бал_ж': 'sum',
        'Макс_бал_о': 'sum',
        'Макс_бал_м': 'sum',
        'Макс_бал_ж': 'sum'})

    klasirane_2020_3_clean["Мин_бал_о"] = klasirane_2020_3_clean.apply(
        lambda row: min(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_о"] == 0 and row["Мин_бал_м"] != 0 and row["Мин_бал_ж"] != 0
        else max(row["Мин_бал_м"], row["Мин_бал_ж"]) if row["Мин_бал_м"] == 0 or row["Мин_бал_ж"] == 0 and row["Мин_бал_о"] == 0
        else row["Мин_бал_о"], axis=1)
    klasirane_2020_3_clean["Макс_бал_о"] = klasirane_2020_3_clean.apply(
        lambda row: max(row["Макс_бал_м"], row["Макс_бал_ж"]) if row["Макс_бал_о"] == 0 else row["Макс_бал_о"], axis=1)
    klasirane_2020_3_clean = klasirane_2020_3_clean.sort_values(by='Код паралелка')
    klasirane_2020_3_clean.reset_index(drop=True, inplace=True)
    klasirane_2020_3_clean = pd.merge(mesta_2020_3_clean, klasirane_2020_3_clean, on="Код паралелка", how='outer')
    klasirane_2020_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
        klasirane_2020_3_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м',
                                'Места_общ_брой_д']].apply(pd.to_numeric, errors='coerce').astype("Int64")
    klasirane_2020_3_clean["Класиране"] = 3
    klasirane_2020_3_clean = klasirane_2020_3_clean[['Район', 'Училище', 'Код паралелка', 'Паралелка', 'Вид на паралелката',
                                                    'Балообразуване',  'Година', 'Код училище', 'Места_о',
                                                     'Места_м', 'Места_д', 'Места_общ_брой', 'Места_общ_брой_м',
                                                     'Места_общ_брой_д', 'Класиране', 'Мин_бал_о', 'Мин_бал_м',
                                                     'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж']]
    mesta_2020_3_clean.index = klasirane_2020_1_clean.index
    # print(f'Klasirane 3: {klasirane_2020_3_clean.shape}')

    # KLASIRANE 4
    mesta_2020_4_clean = mesta_2020_4.drop(mesta_2020_4.columns[[0, 1, 2, 3, 5]], axis=1)
    mesta_2020_4_clean = mesta_2020_4_clean.rename(columns={
                               "Unnamed: 4": "Код паралелка",
                               "Unnamed: 6": "Места_о",
                               "Unnamed: 7": "Места_м",
                               "Unnamed: 8": "Места_д"})
    mesta_2020_4_clean = mesta_2020_4_clean[mesta_2020_4_clean["Код паралелка"].notna()]
    mesta_2020_4_clean = mesta_2020_4_clean.drop(0, axis=0)
    mesta_2020_4_clean = mesta_2020_4_clean.fillna(0)
    mesta_2020_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2020_4_clean[["Места_о", "Места_м", "Места_д"]].\
        replace('-', 0)
    mesta_2020_4_clean[["Места_о", "Места_м", "Места_д"]] = mesta_2020_4_clean[["Места_о", "Места_м", "Места_д"]].\
        astype(int)
    mesta_2020_4_clean['Места_общ_брой'] = mesta_2020_4_clean[["Места_о", "Места_м", "Места_д"]].sum(axis=1)
    mesta_2020_4_clean['Места_общ_брой_м'] = mesta_2020_4_clean[["Места_о", "Места_м"]].sum(axis=1)
    mesta_2020_4_clean['Места_общ_брой_д'] = mesta_2020_4_clean[["Места_о", "Места_д"]].sum(axis=1)
    mesta_2020_4_clean = pd.merge(basic_data_2020, mesta_2020_4_clean, on="Код паралелка", how='outer')
    mesta_2020_4_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']] = \
        mesta_2020_4_clean[["Места_о", "Места_м", "Места_д", 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д']].\
        apply(pd.to_numeric, errors='coerce').astype("Int64")
    mesta_2020_4_clean["Класиране"] = 4
    mesta_2020_4_clean = mesta_2020_4_clean.sort_values(by='Код паралелка')
    mesta_2020_4_clean.reset_index(drop=True, inplace=True)
    mesta_2020_4_clean.index = klasirane_2020_1_clean.index
    # print(f'Klasirane 4: {mesta_2020_4_clean.shape}')

    # Data preparation
    klasirane_2020_combined = pd.concat([klasirane_2020_1_clean.sort_index(), klasirane_2020_2_clean.sort_index(),
                                         klasirane_2020_3_clean.sort_index(), mesta_2020_4_clean.sort_index()], axis=0)
    klasirane_2020_combined.reset_index(drop=True, inplace=True)

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка']
    #
    # klasirane_2020_combined.loc[klasirane_2020_combined['Профил_1'].str.startswith("Чужди езици"), 'Профил_1'] = \
    #     'Чужди езици'

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Чужди езици -АЕ интензивно, ИЕ, ГИ и ИЦ',
                'Чужди езици - АЕ интензивно, ИЕ, ГИ и ИЦ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Чужди езици АЕ интензивно, ИЕ, М, ГИ',
                'Чужди езици - АЕ интензивно, ИЕ, М, ГИ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Чужди езици - интензивно НЕ,  РЕ',
                'Чужди езици - НЕ интензивно, РЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Чужди езици -  интензивно ФЕ, РЕ',
                'Чужди езици -  ФЕ интензивно , РЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Телекомуникационни системи-АЕ',
                'Телекомуникационни системи - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Софтуерни и хардуени науки - АЕ интензивно, КорЕ',
                'Софтуерни и хардуерни науки - АЕ интензивно, КорЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Софтуерни и хардуерни науки /ИЕ/',
                'Софтуерни и хардуерни науки - ИЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Топлотехника - отоплителна климат. вентилационна и хладилна - АЕ (дуална)',
                'Топлотехника-отоплителна климат. вентилационна и хладилна - АЕ (дуална)')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Производство на кулинарни изделия и напитки - готвач',
                'Производство на кулинарни изделия и напитки (готвач)')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Продавач-консултант /АЕ/',
                'Продавач-консултант - АЕ ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Продавач-консултант /РЕ/',
                'Продавач-консултант - РЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Природни науки ИЕ - интензивно, АЕ, БЗО, ХООС',
                'Природни науки - ИЕ интензивно, АЕ, БЗО, ХООС')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Предприемачески - АЕ интензивно; РЕ',
                'Предприемачески - АЕ интензивно, РЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Предприемачески  - АЕ интензивно, РЕ',
                'Предприемачески - АЕ интензивно, РЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Подемно - транспортна техника монтирана на пътни транспортни средства',
                'Подемно-транспортна техника монтирана на пътни транспортни средства')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Логистика на товари и услуги /АЕ/',
                'Логистика на товари и услуги - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Компютърна графика- АЕ',
                'Компютърна графика - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Кетъринг   - ГрЕ',
                'Кетъринг - ГрЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Интериорен дизайн- НЕ',
                'Интериорен дизайн - НЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Графичен дизайн /АЕ/',
                'Графичен дизайн - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Български танци /АЕ/',
                'Български танци - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Автотранспортна техника - техник АЕ',
                'Автотранспортна техника - техник, АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Автомобилна  мехатроника - АЕ',
                'Автомобилна мехатроника - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Интериорен дизайн- НЕ, АЕ',
                'Интериорен дизайн - НЕ, АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Графичен дизайн /',
                'Графичен дизайн')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Логистика на товари и услуги /НЕ/',
                'Логистика на товари и услуги - НЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Логистика на товари и услуги - куриер /АЕ/',
                'Логистика на товари и услуги - куриер АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Логистика на товари и услуги - куриер /РЕ/',
                'Логистика на товари и услуги - куриер РЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace(r'\s*/\s*', ', ', regex=True)


    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Автомобилна  мехатроника - АЕ (дуална)',
                'Автомобилна мехатроника - АЕ (дуална)')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Организация на хотелиерството -  АЕ',
                'Организация на хотелиерството - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Предприемачество - АЕ интензивно, НЕ',
                'Предприемачески - АЕ интензивно, НЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Производство на месо месни продукти и риба - АЕ',
                'Производство на месо, месни продукти и риба - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Хумантарни науки - АЕ интензивно, НЕ',
                'Хуманитарни науки - АЕ интензивно, НЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Чужди езици - АЕ интензивно  ИЕ',
                'Чужди езици - АЕ интензивно, ИЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        replace('Софтуерни и хардуери науки - АЕ',
                'Софтуерни и хардуерни науки - АЕ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        str.replace('Биология и здравно образование -', 'БЗО')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        str.replace('Топлотехника - отоплителна климат. вентилационна и хладилна - АЕ (дуална)',
                    'Топлотехника-отоплителна климат. вентилационна и хладилна - АЕ (дуална)')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        str.replace('интензивно ',
                    'интензивно, ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].\
        str.replace('\n',
                    ' ')

    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].str.lstrip()
    klasirane_2020_combined['Паралелка_формат'] = klasirane_2020_combined['Паралелка_формат'].str.rstrip()

    klasirane_2020_combined[['Профил_1', 'Профил_1x']] = klasirane_2020_combined['Паралелка_формат'].\
        str.split(' - ', n=1, expand=True)

    klasirane_2020_combined['Профил_1'] = klasirane_2020_combined['Профил_1'].str.lstrip()
    klasirane_2020_combined['Профил_1'] = klasirane_2020_combined['Профил_1'].str.rstrip()

    klasirane_2020_combined['Профил_1x'] = klasirane_2020_combined['Профил_1x'].str.lstrip()
    klasirane_2020_combined['Профил_1x'] = klasirane_2020_combined['Профил_1x'].str.rstrip()

    klasirane_2020_combined[['Профил_2', 'Профил_3']] = klasirane_2020_combined['Профил_1x'].\
        str.split(',', n=1, expand=True)

    klasirane_2020_combined[['Профил_1x', 'Профил_2', 'Профил_3']] = klasirane_2020_combined[['Профил_1x', 'Профил_2', 'Профил_3']].fillna('-')

    klasirane_2020_combined['Профил_2'] = klasirane_2020_combined['Профил_2'].str.lstrip()
    klasirane_2020_combined['Профил_2'] = klasirane_2020_combined['Профил_2'].str.rstrip()

    klasirane_2020_combined['Профил_3'] = klasirane_2020_combined['Профил_3'].str.lstrip()
    klasirane_2020_combined['Профил_3'] = klasirane_2020_combined['Профил_3'].str.rstrip()

    klasirane_2020_combined['Профил_2'] = klasirane_2020_combined['Профил_2'].\
        replace('AE интензивно',
                'АЕ интензивно')

    klasirane_2020_combined['Училище_формат'] = klasirane_2020_combined['Училище']
    klasirane_2020_combined['Училище_формат'] = klasirane_2020_combined['Училище_формат'].str.split(',', n=1).str.get(0)

    klasirane_2020_combined['Училище_формат'] = klasirane_2020_combined['Училище_формат']. \
        str.replace('\n',
                    ' ')

    klasirane_2020_combined['Училище_формат'] = klasirane_2020_combined['Училище_формат']. \
        replace('Професионална гимназия по екология и биотехнологии "Проф. д-р Асен Златаров"',
                'ПГЕБ "Проф. д-р Асен Златаров"')

    klasirane_2020_combined['Училище_формат'] = klasirane_2020_combined['Училище_формат']. \
        replace('Професионална гимназия по туризъм "Алеко Константинов"',
                'ПГ туризъм "Алеко Константинов"')

    # unique_values = klasirane_2020_combined['Профил_1x'].sort_values().unique()
    # for value in unique_values:
    #     print(value)
    # print(klasirane_2020_combined.loc[klasirane_2020_combined['Паралелка'].str.startswith('Топлотехника'), 'Паралелка_формат'])

    # print(klasirane_2020_combined[['Профил_1x', 'Профил_2', 'Профил_3']])

    # print(klasirane_2020_combined[['Профил_1', 'Профил_1x', 'Профил_2', 'Профил_3']])

    # Data check
    dataframes = [klasirane_2020_1_clean.sort_index(), klasirane_2020_2_clean.sort_index(),
                  klasirane_2020_3_clean.sort_index(), mesta_2020_4_clean.sort_index()]

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
    return klasirane_2020_combined
