# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

import dash
from  functions.get_portfolio_layout import get_portfolio_layout


# name of strategy
strat_name = 'bkb_world'



dash.register_page(__name__,
                   path='/bkb_world',
                   name='BKB Stocks Global',
                   title='BKB Stocks Global',
                   #image='pg3.png',
                   #description='no description'
)



# Create a lambda function with fixed arguments
serve_layout_lambda = lambda: get_portfolio_layout(strat_name)

layout = serve_layout_lambda
