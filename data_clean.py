import pandas as pd
import numpy as np
import plotly.io as pio
import textwrap

pio.templates.default = "plotly"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format

#----------STATISTIKA ALL YEARS----------
# Stats data load
stats_2023 = pd.read_csv('statistika/statistika_mat_bel_2023.csv')
stats_2022 = pd.read_csv('statistika/statistika_mat_bel_2022.csv')
stats_2021 = pd.read_csv('statistika/statistika_mat_bel_2021.csv')
stats_2020 = pd.read_csv('statistika/statistika_mat_bel_2020.csv')

# Stats data clean-up
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
stats_2023_clean = stats_2023_clean.drop(['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6',  'Unnamed: 8', 'Unnamed: 10', 'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22'], axis=1)
stats_2023_clean = stats_2023_clean.drop([0, 1, 2], axis=0)
stats_2023_clean = stats_2023_clean.fillna(0)
stats_2023_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2023_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2023_clean.reset_index(drop=True, inplace=True)
stats_2023_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 0.5))
stats_2023_clean["Година"] = "2023"
hist, bin_edges = np.histogram(stats_2023_clean.ТОЧКИ, bins=20)
stats_2023_clean['Bin'] = pd.cut(stats_2023_clean.ТОЧКИ, bins=bin_edges)
stats_2023_clean['Bin'] = stats_2023_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")

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
stats_2022_clean = stats_2022_clean.drop(['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6',  'Unnamed: 8', 'Unnamed: 10', 'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23'], axis=1)
stats_2022_clean = stats_2022_clean.drop([0, 1, 2], axis=0)
stats_2022_clean = stats_2022_clean.fillna(0)
stats_2022_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2022_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2022_clean.reset_index(drop=True, inplace=True)
stats_2022_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 0.5))
stats_2022_clean["Година"] = "2022"
hist, bin_edges = np.histogram(stats_2022_clean.ТОЧКИ, bins=20)
stats_2022_clean['Bin'] = pd.cut(stats_2022_clean.ТОЧКИ, bins=bin_edges)
stats_2022_clean['Bin'] = stats_2022_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")

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
stats_2021_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2021_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2021_clean.reset_index(drop=True, inplace=True)
stats_2021_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 1))
stats_2021_clean["Година"] = "2021"
hist, bin_edges = np.histogram(stats_2021_clean.ТОЧКИ, bins=20)
stats_2021_clean['Bin'] = pd.cut(stats_2021_clean.ТОЧКИ, bins=bin_edges)
stats_2021_clean['Bin'] = stats_2021_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")

stats_2020_clean = stats_2020.rename(columns={
                           'СТАТИСТИКА ЗА УСПЕВАЕМОСТТА ОТ НВО В 7. КЛАС ПО БЕЛ И МАТЕМАТИКА - ОБЩО И ПО ПОЛ   26.06.2020 ': "Категория точки",
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
stats_2020_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2020_clean[['общо', 'общо_м', 'общо_д', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2020_clean.reset_index(drop=True, inplace=True)
stats_2020_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 1))
stats_2020_clean["Година"] = "2020"
hist, bin_edges = np.histogram(stats_2020_clean.ТОЧКИ, bins=20)
stats_2020_clean['Bin'] = pd.cut(stats_2020_clean.ТОЧКИ, bins=bin_edges)
stats_2020_clean['Bin'] = stats_2020_clean['Bin'].apply(lambda x: f"{x.left:.0f} - {x.right:.0f}")

# Data preparation
df_statistika_combined = pd.concat([stats_2023_clean, stats_2022_clean, stats_2021_clean, stats_2020_clean], axis=0)
df_statistika_combined["tochki_sum_o"] = df_statistika_combined.общо * df_statistika_combined.ТОЧКИ
df_statistika_combined["tochki_sum_m"] = df_statistika_combined.общо_м * df_statistika_combined.ТОЧКИ
df_statistika_combined["tochki_sum_w"] = df_statistika_combined.общо_д * df_statistika_combined.ТОЧКИ
df_statistika_combined = df_statistika_combined.groupby("Година")[["общо_м", "общо_д", "общо", "tochki_sum_m", "tochki_sum_w", "tochki_sum_o"]].agg("sum")
df_statistika_combined["tochki_avg_m"] = (df_statistika_combined.tochki_sum_m / df_statistika_combined.общо_м).round(2)
df_statistika_combined["tochki_avg_w"] = (df_statistika_combined.tochki_sum_w / df_statistika_combined.общо_д).round(2)
df_statistika_combined["tochki_avg_o"] = (df_statistika_combined.tochki_sum_o / df_statistika_combined.общо).round(2)
df_statistika_combined.reset_index(inplace=True)

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
klasirane_2023_1_clean = klasirane_2023_1_clean.drop('СПРАВКА\nза минималния и максималния бал по паралелки\nв РУО СОФИЯ-ГРАД\nКъм дата 12.07.2023 г.', axis=1)
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
klasirane_2023_2_clean = klasirane_2023_2_clean.drop(['СПРАВКА\nза минималния и максималния бал по паралелки\nв РУО СОФИЯ-ГРАД\nКъм дата 19.07.2023 г.\n', "Unnamed: 5"], axis=1)
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
klasirane_2023_2_clean = klasirane_2023_2_clean.sort_index()

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
klasirane_2023_3_clean = klasirane_2023_3_clean.drop(['СПРАВКА\nза минималния и максималния бал по паралелки\nв РУО СОФИЯ-ГРАД\nКъм дата 31.07.2023 г.\n', "Unnamed: 5"], axis=1)
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
klasirane_2023_4_clean = klasirane_2023_4_clean.drop(['СПРАВКА\nза минималния и максималния бал по паралелки\nв РУО СОФИЯ-ГРАД\nКъм дата 10.08.2023 г.\n', "Unnamed: 5"], axis=1)
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
mesta_2023_3_clean = mesta_2023_3.drop(['СВОБОДНИ МЕСТА ЗА ТРЕТИ ЕТАП НА КЛАСИРАНЕ ПО ПАРАЛЕЛКИ С КОДОВЕ ПО УЧИЛИЩА, \nПРИЕМ В VIII КЛАС ЗА УЧЕБНАТА 2023/ 2024 ГОДИНА ', 'Unnamed: 5'], axis=1)
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
mesta_2023_3_clean["Година"] = "2023"
mesta_2023_3_clean = mesta_2023_3_clean.sort_values(by='Код паралелка')
mesta_2023_3_clean.reset_index(drop=True, inplace=True)
mesta_2023_3_clean.index = klasirane_2023_3_clean.index
klasirane_2023_3_clean_plus = pd.concat([klasirane_2023_3_clean, mesta_2023_3_clean], axis=1, copy=False, ignore_index=False)
klasirane_2023_3_clean_plus = klasirane_2023_3_clean_plus.sort_index()
klasirane_2023_3_clean_plus = klasirane_2023_3_clean_plus.loc[:, ~klasirane_2023_3_clean_plus.columns.duplicated()].copy()

mesta_2023_4_clean = mesta_2023_4.drop(['СВОБОДНИ МЕСТА ЗА ЧЕТВЪРТИ ЕТАП НА КЛАСИРАНЕ ПО ПАРАЛЕЛКИ С КОДОВЕ ПО УЧИЛИЩА, \nПРИЕМ В VIII КЛАС ЗА УЧЕБНАТА 2023/ 2024 ГОДИНА ', 'Unnamed: 5'], axis=1)
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
mesta_2023_4_clean["Година"] = "2023"
mesta_2023_4_clean = mesta_2023_4_clean.sort_values(by='Код паралелка')
mesta_2023_4_clean.reset_index(drop=True, inplace=True)
mesta_2023_4_clean.index = klasirane_2023_4_clean.index
klasirane_2023_4_clean_plus = pd.concat([klasirane_2023_4_clean, mesta_2023_4_clean], axis=1, copy=False, ignore_index=False)
klasirane_2023_4_clean_plus = klasirane_2023_4_clean_plus.sort_index()
klasirane_2023_4_clean_plus = klasirane_2023_4_clean_plus.loc[:, ~klasirane_2023_4_clean_plus.columns.duplicated()].copy()

mesta_2023_5_clean = mesta_2023_5.drop(['СВОБОДНИ МЕСТА СЛЕД ЧЕТВЪРТИ ЕТАП НА КЛАСИРАНЕ ПО ПАРАЛЕЛКИ С КОДОВЕ ПО УЧИЛИЩА, \nПРИЕМ В VIII КЛАС ЗА УЧЕБНАТА 2023/ 2024 ГОДИНА ', 'Unnamed: 5', 'Unnamed: 9'], axis=1)
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
mesta_2023_5_clean["Година"] = "2023"
mesta_2023_5_clean = mesta_2023_5_clean.sort_values(by='Код паралелка')
mesta_2023_5_clean.reset_index(drop=True, inplace=True)
mesta_2023_5_clean.index = klasirane_2023_1_clean.index
mesta_2023_5_clean_ordered = pd.concat([klasirane_2023_1_clean, mesta_2023_5_clean], axis=1, copy=False, ignore_index=False)
mesta_2023_5_clean_ordered = mesta_2023_5_clean_ordered.sort_index()
mesta_2023_5_clean_ordered = mesta_2023_5_clean_ordered.loc[:, ~mesta_2023_5_clean_ordered.columns.duplicated()].copy()
mesta_2023_5_clean_ordered = mesta_2023_5_clean_ordered.drop(['Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж'], axis=1)
klasirane_2023_1_clean = klasirane_2023_1_clean.sort_index()
mesta_2023_5_clean_ordered['Класиране'] = 5

# Data preparation
klasirane_2023_combined = pd.concat([klasirane_2023_1_clean, klasirane_2023_2_clean, klasirane_2023_3_clean_plus, klasirane_2023_4_clean_plus, mesta_2023_5_clean_ordered], axis=0)
klasirane_2023_combined.reset_index(drop=True, inplace=True)

code_to_uchilishte_map = dict(klasirane_2023_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
code_to_paral_map = dict(zip(klasirane_2023_combined['Код паралелка'], klasirane_2023_combined['Паралелка']))

yticks_text = [
    f"{code}<br>{'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=40))}"
    for code in klasirane_2023_combined['Код паралелка'].unique()
]

# yticks_text2 = [
#     f"{code}"
#     for code in klasirane_2023_combined['Код паралелка'].unique()
# ]

yticks_text2 = [
    f"{code}<br>{code_to_paral_map[code][:45]}<br>{code_to_uchilishte_map[code][:45]}..."
    for code in klasirane_2023_combined['Код паралелка'].unique()
]

# yticks_text = [
#     f"{code} - {code_to_paral_map[code]:<40}..."  # Adjust the width as needed
#     for code in klasirane_2023_combined['Код паралелка'].unique()
# ]


