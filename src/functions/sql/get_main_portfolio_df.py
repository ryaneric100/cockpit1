# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:33:16 2022

@author: DCHELD
"""

import pandas as pd
from sqlalchemy import create_engine
import pymysql  # is needed !!!!!
import os
from dotenv import load_dotenv


import plotly.io as io
io.renderers.default='browser'


def get_main_portfolio_df(table_name):

    #load_dotenv("C:\DC_PYTHON\DC_COCKPIT\config.env")
    load_dotenv("/etc/secrets/config.env")
    
    SQL_FLAG  = os.getenv('SQL_FLAG')
    
    if int(SQL_FLAG) == 1:
        SQL_ENGINE  = os.getenv('SQL_RENDER')
    else:
        SQL_ENGINE  = os.getenv('SQL_ENGINE')
    
    
    print(SQL_FLAG)
    print(SQL_ENGINE)
      
    
    # testing with csv
    # df = pd.read_csv('positions.csv') 
    # needs the package: https://pypi.org/project/PyMySQL/    
    #cnx = create_engine('mysql+pymysql://dbmyetf:4sevilla%2A@myetf.ch/myetfch_') 
    cnx = create_engine(SQL_ENGINE) 
    
    #table_name = 'dc_rs_short_ptf'
    
    df = pd.read_sql('SELECT * FROM '+table_name, cnx) #read the entire table
    
    # Convert column names to uppercase and sort by time (was an issue for postgresql)
    df = df.rename(columns=lambda x: x.upper())
    df = df.sort_values(by=['TIME'])
   
    
    df['index'] = pd.to_datetime(dict(year=df.Y, month=df.M, day=df.D))    
    df.set_index('index', inplace = True)
    
    return df
