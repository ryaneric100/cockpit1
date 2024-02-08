
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:33:16 2022

@author: DCHELD
"""

from dash import Input, Output, html, callback, dcc
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from datetime import date
import plotly.graph_objects as go
import plotly.express as px


from functions.get_seasonal_table_from_df import   get_seasonal_table_from_df
from functions.get_stats_table_from_df import   get_stats_table_from_df
from functions.get_current_allocation_from_df import   get_current_allocation_from_df

from functions.get_gauge_from_allocation import  get_gauge_from_allocation
from functions.get_color_dict import  get_color_dict


# import os
# from dotenv import load_dotenv

# load_dotenv("C:\DATA\CLOUD\PROJECTS\COCKPIT_DASH\config.env")
# SQL_ENGINE  = os.getenv('SQL_ENGINE')
# API_KEY  = os.getenv('API_KEY')




def portfolio(df):
        
                
        #df = get_main_portfolio_df('dc_rs_short_ptf')
        df_table = get_seasonal_table_from_df(df,2020)
        df_stats = get_stats_table_from_df(df)
        df_alloc = get_current_allocation_from_df(df,'ASSET_CLASS')


        
        
        # cellStyleTest={
        #     "styleConditions": [
        #         {"condition": "params.value==0", "style": {"backgroundColor": "#eeeeee", "color": "#696969"}},
        #         {"condition": "params.colDef.headerName == 'Year'", "style": {"backgroundColor": "#696969", "color": "white", "border": "1px  grey", "font-size":"12px"}},
        #         {"condition": "params.colDef.headerName == 'YTD'", "style": { "border": "1px  grey", "font-size":"12px"}},
        #         {"condition": "params.value<-0.1", "style": {"backgroundColor": "#e06666", "color": "black", "border": "0px solid grey", "font-size":"12px"}},
        #         {"condition": "params.value>0.1", "style": {"backgroundColor": "#6aa84f", "color": "black", "border": "0px solid grey", "font-size":"12px"}},
        #         {"condition": "params.value>0", "style": {"backgroundColor": "#b6d7a8", "color": "black","border": "0px solid grey", "font-size":"12px"}},
        #         {"condition": "params.value<0", "style": {"backgroundColor": "#f9cb9c", "color": "black","border": "0px solid grey", "font-size":"12px"}},  
        #     ],
        #     "defaultStyle": {"font-weight":"bold", "backgroundColor": "#eeeeee", "color": "#eeeeee", "font-size":"12px",  'border': '0px solid grey' },
        # }
        
        
        cellStyleTest={
            "styleConditions": [
                {"condition": "params.value==0", "style": {"backgroundColor": "#eeeeee", "color": "#696969"}},
                {"condition": "params.colDef.headerName == 'Year'", "style": {"backgroundColor": "#888888", "color": "white", "border": "1px  grey", "font-size":"12px"}},
                {"condition": "params.colDef.headerName == 'YTD'", "style": { "backgroundColor": "	#888888", "color": "white","border": "1px  grey", "font-size":"12px"}},
                {"condition": "params.value>0", "style": {"backgroundColor": "#F7F7F7", "color": "black","border": "0px solid grey", "font-size":"12px"}},
                {"condition": "params.value<0", "style": {"backgroundColor": "#F7F7F7", "color": "black","border": "0px solid grey", "font-size":"12px"}},  
            ],
            "defaultStyle": {"font-weight":"bold", "backgroundColor": "#eeeeee", "color": "#eeeeee", "font-size":"12px",  'border': '0px solid grey' },
        }        
        
        
       # cellStyleTest = {}
        
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
    
    
    
        # cellStyle={
        #     "styleConditions": [
        #         {"condition": "params.value>0", "style": {"color": "green", "font-weight":"bold"}},
        #         {"condition": "params.value<0", "style": {"color": "red", "font-weight":"bold"}},
        #         {"condition": "params.colDef.headerName == 'YTD'", "style": {"backgroundColor": "#800000", "color": "white"}},
        #     ],
        #     "defaultStyle": {"font-weight":"bold"},
           
        # }
    
    
        fig_ptf = create_ptf_chart(df)
        candlestick = dbc.Card(dcc.Graph(figure = fig_ptf, id='myfigure'), body=True)
    
    
        #pie_chart = px.pie(df_alloc, values='WEIGHTS', names='ASSET_CLASS') #, title='Current Asset Allocation')

        # pie_chart = px.pie(df_alloc, names='ASSET_CLASS', values='WEIGHTS', 
        #       color='ASSET_CLASS',
        #       color_discrete_map={asset: color for asset, color in zip(df_alloc['ASSET_CLASS'], df_alloc['COLOR'])})


        # define colors here: 
        # color_dict = {
        #     'CASH':'#bcbcbc',
        #     'Equity':'#2986cc',
        #     'Gold': '#ffd966',
        #     'Bonds': '#6aa84f',
        #     'Commodity':'#bf9000'
            
        #     }
        
        color_dict = get_color_dict()

        pie_chart = px.pie(df_alloc, names='ASSET_CLASS', values='WEIGHTS', 
              color='ASSET_CLASS',
              color_discrete_map= color_dict)



        
        piechart = dbc.Card(dcc.Graph(figure = pie_chart, id='mypie'), body=True)
    
        gauge = get_gauge_from_allocation()
        gaugechart = dbc.Card(dcc.Graph(figure = gauge, id='mygauge'), body=True)
        
        
        
        
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
               #'cellStyle': cellStyleTest
            },
            
            {
               "headerName": "Benchmark",
               "field": "BMK",
               "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
               "type": "rightAligned",
               #'cellStyle': cellStyleTest
            },
            
            
        ]
        
        
    
        stats_table =  html.Div(
            [
                  html.H5("Key Statistics"),      
                dag.AgGrid(
                    
                  id="stats_table",
                  #className="ag-theme-alpine-dark",
                  #className="ag-theme-alpine borders",
                  columnDefs = columnDefsStats, #[{"headerName": i, "field": i, "cellRenderer": "markdown"} for i in df_stats.columns],
                  rowData=df_stats.to_dict("records"),
                  columnSize="sizeToFit",
                  #cellStyle=cellStyleTest,
                  dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single", "pagination": False,"paginationAutoPageSize":True},
                  # style = {"height": "800px", "width": "100%"},

              ),
                
                                            
            ])
    
    
    
        ptf_table =  html.Div(
            [
  
                html.H5("Seasonal Performance"),  
                dag.AgGrid(
                  id="portfolio-grid333",
                  #className="ag-theme-alpine-dark",
                  #className="ag-theme-alpine borders",
                  columnDefs= columnDefs, #[{"headerName": i, "field": i, "cellRenderer": "markdown"} for i in df.columns],
                  rowData=df_table.to_dict("records"),
                  columnSize="sizeToFit",
                  #cellStyle=cellStyleTest,
                  dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single", "pagination": False,"paginationAutoPageSize":True},
                  # style = {"height": "800px", "width": "100%"},

              ),
                
                                            
            ])
                
        
        
       
        
        
        layout_pos = html.Div(
            [
               #dbc.Row([dbc.Col(candlestick,  align="center",width=12, lg=6, xl=6)]),
               dbc.Row([dbc.Col([html.H5("Portfolio Chart"),candlestick],  align="center",width=12, lg=6, xl=6),dbc.Col([html.H5("Current Asset Allocation"),piechart],  align="center",width=12, lg=3, xl=3),dbc.Col([html.H5("Current Exposure"),gaugechart],  align="center",width=12, lg=3, xl=3)]),
               html.Hr(),
               dbc.Row([dbc.Col(stats_table, align="center",width=12, lg=4, xl=4), dbc.Col(ptf_table,  align="center", width=12, lg=8, xl=8)]),
               
              
            ]
        )
        
        
        return layout_pos
        
    

        
        

def create_ptf_chart(df):
     
        
    start_date = '2010-01-01'
    end_date = date.today() # was before: '2023-10-03'
    
   
    # get ytd index
    def get_ytd_index(df):
        cur_year = df.index.max().year
        n=1
        
        while df.index[-n].year==cur_year: 
            n = n+1
        return -n
    
    ytd_ind = get_ytd_index(df)
    
    yr1 = 255
    yr2 = 255*2
    yr5 = 255*4

    
    length = df.shape[0]# shape gets row and cols, rows are at index 0 of tuple

    fig = go.Figure()
    

    fig.add_trace(
        go.Scatter(x=list(df.index),
                   y=list(df.PTF_VAMI),
                    name="close",
                    line=dict(color="#2986CC")))


    #fig.update_yaxes(autorange=True)

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )


    #fig.update_yaxes(range=[0, 100])  # Adjust as per your data

    # fig.update_layout(
    # title={
    #     'text': 'My Plotly Figure Title',
    #     'y':0.9,
    #     'x':0.5,
    #     'xanchor': 'center',
    #     'yanchor': 'top'
    # }
    # )


    #fig.update_layout(title_text='Portfolio Chart')

    # fig.update_layout(
    #     template="plotly_dark",
    #     updatemenus=[
    #         dict(
    #             type="buttons",
    #             direction="right",
    #             x=0.2, #1.1
    #             y=1.2, #1.2
    #             bgcolor = '#AAAAAA',
    #             active = 99,
    #             bordercolor = '#FFFFFF',
    #             font = dict(size=11, color='#000000'),
    #             showactive=True,
    #             buttons=list(
    #                 [
    #                     dict(
    #                         label="Max",                            
    #                         method="update",
    #                         args=[{"y": [df["adjusted_close"]],"x":[df.index[-length:-1]]}],
    #                     ),
    #                     dict(
    #                         label="5 yrs",
    #                         method="update",
    #                         args=[{"y":[df.iloc[-yr5:-1,4]],"x":[df.index[-yr5:-1]]}],
    #                     ),
    #                     dict(
    #                         label="2 yrs",
    #                         method="update",
    #                         args=[{"y":[df.iloc[-yr2:-1,4]],"x":[df.index[-yr2:-1]]}],
    #                     ),
    #                     dict(
    #                         label="1 yr",
    #                         method="update",
    #                         args=[{"y":[df.iloc[-yr1:-1,4]],"x":[df.index[-yr1:-1]]}],
    #                     ),
    #                     dict(
    #                         label="1 month",
    #                         method="update",
    #                         args=[{"y":[df.iloc[-20:-1,4]],"x":[df.index[-20:-1]]}],
    #                     ),
    #                     dict(
    #                         label="YTD",
    #                         method="update",
    #                         args=[{"y": [df.iloc[ytd_ind:-1,4]],"x":[df.index[ytd_ind:-1]]}],
    #                     ),
    #                 ]
    #             ),
    #         )
    #     ]
    # )


    return fig
                
     
        
     
        