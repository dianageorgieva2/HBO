import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.io as pio
from data_statistika import stats_2020_clean, stats_2021_clean, stats_2022_clean, stats_2023_clean, \
    df_statistika_combined
from data_klasirane_2023 import klasirane_2023_combined
from datetime import datetime
from plot_functions import fig3_visualization, fig3_visualization_mobile
from msg_history import get_message_history, create_message
from streamlit.components.v1 import html, components
import base64

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format


# Dashboard layout
pio.templates.default = "simple_white"
st.set_page_config(layout="wide", page_title='НВО', page_icon="favicon.ico")
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


# # Set background image (very hard to visualise properly)
# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()
#
#
# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#     <style>
#     .main {
#     background-image: url("data:image/png;base64,%s");
#     background-size: auto;
#     background-attachment: local;
#     background-repeat: no-repeat;
#     background-position: top left;
#     }
#
#     [data-testid="baseButton-secondaryFormSubmit"] {
#     background-color: rgb(195, 195, 195);
#     }
#     </style>
#     ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#
#
# set_background('images/bg_image_4.png')

header = st.container()
intro = st.container()
st.divider()
visio_1 = st.container()
st.divider()
visio_2 = st.container()
st.divider()
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
        "<p style='text-align: left; font-size: 10px;'>(*Свободните места за младежи и девойки са показани като сбор на местата"
        " с квотa и местата на общо основание.)</p>", unsafe_allow_html=True)
    st.divider()
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
        st.markdown("<h3 style='text-align: center;'>(Национално Външно Оценяване)<br><br></h3>", unsafe_allow_html=True)

# Intro definition
with intro:
    st.markdown(
        "<p style='text-align: center;'>Здравей, aз съм Диана.<br>Преминавайки изпитанието на матурите(НВО) след "
        "7ми клас с моя син, събрахме всички важни данни по темата за гр.София, публикувани от МОН. За мен беше "
        "много полезно да видя цялата информация систематизирана и визуалиирана на едно място, за да вземем в "
        "процеса на кандидастване възможно най-информирано и базирано на данни решение. <br>"
        "Радваме се да споделим тези данни и се надявам те да помогнат и на други. Тук ще намерите НВО резултатите"
        " - 2023 година, средния успех и броя на учениците, успеваемост, най-предпочитани "
        "и паралелки с минимален или никакъв интерес, свободни места за различните класирания, трендове и повече. "
        "Пишете ми в коментарите ако имате въпроси.<br>"
        "УСПЕХ НА ВСИЧКИ 😊</p>", unsafe_allow_html=True)


# Create visualization_1 (fig1 and fig2)
with visio_1:
    col1, col2 = st.columns(2, gap='medium')

    # Data visualization fig1
    with col2:
        st.markdown("<h3 style='text-align: center;'>НВО Успеваемост</h3>", unsafe_allow_html=True)

        fig = go.Figure()
        histogram = go.Histogram(
                           x=stats_2023_clean["Bin"],
                           y=stats_2023_clean[y_column],
                           histfunc='sum',
                           name=2023,
                           )
        fig.add_trace(histogram)

        df_grouped_2022 = stats_2022_clean.query("Година == '2022'").groupby("Bin", as_index=False)[y_column].sum()
        line_2022 = go.Scatter(x=df_grouped_2022["Bin"],
                                 y=df_grouped_2022[y_column],
                                 mode='lines',
                                 line=dict(width=2),
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
        st.markdown("<h3 style='text-align: center;'>НВО статистика</h3>", unsafe_allow_html=True)

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
                                       size=14,
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
visio_2.markdown("<h3 style='text-align: center;'>Детайли - класиране</h3>", unsafe_allow_html=True)

with visio_2:

    # # Option for showing 2022 year results with radio buttons, but I don't like it
    # selected_option = c.radio("", ('2023', '2022'), key="fig3_radio_years", horizontal=True)
    # if selected_option == '2023':
    #     fig3_visualization(klasirane_combined=klasirane_2023_combined, yticks_text2=yticks_text2_2023,
    #     x_column=x_column, x2_column=x2_column)
    # elif selected_option == '2022':
    #     fig3_visualization(klasirane_combined=klasirane_2022_combined, yticks_text2=yticks_text2_2022,
    #     x_column=x_column, x2_column=x2_column)

    mobile_toggle = visio_2.toggle('Адаптирана графика за телефон')

    tab1, tab2 = visio_2.tabs(["2023", "2022"])
    with tab1:
        if mobile_toggle:
            fig3_visualization_mobile(klasirane_combined=klasirane_2023_combined,
                                      x_column=x_column,
                                      x2_column=x2_column)
        else:
            fig3_visualization(klasirane_combined=klasirane_2023_combined,
                               x_column=x_column,
                               x2_column=x2_column)
    with tab2:
        tab2.markdown("<h1 style='text-align: center;'>🛠️</h1><br><p style='text-align: center;'>(не е готово)</p>",
                      unsafe_allow_html=True)


# Message functionality and history features
with comments:
    st.markdown("<h3 style='text-align: center;'>Коментари</h3>", unsafe_allow_html=True)

    msg_history = get_message_history()
    df_messages = pd.DataFrame(list(msg_history))
    for _, message in df_messages.iterrows():
        comments.info(f"{message['name']} ({message['time']})\n"
                      f"{message['text']}")

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

# # Create comments section
# with comments:
#     st.markdown("<h3 style='text-align: center;'>Коментари</h3>", unsafe_allow_html=True)
    # message_html = ""
    # for _, message in msg_history.iterrows():
    #     message_html += f"""
    #     <div style="background-color: whitesmoke; border: 1px solid #ccc; border-radius: 10px;
    #     padding: 5px; margin: 5px; height: auto;">
    #         {icon_html}
    #         <p>{message['name']} ({message['time']})</p>
    #         <p>{message['text']}</p>
    #     </div>
    #     """
    #
    # html_snippet = f"""
    # <div style="height: 300px; overflow-y: scroll;">
    #     {message_html}
    # </div>
    # """
    # html(html_snippet, height=400, scrolling=True)


    # scroller = """
    #     <div>
    #         <style>
    #         .css-5rimss.e1nzilvr5 {
    #             overflow-y: auto;
    #             max-height: 100px;
    #         }
    #         </style>
    #     </div>
    #     """
    #
    # comments.markdown(scroller, unsafe_allow_html=True)
