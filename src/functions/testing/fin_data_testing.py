# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:08:38 2023

@author: DCHELD
"""

import pandas as pd
import yfinance as yf



equities = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "AMZN": "Amazon",
    "GOOGL": "Alphabet",
    "TSLA": "Tesla",
    "BRK-B": "Berkshire Hathaway",
    "UNH": "United Health Group",
    "JNJ": "Johnson & Johnson",
}


def get_stock_data():
    return yf.download(tickers=list(equities.keys()), period="5y", group_by="ticker")


stock_data = get_stock_data()

ticker = 'MSFT'

dff_ticker_hist = stock_data[ticker].reset_index()
dff_ticker_hist["Date"] = pd.to_datetime(dff_ticker_hist["Date"])