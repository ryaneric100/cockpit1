# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:49:05 2023

@author: DCHELD
"""


from eod import EodHistoricalData
import pandas as pd
import plotly.express as px
import datetime
import plotly.graph_objects as go

import plotly.io as io
io.renderers.default='browser'




x = [datetime.datetime(year=2013, month=10, day=4),
     datetime.datetime(year=2013, month=11, day=5),
     datetime.datetime(year=2013, month=12, day=6)]

print(x)

fig = go.Figure(data=[go.Scatter(x=x, y=[1, 3, 6])])
# Use datetime objects to set xaxis range
fig.update_layout(xaxis_range=[datetime.datetime(2013, 10, 17),
                               datetime.datetime(2013, 11, 20)])
fig.show(block=True)

