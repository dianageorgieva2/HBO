# INSTRUCTIONS FOR NEW YEAR FILES IMPORT, CLEANING, STANDARTISATION
# 1. In data_statistika add tats_NEWYEAR_clean
# 2. Import data_klasirane_NEWYEAR
# 3. Update visio_1 with NEWYEAR
# 4. Create df_grouped_NEWYEAR and df_grouped_LASTYEAR and add line_LASTYEAR
# 5. Update visio_2 with NEWYEAR

import pandas as pd
import plotly.graph_objects as go
import streamlit
import streamlit as st
import plotly.io as pio
from data_statistika import all_stats
from data_klasirane_2024 import klasirane_2024_combined_function
from data_klasirane_2023 import klasirane_2023_combined_function
from data_klasirane_2022 import klasirane_2022_combined_function
from data_klasirane_2021 import klasirane_2021_combined_function
from data_klasirane_2020 import klasirane_2020_combined_function
from datetime import datetime
from plot_functions import fig3_visualization
from msg_history import get_message_history, create_message
# from authentication import login_function, signup_function
# from personal_nvo_nvigator import personal_nvo_navigator

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format
PREMIUM = True

# Dashboard layout
pio.templates.default = "simple_white"
st.set_page_config(layout="wide", page_title='NVOnavigator', page_icon="favicon.ico")
config = {
    'scrollZoom': False,
    'displayModeBar': False,
    'showAxisDragHandles': False,
}

hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {visibility: hidden;}
        .stActionButton {visibility: hidden;}
        [data-testid="stHeader"] {visibility: hidden;}
        [data-testid="baseButton-secondaryFormSubmit"] {background-color: rgb(253, 211, 139);}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

header = st.container()
intro = st.container()
st.divider()
visio_1 = st.container()
st.divider()
visio_2 = st.container()
st.divider()
# visio_3 = st.container()
# st.divider()
comments = st.container()

with st.sidebar:
    st.markdown("<h1 style='text-left: center;'>Помощна навигация</h1>", unsafe_allow_html=True)
    selected_option = st.radio("Избери опция:", ('Ученици(общо)', 'Ученици(младежи)*', 'Ученици(девойки)*'),
                               key="radio_button")
    if selected_option == 'Ученици(младежи)*':
        y_column = 'общо_м'
        avg_tochki = "tochki_avg_m"
        x_column = 'Мин_бал_м'
        x2_column = "Места_общ_брой_м"
    elif selected_option == 'Ученици(девойки)*':
        y_column = 'общо_д'
        avg_tochki = "tochki_avg_w"
        x_column = 'Мин_бал_ж'
        x2_column = "Места_общ_брой_д"
    else:
        y_column = 'общо'
        avg_tochki = "tochki_avg_o"
        x_column = 'Мин_бал_о'
        x2_column = "Места_общ_брой"

    st.markdown(
        "<p style='text-align: left; font-size: 10px;'>(*Свободните места за младежи и девойки са показани като сбор "
        "на местата с квотa и местата на общо основание.)</p>", unsafe_allow_html=True)
    st.divider()

    mobile_toggle = st.toggle('Адаптирана версия за смарт телефон')
    st.divider()

    # # Authentication functionality embedded in the sidebar
    # mobile_toggle1 = st.toggle('Данни 2024г.')
    # if mobile_toggle1:
    #     tab1, tab2 = st.sidebar.tabs(["Вход", "Регистрация"])
    #     with tab1:
    #         name, authentication_status, username = login_function()
    #         if authentication_status:
    #             PREMIUM = True
    #             st.success(f'Здравей, {name}! Данните са заредени.')
    #         elif authentication_status == False:
    #             st.error('Неправилeн имейл и/или парола.')
    #         elif authentication_status == None:
    #             st.warning('Моля въведи имейл и парола!')
    #     with tab2:
    #         if signup_function() is True:
    #             PREMIUM = True
    #             st.success('Данните са заредени.')
    # st.divider()
    #
    # personal_toggle = st.toggle('Персонален НВО Навигатор')
    # st.divider()

    st.write("Използван сайт на МОН: [ЛИНК](https://ruo-sofia-grad.com/%D0%B8%D0%B7%D0%BF%D0%B8%D1%82%D0%B8-%D0%B8-"
             "%D0%BF%D1%80%D0%B8%D0%B5%D0%BC-%D0%BD%D0%B0-%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%86%D0%B8/%D0%BF%D1%80%"
             "D0%B8%D0%B5%D0%BC-%D0%BD%D0%B0-%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%86%D0%B8/%D0%BF%D1%80%D0%B8%D0%B5%D0%BC-"
             "%D0%B2-viii-%D0%BA%D0%BB%D0%B0%D1%81/)")

with header:
    col_a, col_b = st.columns([2.5, 7.5])
    with col_a:
        col_a_1, col_a_2, col_a_3 = st.columns([0.1, 99.8, 0.1])
        col_a_2.image('images/bg_image_4.png')

    with col_b:
        st.markdown("<h1 style='text-align: center;'>НВО Навигатор</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>(Национално Външно Оценяване)<br><br></h3>",
                    unsafe_allow_html=True)

# Intro definition
with intro:
    st.markdown(
        "<p style='text-align: center;'>Здравей!<br>Тук са събрани данните относно "
        "Националното Външно Оценяване (НВО) за гр.София, публикувани - "
        "резултати от матурите, класиране, свободни места и още. Целта е информацията да се визуализира на "
        "едно място, за да се даде възможност за интерактивен анализ.<br>"
        "Надявам се 'НВО навигатора' да ти е полезен и те каня да оставиш коментар с въпроси или предложения. <br>"
        "УСПЕХ НА ВСИЧКИ 😊</p>", unsafe_allow_html=True)

    # st.markdown(
    #     "<p style='text-align: center; font-size: 24px;'><strong>В МОМЕНТА ДОБАВЯМЕ ДАННИТЕ ЗА 2024!</strong></p>",
    #     unsafe_allow_html=True
    # )

# Create visualization_1 (fig1 and fig2)
with visio_1:
    col1, col2 = st.columns(2, gap='medium')
    df_statistika_combined, all_stats_list = all_stats(premium=PREMIUM)

    # Data visualization fig1
    with col2:
        st.markdown("<h3 style='text-align: center;'>НВО Успеваемост</h3>", unsafe_allow_html=True)
        fig = go.Figure()
        histogram = go.Histogram(
                           x=all_stats_list[0]["Bin"],
                           y=all_stats_list[0][y_column],
                           histfunc='sum',
                           name=str(all_stats_list[0]["Година"].unique()[0]),
                           hovertemplate='%{y} ученици'
                           )
        fig.add_trace(histogram)
        all_stats_list_lines = all_stats_list[1:]
        for item in all_stats_list_lines:
            df_grouped = item.groupby("Bin", as_index=False)[y_column].sum()
            line = go.Scatter(x=df_grouped["Bin"],
                              y=df_grouped[y_column],
                              mode='lines',
                              line=dict(width=2),
                              name=str(item["Година"].unique()[0]),
                              hovertemplate='%{y} ученици')
            fig.add_traces(line)

        fig.update_layout(
            hovermode="x unified",
            hoverlabel=dict(font_size=10),
            paper_bgcolor="rgba(0, 0, 0, 0)",
            plot_bgcolor="rgba(0, 0, 0, 0)",
            xaxis=dict(
                title='Точки',
                titlefont_size=14,
                tickfont_size=12,
                tickangle=-90,
                fixedrange=True),
            yaxis=dict(
                title='Ученици (бр)',
                titlefont_size=14,
                tickfont_size=12,
                fixedrange=True,
                showline=False),
            legend=dict(orientation="h",
                        yanchor="auto",
                        y=1.2,
                        x=1,
                        xanchor="auto",
                        title=None))
        st.plotly_chart(fig, use_container_width=True, config=config)

    # Data visualization fig2
    with col1:
        st.markdown("<h3 style='text-align: center;'>НВО Статистика</h3>", unsafe_allow_html=True)
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
                                   textfont=dict(size=14,
                                                 color="rgb(221, 132, 82)",
                                                 ),
                                   hoverinfo=None)
        fig2.add_trace(bar_trace)
        fig2.add_trace(scatter_trace)
        fig2.update_traces(hoverinfo='none')

        fig2.update_layout(
            paper_bgcolor="rgba(0, 0, 0, 0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(
                title='Година',
                titlefont_size=14,
                tickfont_size=12,
                tickmode='array',
                tickvals=df_statistika_combined.Година,
                ticktext=df_statistika_combined.Година.astype(str),
                fixedrange=True,),
            yaxis=dict(showticklabels=False, fixedrange=True,),
            yaxis2=dict(
                showticklabels=False,
                anchor='free',
                overlaying='y',
                side='right',
                position=1,
                range=(df_statistika_combined[avg_tochki].min() - 10, df_statistika_combined[avg_tochki].max() + 10),
                fixedrange=True,
                showline=False),
            legend=dict(orientation="h",
                        yanchor="auto",
                        y=1.2,
                        x=1,
                        xanchor="auto",
                        title=None))

        st.plotly_chart(fig2, use_container_width=True, config=config)


# Create visualization_2 (fig3)
visio_2.markdown("<h3 style='text-align: center;'>Класиране - детайли</h3>", unsafe_allow_html=True)

with visio_2:
    #Add the new year vaariable after importing the new year function
    klasirane_2024_combined = klasirane_2024_combined_function()
    klasirane_2023_combined = klasirane_2023_combined_function()
    klasirane_2022_combined = klasirane_2022_combined_function()
    klasirane_2021_combined = klasirane_2021_combined_function()
    klasirane_2020_combined = klasirane_2020_combined_function()

    # Add new year on top of the dictionary
    klasirane_all = [klasirane_2024_combined, klasirane_2023_combined, klasirane_2022_combined, klasirane_2021_combined, klasirane_2020_combined]

    #As a new year is added change the attribute of klasirane_all to point to the last one
    # (i.e. in 2025 it will be 4+1=5)
    for df in klasirane_all:
        for uchilishte_code in df['Код училище']:
            if uchilishte_code in klasirane_all[4]['Код училище'].values:
                df.loc[df['Код училище'] == uchilishte_code, 'Училище_short'] = \
                    klasirane_all[4].loc[klasirane_all[4]['Код училище'] == uchilishte_code, 'Училище_формат'].values[0]
            else:
                df.loc[df['Код училище'] == uchilishte_code, 'Училище_short'] = \
                    df.loc[df['Код училище'] == uchilishte_code, 'Училище_формат'].values


    def button_function_mobile(year_label, klasirane_combined_df):
        fig3_visualization(klasirane_combined=klasirane_combined_df,
                           x_column=x_column,
                           x2_column=x2_column,
                           mobile=True,
                           year=year_label)


    def button_function(year_label, klasirane_combined_df):
        fig3_visualization(klasirane_combined=klasirane_combined_df,
                           x_column=x_column,
                           x2_column=x2_column,
                           mobile=False,
                           year=year_label)

    radio_button = visio_2.radio(label=' ', options=['2024', '2023', '2022', '2021', '2020'], horizontal=True)
    # Add the new year to the radio button options and extend the functionality below when selected
    if radio_button == '2024':
        # if not PREMIUM:
        #     st.write('Регисттрирай се за данните от 2024г.')
        # else:
        #     st.write('В очакване на 1во класиране')

        if mobile_toggle:
            button_function_mobile(year_label=2024, klasirane_combined_df=klasirane_2024_combined)
        else:
            button_function(year_label=2024, klasirane_combined_df=klasirane_2024_combined)

    if radio_button == '2023':
        if mobile_toggle:
            button_function_mobile(year_label=2023, klasirane_combined_df=klasirane_2023_combined)
        else:
            button_function(year_label=2023, klasirane_combined_df=klasirane_2023_combined)

    if radio_button == '2022':
        if mobile_toggle:
            button_function_mobile(year_label=2022, klasirane_combined_df=klasirane_2022_combined)
        else:
            button_function(year_label=2022, klasirane_combined_df=klasirane_2022_combined)

    if radio_button == '2021':
        if mobile_toggle:
            button_function_mobile(year_label=2021, klasirane_combined_df=klasirane_2021_combined)
        else:
            button_function(year_label=2021, klasirane_combined_df=klasirane_2021_combined)

    if radio_button == '2020':
        if mobile_toggle:
            button_function_mobile(year_label=2020, klasirane_combined_df=klasirane_2020_combined)
        else:
            button_function(year_label=2020, klasirane_combined_df=klasirane_2020_combined)

    st.write(
        """
        <div style="font-size: 10px; font-style: italic;">
            Забележка: Балообразуването се формира, както следва: (общо 4 пъти точките от НВО) + 
            (2 оценки от 7. клас от свидетелството за завършено основно образование, превърнати в точки). 
            Изключение са паралелките, за които се балообразува освен с НВО и с резултати от изпити за проверка
             на способностите и/или областни кръгове на олимпиади и национални състезания.
        </div>
        """,
        unsafe_allow_html=True
    )

# with visio_3:
#     if personal_toggle:
#         st.markdown("<h3 style='text-align: center;'>ПЕРСОНАЛЕН НВО НАВИГАТОР</h3>", unsafe_allow_html=True)
#         personal_nvo_navigator(klasirane_combined_df=klasirane_2023_combined)
#
#     klasirane_2023_combined['Мин_бал_о'] = klasirane_2023_combined['Мин_бал_о'].fillna(0)
#     aggregated_df = klasirane_2023_combined.groupby('Код паралелка').agg({
#         'Паралелка': 'first',
#         'Училище_short': 'first',
#         'Мин_бал_о': lambda x: list(map(float, x)),
#     })
#     # print(klasirane_2023_combined[klasirane_2023_combined["Класиране"] == 1].shape)
#     # print(type(aggregated_df['Мин_бал_о'].iloc[0][0]))  # This should show 'int'

# Message functionality and history features
st.markdown("<h3 style='text-align: center;'>Коментари</h3>", unsafe_allow_html=True)

msg_history = get_message_history()
df_messages = pd.DataFrame(list(reversed(msg_history)))

comments_html = ""
for _, message in df_messages.iterrows():
    comments_html += f"<b><u>{message['name']} ({message['time']}</u></b>)<br>{message['text']}<br><br>"

html_snippet = f"""
    <div style="max-height: 300px; overflow-y: scroll; border: 1px solid #dddddd; border-radius: 10px; padding: 10px;">
        {comments_html}
    </div>
"""
st.markdown(html_snippet, unsafe_allow_html=True)

# Create message form feature
with st.form(key='form1', clear_on_submit=True):
    user_name = st.text_input("Име")
    user_message = st.text_area("Съобщение")
    submit_button = st.form_submit_button("Изпрати")
    if submit_button:
        if user_name and user_message:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            new_message = {
                "name": user_name,
                "text": user_message,
                "time": timestamp
            }
            create_message(msg=new_message)
            comments.info(f"{new_message['name']} ({new_message['time']})\n"
                          f"{new_message['text']}")
