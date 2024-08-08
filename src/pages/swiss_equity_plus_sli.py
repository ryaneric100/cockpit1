# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

import dash
from  functions.get_portfolio_layout import get_portfolio_layout


# name of strategy
strat_name = 'swiss_equity_plus_sli'


dash.register_page(__name__,
                   path='/swiss_equity_plus_sli',
                   name='DC Swiss Equity Select',
                   title='DC Swiss Equity Select',
                   # order = 3,
                   #image='pg3.png',
                   #description='Learn all about the heatmap.'
)




# Create a lambda function with fixed arguments
serve_layout_lambda = lambda: get_portfolio_layout(strat_name)

layout = serve_layout_lambda



