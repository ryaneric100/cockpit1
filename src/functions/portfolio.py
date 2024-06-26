
# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""
from dash import Input, Output, html, dcc, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import dash
import pandas as pd
from io import StringIO
from functions.get_stats_table_from_df import   get_stats_table_from_df
from functions.get_current_allocation_from_df import   get_current_allocation_from_df
from functions.get_color_dict import  get_color_dict



def portfolio(df):
        
        df_stats = get_stats_table_from_df(df)
        df_alloc = get_current_allocation_from_df(df,'ASSET_CLASS')
        df_alloc_sector = get_current_allocation_from_df(df,'SECTOR')
        df_alloc_region = get_current_allocation_from_df(df,'FX')
        
        # time series chart: 
        portfolio_chart = dbc.Card(dcc.Graph(id='time-series-chart'), body=True)

        # get color for pie charts: 
        color_dict = get_color_dict()

        # asste classes:     
        pie_chart_asset_class = px.pie(df_alloc, names='ASSET_CLASS', values='WEIGHTS', color='ASSET_CLASS',color_discrete_map= color_dict)
        piechart_assetclass_card = dbc.Card(dcc.Graph(figure = pie_chart_asset_class, id='mypie'), body=True)
    
        # sectors: 
        pie_chart_sector = px.pie(df_alloc_sector, names='ASSET_CLASS', values='WEIGHTS', color='ASSET_CLASS',color_discrete_map= color_dict)
        piechart_sector_card = dbc.Card(dcc.Graph(figure = pie_chart_sector, id='mypie2'), body=True)
        
        # fx: 
        pie_chart_region = px.pie(df_alloc_region, names='ASSET_CLASS', values='WEIGHTS',color='ASSET_CLASS',color_discrete_map= color_dict)       
        piechart_region_card = dbc.Card(dcc.Graph(figure = pie_chart_region, id='mypie3'), body=True)
    
        
        
        # ytd card/box:     
        ytd = round(df_stats.Ptf[0]*100,2)
                
        ytd_card = dbc.Card(
            dbc.CardBody(
                [
                    html.H1(str(ytd) +"%" , className="YTD"),
                    html.P(
                        "Inception:  "
                        "Description"
                    ),
                ]
            )
        )

        
        # radio buttons for time range selection: 
        radion_items =   dbc.Card(dcc.RadioItems(
        id='time-range',
        options=[
            {'label': ' YTD', 'value': 'ytd'},
            {'label': ' 1 Month', 'value': '1mo'},
            {'label': ' 3 Months', 'value': '3mo'},
            {'label': ' 6 Months', 'value': '6mo'},
            {'label': ' 1 Year', 'value': '1y'},
            {'label': ' 5 Years', 'value': '5y'},
        ],
        value='ytd',
        #labelStyle={'display': 'inline-block'}
        ),body=True)
        
       
       
        # layout of screen: 
        layout_pos = html.Div(
            [
               dcc.Store(id='data-store', data=df.to_json(orient='split')), 
               dbc.Row([dbc.Col([html.H5("Portfolio Chart"),portfolio_chart],  align="center",width=12, lg=8, xl=8),dbc.Col([html.H5("Time Range"),radion_items],  align="top",width=12, lg=2, xl=2),dbc.Col([html.H5("YTD"),ytd_card],  align="top",width=12, lg=2, xl=2)]),
               html.Hr(), 
               dbc.Row([dbc.Col([html.H5("Current Asset Allocation"),piechart_assetclass_card],  align="center",width=12, lg=4, xl=4),dbc.Col([html.H5("Current Sector Allocation"),piechart_sector_card],  align="center",width=12, lg=4, xl=4),dbc.Col([html.H5("Current FX Allocation"),piechart_region_card],  align="center",width=12, lg=4, xl=4)]),
            ]
        )
        
        
        return layout_pos
        
    


# Callback zur Aktualisierung des Diagramms basierend auf dem ausgewählten Zeitraum
@dash.callback(
    Output('time-series-chart', 'figure'),
    Input('time-range', 'value'),
    State('data-store', 'data')
)
def update_chart(time_range,json_data):
    
    json_data = StringIO(json_data)
    
    df = pd.read_json(json_data, orient='split')
    
    # get ytd index
    def get_ytd_index(df):
        cur_year = df.index.max().year
        n=1
        
        while df.index[-n].year==cur_year: 
            n = n+1
        return -n
    
    ytd_ind = get_ytd_index(df)
    
    yr1 = 255
    yr5 = 255*4


    if time_range == 'ytd':
      df =   df.iloc[ytd_ind:-1,:]
    elif time_range == '1mo':
       df =   df.iloc[-20:-1,:]
    elif time_range == '3mo':
       df =   df.iloc[-60:-1,:]
    elif time_range == '6mo':
      df =   df.iloc[-180:-1,:] 
    elif time_range == '1y':
        df =   df.iloc[-yr1:-1,:]
    elif time_range == '5y':
        df =   df.iloc[-yr5:-1,:]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=list(df.index),
                   y=list(df.PTF_VAMI),
                    name="close",
                    line=dict(color="#2986CC")))
    
    # # BMK
    # fig.add_trace(
    #     go.Scatter(
    #         x=list(df.index),
    #         y=list(df.BMK_VAMI),
    #         name="Second VAMI",  # Replace with the actual name for the legend
    #         line=dict(color="#FF5733")  # Change color as needed
    #     )
    # )
        
    
    return fig




      
                
     
        
     
        