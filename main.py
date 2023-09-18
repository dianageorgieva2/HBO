import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import io
import streamlit.components.v1 as components
import plotly.io as pio
import plotly.subplots as sp
from data_clean import stats_2020_clean, stats_2021_clean, stats_2022_clean, stats_2023_clean, df_statistika_combined, \
    klasirane_2023_combined, yticks_text2

pio.templates.default = "plotly"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format

# Dashboard layout
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Национално Външно Оценяване (НВО)<br><br></h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2, gap='medium')
c = st.container()

# Data visualization fig1
with col2:
    st.markdown("<h3 style='text-align: center;'>НВО Успеваемост</h3>", unsafe_allow_html=True)

    selected_column = st.radio("Избери опция:", ('Ученици(общо)', 'Ученици(младежи)', 'Ученици(девойки)'), key="col1_radio", horizontal=True)
    if selected_column == 'Ученици(младежи)':
        y_column = 'общо_м'
    elif selected_column == 'Ученици(девойки)':
        y_column = 'общо_д'
    else:
        y_column = 'общо'

    fig = go.Figure()
    histogram = go.Histogram(
                       x=stats_2023_clean["Bin"],
                       y=stats_2023_clean[y_column],
                       # color=stats_2023_clean["Година"],
                       histfunc='sum',
                       name=2023,
                       )
    fig.add_trace(histogram)

    df_grouped_2022 = stats_2022_clean.query("Година == '2022'").groupby("Bin", as_index=False)[y_column].sum()
    line_2022 = go.Scatter(x=df_grouped_2022["Bin"],
                             y=df_grouped_2022[y_column],
                             mode='lines',
                             line=dict(width=2),
                             # hoverinfo='name',
                             name='2022')
    df_grouped_2021 = stats_2021_clean.query("Година == '2021'").groupby("Bin", as_index=False)[y_column].sum()
    line_2021 = go.Scatter(x=df_grouped_2022["Bin"],
                             y=df_grouped_2021[y_column],
                             mode='lines',
                             line=dict(width=2),
                             name='2021')
    df_grouped_2020 = stats_2020_clean.query("Година == '2020'").groupby("Bin", as_index=False)[y_column].sum()
    line_2020 = go.Scatter(x=df_grouped_2022["Bin"],
                             y=df_grouped_2020[y_column],
                             mode='lines',
                             line=dict(width=2),
                             marker=dict(size=6),
                             name='2020')
    fig.add_traces([line_2022, line_2021, line_2020])

    fig.update_layout(
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_size=10,
        ),
        xaxis=dict(
            title='Точки',
            titlefont_size=14,
            tickfont_size=12,
            tickangle=-90),
        yaxis=dict(
            title='Ученици (бр)',
            titlefont_size=14,
            tickfont_size=12),
        legend=dict(orientation="h",
                    yanchor="auto",
                    y=1.2,
                    x=1,
                    xanchor="auto",
                    title=None))
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# Data visualization fig2
with col1:
    st.markdown("<h3 style='text-align: center;'>НВО статистика</h3>", unsafe_allow_html=True)

    selected_option = st.radio("Избери опция:", ('Ученици(общо)', 'Ученици(младежи)', 'Ученици(девойки)'), key="col2_radio", horizontal=True)
    if selected_option == 'Ученици(младежи)':
        y_column = 'общо_м'
        avg_tochki = "tochki_avg_m"
    elif selected_option == 'Ученици(девойки)':
        y_column = 'общо_д'
        avg_tochki = "tochki_avg_w"
    else:
        y_column = 'общо'
        avg_tochki = "tochki_avg_o"

    fig2 = go.Figure()
    bar_trace = go.Bar(x=df_statistika_combined["Година"],
                       y=df_statistika_combined[y_column],
                       text=df_statistika_combined[y_column],
                       name="Ученици(брой)",
                       textposition="outside",
                       cliponaxis=False,
                       textfont=dict(size=12),
                       hoverinfo=None)
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
                                   color="rgb(239, 85, 59)",
                               ),
                               hoverinfo=None)
    fig2.add_trace(bar_trace)
    fig2.add_trace(scatter_trace)
    fig2.update_traces(hoverinfo='none')

    fig2.update_layout(
        xaxis=dict(
            title='Година',
            titlefont_size=14,
            tickfont_size=12,
            tickmode='array',
            tickvals=df_statistika_combined.Година,
            ticktext=df_statistika_combined.Година.astype(str)),
        yaxis=dict(showticklabels=False),
        yaxis2=dict(
            showticklabels=False,
            anchor='free',
            overlaying='y',
            side='right',
            position=1,
            range=(df_statistika_combined[avg_tochki].min() - 10, df_statistika_combined[avg_tochki].max() + 10)),
        legend=dict(orientation="h",
                      yanchor="auto",
                      y=1.2,
                      x=1,
                      xanchor="auto",
                      title=None))

    st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})

#----------KLASIRANE----------
# Create fig3
with c:
    st.markdown("<h3 style='text-align: center;'>Класиране 2023 - детайли</h3>", unsafe_allow_html=True)

    selected_option = st.radio("Избери опция:", ('Ученици(общо)', 'Ученици(младежи)', 'Ученици(девойки)'), key="fig3_radio",
                               horizontal=True)
    if selected_option == 'Ученици(младежи)':
        x_column = 'Мин_бал_м'
        x2_column = "Места_м"
    elif selected_option == 'Ученици(девойки)':
        x_column = 'Мин_бал_ж'
        x2_column = "Места_д"
    else:
        x_column = 'Мин_бал_о'
        x2_column = "Места_общ_брой"

    fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, vertical_spacing=0.05, column_widths=[0.85, 0.10])
    code_to_uchilishte_map = dict(klasirane_2023_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
    code_to_paral_map = dict(zip(klasirane_2023_combined['Код паралелка'], klasirane_2023_combined['Паралелка']))

    for k in klasirane_2023_combined[klasirane_2023_combined['Класиране'] != 5]['Класиране'].unique():
        df_k = klasirane_2023_combined[klasirane_2023_combined['Класиране'] == k]
        hover_text = [f"{code} {code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
            for code in df_k['Код паралелка'].unique()]
        bars = go.Bar(x=df_k[x_column],
                               y=df_k['Код паралелка'],
                               name=f'{k} класиране',
                               text=df_k[x_column],
                               textposition="outside",
                               cliponaxis=False,
                               textfont=dict(size=12),
                                hoverinfo='none',
                               hovertext=hover_text,
                               hovertemplate='%{hovertext}<br>Мин. бал: %{x}',
                               orientation="h")
        fig3.add_trace(bars, row=1, col=1)

    placeholder = 550
    for k in klasirane_2023_combined[klasirane_2023_combined['Класиране'] >= 3]['Класиране'].unique():
        df_k = klasirane_2023_combined[klasirane_2023_combined['Класиране'] == k]
        mesta = go.Scatter(x=np.full(df_k.shape[0], f'    за {k}кл.'),
                           y=df_k['Код паралелка'],
                           text=df_k[x2_column],
                           mode='text',
                           textfont=dict(size=10),
                           showlegend=False,
                           hoverinfo='none',
                           )
        placeholder += 30
        fig3.add_trace(mesta, row=1, col=2)

    # custom_width = 1200
    # yticks_text_long = [f"{code}<br>{code_to_paral_map[code][:45]}<br>{code_to_uchilishte_map[code][:45]}..."
    #     for code in klasirane_2023_combined['Код паралелка'].unique()]
    # yticks_text_short = klasirane_2023_combined['Код паралелка'].unique()
    #
    # if custom_width <= 70:
    #     yticks_text = yticks_text_short
    # else:
    #     yticks_text = yticks_text_long

    fig3.update_layout(
        # autosize=True,
        # minreducedwidth=100,
        # paper_bgcolor='yellowgreen',
        height=len(klasirane_2023_combined) * 12,
        plot_bgcolor='white',
        dragmode=False,
        # hovermode='y unified',
        margin=dict(l=5, r=5),
        legend=dict(orientation="v",
                    yanchor="bottom",
                    y=1.0001,
                    xanchor='left',
                    x=0),
        xaxis=dict(title='Минимален бал',
                   titlefont_size=12,
                   # automargin=True,
                   side="top",
                   showticklabels=False,
                   showgrid=False,
                   domain=[0, 0.85],
                   ),
        xaxis2=dict(title='Свободни места',
                   titlefont_size=12,
                   automargin=True,
                   side="top",
                   showticklabels=True,
                   showgrid=False,
                    type='category',
                    tickangle=-90,
                    domain=[0.9, 1],
                    ),
        yaxis=dict(showticklabels=True,
                    automargin=True,
                    type='category',
                    showgrid=False,
                    tickmode='array',
                    side='left',
                    ticktext=yticks_text2,
                    range=[len(klasirane_2023_combined['Код паралелка'].unique()) - .5, -.5],
                    tickvals=klasirane_2023_combined['Код паралелка'].unique(),
                    position=0,
                   ),
        yaxis2=dict(showticklabels=False,
                   automargin=True,
                   type='category',
                   showgrid=False,
                   tickmode='array',
                   side='right',
                   ticktext=yticks_text2,
                   range=[len(klasirane_2023_combined['Код паралелка'].unique()) - .5, -.5],
                   tickvals=klasirane_2023_combined['Код паралелка'].unique(),
                   position=0,
                   )
    )

    config = {
        'scrollZoom': False,
        'displayModeBar': False,
        'responsive': True,
        'showTips': True,
    }

    buffer = io.StringIO()
    fig3.write_html(buffer, full_html=True, include_plotlyjs=True, config=config)
    components.html(buffer.getvalue(), width=None, height=600, scrolling=True)

