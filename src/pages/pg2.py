# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""


import dash
from dash import  html, callback, Output, Input
import dash_bootstrap_components as dbc
from  functions.overview_table_ag import overview_table_ag


dash.register_page(__name__,
                   path='/overview',
                   name='Overview Portfolios',
                   title='Overview Portfolios',
                   image='pg3.png',
                   description='Learn all about the heatmap.'
)




layout = html.Div(
    [
 dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Portfolios", tab_id="tab-etf"),
                    dbc.Tab(label="Portfolio Module", tab_id="tab-stocks"),
                    #dbc.Tab(label="Sub Portfolios", tab_id="sub-ptfs"),
                ],
                id="card-tabs2",
                active_tab="tab-etf",
            )
        ),
        dbc.CardBody(html.P(id="card-content2", className="card-text")),
    ]
)
    
  ]
)


@callback(
    Output("card-content2", "children"), [Input("card-tabs2", "active_tab")]
)

def render_content(active_tab):
    if active_tab == 'tab-etf':
        return overview_table_ag(1)  # overview_table1()
    elif active_tab == 'tab-stocks':
       return overview_table_ag(2)  # overview_table1()
    # elif active_tab == 'sub-ptfs':
    #   return overview_table_ag(3)  # overview_table1()
