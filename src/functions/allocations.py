# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

from dash import Input, Output, html, dcc, State
import pandas as pd
import dash
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import plotly.express as px
from functions.get_historical_allocations_from_df import  get_historical_allocations_from_df
from functions.get_current_allocation_from_df import  get_current_allocation_from_df
from functions.get_color_dict import  get_color_dict
from io import StringIO



def allocations(df):
        
       
    df_drop_down = pd.DataFrame({'Category': ['Asset Class', 'FX', 'Sectors', 'Regions']})
    
    
    
    # App layout
    layout = html.Div([
        dcc.Store(id='data-store', data=df.to_json(orient='split')),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='category-dropdown-allocation',
                    options=[{'label': category, 'value': category} for category in df_drop_down['Category'].unique()],
                    value='Asset Class',  # Default value
                ),
            ], width=2)
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([html.H5("Actual Allocation"),dcc.Graph(id='pie-chart-allocation')], width=6),
            dbc.Col([html.H5("Historical Allocation"),dcc.Graph(id='area-char-allocation')], width=6)
        ])
    ])
    
    
    return layout
    
    
# Callback to update the charts
@dash.callback(
    [Output('pie-chart-allocation', 'figure'),
     Output('area-char-allocation', 'figure')],
    [Input('category-dropdown-allocation', 'value')],
    [State('data-store', 'data')]
)
def update_charts(selected_category,json_data):
    
    print('check') 
    
        
    if selected_category == 'Asset Class':
        cat = 'ASSET_CLASS'
    elif selected_category == 'FX':
        cat = 'FX'
    elif selected_category == 'Sectors':
        cat = 'SECTOR'
    elif selected_category == 'Regions':
        cat = 'REGION'
    else:
        print('Category not defined')
        
    
    json_data = StringIO(json_data)
    df = pd.read_json(json_data, orient='split')
    df_alloc = get_current_allocation_from_df(df,cat)
    df_alloc_hist = get_historical_allocations_from_df(df,cat)
    color_dict = get_color_dict()

    # Create pie chart:
    pie_fig = px.pie(df_alloc, values='WEIGHTS', names='ASSET_CLASS',
                    color='ASSET_CLASS', 
                    color_discrete_map= color_dict
                     ) 


    # Create a time allocation chart: 
    area_fig = go.Figure()

    # Loop through each column (except for the x-axis column)
    for col in df_alloc_hist.columns:  # Assuming the first column is for the x-axis
        area_fig.add_trace(
            go.Scatter(
                y=df_alloc_hist[col],
                x=df_alloc_hist.index,
                fill='tonexty',
                # Customize your trace here (e.g., name, mode, line properties)
                name=col,
                stackgroup='one',
                line=dict(width=0,color= color_dict.get(col, None)),
                #mode = 'none'
            )
        )

    # Customize the layout
    area_fig.update_layout(
        #title="Historical Allocation",
        xaxis_title="Time",
        yaxis_title="% Allocation",
        yaxis_range=(0, 1)
    )    


    return pie_fig, area_fig





    

