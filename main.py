import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.io as pio
from data_statistika import stats_2020_clean, stats_2021_clean, stats_2022_clean, stats_2023_clean, \
    df_statistika_combined
from data_klasirane_2023 import klasirane_2023_combined, yticks_text2_2023
from data_klasirane_2022 import klasirane_2022_combined, yticks_text2_2022
from datetime import datetime
from plot_functions import fig3_visualization
from streamlit.components.v1 import html


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format


# Dashboard layout
pio.templates.default = "plotly"
st.set_page_config(layout="wide", page_title='НВО', page_icon="favicon.ico")
config = {
    'scrollZoom': False,
    'displayModeBar': False,
    'showAxisDragHandles': False,
}

st.markdown("<h1 style='text-align: center;'>Национално Външно Оценяване (НВО) - БОРД<br><br></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Здравейте, aз съм Диана.<br>Преминавайки изпитанието на матурите(НВО) след 7ми клас с моя син, "
            "събрахме всички важни данни публикувани от МОН по темата за гр. София. За мен беше много полезно да видя цялата "
            "информация систематизирана и визуалиирана на едно място, за да вземем в процеса на кандидастване възможно"
            " най-информирано и базирано на данни решение. <br>"
            "Радваме се да споделим тези данни и се надявам те да помогнат и на други. Тук ще намерите НВО резултатите - 2023 година, средния успех и броя на учениците, успеваемост, най-предпочитани "
            "и паралелки с минимален или никакъв интерес, свободни места за различните класирания, трендове и повече. "
            "Пишете ми в коментарите ако искате да добавим още информация или имате въпроси.<br>"
            "УСПЕХ НА ВСИЧКИ 😊</p>", unsafe_allow_html=True)
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
            tickangle=-90,
            fixedrange=True),
        yaxis=dict(
            title='Ученици (бр)',
            titlefont_size=14,
            tickfont_size=12,
            fixedrange=True,),
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
                                   size=14,
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
            ticktext=df_statistika_combined.Година.astype(str),
            fixedrange=True,),
        yaxis=dict(showticklabels=False,fixedrange=True,),
        yaxis2=dict(
            showticklabels=False,
            anchor='free',
            overlaying='y',
            side='right',
            position=1,
            range=(df_statistika_combined[avg_tochki].min() - 10, df_statistika_combined[avg_tochki].max() + 10),
            fixedrange=True,),
        legend=dict(orientation="h",
                      yanchor="auto",
                      y=1.2,
                      x=1,
                      xanchor="auto",
                      title=None))

    st.plotly_chart(fig2, use_container_width=True, config=config)

st.divider()

# #----------KLASIRANE----------
# # Create fig3
c = st.container()
with c:
    c.markdown("<h3 style='text-align: center;'>Детайли - класиране</h3>", unsafe_allow_html=True)
    selected_option = c.radio("Избери опция:", ('Ученици(общо)', 'Ученици(младежи)', 'Ученици(девойки)'),
                               key="fig3_radio", horizontal=True)
    if selected_option == 'Ученици(младежи)':
        x_column = 'Мин_бал_м'
        x2_column = "Места_м"
    elif selected_option == 'Ученици(девойки)':
        x_column = 'Мин_бал_ж'
        x2_column = "Места_д"
    else:
        x_column = 'Мин_бал_о'
        x2_column = "Места_общ_брой"

    tab1, tab2 = c.tabs(["2023", "2022"])
    with tab1:
        fig3_visualization(klasirane_combined=klasirane_2023_combined, yticks_text2=yticks_text2_2023, x_column=x_column, x2_column=x2_column)
    with tab2:
        fig3_visualization(klasirane_combined=klasirane_2022_combined, yticks_text2=yticks_text2_2022, x_column=x_column, x2_column=x2_column)


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
st.markdown("<h3 style='text-align: center;'>Коментари</h3>", unsafe_allow_html=True)

c2 = st.container()
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

with c2:
    # message_html = ""
    # for _, message in msg_history.iterrows():
    #     # You can use Font Awesome icons for the icons
    #     # Replace 'fa-icon-name' with the desired Font Awesome icon name
    #     icon_html = f'<i class="fas fa-icon-name" style="margin-right: 5px;"></i>'
    #
    #     message_html += f"""
    #     <div style="background-color: whitesmoke; border: 1px solid #ccc; border-radius: 10px; padding: 5px; margin: 5px; height: auto;">
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

    # This is a non working scroll solution
    for _, message in msg_history.iterrows():
        c2.info(f"{message['name']}")

    scroller = """
        <div>
            <style>
            .css-y4qx5j.e1f1d6gn0 {
                overflow-y: auto;
                max-height: 100px;
            }
            </style>
        </div>
        """

    c2.markdown(scroller, unsafe_allow_html=True)
