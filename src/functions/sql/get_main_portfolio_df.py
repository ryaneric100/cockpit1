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


    
    #load_dotenv("C:\DATA\CLOUD\PROJECTS\COCKPIT_DASH\config.env")
    load_dotenv("/etc/secrets/config.env")

    SQL_ENGINE  = os.getenv('SQL_ENGINE')
          
    # testing with csv
    # df = pd.read_csv('positions.csv') 
    # needs the package: https://pypi.org/project/PyMySQL/    
    #cnx = create_engine('mysql+pymysql://dbmyetf:4sevilla%2A@myetf.ch/myetfch_') 
    cnx = create_engine(SQL_ENGINE) 
    
    #table_name = 'dc_rs_short_ptf'
    
    df = pd.read_sql('SELECT * FROM '+table_name, cnx) #read the entire table
    
    df['index'] = pd.to_datetime(dict(year=df.Y, month=df.M, day=df.D))    
    df.set_index('index', inplace = True)
    
    return df
