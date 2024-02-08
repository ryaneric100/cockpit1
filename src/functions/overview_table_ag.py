# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:33:16 2022

@author: DCHELD
"""
from dash import  html
import pandas as pd
import dash_ag_grid as dag
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv



#load_dotenv("C:\DATA\CLOUD\PROJECTS\COCKPIT_DASH\config.env")
load_dotenv("/etc/secrets/config.env")

SQL_ENGINE  = os.getenv('SQL_ENGINE')




def overview_table_ag(flag):
    
    
        if flag == 1:

            cnx = create_engine(SQL_ENGINE) 
            df = pd.read_sql('SELECT * FROM overview_table_cockpit_dash', cnx) #read the entire table
            print(df)
        
        # filename = 'overview.csv'
        elif flag == 2:

            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "overview_stocks.csv"
            abs_file_path = os.path.join(script_dir, rel_path)

            #filename = 'overview_stocks.csv'
            df = pd.read_csv(abs_file_path)
        elif flag == 3:
             filename = 'overview_subptfs.csv'
             df = pd.read_csv(filename)
            
        

        # df = pd.read_csv(filename)
        
        df['PORTFOLIO'] = [create_link(url,solution) for url,solution in zip(df["URL"],df["PORTFOLIO"])]
        df.drop(['URL'], axis = 1, inplace = True)
    
        df['TRADE ALERT'] = df['TRADE ALERT'].apply(lambda x: '🔴' if x > 0 else ' ')
        df['DATA ALERT'] = df['DATA ALERT'].apply(lambda x: '🔔' if x > 0 else ' ')
        
        print(df)
        
        defaultColDef = {
            "filter": True,
            "resizable": True,
            "sortable": True,
            "editable": False,
            "floatingFilter": True,
        }
        
        
        columnDefs = [
            {
                "headerName": "Portfolio Name",
                "field": "PORTFOLIO",
                #"dangerously_allow_code": True,
                "cellRenderer": "markdown",
                "suppressSizeToFit":True,
                "width":"300px",
                
            },
            {
                "headerName": "Stratgey Type",
                "field": "STRATEGY",
                "type": "leftAligned",
               
            },
            {
                "headerName": "FX",
                "field": "FX",
                "type": "centerAligned",
               
            },
            {
                "headerName": "YTD (%)",
                "field": "YTD",
                "type": "centerAligned",
                
               
            },
            {
                "headerName": "Data up to",
                "field": "DATA_UP_TO",
                "type": "centerAligned",
               
            },
            {
                "headerName": "Last Run Model",
                "field": "LAST_RUN",
               "type": "centerAligned",

            },
            {
                "headerName": "Last Trade",
                "field": "LAST_TRADE",
               "type": "centerAligned",
                
            },
            {
                "headerName": "Trade Alert",
                "field": "TRADE ALERT",
                #"dangerously_allow_code": True,
                "cellRenderer": "markdown",
                "type": "centerAligned",
            },
            {
                "headerName": "Data Alert",
                "field": "DATA ALERT",
                "cellRenderer": "markdown",
                #"dangerously_allow_html": True,
                "type": "centerAligned",

            },
        ]
        
        test =  html.Div(
            [
                  dag.AgGrid(
                  id="portfolio-grid_overview",
                  #className="ag-theme-alpine-dark",
                  columnDefs=columnDefs,
                  rowData=df.to_dict("records"),
                  columnSize="sizeToFit",
                  #defaultColDef=defaultColDef,
                  #cellStyle=cellStyle,
                  dangerously_allow_code=True,
                  dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single", "pagination": True,"paginationAutoPageSize":True},
                 style = {"height": "800px", "width": "100%"}
              )
             
                                            
            ]
        )
        return test


def create_link(url:str,solution:str) -> str:
    return f'''<a href="{url}">{solution}</a> '''

#  columnDefs=[{"headerName": i, "field": i, "cellRenderer": "markdown"} for i in df.columns],
# columnDefs=[{"headerName": i, "field": i, "cellRenderer": "markdown", "dangerously_allow_html":"True"} for i in df.columns],
