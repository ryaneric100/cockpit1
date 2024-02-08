# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:33:16 2022

@author: DCHELD
"""

import pandas as pd
from sqlalchemy import create_engine
import pymysql

  
# needs the package: https://pypi.org/project/PyMySQL/    
cnx = create_engine('mysql+pymysql://dbmyetf:4sevilla%2A@myetf.ch/myetfch_') 
df = pd.read_sql('SELECT * FROM overview_table_cockpit_dash', cnx) #read the entire table


df = pd.read_sql('SELECT * FROM test_table', cnx) #read the entire table


print(df)
        


# filename = 'overview.csv'
# dfcsv = pd.read_csv(filename)

# print(dfcsv)