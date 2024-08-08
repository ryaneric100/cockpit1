# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

import dash
from  functions.get_portfolio_layout import get_portfolio_layout


# name of strategy
strat_name = 'global_kombi_steigen'


dash.register_page(__name__,
                   path='/global_kombi_steigen',
                   name='DC Steigen Combi 10/20',
                   title='DC Steigen Combi 10/20',
                   # order = 3,
                   #image='pg3.png',
                   #description='Learn all about the heatmap.'
)




# Create a lambda function with fixed arguments
serve_layout_lambda = lambda: get_portfolio_layout(strat_name)

layout = serve_layout_lambda


