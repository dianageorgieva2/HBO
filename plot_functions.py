# INSTRUCTIONS FOR NEW YEAR FILES IMPORT, CLEANING, STANDARTISATION
# 1. Add filter_NEWYEAR() function as a copy from past year and change manually the year
# 2. Update df_multiselect

import numpy as np
import plotly.graph_objects as go
import io
import streamlit.components.v1 as components
import plotly.subplots as sp
import textwrap
import streamlit as st
import plotly


# Visualization of fig3 for desktop
def fig3_visualization(klasirane_combined, x_column, x2_column, mobile, year):

    # Define filter function for 2025
    def filter_2025():
        df = klasirane_combined
        filters = ['Училище_формат', 'Код паралелка', 'Паралелка_формат', 'Профил_1', 'Профил_2']
        placeholder_names = ['Училище', 'Код паралелка', 'Паралелка', 'Профил_1', 'Профил_2']

        filters = {filter_name: [] for filter_name in filters}

        if 'filters' not in st.session_state:
            st.session_state['filters'] = filters

        def filter_df(except_filter=None):
            filtered_df = df.copy()
            for key, values in st.session_state.filters.items():
                if key != except_filter and values:
                    filtered_df = filtered_df[filtered_df[key].isin(values)]
            return filtered_df

        def display_filters(num_columns=5, gap="small"):
            filters_changed = False
            counter = 1
            max_value = num_columns
            col_list = st.columns(num_columns, gap=gap)

            for filter_name in st.session_state.filters.keys():
                filtered_df = filter_df(filter_name)
                options = sorted(filtered_df[filter_name].unique().tolist())

                # Remove selected values that are not in options anymore
                valid_selections = [v for v in st.session_state.filters[filter_name] if v in options]
                if valid_selections != st.session_state.filters[filter_name]:
                    st.session_state.filters[filter_name] = valid_selections
                    filters_changed = True

                with col_list[counter - 1]:
                    selected = st.multiselect(" ", options,
                                              default=st.session_state.filters[filter_name],
                                              placeholder=f"{placeholder_names[counter - 1]}")

                # increase counter and reset to 1 if max_value is reached
                counter += 1
                counter = counter % (max_value + 1)
                if counter == 0:
                    counter = 1

                if selected != st.session_state.filters[filter_name]:
                    st.session_state.filters[filter_name] = selected
                    filters_changed = True

            if filters_changed:
                st.rerun()

        display_filters(num_columns=5, gap="small")
        return filter_df()

    # Define filter function for 2024
    def filter_2024():
        df = klasirane_combined
        filters = ['Училище_формат', 'Код паралелка', 'Паралелка_формат', 'Профил_1', 'Профил_2']
        placeholder_names = ['Училище', 'Код паралелка', 'Паралелка', 'Профил_1', 'Профил_2']

        filters = {filter_name: [] for filter_name in filters}

        if 'filters' not in st.session_state:
            st.session_state['filters'] = filters

        def filter_df(except_filter=None):
            filtered_df = df.copy()
            for key, values in st.session_state.filters.items():
                if key != except_filter and values:
                    filtered_df = filtered_df[filtered_df[key].isin(values)]
            return filtered_df

        def display_filters(num_columns=5, gap="small"):
            filters_changed = False
            counter = 1
            max_value = num_columns
            col_list = st.columns(num_columns, gap=gap)

            for filter_name in st.session_state.filters.keys():
                filtered_df = filter_df(filter_name)
                options = sorted(filtered_df[filter_name].unique().tolist())

                # Remove selected values that are not in options anymore
                valid_selections = [v for v in st.session_state.filters[filter_name] if v in options]
                if valid_selections != st.session_state.filters[filter_name]:
                    st.session_state.filters[filter_name] = valid_selections
                    filters_changed = True

                with col_list[counter - 1]:
                    selected = st.multiselect(" ", options,
                                              default=st.session_state.filters[filter_name],
                                              placeholder=f"{placeholder_names[counter - 1]}")

                # increase counter and reset to 1 if max_value is reached
                counter += 1
                counter = counter % (max_value + 1)
                if counter == 0:
                    counter = 1

                if selected != st.session_state.filters[filter_name]:
                    st.session_state.filters[filter_name] = selected
                    filters_changed = True

            if filters_changed:
                st.rerun()

        display_filters(num_columns=5, gap="small")
        return filter_df()

    # Define filter function for 2023
    def filter_2023():
        df = klasirane_combined
        filters = ['Училище_формат', 'Код паралелка', 'Паралелка_формат', 'Профил_1', 'Профил_2']
        placeholder_names = ['Училище', 'Код паралелка', 'Паралелка', 'Профил_1', 'Профил_2']

        filters = {filter_name: [] for filter_name in filters}

        if 'filters' not in st.session_state:
            st.session_state['filters'] = filters

        def filter_df(except_filter=None):
            filtered_df = df.copy()
            for key, values in st.session_state.filters.items():
                if key != except_filter and values:
                    filtered_df = filtered_df[filtered_df[key].isin(values)]
            return filtered_df

        def display_filters(num_columns=5, gap="small"):
            filters_changed = False
            counter = 1
            max_value = num_columns
            col_list = st.columns(num_columns, gap=gap)

            for filter_name in st.session_state.filters.keys():
                filtered_df = filter_df(filter_name)
                options = sorted(filtered_df[filter_name].unique().tolist())

                # Remove selected values that are not in options anymore
                valid_selections = [v for v in st.session_state.filters[filter_name] if v in options]
                if valid_selections != st.session_state.filters[filter_name]:
                    st.session_state.filters[filter_name] = valid_selections
                    filters_changed = True

                with col_list[counter - 1]:
                    selected = st.multiselect(" ", options,
                                              default=st.session_state.filters[filter_name],
                                              placeholder=f"{placeholder_names[counter - 1]}")

                # increase counter and reset to 1 if max_value is reached
                counter += 1
                counter = counter % (max_value + 1)
                if counter == 0:
                    counter = 1

                if selected != st.session_state.filters[filter_name]:
                    st.session_state.filters[filter_name] = selected
                    filters_changed = True

            if filters_changed:
                st.rerun()

        display_filters(num_columns=5, gap="small")
        return filter_df()

    # Define filter function for 2022
    def filter_2022():
        df2 = klasirane_combined
        filters2 = ['Училище_формат', 'Код паралелка', 'Паралелка_формат', 'Профил_1', 'Профил_2']
        placeholder_names2 = ['Училище', 'Код паралелка', 'Паралелка', 'Профил_1', 'Профил_2']
        filters2 = {filter_name: [] for filter_name in filters2}

        if 'filters2' not in st.session_state:
            st.session_state['filters2'] = filters2

        def filter_df2(except_filter2=None):
            filtered_df2 = df2.copy()
            for key, values in st.session_state.filters2.items():
                if key != except_filter2 and values:
                    filtered_df2 = filtered_df2[filtered_df2[key].isin(values)]
            return filtered_df2

        def display_filters2(num_columns2=5, gap2="small"):
            filters_changed2 = False
            counter2 = 1
            max_value2 = num_columns2
            col_list2 = st.columns(num_columns2, gap=gap2)

            for filter_name in st.session_state.filters2.keys():
                filtered_df2 = filter_df2(filter_name)
                options2 = sorted(filtered_df2[filter_name].unique().tolist())

                # Remove selected values that are not in options anymore
                valid_selections2 = [v for v in st.session_state.filters2[filter_name] if v in options2]
                if valid_selections2 != st.session_state.filters2[filter_name]:
                    st.session_state.filters2[filter_name] = valid_selections2
                    filters_changed2 = True

                with col_list2[counter2 - 1]:
                    selected2 = st.multiselect(" ", options2,
                                               default=st.session_state.filters2[filter_name],
                                               placeholder=f"{placeholder_names2[counter2 - 1]}")

                # increase counter and reset to 1 if max_value is reached
                counter2 += 1
                counter2 = counter2 % (max_value2 + 1)
                if counter2 == 0:
                    counter2 = 1

                if selected2 != st.session_state.filters2[filter_name]:
                    st.session_state.filters2[filter_name] = selected2
                    filters_changed2 = True

            if filters_changed2:
                st.rerun()

        display_filters2(num_columns2=5, gap2="small")
        return filter_df2()

    # Define filter function for 2021
    def filter_2021():
        df3 = klasirane_combined
        filters3 = ['Училище_формат', 'Код паралелка', 'Паралелка_формат', 'Профил_1', 'Профил_2']
        placeholder_names3 = ['Училище', 'Код паралелка', 'Паралелка', 'Профил_1', 'Профил_2']
        filters3 = {filter_name: [] for filter_name in filters3}

        if 'filters3' not in st.session_state:
            st.session_state['filters3'] = filters3

        def filter_df3(except_filter3=None):
            filtered_df3 = df3.copy()
            for key, values in st.session_state.filters3.items():
                if key != except_filter3 and values:
                    filtered_df3 = filtered_df3[filtered_df3[key].isin(values)]
            return filtered_df3

        def display_filters3(num_columns3=5, gap3="small"):
            filters_changed3 = False
            counter3 = 1
            max_value3 = num_columns3
            col_list3 = st.columns(num_columns3, gap=gap3)

            for filter_name in st.session_state.filters3.keys():
                filtered_df3 = filter_df3(filter_name)
                options3 = sorted(filtered_df3[filter_name].unique().tolist())

                # Remove selected values that are not in options anymore
                valid_selections3 = [v for v in st.session_state.filters3[filter_name] if v in options3]
                if valid_selections3 != st.session_state.filters3[filter_name]:
                    st.session_state.filters3[filter_name] = valid_selections3
                    filters_changed3 = True

                with col_list3[counter3 - 1]:
                    selected3 = st.multiselect(" ", options3,
                                               default=st.session_state.filters3[filter_name],
                                               placeholder=f"{placeholder_names3[counter3 - 1]}")

                # increase counter and reset to 1 if max_value is reached
                counter3 += 1
                counter3 = counter3 % (max_value3 + 1)
                if counter3 == 0:
                    counter3 = 1

                if selected3 != st.session_state.filters3[filter_name]:
                    st.session_state.filters3[filter_name] = selected3
                    filters_changed3 = True

            if filters_changed3:
                st.rerun()

        display_filters3(num_columns3=5, gap3="small")
        return filter_df3()

    # Define filter function for 2020
    def filter_2020():
        df0 = klasirane_combined
        filters0 = ['Училище_формат', 'Код паралелка', 'Паралелка_формат', 'Профил_1', 'Профил_2']
        placeholder_names0 = ['Училище', 'Код паралелка', 'Паралелка', 'Профил_1', 'Профил_2']
        filters0 = {filter_name: [] for filter_name in filters0}

        if 'filters0' not in st.session_state:
            st.session_state['filters0'] = filters0

        def filter_df0(except_filter0=None):
            filtered_df0 = df0.copy()
            for key, values in st.session_state.filters0.items():
                if key != except_filter0 and values:
                    filtered_df0 = filtered_df0[filtered_df0[key].isin(values)]
            return filtered_df0

        def display_filters0(num_columns0=5, gap0="small"):
            filters_changed0 = False
            counter0 = 1
            max_value0 = num_columns0
            col_list0 = st.columns(num_columns0, gap=gap0)

            for filter_name in st.session_state.filters0.keys():
                filtered_df0 = filter_df0(filter_name)
                options0 = sorted(filtered_df0[filter_name].unique().tolist())

                # Remove selected values that are not in options anymore
                valid_selections0 = [v for v in st.session_state.filters0[filter_name] if v in options0]
                if valid_selections0 != st.session_state.filters0[filter_name]:
                    st.session_state.filters0[filter_name] = valid_selections0
                    filters_changed0 = True

                with col_list0[counter0 - 1]:
                    selected0 = st.multiselect(" ", options0,
                                               default=st.session_state.filters0[filter_name],
                                               placeholder=f"{placeholder_names0[counter0 - 1]}")

                # increase counter and reset to 1 if max_value is reached
                counter0 += 1
                counter0 = counter0 % (max_value0 + 1)
                if counter0 == 0:
                    counter0 = 1

                if selected0 != st.session_state.filters0[filter_name]:
                    st.session_state.filters0[filter_name] = selected0
                    filters_changed0 = True

            if filters_changed0:
                st.rerun()

        display_filters0(num_columns0=5, gap0="small")
        return filter_df0()

    # Select which filter function to be used
    if not st.multiselect:
        df_multiselect = klasirane_combined
    else:
        if year == 2025:  # Add the new year function
            df_multiselect = filter_2025()
        elif year == 2024:
            df_multiselect = filter_2024()
        elif year == 2023:
            df_multiselect = filter_2023()
        elif year == 2022:
            df_multiselect = filter_2022()
        elif year == 2021:
            df_multiselect = filter_2021()
        elif year == 2020:
            df_multiselect = filter_2020()

    fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, column_widths=[0.23, 0.77])
    code_to_uchilishte_map = dict(df_multiselect[['Код паралелка', 'Училище_short']].astype(str).drop_duplicates().values)
    code_to_paral_map = dict(zip(df_multiselect['Код паралелка'], df_multiselect['Паралелка']))
    code_to_uchilishte_map_hover = dict(df_multiselect[['Код паралелка', 'Училище_формат']].drop_duplicates().values)
    code_to_bal_map_hover = dict(df_multiselect[['Код паралелка', 'Балообразуване']].drop_duplicates().values)

    for k in df_multiselect['Класиране'].unique():
        df_k = df_multiselect[df_multiselect['Класиране'] == k]
        # hover_text_fig3 = [f"{code} {code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
        #     for code in df_k['Код паралелка'].unique()]
        hover_text_fig3 = [f"{code} {'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=45))}<br>"
                           f"{'<br>'.join(textwrap.wrap(code_to_uchilishte_map_hover[code], width=45))}<br>" \
                           f"{'<br>'.join(textwrap.wrap(code_to_bal_map_hover[code], width=45))}"
                           for code in df_k['Код паралелка'].unique()]

        bars = go.Bar(x=df_k[x_column],
                      y=df_k['Код паралелка'],
                      name=f'{k} класиране',
                      offsetgroup=f'{k} класиране',
                      legendgroup=f'{k} класиране',
                      text=df_k[x_column],
                      textposition="outside",
                      cliponaxis=False,
                      textfont=dict(size=12),
                      hoverlabel=dict(namelength=-1),
                      hovertext=hover_text_fig3,
                      hovertemplate='%{hovertext}<br>Мин. бал: %{x}, <extra></extra>',
                      orientation="h",
                      showlegend=False,
                      # width=0.2,
                      )

        fig3.add_trace(bars, row=1, col=2)

    cols = plotly.colors.DEFAULT_PLOTLY_COLORS
    color_position = 0
    for k in df_multiselect['Класиране'].unique():
        df_k = df_multiselect[df_multiselect['Класиране'] == k]
        if not mobile:
            yticks_text = [f"{'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=30))} " 
                           f"<br> <i style='color:#808095;'>{code_to_uchilishte_map[code][:25]}</i>"
                           f"{'...' if len(code_to_uchilishte_map[code]) > 25 else ''}"
                           for code in df_multiselect['Код паралелка'].unique()]

        else:
            yticks_text = [f"{code}" for code in df_multiselect['Код паралелка'].unique()]

        mesta = go.Scatter(x=np.full(len(df_k), 'Свободни<br>места'),
                           y=df_k['Код паралелка'],
                           name=f'{k} класиране',
                           offsetgroup=f'{k} класиране',
                           legendgroup=f'{k} класиране',
                           text=df_k[x2_column],
                           textposition="middle right",
                           mode='text+markers',
                           textfont=dict(size=9),
                           marker=dict(color=cols[color_position], size=8, symbol="square"),
                           orientation='h',
                           hoverinfo="none",  # Disable hover interactions
                           )
        fig3.add_trace(mesta, row=1, col=1)
        color_position += 1

        fig3.update_layout(
            scattermode='group',
            hoverlabel_align='left',
            height=len(df_multiselect) * 13 + 180,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            dragmode=False,
            margin=dict(l=5, r=5, pad=13.5),
            legend=dict(orientation="h",
                        yanchor="bottom",
                        y=1,
                        ),
            xaxis2=dict(title='Минимален бал',
                        showticklabels=False,
                        showgrid=False,
                        showline=False,
                        domain=[0.23, 0.93],
                        tickvals=[],
                        # automargin=True,
                        # title_standoff=50
                        ),
            xaxis=dict(title='Св. места',
                       showticklabels=False,
                       showgrid=False,
                       showline=False,
                       type='category',
                       domain=[0, 0.23],
                       tickvals=[],
                       # automargin=True,
                       # title_standoff=50
                       ),
            yaxis=dict(showticklabels=True,
                       type='category',
                       showgrid=False,
                       tickmode='array',
                       side='left',
                       ticktext=yticks_text,
                       range=[len(df_multiselect['Код паралелка'].unique()) - .8, -.5],
                       tickvals=df_multiselect['Код паралелка'].unique(),
                       ),
            yaxis2=dict(showticklabels=False,
                        type='category',
                        showgrid=False,
                        showline=False,
                        position=1,
                        tickmode='array',
                        side='right',
                        range=[len(df_multiselect['Код паралелка'].unique()) - .8, -.5],
                        tickvals=[],
                        )
        )

    config = {
        'scrollZoom': False,
        'displayModeBar': False,
        'showAxisDragHandles': False,
    }

    buffer = io.StringIO()
    fig3.write_html(buffer, full_html=True, include_plotlyjs=True, config=config)
    components.html(buffer.getvalue(), width=None, height=600, scrolling=True)

    with st.expander("Таблица с данните"):
        st.dataframe(data=df_multiselect,
                     column_order=('Код паралелка', 'Паралелка_формат', 'Училище_формат', 'Училище_short', 'Район',
                                   'Вид на паралелката', 'Балообразуване', 'Форма на обучение', 'Брой паралелки',
                                   'Година', 'Места_общ_брой', 'Места_общ_брой_м', 'Места_общ_брой_д', 'Класиране',
                                   'Мин_бал_о', 'Мин_бал_м', 'Мин_бал_ж', 'Макс_бал_о', 'Макс_бал_м', 'Макс_бал_ж',
                                   'Профил_1', 'Профил_2', 'Профил_3'),
                     column_config={
                         'Код паралелка': 'Код паралелка',
                         'Паралелка_формат': 'Паралелка',
                         'Училище_формат': 'Училище',
                         'Училище_short': 'Училище(съкр.)',
                         'Район': 'Район',
                         'Вид на паралелката': 'Вид на паралелката',
                         'Балообразуване': 'Балообразуване',
                         'Форма на обучение': 'Форма на обучение',
                         'Брой паралелки': 'Брой паралелки',
                         'Места_общ_брой': 'Места общ брой (o)',
                         'Места_общ_брой_м': 'Места общ брой (м)',
                         'Места_общ_брой_д': 'Места общ брой (д)',
                         'Класиране': 'Класиране',
                         'Мин_бал_о': 'Мин. бал (о)',
                         'Мин_бал_м': 'Мин. бал (м)',
                         'Мин_бал_ж': 'Мин. бал (д)',
                         'Макс_бал_о': 'Макс. бал (о)',
                         'Макс_бал_м': 'Макс. бал(м)',
                         'Макс_бал_ж': 'Макс. бал(д)',
                         'Профил_1': 'Профил 1',
                         'Профил_2': 'Профил 2',
                         'Профил_3': 'Профил 3'})
