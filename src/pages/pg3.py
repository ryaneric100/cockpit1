# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

import dash
from dash import  html, callback, Output, Input, dcc, State
import dash_bootstrap_components as dbc
from  functions.trading import trading
from  functions.positions import positions
from  functions.statistics import statistics
from  functions.portfolio import portfolio
from  functions.allocations import  allocations
from  functions.contributions import contributions
from functions.sql.get_main_portfolio_df import   get_main_portfolio_df
from io import StringIO
import pandas as pd

from  functions.get_portfolio_layout import get_portfolio_layout


# name of strategy
#strat_name = 'dc_ai_ptf'
strat_name = 'dc_rs_short'
#strat_name = 'swiss_equity_plus_sli_ptf'




dash.register_page(__name__,
                   path='/dc_rs_short_ptf',
                   name='Portfolio1',
                   title='Portfolio',
                   # order = 3,
                   #image='pg3.png',
                   description='Learn all about the heatmap.'
)



#page_layout = get_portfolio_layout(strat_name)


# Create a lambda function with fixed arguments
serve_layout_lambda = lambda: get_portfolio_layout(strat_name)


layout = serve_layout_lambda 


# def page_layout():

#     df = get_main_portfolio_df(strat_name) 
    
#     layout = html.Div([
          
#       dcc.Store(id='data-store-df', data=df.to_json(orient='split')),
        
#       html.Hr(),  
#       html.H5('Portfolio xyz') ,
         
#       dbc.Card(
#         [
#             dbc.CardHeader(
#                 dbc.Tabs(
#                     [
#                         dbc.Tab(label="PORTFOLIO", tab_id="tab-ptf"),
#                         dbc.Tab(label="POSITIONS", tab_id="tab-positions"),
#                         dbc.Tab(label="STATISTICS", tab_id="tab-stats"),
#                         dbc.Tab(label="ALLOCATIONS", tab_id="tab-allocations"),
#                         dbc.Tab(label="CONTRIBUTIONS", tab_id="tab-contributions"),
#                         dbc.Tab(label="TRADING", tab_id="tab-trading"),
#                         dbc.Tab(label="RANKINGS", tab_id="tab-infos"),
#                         dbc.Tab(label="DATA", tab_id="tab-data"),
#                     ],
#                     id="card-tabs",
#                     active_tab="tab-ptf",
#                 )
#             ),
#             dbc.CardBody(html.P(id="card-content", className="card-text")),
#         ]
#         ),
     
#       ]
#     )
#     return layout




# layout = page_layout

 


# @callback(
#     Output("card-content", "children"), 
#     [Input("card-tabs", "active_tab")],
#     [State('data-store-df', 'data')]
# )

# def render_content(active_tab, json_data):
    
#     json_data = StringIO(json_data)
#     df = pd.read_json(json_data, orient='split')
    
#     #df = get_main_portfolio_df(strat_name)
    
#     if active_tab == 'tab-ptf':
#         return portfolio(df)
#     elif active_tab == 'tab-positions':
#         return positions(df)
#     elif active_tab == 'tab-stats':
#         return statistics(df)
#     elif active_tab == 'tab-allocations':
#         return allocations(df)
#     elif active_tab == 'tab-contributions':
#         return contributions(df)
#     elif active_tab == 'tab-trading':
#         return trading(df)
    
    
    


# # @callback(Output('data-store-df', 'data'),
# #               [Input('url', 'pathname')])
# # def update_data(pathname):
# #     strat_name = 'dc_rs_short_ptf'
# #     df = get_main_portfolio_df(strat_name)
# #     return df.to_json(orient='split')
   
    