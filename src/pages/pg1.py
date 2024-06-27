# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""


import dash
from dash import  html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
from  functions.markets import markets

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/',  # '/' is home page and it represents the url
                   name='Home',  # name of page, commonly used as name of link
                   title='Markets',  # title that appears on browser's tab
                   image='pg1.png',  # image in the assets folder
                   description='Market Overview'
)



# world maps
# heat map for eco stuff


layout = html.Div(
    [
 dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Market Overview", tab_id="market"),
                    dbc.Tab(label="Sectors", tab_id="sectors"),
                    dbc.Tab(label="Liquidity", tab_id="liquidity"),
                ],
                id="card-tabs-market",
                active_tab="market",
            )
        ),
        dbc.CardBody(html.P(id="card-content-market", className="card-text")),
    ]
)
    
  ]
)


@callback(
    Output("card-content-market", "children"), [Input("card-tabs-market", "active_tab")]
)

def render_content(active_tab):
    if active_tab == 'market':
        return  markets()
    elif active_tab == 'sectors':
       return markets()
    elif active_tab == 'liquidity':
      return markets()





