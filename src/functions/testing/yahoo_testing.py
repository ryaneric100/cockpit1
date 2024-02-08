# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:47:09 2024

@author: DCHELD
"""
import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Fetch historical stock data
ticker = "DTLC.SW"  # Replace with your desired stock symbol
data = yf.download(ticker, start="2023-01-01", end="2024-01-11")

# Create a subplot
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                    vertical_spacing=0.03, 
                    subplot_titles=(ticker + ' Candlestick Chart', 'Volume'), 
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
fig.update_layout(title=ticker + ' Stock Candlestick Chart with Volume', 
                  xaxis_rangeslider_visible=False)
fig.show()




