# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

import dash
from  functions.get_portfolio_layout import get_portfolio_layout


# name of strategy
#strat_name = 'dc_ai_ptf'
strat_name = 'bkb'
#strat_name = 'swiss_equity_plus_sli_ptf'




dash.register_page(__name__,
                   path='/bkb',
                   name='BKB',
                   title='BKB',
                   #image='pg3.png',
                   #description='Learn all about the heatmap.'
)




# Create a lambda function with fixed arguments
serve_layout_lambda = lambda: get_portfolio_layout(strat_name)

layout = serve_layout_lambda
