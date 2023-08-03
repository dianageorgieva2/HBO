import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.title("HBO DASHBOARD")

# Stats data load
pd.options.display.float_format = '{:,.2f}'.format
stats_2023 = pd.read_csv('Statistika_na_uspewaemostta_BEL_MAT.csv')
stats_2022 = pd.read_csv('statistika_mat_bel_2022.csv')

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
                           "Unnamed: 17": "общо_ж"})
stats_2023_clean = stats_2023_clean.drop(['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6',  'Unnamed: 8', 'Unnamed: 10', 'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22'], axis=1)
stats_2023_clean = stats_2023_clean.drop([0, 1, 2], axis=0)
stats_2023_clean = stats_2023_clean.fillna(0)
stats_2023_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2023_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2023_clean.reset_index(drop=True, inplace=True)
stats_2023_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 0.5))
stats_2023_clean["Година"] = "2023"
stats_2023_clean['Bin'] = pd.cut(stats_2023_clean.ТОЧКИ, bins=20, include_lowest=True)
stats_2023_clean['Bin'] = stats_2023_clean['Bin'].apply(lambda x: f"{x.left:.1f} - {x.right:.1f}")

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
stats_2022_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 0.5))
stats_2022_clean["Година"] = "2022"
stats_2022_clean['Bin'] = pd.cut(stats_2022_clean.ТОЧКИ, bins=20, include_lowest=True)
stats_2022_clean['Bin'] = stats_2022_clean['Bin'].apply(lambda x: f"{x.left:.1f} - {x.right:.1f}")

# df_combined_2 = pd.concat([stats_2023_clean, stats_2022_clean], axis=0)
# avg_br_m_2023 = df_combined_2[df_combined_2["Година"] == "2023"].общо_м.sum()
# avg_tochki_m_2023 = sum(df_combined_2[df_combined_2["Година"] == "2023"].общо_м * df_combined_2[df_combined_2["Година"] == "2023"].ТОЧКИ)/avg_br_m_2023
# avg_br_m_2022 = df_combined_2[df_combined_2["Година"] == "2022"].общо_м.sum()
# avg_tochki_m_2022 = sum(df_combined_2[df_combined_2["Година"] == "2022"].общо_м * df_combined_2[df_combined_2["Година"] == "2022"].ТОЧКИ)/avg_br_m_2022

# Layout
selected_column = st.radio("Select a column to display:", ('общо_м', 'общо_ж', 'общо'))
if selected_column == 'общо_м':
    y_column = 'общо_м'
elif selected_column == 'общо_ж':
    y_column = 'общо_ж'
else:
    y_column = 'общо'


# Data Visualization
fig = px.histogram(stats_2023_clean,
                   x="Bin",
                   y=y_column,
                   color="Година",
                   histfunc='sum',
                   text_auto='.2s')
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

df_grouped_2022 = stats_2022_clean.query("Година == '2022'").groupby("Bin", as_index=False)[y_column].sum()
fig.add_trace(go.Scatter(x=df_grouped_2022["Bin"],
                         y=df_grouped_2022[y_column],
                         mode='lines',
                         line=dict(width=1),
                         name='2022'))

fig.update_layout(
    title='НВО Статистика на резултатите',
    xaxis=dict(
        title='Точки',
        titlefont_size=14,
        tickfont_size=12,
        tickangle=-90),
    yaxis=dict(
        title='Ученици (бр)',
        titlefont_size=14,
        tickfont_size=12))

st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig)
