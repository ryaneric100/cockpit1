# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:33:16 2022

@author: DCHELD
"""

from dash import  html
import dash_ag_grid as dag
from functions.get_trades_from_df import  get_trades_from_df



def trading(df):
        
        #df = get_main_portfolio_df('dc_rs_short_ptf')
        df_trades = get_trades_from_df(df)
        
    
        ptf_table =  html.Div(
            [
  
                dag.AgGrid(
                  id="portfolio-grid2",
                  #className="ag-theme-alpine-dark",
                  columnDefs=[{"headerName": i, "field": i, "cellRenderer": "markdown"} for i in df_trades.columns],
                  rowData=df_trades.to_dict("records"),
                  columnSize="sizeToFit",
                  #defaultColDef=defaultColDef,
                  #cellStyle=cellStyle,
                  #dangerously_allow_html=True,
                  dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single", "pagination": False,"paginationAutoPageSize":True},
                  # style = {"height": "800px", "width": "100%"},
                  csvExportParams={
                  "fileName": "ag_grid_test.csv",
                 },
              ),
                
                html.Div(
                    html.Button("Download CSV", id="csv-button", n_clicks=0),
               ), 
                                            
            ])
                
        
        return ptf_table
        
    
    


        

    
    


     
        
     
        
     
        