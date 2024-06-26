
# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""

from dash import  html
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from functions.get_seasonal_table_from_df import   get_seasonal_table_from_df
from functions.get_stats_table_from_df import   get_stats_table_from_df



def statistics(df):
        
    
        df_table = get_seasonal_table_from_df(df,2020)
        df_stats = get_stats_table_from_df(df)


        
        cellStyleTest={
            "styleConditions": [
                {"condition": "params.value==0", "style": {"backgroundColor": "#eeeeee", "color": "#696969"}},
                {"condition": "params.colDef.headerName == 'Year'", "style": {"backgroundColor": "#696969", "color": "white", "border": "1px  grey", "font-size":"12px"}},
                {"condition": "params.colDef.headerName == 'YTD'", "style": { "border": "1px  grey", "font-size":"12px"}},
                {"condition": "params.value<-0.05", "style": {"backgroundColor": "#e06666", "color": "black", "border": "1px solid grey", "font-size":"12px"}},
                {"condition": "params.value>0.05", "style": {"backgroundColor": "#6aa84f", "color": "black", "border": "0px solid grey", "font-size":"12px"}},
                {"condition": "params.value>0", "style": {"backgroundColor": "#b6d7a8", "color": "black","border": "0px solid grey", "font-size":"12px"}},
                {"condition": "params.value<0", "style": {"backgroundColor": "#f9cb9c", "color": "black","border": "0px solid grey", "font-size":"12px"}},  
            ],
            "defaultStyle": {"font-weight":"bold", "backgroundColor": "#eeeeee", "color": "#eeeeee", "font-size":"12px",  'border': '0px solid grey' },
        }
        
        
     
        columnDefs = [
            
            {
                "headerName": "Year",
                "field": "Year",
                "type": "rightAligned",
                'cellStyle': cellStyleTest
            },
            {
                "headerName": "YTD",
                "field": "YTD",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                "type": "rightAligned",
                'cellStyle': cellStyleTest
              
            },
            {
                "headerName": "Jan",
                "field": "Jan",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                "type": "rightAligned",
                'cellStyle': cellStyleTest
            },
            {
                "headerName": "Feb",
                "field": "Feb",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                "type": "rightAligned",
                'cellStyle': cellStyleTest
            },
            
            {
               "headerName": "Mar",
               "field": "Mar",
               "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
               "type": "rightAligned",
               'cellStyle': cellStyleTest
            },
            
            {
               "headerName": "Apr",
               "field": "Apr",
               "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
               "type": "rightAligned",
               'cellStyle': cellStyleTest
            },
            
            {
               "headerName": "May",
               "field": "May",
               "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
               "type": "rightAligned",
               'cellStyle': cellStyleTest
            },
           
             {
                 "headerName": "Jun",
                 "field": "Jun",
                 "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                 "type": "rightAligned",
                 'cellStyle': cellStyleTest
             },
             {
                 "headerName": "Jul",
                 "field": "Jul",
                 "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                 "type": "rightAligned",
                 'cellStyle': cellStyleTest
             },
             
             {
                "headerName": "Aug",
                "field": "Aug",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                "type": "rightAligned",
                'cellStyle': cellStyleTest
             },
             
             {
                "headerName": "Sep",
                "field": "Sep",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                "type": "rightAligned",
                'cellStyle': cellStyleTest
             },
             
             {
                "headerName": "Oct",
                "field": "Oct",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"}, 
                "type": "rightAligned",
                'cellStyle': cellStyleTest
             },    
             
             {
                "headerName": "Nov",
                "field": "Nov",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                "type": "rightAligned",
                'cellStyle': cellStyleTest
                
             },
             
             {
                "headerName": "Dec",
                "field": "Dec",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
                "font-weight":"bold",
                "type": "rightAligned",
                'cellStyle': cellStyleTest
                
             },  
            
        ]
    
    
    

        
        columnDefsStats = [
            
            {
               "headerName": "Statistics",
               "field": "Stat"
            },
            
            {
               "headerName": "Portfolio",
               "field": "Ptf",
               "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
               "type": "rightAligned",
            },
            
            {
               "headerName": "Benchmark",
               "field": "BMK",
               "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
               "type": "rightAligned",
            },
            
            
        ]
        
        
    
        stats_table =  html.Div(
            [
                  html.H5("Key Statistics"),      
                dag.AgGrid(
                    
                  id="stats_table",
                  className="ag-theme-alpine",
                  columnDefs = columnDefsStats, #[{"headerName": i, "field": i, "cellRenderer": "markdown"} for i in df_stats.columns],
                  rowData=df_stats.to_dict("records"),
                  columnSize="sizeToFit",
                  dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single", "pagination": False,"paginationAutoPageSize":True},
                  # style = {"height": "800px", "width": "100%"},
              ),
                
                                            
            ])
    
    
    
        ptf_table =  html.Div(
            [
                html.H5("Seasonal Performance"),  
                dag.AgGrid(
                  id="ag-seasonal",
                  className="ag-theme-alpine",
                  columnDefs= columnDefs, #[{"headerName": i, "field": i, "cellRenderer": "markdown"} for i in df.columns],
                  rowData=df_table.to_dict("records"),
                  columnSize="sizeToFit",
                  dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single", "pagination": False,"paginationAutoPageSize":True},
                  # style = {"height": "800px", "width": "100%"},
              ),
                
            ])
                
        
        
        
        layout_pos = html.Div(
            [
               html.Hr(),
               dbc.Row([dbc.Col(stats_table, align="center",width=12, lg=4, xl=4), dbc.Col(ptf_table,  align="center", width=12, lg=8, xl=8)]),
            ]
        )
        
        
        return layout_pos
        
    

  