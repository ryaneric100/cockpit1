# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:11:07 2023

@author: DCHELD
"""
import pandas as pd
import calendar



def get_seasonal_table_from_df(df,start_year):

    # seasonal table: 
    start_year = 2018
    # start / end 
    # handle data frame/series
    # input returns, not vami
    # different freqeuencies
    
    if type(df) == pd.DataFrame:    
        monthly_performance = df.PTF_VAMI.resample('ME').ffill().pct_change()   # changed M to ME
        #monthly_performance = df.adjusted_close.resample('M').ffill().pct_change()
        
    elif type(df) == pd.Series:
        monthly_performance = df.resample('ME').ffill().pct_change()  # changed M to ME
        
    
    monthly_performance = monthly_performance.to_frame('Performance')
    monthly_performance['Year'] = monthly_performance.index.to_series().dt.year
    monthly_performance['Month'] = monthly_performance.index.to_series().dt.month
    
    pivot_df = monthly_performance.pivot(index='Year', columns='Month', values='Performance')
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_names = list(calendar.month_abbr[1:]) # this gives month abbreviatons Jan, Feb, ...
    pivot_df.columns = month_names #[:pivot_df.shape[1]]
    
    
    if type(df) == pd.DataFrame:    
        yearly_performance = df.PTF_VAMI.resample('YE').ffill().pct_change().to_frame('YTD')    # changed A to YE
        #yearly_performance = df.adjusted_close.resample('A').ffill().pct_change().to_frame('Yearly_Performance')
    elif type(df) == pd.Series:
        yearly_performance = df.resample('YE').ffill().pct_change().to_frame('YTD')   # changed A to YE
    
    
    yearly_performance['Year'] = yearly_performance.index.year
    
    # Ensure the yearly_performance DataFrame has Year as a column
    yearly_performance.reset_index(drop=True, inplace=True)
    
    # Join the yearly performance with the monthly performance pivot table
    final_df = pivot_df.merge(yearly_performance, on='Year', how='left')
    final_df = final_df[final_df.Year > start_year]
    
    return final_df
