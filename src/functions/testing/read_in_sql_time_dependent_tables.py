# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:33:16 2022

@author: DCHELD
"""

from dash import Input, Output, html, dcc
import pandas as pd
import dash_ag_grid as dag
from sqlalchemy import create_engine
import pymysql  # is needed !!!!!
import os
from dotenv import load_dotenv
import dash
from datetime import date
from eod import EodHistoricalData
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import plotly.express as px

import plotly.io as io
io.renderers.default='browser'


load_dotenv("C:\DATA\CLOUD\PROJECTS\COCKPIT_DASH\config.env")
SQL_ENGINE  = os.getenv('SQL_ENGINE')
API_KEY  = os.getenv('API_KEY')
      
#df = pd.read_csv('positions.csv')
# needs the package: https://pypi.org/project/PyMySQL/    
#cnx = create_engine('mysql+pymysql://dbmyetf:4sevilla%2A@myetf.ch/myetfch_') 
cnx = create_engine(SQL_ENGINE) 

#df_sql = pd.read_sql('SELECT * FROM overview_table_cockpit_dash', cnx) #read the entire table


df = pd.read_sql('SELECT * FROM dc_rs_short_ptf', cnx) #read the entire table
#df = df_sql.loc[:,['TICKER','NAME', 'TICKER_2', 'ASSET_CLASS', 'SECTOR', 'RET_20']]


df['date'] = pd.to_datetime(dict(year=df.Y, month=df.M, day=df.D))    
df.set_index('date', inplace = True)
fig = px.line(df, x=df.index, y='PTF_VAMI', title = 'test')


#weights_last = df.iloc[-1,4:df.shape[1]]

#fig = px.pie(values = weights_last, names = weights_last.index)
fig.show()



#fig.show()