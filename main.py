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
import textwrap
from datetime import datetime

pio.templates.default = "plotly"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format

# Dashboard layout
st.set_page_config(layout="wide", page_title='НВО', page_icon="favicon.ico")
st.markdown("<h1 style='text-align: center;'>Национално Външно Оценяване (НВО)<br><br></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Здравейте, aз съм Диана.<br>Преминавайки изпитанието на матурите(НВО) след 7ми клас с моя син, "
            "събрахме всички важни данни публикувани от МОН по темата. За мен беше много полезно да видя цялата "
            "информация систематизирана и визуалиирана на едно място, за да вземем в процеса на кандидастване възможно"
            " най-информирано и базирано на данни решение. <br>"
            "Радвам се да споделим тези данни и се надявам те да помогнат и на други. Тук ще намерите НВО резултатите - 2023 година, средния успех и броя на учениците, успеваемост, най-предпочитани "
            "и паралелки с минимален или никакъв интерес, свободни места за различните класирания, трендове и повече. "
            "Пишете ми в коментарите ако искате да добавим още нещо или имате въпроси.<br>"
            "УСПЕХ НА ВСИЧКИ!</p>", unsafe_allow_html=True)
st.write("Използван сайт на МОН: [ЛИНК](https://ruo-sofia-grad.com/%D0%B8%D0%B7%D0%BF%D0%B8%D1%82%D0%B8-%D0%B8-%D0%BF%D1%80%D0%B8%D0%B5%D0%BC-%D0%BD%D0%B0-%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%86%D0%B8/%D0%BF%D1%80%D0%B8%D0%B5%D0%BC-%D0%BD%D0%B0-%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%86%D0%B8/%D0%BF%D1%80%D0%B8%D0%B5%D0%BC-%D0%B2-viii-%D0%BA%D0%BB%D0%B0%D1%81/)")


col1, col2 = st.columns(2, gap='medium')

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
    # bar_trace.update(textfont_color=bar_trace.marker.color)

    scatter_trace = go.Scatter(x=df_statistika_combined["Година"],
                               y=df_statistika_combined[avg_tochki],
                               name="Среден успех(точки)",
                               mode='lines+text+markers',
                               yaxis='y2',
                               text=df_statistika_combined[avg_tochki],
                               textposition="top center",
                               cliponaxis=False,
                               textfont=dict(
                                   size=14,
                                   color="rgb(239, 85, 59)",
                               ),
                               hoverinfo=None)
    # scatter_trace.update(textfont_color=scatter_trace.marker.color)
    # fig2.update_traces(textfont_color=dict(type='markers'))
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

st.divider()

#----------KLASIRANE----------
# Create fig3
c = st.container()
with c:
    st.markdown("<h3 style='text-align: center;'>Класиране 2023 - детайли</h3>", unsafe_allow_html=True)
    multiselect = st.multiselect("Ако искаш да филтрираш по определени училища, избери от списъка:", options=klasirane_2023_combined['Училище'].drop_duplicates().sort_values(), placeholder="Избери училище/а")
    df_multiselect = klasirane_2023_combined[klasirane_2023_combined["Училище"].isin(multiselect)]

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

    if df_multiselect.empty:
        fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, vertical_spacing=0.20, column_widths=[0.65, 0.15])
        code_to_uchilishte_map = dict(klasirane_2023_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
        code_to_paral_map = dict(zip(klasirane_2023_combined['Код паралелка'], klasirane_2023_combined['Паралелка']))

        for k in klasirane_2023_combined[klasirane_2023_combined['Класиране'] != 5]['Класиране'].unique():
            df_k = klasirane_2023_combined[klasirane_2023_combined['Класиране'] == k]
            # hover_text = [f"{code} {code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
            #     for code in df_k['Код паралелка'].unique()]
            hover_text = [f"{code} {'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=45))}<br>{'<br>'.join(textwrap.wrap(code_to_uchilishte_map[code], width=45))}"
                for code in df_k['Код паралелка'].unique()]

            bars = go.Bar(x=df_k[x_column],
                                   y=df_k['Код паралелка'],
                                   name=f'{k} класиране',
                                   text=df_k[x_column],
                                   textposition="outside",
                                   cliponaxis=False,
                                   textfont=dict(size=12),
                                    hoverlabel=dict(namelength=-1),
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

        fig3.update_layout(
            hoverlabel_align='left',
            height=len(klasirane_2023_combined) * 12,
            plot_bgcolor='white',
            dragmode=False,
            margin=dict(l=5, r=5),
            legend=dict(orientation="v",
                        yanchor="bottom",
                        y=1.0001,
                        xanchor='left',
                        x=0),
            xaxis=dict(title='Минимален бал',
                       titlefont_size=12,
                       side="top",
                       showticklabels=False,
                       showgrid=False,
                       domain=[0, 0.65],
                       ),
            xaxis2=dict(title='Свободни места',
                       titlefont_size=12,
                       side="top",
                       showticklabels=True,
                       showgrid=False,
                        type='category',
                        tickangle=-90,
                        domain=[0.85, 1],
                        ),
            yaxis=dict(showticklabels=True,
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
    else:
        fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, vertical_spacing=0.20, column_widths=[0.65, 0.15])
        code_to_uchilishte_map = dict(df_multiselect[['Код паралелка', 'Училище']].drop_duplicates().values)
        code_to_paral_map = dict(zip(df_multiselect['Код паралелка'], df_multiselect['Паралелка']))

        for k in df_multiselect[df_multiselect['Класиране'] != 5]['Класиране'].unique():
            df_k = df_multiselect[df_multiselect['Класиране'] == k]
            hover_text = [
                f"{code} {'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=45))}<br>{'<br>'.join(textwrap.wrap(code_to_uchilishte_map[code], width=45))}"
                for code in df_k['Код паралелка'].unique()]

            bars = go.Bar(x=df_k[x_column],
                          y=df_k['Код паралелка'],
                          name=f'{k} класиране',
                          text=df_k[x_column],
                          textposition="outside",
                          cliponaxis=False,
                          textfont=dict(size=12),
                          hoverlabel=dict(namelength=-1),
                          hovertext=hover_text,
                          hovertemplate='%{hovertext}<br>Мин. бал: %{x}',
                          orientation="h")
            fig3.add_trace(bars, row=1, col=1)

        placeholder = 550
        for k in df_multiselect[df_multiselect['Класиране'] >= 3]['Класиране'].unique():
            df_k = df_multiselect[df_multiselect['Класиране'] == k]
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
        yticks_text2_multiselect = [
            f"{code}-{'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=25))}"
            for code in df_multiselect['Код паралелка'].unique()
        ]
        fig3.update_layout(
            hoverlabel_align='left',
            height=len(df_multiselect) * 12 + 180,
            # plot_bgcolor='F6F4EB',
            # paper_bgcolor='F6F4EB',
            dragmode=False,
            margin=dict(l=5, r=5),
            legend=dict(orientation="v",
                        yanchor="bottom",
                        y=1.0001,
                        xanchor='left',
                        x=0),
            xaxis=dict(title='Минимален бал',
                       titlefont_size=12,
                       side="top",
                       showticklabels=False,
                       showgrid=False,
                       domain=[0, 0.65],
                       ),
            xaxis2=dict(title='Свободни места',
                        titlefont_size=12,
                        side="top",
                        showticklabels=True,
                        showgrid=False,
                        type='category',
                        tickangle=-90,
                        domain=[0.85, 1],
                        ),
            yaxis=dict(showticklabels=True,
                       type='category',
                       showgrid=False,
                       tickmode='array',
                       side='left',
                       ticktext=yticks_text2_multiselect,
                       range=[len(df_multiselect['Код паралелка'].unique()) - .5, -.5],
                       tickvals=df_multiselect['Код паралелка'].unique(),
                       position=0,
                       ),
            yaxis2=dict(showticklabels=False,
                        type='category',
                        showgrid=False,
                        tickmode='array',
                        side='right',
                        ticktext=yticks_text2_multiselect,
                        range=[len(df_multiselect['Код паралелка'].unique()) - .5, -.5],
                        tickvals=df_multiselect['Код паралелка'].unique(),
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


# Message functionality and history
def load_msg_history():
    try:
        msg_history = pd.read_csv("msg_history.csv")
    except FileNotFoundError:
        msg_history = pd.DataFrame(columns=["name", "text", "time"])
    return msg_history


def save_msg_history(msg_history):
    msg_history.to_csv("msg_history.csv", index=False)


msg_history = load_msg_history()

st.divider()
c2 = st.container()
c2.markdown("<h3 style='text-align: center;'>Коментари</h3>", unsafe_allow_html=True)

with st.form(key='form1', clear_on_submit=True):
    user_name = st.text_input("Име")
    user_message = st.text_area("Съобщение")
    submit_button = st.form_submit_button("Изпрати")
    if submit_button:
        if user_name and user_message:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            message = {
                "name": user_name,
                "text": user_message,
                "time": timestamp
            }
            msg_history = pd.concat([msg_history, pd.DataFrame([message])])
            save_msg_history(msg_history)

for _, message in msg_history.iterrows():
    messages = c2.info(f"{message['name']} ({message['time']}) \n{message['text']}")

# html(messages, width=None, height=100, scrolling=True)
