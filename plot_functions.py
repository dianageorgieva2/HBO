import numpy as np
import plotly.graph_objects as go
import io
import streamlit.components.v1 as components
import plotly.subplots as sp
import textwrap
import streamlit as st
import plotly


# Visualization of fig3 for desktop
def fig3_visualization(klasirane_combined, x_column, x2_column):
    multiselect = st.multiselect("Ако искаш да филтрираш по определено училище/а, избери от списъка:",
                                 options=klasirane_combined['Училище'].drop_duplicates().sort_values(),
                                 placeholder="Избери училище/а")
    df_multiselect = klasirane_combined[klasirane_combined["Училище"].isin(multiselect)]

    if df_multiselect.empty:
        fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, column_widths=[0.20, 0.80])
        code_to_uchilishte_map = dict(klasirane_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
        code_to_paral_map = dict(zip(klasirane_combined['Код паралелка'], klasirane_combined['Паралелка']))

        for k in klasirane_combined['Класиране'].unique():
            df_k = klasirane_combined[klasirane_combined['Класиране'] == k]
            # hover_text = [f"{code} {code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
            #     for code in df_k['Код паралелка'].unique()]
            hover_text = [f"{code} {'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=45))}<br>{'<br>'.join(textwrap.wrap(code_to_uchilishte_map[code], width=45))}"
                for code in df_k['Код паралелка'].unique()]
            yticks_text2_2023 = [
                f"{code}-{'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=25))}"
                for code in klasirane_combined['Код паралелка'].unique()]

            bars = go.Bar(x=df_k[x_column],
                                   y=df_k['Код паралелка'],
                                   name=f'{k} класиране',
                                   offsetgroup=f'{k} класиране',
                                   text=df_k[x_column],
                                   textposition="outside",
                                   cliponaxis=False,
                                   textfont=dict(size=12),
                                   hoverlabel=dict(namelength=-1),
                                   hovertext=hover_text,
                                   hovertemplate='%{hovertext}<br>Мин. бал: %{x}',
                                   orientation="h")

            fig3.add_trace(bars, row=1, col=2)

        cols = plotly.colors.DEFAULT_PLOTLY_COLORS
        color_position = 0
        for k in klasirane_combined['Класиране'].unique():
            df_k = klasirane_combined[klasirane_combined['Класиране'] == k]
            yticks_text2_2023 = [
                f"{code}-{'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=25))}"
                for code in klasirane_combined['Код паралелка'].unique()]
            mesta = go.Scatter(x=np.full(len(df_k), 'Свободни<br>места'),
                                   y=df_k['Код паралелка'],
                                    name=f'{k} класиране',
                                    offsetgroup=f'{k} класиране',
                                   text=df_k[x2_column],
                                   textposition="middle right",
                                    mode='text+markers',
                                   textfont=dict(size=9),
                                    marker=dict(color=cols[color_position], size=8, symbol="square"),
                                    orientation='h',
                                    hoverinfo="none",  # Disable hover interactions
                                    showlegend=False,)
            fig3.add_trace(mesta, row=1, col=1)
            color_position +=1

            fig3.update_layout(
                scattermode='group',
                hoverlabel_align='left',
                height=len(klasirane_combined) * 12,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                dragmode=False,
                margin=dict(l=5, r=5),
                legend=dict(orientation="v",
                            yanchor="bottom",
                            y=1.0001,
                            xanchor='right',
                            x=1),
                xaxis2=dict(title='Минимален бал',
                           titlefont_size=12,
                           side="top",
                           showticklabels=False,
                           showgrid=False,
                           showline=False,
                           domain=[0.20, 1],
                           tickvals=[],
                           ),
                xaxis=dict(side="top",
                           showticklabels=True,
                           showgrid=False,
                            showline=False,
                            type='category',
                            domain=[0, 0.20],
                            tickangle=-90,
                            ),
                yaxis=dict(showticklabels=True,
                           type='category',
                           showgrid=False,
                           tickmode='array',
                           side='left',
                           ticktext=yticks_text2_2023,
                           range=[len(klasirane_combined['Код паралелка'].unique()) - .5, -.5],
                           tickvals=klasirane_combined['Код паралелка'].unique(),
                           ),
                yaxis2=dict(showticklabels=False,
                            type='category',
                            showgrid=False,
                            showline=False,
                            position=1,
                            tickmode='array',
                            side='right',
                            range=[len(klasirane_combined['Код паралелка'].unique()) - .5, -.5],
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

    else:
        fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, column_widths=[0.20, 0.80])
        code_to_uchilishte_map = dict(df_multiselect[['Код паралелка', 'Училище']].drop_duplicates().values)
        code_to_paral_map = dict(zip(df_multiselect['Код паралелка'], df_multiselect['Паралелка']))

        for k in df_multiselect['Класиране'].unique():
            df_k = df_multiselect[df_multiselect['Класиране'] == k]
            # hover_text = [f"{code} {code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
            #     for code in df_k['Код паралелка'].unique()]
            hover_text = [
                f"{code} {'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=45))}<br>{'<br>'.join(textwrap.wrap(code_to_uchilishte_map[code], width=45))}"
                for code in df_k['Код паралелка'].unique()]

            bars = go.Bar(x=df_k[x_column],
                          y=df_k['Код паралелка'],
                          name=f'{k} класиране',
                          offsetgroup=f'{k} класиране',
                          text=df_k[x_column],
                          textposition="outside",
                          cliponaxis=False,
                          textfont=dict(size=12),
                          hoverlabel=dict(namelength=-1),
                          hovertext=hover_text,
                          hovertemplate='%{hovertext}<br>Мин. бал: %{x}',
                          orientation="h")

            fig3.add_trace(bars, row=1, col=2)

        cols = plotly.colors.DEFAULT_PLOTLY_COLORS
        color_position = 0
        for k in df_multiselect['Класиране'].unique():
            df_k = df_multiselect[df_multiselect['Класиране'] == k]
            yticks_text2_2023_multi = [
                f"{code}-{'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=25))}"
                for code in df_multiselect['Код паралелка'].unique()]
            mesta = go.Scatter(x=np.full(len(df_k), 'Свободни<br>места'),
                               y=df_k['Код паралелка'],
                               name=f'{k} класиране',
                               offsetgroup=f'{k} класиране',
                               text=df_k[x2_column],
                               textposition="middle right",
                               mode='text+markers',
                               textfont=dict(size=9),
                               marker=dict(color=cols[color_position], size=8, symbol="square"),
                               orientation='h',
                               hoverinfo="none",  # Disable hover interactions
                               showlegend=False, )
            fig3.add_trace(mesta, row=1, col=1)
            color_position += 1

            fig3.update_layout(
                scattermode='group',
                hoverlabel_align='left',
                height=len(df_multiselect) * 12 + 180,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                dragmode=False,
                margin=dict(l=5, r=5),
                legend=dict(orientation="v",
                            yanchor="bottom",
                            y=1.0001,
                            xanchor='right',
                            x=1),
                xaxis2=dict(title='Минимален бал',
                            titlefont_size=12,
                            side="top",
                            showticklabels=False,
                            showgrid=False,
                            showline=False,
                            domain=[0.20, 1],
                            tickvals=[],
                            ),
                xaxis=dict(side="top",
                           showticklabels=True,
                           showgrid=False,
                           showline=False,
                           type='category',
                           domain=[0, 0.20],
                           tickangle=-90,
                           ),
                yaxis=dict(showticklabels=True,
                           type='category',
                           showgrid=False,
                           tickmode='array',
                           side='left',
                           ticktext=yticks_text2_2023_multi,
                           range=[len(df_multiselect['Код паралелка'].unique()) - .5, -.5],
                           tickvals=df_multiselect['Код паралелка'].unique(),
                           ),
                yaxis2=dict(showticklabels=False,
                            type='category',
                            showgrid=False,
                            showline=False,
                            position=1,
                            tickmode='array',
                            side='right',
                            range=[len(df_multiselect['Код паралелка'].unique()) - .5, -.5],
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


# Visualization of fig3 for mobile
def fig3_visualization_mobile(klasirane_combined, x_column, x2_column):
    multiselect = st.multiselect("Ако искаш да филтрираш по определено училище/а, избери от списъка:",
                                 options=klasirane_combined['Училище'].drop_duplicates().sort_values(),
                                 placeholder="Избери училище/а")
    df_multiselect = klasirane_combined[klasirane_combined["Училище"].isin(multiselect)]

    if df_multiselect.empty:
        fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, column_widths=[0.20, 0.80])
        code_to_uchilishte_map = dict(klasirane_combined[['Код паралелка', 'Училище']].drop_duplicates().values)
        code_to_paral_map = dict(zip(klasirane_combined['Код паралелка'], klasirane_combined['Паралелка']))

        for k in klasirane_combined['Класиране'].unique():
            df_k = klasirane_combined[klasirane_combined['Класиране'] == k]
            # hover_text = [f"{code} {code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
            #     for code in df_k['Код паралелка'].unique()]
            hover_text = [
                f"{code} {'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=40))}<br>{'<br>'.join(textwrap.wrap(code_to_uchilishte_map[code], width=40))}"
                for code in df_k['Код паралелка'].unique()]

            bars = go.Bar(x=df_k[x_column],
                          y=df_k['Код паралелка'],
                          name=f'{k} класиране',
                          offsetgroup=f'{k} класиране',
                          text=df_k[x_column],
                          textposition="outside",
                          cliponaxis=False,
                          textfont=dict(size=12),
                          hoverlabel=dict(namelength=-1),
                          hovertext=hover_text,
                          hovertemplate='%{hovertext}<br>Мин. бал: %{x}',
                          orientation="h")

            fig3.add_trace(bars, row=1, col=2)

        cols = plotly.colors.DEFAULT_PLOTLY_COLORS
        color_position = 0
        for k in klasirane_combined['Класиране'].unique():
            df_k = klasirane_combined[klasirane_combined['Класиране'] == k]
            yticks_text2_2023_mobile = [
                f"{code}"
                for code in klasirane_combined['Код паралелка'].unique()]
            mesta = go.Scatter(x=np.full(len(df_k), 'Свободни<br>места'),
                               y=df_k['Код паралелка'],
                               name=f'{k} класиране',
                               offsetgroup=f'{k} класиране',
                               text=df_k[x2_column],
                               textposition="middle right",
                               mode='text+markers',
                               textfont=dict(size=9),
                               marker=dict(color=cols[color_position], size=8, symbol="square"),
                               orientation='h',
                               hoverinfo="none",  # Disable hover interactions
                               showlegend=False, )
            fig3.add_trace(mesta, row=1, col=1)
            color_position += 1

            fig3.update_layout(
                scattermode='group',
                hoverlabel_align='left',
                height=len(klasirane_combined) * 12,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                dragmode=False,
                margin=dict(l=5, r=5),
                legend=dict(orientation="v",
                            yanchor="bottom",
                            y=1.0001,
                            xanchor='right',
                            x=1),
                xaxis2=dict(title='Минимален бал',
                            titlefont_size=12,
                            side="top",
                            showticklabels=False,
                            showgrid=False,
                            showline=False,
                            domain=[0.20, 1],
                            tickvals=[],
                            ),
                xaxis=dict(side="top",
                           showticklabels=True,
                           showgrid=False,
                           showline=False,
                           type='category',
                           domain=[0, 0.20],
                           tickangle=-90,
                           ),
                yaxis=dict(showticklabels=True,
                           type='category',
                           showgrid=False,
                           tickmode='array',
                           side='left',
                           ticktext=yticks_text2_2023_mobile,
                           range=[len(klasirane_combined['Код паралелка'].unique()) - .5, -.5],
                           tickvals=klasirane_combined['Код паралелка'].unique(),
                           ),
                yaxis2=dict(showticklabels=False,
                            type='category',
                            showgrid=False,
                            showline=False,
                            position=1,
                            tickmode='array',
                            side='right',
                            range=[len(klasirane_combined['Код паралелка'].unique()) - .5, -.5],
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

    else:
        fig3 = sp.make_subplots(rows=1, cols=2, shared_xaxes=True, column_widths=[0.20, 0.80])
        code_to_uchilishte_map = dict(df_multiselect[['Код паралелка', 'Училище']].drop_duplicates().values)
        code_to_paral_map = dict(zip(df_multiselect['Код паралелка'], df_multiselect['Паралелка']))

        for k in df_multiselect['Класиране'].unique():
            df_k = df_multiselect[df_multiselect['Класиране'] == k]
            # hover_text = [f"{code} {code_to_paral_map[code]}<br>{code_to_uchilishte_map[code]}"
            #     for code in df_k['Код паралелка'].unique()]
            hover_text = [
                f"{code} {'<br>'.join(textwrap.wrap(code_to_paral_map[code], width=40))}<br>{'<br>'.join(textwrap.wrap(code_to_uchilishte_map[code], width=40))}"
                for code in df_k['Код паралелка'].unique()]

            bars = go.Bar(x=df_k[x_column],
                          y=df_k['Код паралелка'],
                          name=f'{k} класиране',
                          offsetgroup=f'{k} класиране',
                          text=df_k[x_column],
                          textposition="outside",
                          cliponaxis=False,
                          textfont=dict(size=12),
                          hoverlabel=dict(namelength=-1),
                          hovertext=hover_text,
                          hovertemplate='%{hovertext}<br>Мин. бал: %{x}',
                          orientation="h")

            fig3.add_trace(bars, row=1, col=2)

        cols = plotly.colors.DEFAULT_PLOTLY_COLORS
        color_position = 0
        for k in df_multiselect['Класиране'].unique():
            df_k = df_multiselect[df_multiselect['Класиране'] == k]
            yticks_text2_2023_mobile_multi = [
                f"{code}"
                for code in df_multiselect['Код паралелка'].unique()]
            mesta = go.Scatter(x=np.full(len(df_k), 'Свободни<br>места'),
                               y=df_k['Код паралелка'],
                               name=f'{k} класиране',
                               offsetgroup=f'{k} класиране',
                               text=df_k[x2_column],
                               textposition="middle right",
                               mode='text+markers',
                               textfont=dict(size=9),
                               marker=dict(color=cols[color_position], size=8, symbol="square"),
                               orientation='h',
                               hoverinfo="none",  # Disable hover interactions
                               showlegend=False, )
            fig3.add_trace(mesta, row=1, col=1)
            color_position += 1

            fig3.update_layout(
                scattermode='group',
                hoverlabel_align='left',
                height=len(df_multiselect) * 12 + 180,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                dragmode=False,
                margin=dict(l=5, r=5),
                legend=dict(orientation="v",
                            yanchor="bottom",
                            y=1.0001,
                            xanchor='right',
                            x=1),
                xaxis2=dict(title='Минимален бал',
                            titlefont_size=12,
                            side="top",
                            showticklabels=False,
                            showgrid=False,
                            showline=False,
                            domain=[0.20, 1],
                            tickvals=[],
                            ),
                xaxis=dict(side="top",
                           showticklabels=True,
                           showgrid=False,
                           showline=False,
                           type='category',
                           domain=[0, 0.20],
                           tickangle=-90,
                           ),
                yaxis=dict(showticklabels=True,
                           type='category',
                           showgrid=False,
                           tickmode='array',
                           side='left',
                           ticktext=yticks_text2_2023_mobile_multi,
                           range=[len(df_multiselect['Код паралелка'].unique()) - .5, -.5],
                           tickvals=df_multiselect['Код паралелка'].unique(),
                           ),
                yaxis2=dict(showticklabels=False,
                            type='category',
                            showgrid=False,
                            showline=False,
                            position=1,
                            tickmode='array',
                            side='right',
                            range=[len(df_multiselect['Код паралелка'].unique()) - .5, -.5],
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
