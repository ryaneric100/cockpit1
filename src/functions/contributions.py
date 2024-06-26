# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

from dash import Input, Output, html, dcc, State
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from functions.get_contributions_from_df import  get_contributions_from_df
from functions.get_color_dict import  get_color_dict
from io import StringIO


def contributions(df):
        
       
    df_drop_down = pd.DataFrame({'Category': ['1 Month', '3 Months', '1 Year', 'YTD']})
    
    # App layout
    layout = html.Div([
        dcc.Store(id='data-store', data=df.to_json(orient='split')),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='category-dropdown-contr',
                    options=[{'label': category, 'value': category} for category in df_drop_down['Category'].unique()],
                    value='1 Month',  # Default value
                ),
            ], width=2)
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([html.H5("Asset Class Contribution"),dcc.Graph(id='bar-chart-contr')], align="center",width=12, lg=6, xl=6),
            dbc.Col([html.H5("Position Contribution"),dcc.Graph(id='bar-chart-contr-pos')], align="center",width=12, lg=6, xl=6)
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([html.H5("Sector Contribution"),dcc.Graph(id='bar-chart-contr-sect')], align="center",width=12, lg=6, xl=6),
            dbc.Col([html.H5("FX Contribution"),dcc.Graph(id='bar-chart-contr-fx')], align="center",width=12, lg=6, xl=6)
        ])
    ])
    
    
    return layout
    
    
# Callback to update the charts
@dash.callback(
    [Output('bar-chart-contr', 'figure'),
     Output('bar-chart-contr-pos', 'figure'),
     Output('bar-chart-contr-sect', 'figure'),
     Output('bar-chart-contr-fx', 'figure')],
    [Input('category-dropdown-contr', 'value')],
    [State('data-store', 'data')]
)
def update_charts(selected_category,json_data):
    
    print('check') 
    
    
    if selected_category == '1 Month':
        period = '1M'
    elif selected_category == '3 Months':
        period = '3M'
    elif selected_category == '1 Year':
        period = '1Y'
    elif selected_category == 'YTD':
        period = 'YTD'
    else:
        print('Category not defined')
        
     
    #· get all colrs from dictionary:     
    color_dict = get_color_dict()        
        
    json_data = StringIO(json_data)
    df = pd.read_json(json_data, orient='split')
   

    df_contribution = get_contributions_from_df(df,'ASSET_CLASS',period)

    #bar_fig = px.bar(x=df_contribution.values, y=df_contribution.index, orientation='h', color=df_contribution.index)
    bar_fig = px.bar(x=df_contribution.values, y=df_contribution.index, orientation='h', color=df_contribution.index, color_discrete_map=color_dict) # dict(zip(df_contr_sect.index, colors))
    bar_fig.update_xaxes(title_text='Contribution %')
    bar_fig.update_yaxes(title_text='')
    
    
    df_contr_pos = get_contributions_from_df(df,'TICKER',period)

    #bar_fig = px.bar(x=df_contribution.values, y=df_contribution.index, orientation='h', color=df_contribution.index)
    bar_fig_pos = px.bar(x=df_contr_pos.values, y=df_contr_pos.index, orientation='h', color=df_contr_pos.index, color_discrete_map=color_dict)
    bar_fig_pos.update_xaxes(title_text='Contribution %')
    bar_fig_pos.update_yaxes(title_text='')
        

    df_contr_fx = get_contributions_from_df(df,'SECTOR',period)

    #bar_fig = px.bar(x=df_contribution.values, y=df_contribution.index, orientation='h', color=df_contribution.index)
    bar_fig_fx = px.bar(x=df_contr_fx.values, y=df_contr_fx.index, orientation='h', color=df_contr_fx.index, color_discrete_map=color_dict)
    bar_fig_fx.update_xaxes(title_text='Contribution %')
    bar_fig_fx.update_yaxes(title_text='')


    df_contr_sect = get_contributions_from_df(df,'FX',period)

    #bar_fig = px.bar(x=df_contribution.values, y=df_contribution.index, orientation='h', color=df_contribution.index)
    bar_fig_sect = px.bar(x=df_contr_sect.values, y=df_contr_sect.index, orientation='h', color=df_contr_sect.index, color_discrete_map=color_dict)
    bar_fig_sect.update_xaxes(title_text='Contribution %')
    bar_fig_sect.update_yaxes(title_text='')


    return bar_fig, bar_fig_pos, bar_fig_fx, bar_fig_sect





    

