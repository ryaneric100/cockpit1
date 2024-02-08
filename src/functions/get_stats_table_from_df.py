# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:11:07 2023

@author: DCHELD
"""
import pandas as pd
import numpy as np


def get_stats_table_from_df(df):

 

    # PTF_VAMI
    
    # # Current date (or the latest date in your dataset)
    # current_date = df.index.max()
    
    # # Calculate the first value of the year and the month
    # first_of_year = df[df.index.year == current_date.year].iloc[0]['PTF_VAMI']
    # first_of_month = df[df.index.month == current_date.month].iloc[0]['PTF_VAMI']
    
    # # Latest value
    # latest_value = df.iloc[-1]['PTF_VAMI']
    
    # # Calculate YTD and MTD performance
    # ytd_performance = ((latest_value - first_of_year) / first_of_year) * 100
    # mtd_performance = ((latest_value - first_of_month) / first_of_month) * 100
    
    # # print(f"YTD Performance: {ytd_performance:.2f}%")
    # # print(f"MTD Performance: {mtd_performance:.2f}%")



    # # create a dummy dataframe: 
    
    # # initialize list of lists 
    # data = [['YTD', 10,4], ['MTD', 15, 10], ['Start', 14, 23]] 
      
    # # Create the pandas DataFrame 
    # stats_df = pd.DataFrame(data, columns=['Stat', 'Ptf', 'BMK']) 
      
   
# Assuming df is your DataFrame with 'price' column and datetime index

    # Calculate daily returns
    df['daily_returns'] = df['PTF_VAMI'].pct_change()
    
    # YTD Return
    ytd_return = df['PTF_VAMI'].loc[df.index.year == df.index.year.max()].iloc[-1] / df['PTF_VAMI'].loc[df.index.year == df.index.year.max()].iloc[0] - 1
    
    # MTD Return
    mtd_return = df['PTF_VAMI'].loc[df.index.month == df.index.month.max()].iloc[-1] / df['PTF_VAMI'].loc[df.index.month == df.index.month.max()].iloc[0] - 1
    
    # Return Since Start
    return_since_start = df['PTF_VAMI'].iloc[-1] / df['PTF_VAMI'].iloc[0] - 1
    
    # Volatility (Annualized)
    volatility = df['PTF_RET'].std() * np.sqrt(252)
    
    # Maximum Drawdown
    rolling_max = df['PTF_VAMI'].cummax()
    daily_drawdown = df['PTF_VAMI'] / rolling_max - 1.0
    max_drawdown = daily_drawdown.cummin().min()
    
    # Sharpe Ratio (Assuming risk-free rate is 0 for simplicity)
    sharpe_ratio = df['PTF_RET'].mean() / df['PTF_RET'].std() * np.sqrt(252)
    
    # Print the statistics
    print(f"YTD Return: {ytd_return:.2%}")
    print(f"MTD Return: {mtd_return:.2%}")
    print(f"Return Since Start: {return_since_start:.2%}")
    print(f"Annualized Volatility: {volatility:.2%}")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    
    
    # put figures in dataframe: 
    
    # create a dummy dataframe: 
    
    # initialize list of lists 
    data = [['YTD', ytd_return,ytd_return], ['MTD', mtd_return, mtd_return], 
            ['Start', return_since_start, return_since_start],
            ['Volatility', volatility, volatility],
            ['Draw-Down', max_drawdown, max_drawdown]] 
      
    # Create the pandas DataFrame 
    stats_df = pd.DataFrame(data, columns=['Stat', 'Ptf', 'BMK']) 

    
    return stats_df
