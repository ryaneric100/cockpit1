# -*- coding: utf-8 -*-
"""
Created on June 2024

@author: Ryan Held 
"""


from dash import Input, Output, html, dcc, ALL
import pandas as pd
import dash_ag_grid as dag
import dash
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import datetime
import numpy as np
import yfinance as yf
from plotly.subplots import make_subplots
from functions.get_positions_from_df import get_positions_from_df


# for EOD data:
#------------------------------------------------------------------------------    
# import os
# from dotenv import load_dotenv
#import requests
#from eod import EodHistoricalData
# load_dotenv("C:\DATA\CLOUD\PROJECTS\COCKPIT_DASH\config.env")
# SQL_ENGINE  = os.getenv('SQL_ENGINE')
# API_KEY  = os.getenv('API_KEY')
#------------------------------------------------------------------------------


def positions(df):
        
    
        df_positions = get_positions_from_df(df)
    
        
        # definition of table: 
        #----------------------------------------------------------------------
        columnDefs = [
            {
                "headerName": "Ticker",
                "field": "POSITIONS",
            },
            {
                "headerName": "Name",
                "field": "NAME",
            },
   
            
            {
                "headerName": "ISIN",
                "field": "ISIN",
            },
            
            {
                "headerName": "Asset Class",
                "field": "ASSET_CLASS",
            },
            
            {
                "headerName": "Weight",
                "field": "WEIGHTS",
                "type": "leftAligned",
                "filter": "agNumberColumnFilter",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
            },
            
            {
                "headerName": "Bought",
                "field": "DATE_BUY",
                "type": "leftAligned",
               # "valueGetter": {"function": "d3.timeParse('%Y-%m-%d')(params.data.date)"},
               # "valueFormatter": {"function": "d3.timeFormat('%m/%d/%Y')(params.value)"},
            },
            
            
            {
                "headerName": "Return since buy",
                "field": "RETURN_BUY",
                "type": "leftAligned",
                "filter": "agNumberColumnFilter",
                "valueFormatter": {"function": "d3.format('.1%')(params.value)"},
            },
            
            
    
           
        ]
        
        
        
        position_table =  html.Div(
            [
                dag.AgGrid(
                  id="position_table",
                  #className="ag-theme-alpine-dark",
                  className="ag-theme-alpine",
                  columnDefs= columnDefs, #[{"headerName": i, "field": i, "cellRenderer": "markdown"} for i in df_positions.columns],
                  rowData=df_positions.to_dict("records"),
                  columnSize="sizeToFit",
                  #cellStyle=cellStyleTest,
                  dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single", "pagination": False,"paginationAutoPageSize":True},
                  # style = {"height": "800px", "width": "100%"},
                  csvExportParams={
                  "fileName": "portfolio_positions.csv",
                 },

              ),
                
                
            html.Div(
                html.Button("Download CSV", id="csv-button", n_clicks=0),
           ), 
            ])

        #----------------------------------------------------------------------
        # end definition of table
        


        
        radio_item = dcc.RadioItems(
            id='time-range-selector',
            options=[
                {'label': '1 Month', 'value': '1M'},
                {'label': '1 Year', 'value': '1Y'},
                {'label': '5 Years', 'value': '5Y'}
            ],
            value='1M',  # Default value
            labelStyle={'display': 'inline-block',  'margin-right': '20px'}  # Style for horizontal arrangement
        ),
 
  
    
        chart_item =  dcc.RadioItems(
           id='chart-type',
           options=[
           {'label': 'Candlestick Chart', 'value': 'candlestick'},
           {'label': 'Line Plot', 'value': 'line'},
           ],
           value='candlestick',  # Default value
           labelStyle={'display': 'inline-block',  'margin-right': '20px'}  # Style for horizontal arrangement
           ),
    
        
    
        # get tickers for download in yahoo (or EOD):
        #----------------------------------------------------------------------
        df_isin = df_positions[(df_positions.ISIN!='N') & (df_positions.ISIN!='no isin nr.')] 
        number_of_charts = df_isin.shape[0]
        isin_numbers = df_isin.ISIN.tolist() # for EOD
        
        df_bb_tickers = df_positions[(df_positions.TICKER!='CASH')] 
        number_of_charts = df_bb_tickers.shape[0]
        print(number_of_charts)
        bb_tickers = df_bb_tickers.TICKER.tolist()
        
        # convert to Yahoo tickers: 
        for i in range(len(bb_tickers)):
            
            bb_tickers[i] = bb_tickers[i].replace(" Equity", "")
            bb_tickers[i] = bb_tickers[i].replace(" ", ".")
            bb_tickers[i] = bb_tickers[i].replace("SE", "SW")
            bb_tickers[i] = bb_tickers[i].replace(".US", "")
            
            print(bb_tickers)
        #----------------------------------------------------------------------
    
    
        # define layout:  
        #----------------------------------------------------------------------
        
        layout_pos = html.Div(
            [
               dbc.Row([dbc.Col(position_table)]), 
               html.Hr(),
              # dbc.Row([dbc.Col(radio_item),dbc.Col(chart_item)]), 
              # dbc.Row(create_charts(number_of_charts,bb_tickers))
              # dbc.Row([dbc.Col(table)]) 
            ]
        )
                
        return layout_pos                 
    
    
    
    
# TESTING --------------------------------------------------------------------- 
    

# Function to create a row of charts
def create_chart_row(chart_ids):
    return html.Div(
        [dcc.Graph(id={'type': 'dynamic-graph', 'index': i}) for i in chart_ids],
        style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}
    )

# Creating rows of charts with 3 charts per row
def create_charts(number_of_charts, isin_numbers):
    rows = []
    for i in range(0, number_of_charts, 3):
        row_chart_ids = range(i, min(i + 3, number_of_charts))
        
        # test 
        #row_chart_ids = ['id1', 'id2','id3']
        #row_chart_ids = isin_numbers[list(row_chart_ids)]
        
        chart_ids = [isin_numbers[i] for i in row_chart_ids]
        
        rows.append(create_chart_row(chart_ids))
    return rows



# used for testing - random data points: 
def generate_sample_data(num_points=1000):
    now = datetime.datetime.now()
    end_date = now
    start_date = now - datetime.timedelta(days=1000)
    dates = pd.date_range(start=start_date, end=end_date, periods=num_points)

    # Generate random values
    values = np.random.rand(num_points) * 100  # Random values between 0 and 100

    return dates, values



# eod data - isin lookup for tickers:  
# def get_stock_data(isin):
    
#     start_date = '2020-01-01'
#     end_date = '2024-11-12'

#     print(isin)
    
#     url = 'https://eodhistoricaldata.com/api/search/{' + isin +'}?api_token=6161c40a1fd949.18608293'
#     response = requests.get(url)
#     response_json = response.json()
    
#     if response_json == []:
#         eod_ticker = 'NESN.SW'
        
#         # create empty df: 
#         date_range = pd.date_range(start=start_date, end=end_date)
#         df = pd.DataFrame(index=date_range)
#         df['open'] = 0
#         df['high'] = 0
#         df['low'] = 0
#         df['close'] = 0
#         df['adjusted_close'] = 0
#         df['volume'] = 0
        
        
#     else:
#        #print(response_json)
#        eod_ticker = response_json[0]['Code'] +'.'+ response_json[0]['Exchange']
        
#        print(API_KEY)
#        client = EodHistoricalData('6161c40a1fd949.18608293')
#        json_resp = client.get_prices_eod(eod_ticker, period = 'd', from_ = start_date, to = end_date, order = 'a')
#        df = pd.DataFrame(json_resp)
#        df = df.set_index('date')
#        df.index = pd.to_datetime(df.index) # <--- important to get datetime functions!
        
#     return df





# Callback to update all dynamic graphs
@dash.callback(
    Output({'type': 'dynamic-graph', 'index': ALL}, 'figure'),
    [Input('time-range-selector', 'value')],
    [Input('chart-type', 'value')],
    [Input({'type': 'dynamic-graph', 'index': ALL}, 'id')]
)
def update_graphs(time_range,chart_type, graph_ids):
    
    # graph_ids is a list of dictionaries in the form: 
    #     [{'type': 'dynamic-graph', 'index': 0}, {'type': 'dynamic-graph', 'index': 1}]
    
    figures = []
    
    
    for dictionary in graph_ids:
        index_value = dictionary['index']
        print("Index value:", index_value)

    
        #old: eod data
    
        # df_data = get_stock_data(index_value)
        # dates = df_data.index
        # values_close = df_data.adjusted_close
        # values_open = df_data.open
        # values_high = df_data.high
        # values_low = df_data.low
        # values_vol = df_data.volume
        #end_date = dates.max()
        # num_charts = len(graph_ids)
        
        now = datetime.datetime.now()
        end_date = now
        
        
        if time_range == '1M':
            start_date = end_date - datetime.timedelta(days=30)
        elif time_range == '1Y':
            start_date = end_date - datetime.timedelta(days=250)
        else:  # '5Y'
            start_date = end_date - datetime.timedelta(days=2500)
            
        
        ticker = index_value   # Replace with your desired stock symbol  "SPICHA.SW" 
        data = yf.download(ticker, start=start_date, end=end_date)
        
        
        
        # filtered_dates = dates[(dates >= start_date) & (dates <= end_date)]
        # filtered_values = values_close[(dates >= start_date) & (dates <= end_date)]
        # filtered_open = values_open[(dates >= start_date) & (dates <= end_date)]
        # filtered_high = values_high[(dates >= start_date) & (dates <= end_date)]
        # filtered_low = values_low[(dates >= start_date) & (dates <= end_date)]
        # filtered_vol = values_vol[(dates >= start_date) & (dates <= end_date)]


        if chart_type == 'line':

           # normal line plot ----------------------------------------------------    
            fig = go.Figure(data=[go.Scatter(x=data.index, y=data['Close'])])
            fig.update_layout(
                xaxis_range=[start_date, end_date],
                title = index_value
                )
            
            figures.append(fig)
           #   ----------------------------------------------------------------------
        else: # candlestick chart
        
            # Create a subplot
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                                vertical_spacing=0.03, 
                                #subplot_titles=(index_value, 'Volume'), 
                                row_width=[0.2, 0.7])
    
    
            # Add Candlestick plot
            fig.add_trace(go.Candlestick(x=data.index, 
                                         open=data['Open'], 
                                         high=data['High'], 
                                         low=data['Low'], 
                                         close=data['Close']),
                          row=1, col=1)
            
            # Add Volume Bar plot
            fig.add_trace(go.Bar(x=data.index, y=data['Volume'], marker_color='blue'),
                          row=2, col=1)
            
            # Update layout
            fig.update_layout(
                        xaxis_range=[start_date, end_date],
                        title=index_value, 
                              xaxis_rangeslider_visible=False
                              )
            
            figures.append(fig)



    return figures


    
    


@dash.callback(
  Output("position_table", "exportDataAsCsv"),
  Input("csv-button", "n_clicks"),
  )
def export_data_as_csv(n_clicks):
  if n_clicks:
    return True
   
     
   
  
    
  
    

# TESTING ---------------------------------------------------------------------






# @dash.callback(
#     Output("candlestick4", "figure"),
#     #Input("portfolio-grid3", "selectedRows"),
#     Input("position_table", "selectedRows"),
# )
# def update_candlestick(selected_row):
#     if selected_row is None:
#         ticker = "AAPL.US"
#     else:
#         ticker = selected_row[0]["TICKER"]
#         #ticker = selected_row[0]["TICKER_2"]
#         #company = selected_row[0]["company"]
#         #ticker = "AAPL.US"
#         #company = "Apple"
#         #ticker = "AAPL.US"
       
        
        
#     start_date = '2010-01-01'
#     end_date = date.today() # was before: '2023-10-03'
    
        

#     #dff_ticker_hist = stock_data[ticker].reset_index()
#     dff_ticker_hist = get_stock_data(ticker,start_date,end_date)
#     #dff_ticker_hist["date"] = pd.to_datetime(dff_ticker_hist["date"])
    
#     df = dff_ticker_hist
    
    
#     # get ytd index
#     def get_ytd_index(df):
#         cur_year = df.index.max().year
#         n=1
        
#         while df.index[-n].year==cur_year: 
#             n = n+1
#         return -n
    
#     ytd_ind = get_ytd_index(df)
    
#     yr1 = 255
#     yr2 = 255*2
#     yr5 = 255*4

    
#     length = df.shape[0]# shape gets row and cols, rows are at index 0 of tuple

#     fig = go.Figure()
    

#     fig.add_trace(
#         go.Scatter(x=list(df.index),
#                     y=list(df.adjusted_close),
#                     name="close",
#                     line=dict(color="#33CFA5")))


    
#     fig.update_xaxes(
#         rangeslider_visible=True,
#         rangeselector=dict(
#             buttons=list([
#                 dict(count=1, label="1m", step="month", stepmode="backward"),
#                 dict(count=6, label="6m", step="month", stepmode="backward"),
#                 dict(count=1, label="YTD", step="year", stepmode="todate"),
#                 dict(count=1, label="1y", step="year", stepmode="backward"),
#                 dict(step="all")
#             ])
#         )
#     )
    
    
    
#     # fig.update_layout(
#     #     #template="plotly_dark",
#     #     updatemenus=[
#     #         dict(
#     #             type="buttons",
#     #             direction="right",
#     #             x=0.3, #1.1
#     #             y=1.2, #1.2
#     #             bgcolor = '#AAAAAA',
#     #             active = 99,
#     #             bordercolor = '#FFFFFF',
#     #             font = dict(size=11, color='#000000'),
#     #             showactive=True,
#     #             buttons=list(
#     #                 [
#     #                     dict(
#     #                         label="Max",
#     #                         method="update",
#     #                         args=[{"y": [df["adjusted_close"]],"x":[df.index[-length:-1]]}],
#     #                     ),
#     #                     dict(
#     #                         label="5 yrs",
#     #                         method="update",
#     #                         args=[{"y":[df.iloc[-yr5:-1,4]],"x":[df.index[-yr5:-1]]}],
#     #                     ),
#     #                     dict(
#     #                         label="2 yrs",
#     #                         method="update",
#     #                         args=[{"y":[df.iloc[-yr2:-1,4]],"x":[df.index[-yr2:-1]]}],
#     #                     ),
#     #                     dict(
#     #                         label="1 yrs",
#     #                         method="update",
#     #                         args=[{"y":[df.iloc[-yr1:-1,4]],"x":[df.index[-yr1:-1]]}],
#     #                     ),
#     #                     dict(
#     #                         label="1 month",
#     #                         method="update",
#     #                         args=[{"y":[df.iloc[-20:-1,4]],"x":[df.index[-20:-1]]}],
#     #                     ),
#     #                     dict(
#     #                         label="YTD",
#     #                         method="update",
#     #                         args=[{"y": [df.iloc[ytd_ind:-1,4]],"x":[df.index[ytd_ind:-1]]}],
#     #                     ),
#     #                 ]
#     #             ),
#     #         )
#     #     ]
#     # )


#     return fig
        

        
     
        