# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

import dash
from  functions.get_portfolio_layout import get_portfolio_layout


# name of strategy
strat_name = 'dc_steigen_no_us'


dash.register_page(__name__,
                   path='/dc_steigen_no_us',
                   name='DC Steigen 15 ex US',
                   title='DC Steigen 15 ex US',
                   # order = 3,
                   #image='pg3.png',
                   #description='Learn all about the heatmap.'
)




# Create a lambda function with fixed arguments
serve_layout_lambda = lambda: get_portfolio_layout(strat_name)

layout = serve_layout_lambda


