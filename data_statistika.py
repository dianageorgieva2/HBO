# INSTRUCTIONS FOR NEW YEAR FILES IMPORT, CLEANING, STANDARTISATION
# 0. Transform xls or pdf file to csv and copy in the PYcharm folder HBO under the PC/user/diana folder
# 1. Copy data_statistika_LAST YEAR into the same file and change manually the name (don't refactor or replace all)
# 2. Import correct files from the respective folder
# 3. Add stats_NEWYEAR_clean to the combined_stats at the bottom

import pandas as pd
import numpy as np
import plotly.io as pio
from datetime import datetime

pio.templates.default = "plotly"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format

# ----------STATISTIKA ALL YEARS----------

# Stats data 2025
stats_2025 = pd.read_csv('statistika/statistika_mat_bel_2025.csv', encoding='utf-8', encoding_errors='ignore')
stats_2025_clean = stats_2025.drop([0, 1, 2, 3], axis=0)

stats_2025_clean = stats_2025_clean.rename(columns={
                           "Column1": "Категория точки",
                           "Column2": "БЕЛ",
                           "Column4": "БЕЛ_м",
                           "Column6": "БЕЛ_ж",
                           "Column8": "МАТ",
                           "Column10": "МАТ_м",
                           "Column12": "МАТ_ж",
                           "Column14": "общо",
                           # "Column15": "общо>",
                           "Column16": "общо_м",
                           # "Column17": "общо_м>",
                           "Column18": "общо_д",
                           # "Column19": "общо_д>"
                            })

stats_2025_clean = stats_2025_clean.drop(["Column3", "Column5", "Column7",  "Column9", "Column11",
                                          "Column13", 'Column15', 'Column17', 'Column19'], axis=1)
stats_2025_clean = stats_2025_clean.fillna(0)
stats_2025_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = \
    stats_2025_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2025_clean.reset_index(drop=True, inplace=True)
stats_2025_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 1))
stats_2025_clean["Година"] = "2025"
hist, bin_edges = np.histogram(stats_2025_clean.ТОЧКИ, bins=20)
stats_2025_clean['Bin'] = pd.cut(stats_2025_clean.ТОЧКИ, bins=bin_edges)
stats_2025_clean['Bin'] = stats_2025_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")
stats_2025_clean['преди_мен_о'] = stats_2025_clean['общо'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2025_clean['преди_мен_м'] = stats_2025_clean['общо_м'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2025_clean['преди_мен_д'] = stats_2025_clean['общо_д'].cumsum().transform(lambda x: x.iloc[-1] - x)

# Stats data 2024
stats_2024 = pd.read_csv('statistika/statistika_mat_bel_2024.csv', encoding='utf-8', encoding_errors='ignore')
stats_2024_clean = stats_2024.rename(columns={
                           "Статистика за успеваемостта, НВО 7. клас": "Категория точки",
                           "Unnamed: 1": "БЕЛ",
                           "Unnamed: 3": "БЕЛ_м",
                           "Unnamed: 5": "БЕЛ_ж",
                           "Unnamed: 7": "МАТ",
                           "Unnamed: 9": "МАТ_м",
                           "Unnamed: 11": "МАТ_ж",
                           "Unnamed: 13": "общо",
                           "Unnamed: 15": "общо_м",
                           "Unnamed: 17": "общо_д"})
stats_2024_clean = stats_2024_clean.drop(['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6',  'Unnamed: 8', 'Unnamed: 10',
                                          'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18'], axis=1)
stats_2024_clean = stats_2024_clean.drop([0, 1, 2, 3], axis=0)
stats_2024_clean = stats_2024_clean.fillna(0)
stats_2024_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = \
    stats_2024_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2024_clean.reset_index(drop=True, inplace=True)
stats_2024_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 0.5))
stats_2024_clean["Година"] = "2024"
hist, bin_edges = np.histogram(stats_2024_clean.ТОЧКИ, bins=20)
stats_2024_clean['Bin'] = pd.cut(stats_2024_clean.ТОЧКИ, bins=bin_edges)
stats_2024_clean['Bin'] = stats_2024_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")
stats_2024_clean['преди_мен_о'] = stats_2024_clean['общо'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2024_clean['преди_мен_м'] = stats_2024_clean['общо_м'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2024_clean['преди_мен_д'] = stats_2024_clean['общо_д'].cumsum().transform(lambda x: x.iloc[-1] - x)

# Stats data 2023
stats_2023 = pd.read_csv('statistika/statistika_mat_bel_2023.csv', encoding='utf-8', encoding_errors='ignore')
stats_2023_clean = stats_2023.rename(columns={
                           "Статистика за успеваемостта, НВО 7. клас": "Категория точки",
                           "Unnamed: 1": "БЕЛ",
                           "Unnamed: 3": "БЕЛ_м",
                           "Unnamed: 5": "БЕЛ_ж",
                           "Unnamed: 7": "МАТ",
                           "Unnamed: 9": "МАТ_м",
                           "Unnamed: 11": "МАТ_ж",
                           "Unnamed: 13": "общо",
                           "Unnamed: 15": "общо_м",
                           "Unnamed: 17": "общо_д"})
stats_2023_clean = stats_2023_clean.drop(['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6',  'Unnamed: 8', 'Unnamed: 10',
                                          'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18', 'Unnamed: 19',
                                          'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22'], axis=1)
stats_2023_clean = stats_2023_clean.drop([0, 1, 2], axis=0)
stats_2023_clean = stats_2023_clean.fillna(0)
stats_2023_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = \
    stats_2023_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2023_clean.reset_index(drop=True, inplace=True)
stats_2023_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 0.5))
stats_2023_clean["Година"] = "2023"
hist, bin_edges = np.histogram(stats_2023_clean.ТОЧКИ, bins=20)
stats_2023_clean['Bin'] = pd.cut(stats_2023_clean.ТОЧКИ, bins=bin_edges)
stats_2023_clean['Bin'] = stats_2023_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")
stats_2023_clean['преди_мен_о'] = stats_2023_clean['общо'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2023_clean['преди_мен_м'] = stats_2023_clean['общо_м'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2023_clean['преди_мен_д'] = stats_2023_clean['общо_д'].cumsum().transform(lambda x: x.iloc[-1] - x)


# Stats data 2022
stats_2022 = pd.read_csv('statistika/statistika_mat_bel_2022.csv', encoding='utf-8', encoding_errors='ignore')
stats_2022_clean = stats_2022.rename(columns={
                           "Статистика за успеваемостта, НВО 7. клас, 2022 г.": "Категория точки",
                           "Unnamed: 1": "БЕЛ",
                           "Unnamed: 3": "БЕЛ_м",
                           "Unnamed: 5": "БЕЛ_ж",
                           "Unnamed: 7": "МАТ",
                           "Unnamed: 9": "МАТ_м",
                           "Unnamed: 11": "МАТ_ж",
                           "Unnamed: 13": "общо",
                           "Unnamed: 15": "общо_м",
                           "Unnamed: 17": "общо_д"})
stats_2022_clean = stats_2022_clean.drop(['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6',  'Unnamed: 8', 'Unnamed: 10',
                                          'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18', 'Unnamed: 19',
                                          'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23'], axis=1)
stats_2022_clean = stats_2022_clean.drop([0, 1, 2], axis=0)
stats_2022_clean = stats_2022_clean.fillna(0)
stats_2022_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = \
    stats_2022_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2022_clean.reset_index(drop=True, inplace=True)
stats_2022_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 0.5))
stats_2022_clean["Година"] = "2022"
hist, bin_edges = np.histogram(stats_2022_clean.ТОЧКИ, bins=20)
stats_2022_clean['Bin'] = pd.cut(stats_2022_clean.ТОЧКИ, bins=bin_edges)
stats_2022_clean['Bin'] = stats_2022_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")
stats_2022_clean['преди_мен_о'] = stats_2022_clean['общо'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2022_clean['преди_мен_м'] = stats_2022_clean['общо_м'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2022_clean['преди_мен_д'] = stats_2022_clean['общо_д'].cumsum().transform(lambda x: x.iloc[-1] - x)

# Stats data 2021
stats_2021 = pd.read_csv('statistika/statistika_mat_bel_2021.csv', encoding='utf-8', encoding_errors='ignore')
stats_2021_clean = stats_2021.rename(columns={
                           "Статистика за успеваемост по полове и изпити, РУО СОФИЯ-ГРАД": "Категория точки",
                           "Unnamed: 1": "БЕЛ",
                           "Unnamed: 2": "МАТ",
                           "Unnamed: 3": "общо",
                           "Unnamed: 4": "БЕЛ_м",
                           "Unnamed: 5": "МАТ_м",
                           "Unnamed: 6": "общо_м",
                           "Unnamed: 7": "БЕЛ_ж",
                           "Unnamed: 8": "МАТ_ж",
                           "Unnamed: 9": "общо_д"})
stats_2021_clean = stats_2021_clean.drop([0], axis=0)
stats_2021_clean = stats_2021_clean.fillna(0)
stats_2021_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = \
    stats_2021_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2021_clean.reset_index(drop=True, inplace=True)
stats_2021_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 1))
stats_2021_clean["Година"] = "2021"
hist, bin_edges = np.histogram(stats_2021_clean.ТОЧКИ, bins=20)
stats_2021_clean['Bin'] = pd.cut(stats_2021_clean.ТОЧКИ, bins=bin_edges)
stats_2021_clean['Bin'] = stats_2021_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")
stats_2021_clean['преди_мен_о'] = stats_2021_clean['общо'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2021_clean['преди_мен_м'] = stats_2021_clean['общо_м'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2021_clean['преди_мен_д'] = stats_2021_clean['общо_д'].cumsum().transform(lambda x: x.iloc[-1] - x)

# Stats data 2020
stats_2020 = pd.read_csv('statistika/statistika_mat_bel_2020.csv', encoding='utf-8', encoding_errors='ignore')
stats_2020_clean = stats_2020.rename(columns={
                           'СТАТИСТИКА ЗА УСПЕВАЕМОСТТА ОТ НВО В 7. КЛАС ПО БЕЛ И МАТЕМАТИКА - ОБЩО И ПО ПОЛ   '
                           '26.06.2020 ': "Категория точки",
                           "Unnamed: 1": "БЕЛ",
                           "Unnamed: 2": "МАТ",
                           "Unnamed: 3": "общо",
                           "Unnamed: 4": "БЕЛ_м",
                           "Unnamed: 5": "МАТ_м",
                           "Unnamed: 6": "общо_м",
                           "Unnamed: 7": "БЕЛ_ж",
                           "Unnamed: 8": "МАТ_ж",
                           "Unnamed: 9": "общо_д"})
stats_2020_clean = stats_2020_clean.drop([0], axis=0)
stats_2020_clean = stats_2020_clean.fillna(0)
stats_2020_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = \
    stats_2020_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2020_clean.reset_index(drop=True, inplace=True)
stats_2020_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 1))
stats_2020_clean["Година"] = "2020"
hist, bin_edges = np.histogram(stats_2020_clean.ТОЧКИ, bins=20)
stats_2020_clean['Bin'] = pd.cut(stats_2020_clean.ТОЧКИ, bins=bin_edges)
stats_2020_clean['Bin'] = stats_2020_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")
stats_2020_clean['преди_мен_о'] = stats_2020_clean['общо'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2020_clean['преди_мен_м'] = stats_2020_clean['общо_м'].cumsum().transform(lambda x: x.iloc[-1] - x)
stats_2020_clean['преди_мен_д'] = stats_2020_clean['общо_д'].cumsum().transform(lambda x: x.iloc[-1] - x)


# Data preparation with input if PREMIUM or not
def all_stats(premium):
    all_stats_list = [stats_2025_clean, stats_2024_clean, stats_2023_clean, stats_2022_clean, stats_2021_clean, stats_2020_clean]
    if premium is True:
        df_statistika_combined = pd.concat(all_stats_list, axis=0)
    else:
        all_stats_list = all_stats_list[1:]
        df_statistika_combined = pd.concat(all_stats_list, axis=0)
    # df_statistika_combined = pd.concat([stats_2024_clean, stats_2023_clean, stats_2022_clean, stats_2021_clean, stats_2020_clean], axis=0)
    df_statistika_combined["tochki_sum_o"] = df_statistika_combined.общо * df_statistika_combined.ТОЧКИ
    df_statistika_combined["tochki_sum_m"] = df_statistika_combined.общо_м * df_statistika_combined.ТОЧКИ
    df_statistika_combined["tochki_sum_w"] = df_statistika_combined.общо_д * df_statistika_combined.ТОЧКИ
    df_statistika_grouped = df_statistika_combined.groupby("Година")[["общо_м", "общо_д", "общо", "tochki_sum_m",
                                                                       "tochki_sum_w", "tochki_sum_o"]].agg("sum")
    df_statistika_grouped["tochki_avg_m"] = (df_statistika_grouped.tochki_sum_m / df_statistika_grouped.общо_м).round(2)
    df_statistika_grouped["tochki_avg_w"] = (df_statistika_grouped.tochki_sum_w / df_statistika_grouped.общо_д).round(2)
    df_statistika_grouped["tochki_avg_o"] = (df_statistika_grouped.tochki_sum_o / df_statistika_grouped.общо).round(2)
    df_statistika_grouped.reset_index(inplace=True)
    return df_statistika_combined, df_statistika_grouped, all_stats_list
