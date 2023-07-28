import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import textwrap
import matplotlib.ticker as ticker

pd.options.display.float_format = '{:,.2f}'.format
stats_2023 = pd.read_csv('Statistika_na_uspewaemostta_BEL_MAT.csv')
stats_2022 = pd.read_csv('statistika_mat_bel_2022.csv')

# Stats clean-up
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
                           "Unnamed: 17": "общо_ж"})
stats_2023_clean = stats_2023_clean.drop(['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6',  'Unnamed: 8', 'Unnamed: 10', 'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22'], axis=1)
stats_2023_clean = stats_2023_clean.drop([0, 1, 2], axis=0)
stats_2023_clean = stats_2023_clean.fillna(0)
stats_2023_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2023_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2023_clean.reset_index(drop=True, inplace=True)
stats_2023_clean["ТОЧКИ"] = pd.Series(np.arange(0,201,0.5))
stats_2023_clean["Година"] = "2023"

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
                           "Unnamed: 17": "общо_ж"})
stats_2022_clean = stats_2022_clean.drop(['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6',  'Unnamed: 8', 'Unnamed: 10', 'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23'], axis=1)
stats_2022_clean = stats_2022_clean.drop([0, 1, 2], axis=0)
stats_2022_clean = stats_2022_clean.fillna(0)
stats_2022_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2022_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2022_clean.reset_index(drop=True, inplace=True)
stats_2022_clean["ТОЧКИ"] = pd.Series(np.arange(0,201,0.5))
stats_2022_clean["Година"] = "2022"

df_combined_2 = pd.concat([stats_2023_clean, stats_2022_clean], axis=0)

plt.figure(figsize=(7,4), dpi=200)
# df_combined_2[df_combined_2["Година"] == "2023"]

df_combined_2['Bin'] = pd.cut(df_combined_2.ТОЧКИ, bins=20)
sns.barplot(data=df_combined_2,
                  x=df_combined_2["Bin"].astype(str),
                  y="общо_м",
                  hue="Година",
                  estimator='sum',
                  errorbar=None)
sns.lineplot(data=df_combined_2,
                   x=df_combined_2["Bin"].astype(str),
                   y="общо_ж",
                   hue="Година",
                   linewidth=.5,
                   estimator='sum',
                   errorbar=None)
plt.xticks(rotation=90, fontsize=6)
plt.yticks(fontsize=6)
plt.xlabel('Точки', fontsize=8)
plt.ylabel('Ученици(м)', fontsize=8)
plt.legend(fontsize=6)

avg_br_m_2023 = df_combined_2[df_combined_2["Година"] == "2023"].общо_м.sum()
avg_tochki_m_2023 = sum(df_combined_2[df_combined_2["Година"] == "2023"].общо_м * df_combined_2[df_combined_2["Година"] == "2023"].ТОЧКИ)/avg_br_m_2023
avg_br_m_2022 = df_combined_2[df_combined_2["Година"] == "2022"].общо_м.sum()
avg_tochki_m_2022 = sum(df_combined_2[df_combined_2["Година"] == "2022"].общо_м * df_combined_2[df_combined_2["Година"] == "2022"].ТОЧКИ)/avg_br_m_2022

plt.title(f"2023(м)      ученици: {avg_br_m_2023}     ср.успех: {avg_tochki_m_2023.round(2)}\n2022(м)      ученици: {avg_br_m_2022}     ср.успех: {avg_tochki_m_2022.round(2)}", fontsize=10)
plt.show()