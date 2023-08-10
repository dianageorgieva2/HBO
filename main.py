import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format


#----------STATISTIKA----------
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
                           "Unnamed: 9": "общо_ж"})
stats_2021_clean = stats_2021_clean.drop([0], axis=0)
stats_2021_clean = stats_2021_clean.fillna(0)
stats_2021_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2021_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2021_clean.reset_index(drop=True, inplace=True)
stats_2021_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 1))
stats_2021_clean["Година"] = "2021"
stats_2021_clean['Bin'] = pd.cut(stats_2021_clean.ТОЧКИ, bins=20, include_lowest=True)
stats_2021_clean['Bin'] = stats_2021_clean['Bin'].apply(lambda x: f"{x.left:.1f} - {x.right:.1f}")

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
                           "Unnamed: 9": "общо_ж"})
stats_2020_clean = stats_2020_clean.drop([0], axis=0)
stats_2020_clean = stats_2020_clean.fillna(0)
stats_2020_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']] = stats_2020_clean[['общо', 'общо_м', 'общо_ж', 'МАТ', 'МАТ_м', 'МАТ_ж', 'БЕЛ', 'БЕЛ_м', 'БЕЛ_ж']].astype(int)
stats_2020_clean.reset_index(drop=True, inplace=True)
stats_2020_clean["ТОЧКИ"] = pd.Series(np.arange(0, 201, 1))
stats_2020_clean["Година"] = "2020"
stats_2020_clean['Bin'] = pd.cut(stats_2020_clean.ТОЧКИ, bins=20, include_lowest=True)
stats_2020_clean['Bin'] = stats_2020_clean['Bin'].apply(lambda x: f"{x.left:.1f} - {x.right:.1f}")

# Layout
st.set_page_config(layout="wide")
st.title("HBO DASHBOARD")
col1, col2 = st.columns(2, gap='medium')

with col2:
    selected_column = st.radio("Изберете опция:", ('Ученици(общо)', 'Ученици(мъже)', 'Ученици(жени)'), key="col1_radio", horizontal=True)
    if selected_column == 'Ученици(мъже)':
        y_column = 'общо_м'
    elif selected_column == 'Ученици(жени)':
        y_column = 'общо_ж'
    else:
        y_column = 'общо'

    # Data visualization fig1
    fig = px.histogram(stats_2023_clean,
                       x="Bin",
                       y=y_column,
                       color="Година",
                       histfunc='sum')
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

    df_grouped_2022 = stats_2022_clean.query("Година == '2022'").groupby("Bin", as_index=False)[y_column].sum()
    fig.add_trace(go.Scatter(x=df_grouped_2022["Bin"],
                             y=df_grouped_2022[y_column],
                             mode='lines',
                             line=dict(width=2),
                             name='2022'))
    df_grouped_2021 = stats_2021_clean.query("Година == '2021'").groupby("Bin", as_index=False)[y_column].sum()
    fig.add_trace(go.Scatter(x=df_grouped_2022["Bin"],
                             y=df_grouped_2021[y_column],
                             mode='lines',
                             line=dict(width=2),
                             name='2021'))
    df_grouped_2020 = stats_2020_clean.query("Година == '2020'").groupby("Bin", as_index=False)[y_column].sum()
    fig.add_trace(go.Scatter(x=df_grouped_2022["Bin"],
                             y=df_grouped_2020[y_column],
                             mode='lines',
                             line=dict(width=2),
                             marker=dict(size=6),
                             name='2020'))

    fig.update_layout(
        title='НВО Успеваемост',
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

with col1:

    # Data preparation
    df_statistika_combined = pd.concat([stats_2023_clean, stats_2022_clean, stats_2021_clean, stats_2020_clean], axis=0)
    df_statistika_combined["tochki_sum_o"] = df_statistika_combined.общо * df_statistika_combined.ТОЧКИ
    df_statistika_combined["tochki_sum_m"] = df_statistika_combined.общо_м * df_statistika_combined.ТОЧКИ
    df_statistika_combined["tochki_sum_w"] = df_statistika_combined.общо_ж * df_statistika_combined.ТОЧКИ
    df_statistika_combined = df_statistika_combined.groupby("Година")[["общо_м", "общо_ж", "общо", "tochki_sum_m", "tochki_sum_w", "tochki_sum_o"]].agg("sum")
    df_statistika_combined["tochki_avg_m"] = (df_statistika_combined.tochki_sum_m / df_statistika_combined.общо_м).round(2)
    df_statistika_combined["tochki_avg_w"] = (df_statistika_combined.tochki_sum_w / df_statistika_combined.общо_ж).round(2)
    df_statistika_combined["tochki_avg_o"] = (df_statistika_combined.tochki_sum_o / df_statistika_combined.общо).round(2)
    df_statistika_combined.reset_index(inplace=True)

    selected_option = st.radio("Изберете опция:", ('Ученици(общо)', 'Ученици(мъже)', 'Ученици(жени)'), key="col2_radio", horizontal=True)
    if selected_option == 'Ученици(мъже)':
        y_column = 'общо_м'
        avg_tochki = "tochki_avg_m"
    elif selected_option == 'Ученици(жени)':
        y_column = 'общо_ж'
        avg_tochki = "tochki_avg_w"
    else:
        y_column = 'общо'
        avg_tochki = "tochki_avg_o"

    # Data visualization fig2
    fig2 = go.Figure()
    bar_trace = go.Bar(x=df_statistika_combined["Година"],
                       y=df_statistika_combined[y_column],
                       text=df_statistika_combined[y_column],
                       name="Ученици(брой)",
                       textposition="outside",
                       cliponaxis=False,
                       textfont=dict(size=12))
    scatter_trace = go.Scatter(x=df_statistika_combined["Година"],
                               y=df_statistika_combined[avg_tochki],
                               name="Среден успех(точки)",
                               mode='lines+text+markers',
                               yaxis='y2',
                               text=df_statistika_combined[avg_tochki],
                               textposition="top center",
                               cliponaxis=False,
                               textfont=dict(
                                   size=12,
                                   color="rgb(131, 201, 255)"))
    fig2.add_trace(bar_trace)
    fig2.add_trace(scatter_trace)

    fig2.update_layout(
        title='НВО Статистика',
        xaxis=dict(
            title='Година',
            titlefont_size=14,
            tickfont_size=12,
            tickmode='array',
            tickvals=df_statistika_combined.Година,
            ticktext=df_statistika_combined.Година.astype(str)),
        yaxis=dict(tickfont_size=12,),
        yaxis2=dict(
            tickfont_size=12,
            anchor='free',
            overlaying='y',
            side='right',
            position=1,
            range=(df_statistika_combined[avg_tochki].min() - 10, df_statistika_combined[avg_tochki].max() + 10)))

    st.plotly_chart(fig2, use_container_width=True)

#----------KLASIRANE----------
#layout
c = st.container()

# Data import
mesta_2023_3 = pd.read_csv('klasirane/2023/svobodni_mesta_za_3_etap_2023-3 (1).csv')
mesta_2023_4 = pd.read_csv('klasirane/2023/svobodni_mesta_za_4_etap_2023.csv')
klasirane_2023_1 = pd.read_csv('klasirane/2023/min_maх_paralelki_1.etap_2023 (3).csv')
klasirane_2023_2 = pd.read_csv('klasirane/2023/min_max_2_etap_2023 (1).csv')
klasirane_2023_3 = pd.read_csv('klasirane/2023/min_max_po_paralelki_3_etap_2023 (1).csv')
klasirane_2023_4 = pd.read_csv('klasirane/2023/min_max_po_par_4_etap_2023 (1).csv')


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
klasirane_2023_1_clean["Година"] = "2023"
klasirane_2023_1_clean = klasirane_2023_1_clean.sort_values(by='Мин_бал_о', ascending=False)
klasirane_2023_1_clean.reset_index(drop=True, inplace=True)

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
klasirane_2023_2_clean["Година"] = "2023"
klasirane_2023_2_clean = klasirane_2023_2_clean.sort_values(by='Мин_бал_о', ascending=False)
klasirane_2023_2_clean.reset_index(drop=True, inplace=True)

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
klasirane_2023_3_clean["Година"] = "2023"
klasirane_2023_3_clean = klasirane_2023_3_clean.sort_values(by='Мин_бал_о', ascending=False)
klasirane_2023_3_clean.reset_index(drop=True, inplace=True)

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
klasirane_2023_4_clean["Година"] = "2023"
klasirane_2023_4_clean = klasirane_2023_4_clean.sort_values(by='Мин_бал_о', ascending=False)
klasirane_2023_4_clean.reset_index(drop=True, inplace=True)


klasirane_2023_combined = pd.concat([klasirane_2023_1_clean, klasirane_2023_2_clean, klasirane_2023_3_clean, klasirane_2023_4_clean], axis=0)
klasirane_2023_combined.reset_index(drop=True, inplace=True)
klasirane_2023_combined.sort_values(by='Класиране', ascending=False)

code_to_uchilishte_map = dict(klasirane_2023_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
code_to_paral_map = dict(zip(klasirane_2023_combined['Код паралелка'], klasirane_2023_combined['Паралелка']))
yticks_text = [f"{code} - {code_to_paral_map[code]}" for code in klasirane_2023_combined['Код паралелка'].unique()]
hover_text = [f"{code_to_uchilishte_map[code]}" for code in klasirane_2023_combined['Код паралелка'].unique()]

# Create fig3
with c:
    selected_option = st.radio("Изберете опция:", ('Ученици(общо)', 'Ученици(мъже)', 'Ученици(жени)'), key="fig3_radio",
                               horizontal=True)
    if selected_option == 'Ученици(мъже)':
        x_column = 'Мин_бал_м'
        max_bal = "Макс_бал_м"
    elif selected_option == 'Ученици(жени)':
        x_column = 'Мин_бал_ж'
        max_bal = "Макс_бал_ж"
    else:
        x_column = 'Мин_бал_о'
        max_bal = "Макс_бал_о"

    fig3 = go.Figure()
    for k in klasirane_2023_combined['Класиране'].unique():
        df_к = klasirane_2023_combined[klasirane_2023_combined['Класиране'] == k]
        # noinspection PyTypeChecker
        fig3.add_traces(go.Bar(x=df_к[x_column],
                               y=df_к['Код паралелка'],
                               name=f'{k} класиране',
                               text=df_к[x_column],
                               textposition="outside",
                               cliponaxis=False,
                               textfont=dict(size=14),
                               hoverinfo='text',
                               hovertext=hover_text,
                               orientation="h"))

    fig3.update_layout(
        title='Класиране - детайли',
        height=15000,
        xaxis=dict(
            title='Минимален бал',
            titlefont_size=14,
            tickfont_size=12),
        yaxis=dict(tickfont_size=12,
                   autorange="reversed",
                   type='category',
                   tickmode='array',
                   ticktext=yticks_text,
                   tickvals=klasirane_2023_combined['Код паралелка']),
        hoverlabel=dict(
            bgcolor="pink",
            font_size=14,
            align='left'))

    st.plotly_chart(fig3, use_container_width=True)
