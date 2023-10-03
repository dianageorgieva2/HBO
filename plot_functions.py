import numpy as np
import plotly.graph_objects as go
import io
import streamlit.components.v1 as components
import plotly.subplots as sp
import textwrap
import plotly.io as pio
import streamlit as st


# Visualization of fig3
def fig3_visualization(klasirane_combined, yticks_text2, x_column, x2_column):
    multiselect = st.multiselect("Ако искаш да филтрираш по определено училище/а, избери от списъка:",
                                 options=klasirane_combined['Училище'].drop_duplicates().sort_values(),
                                 placeholder="Избери училище/а")
    df_multiselect = klasirane_combined[klasirane_combined["Училище"].isin(multiselect)]

    if df_multiselect.empty:
        fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, vertical_spacing=0.20, column_widths=[0.65, 0.15])
        code_to_uchilishte_map = dict(klasirane_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
        code_to_paral_map = dict(zip(klasirane_combined['Код паралелка'], klasirane_combined['Паралелка']))

        for k in klasirane_combined['Класиране'].unique()[:-1]:
            df_k = klasirane_combined[klasirane_combined['Класиране'] == k]
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
        for k in klasirane_combined[klasirane_combined['Класиране'] >= 3]['Класиране'].unique():
            df_k = klasirane_combined[klasirane_combined['Класиране'] == k]
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
            height=len(klasirane_combined) * 12,
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
                       range=[len(klasirane_combined['Код паралелка'].unique()) - .5, -.5],
                       tickvals=klasirane_combined['Код паралелка'].unique(),
                       position=0,
                       ),
            yaxis2=dict(showticklabels=False,
                        type='category',
                        showgrid=False,
                        tickmode='array',
                        side='right',
                        ticktext=yticks_text2,
                        range=[len(klasirane_combined['Код паралелка'].unique()) - .5, -.5],
                        tickvals=klasirane_combined['Код паралелка'].unique(),
                        position=0,
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

    else:
        fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, vertical_spacing=0.20, column_widths=[0.65, 0.15])
        code_to_uchilishte_map = dict(df_multiselect[['Код паралелка', 'Училище']].drop_duplicates().values)
        code_to_paral_map = dict(zip(df_multiselect['Код паралелка'], df_multiselect['Паралелка']))

        for k in df_multiselect['Класиране'].unique()[:-1]:
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
            'showAxisDragHandles': False,
        }
        
        pio.templates.default = "plotly"
        buffer = io.StringIO()
        fig3.write_html(buffer, full_html=True, include_plotlyjs=True, config=config)
        components.html(buffer.getvalue(), width=None, height=600, scrolling=True)

    return fig3
