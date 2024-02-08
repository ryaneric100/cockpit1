# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:11:07 2023

@author: DCHELD
"""
import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


def get_contributions_from_df(df,cat,period):
    
    current_date = datetime.now().date()
   
    one_year_before = current_date - relativedelta(years=1)
    one_month_before = current_date - relativedelta(months=1)
    three_months_ago = current_date - relativedelta(months=3)
    
    current_year = datetime.now().year
    start_of_year = date(current_year, 1, 1)


    print("One year before:", one_year_before.strftime('%Y-%m-%d'))
    print("One month before:", one_month_before.strftime('%Y-%m-%d'))
    
    if period == '1Y':
        start_date = datetime(one_year_before.year, one_year_before.month, one_year_before.day)
    elif period == '1M':
        start_date = datetime(one_month_before.year, one_month_before.month, one_month_before.day)
    elif period == '3M':
        start_date = datetime(three_months_ago.year, three_months_ago.month, three_months_ago.day)
    elif period == 'YTD':
        start_date = datetime(start_of_year.year, start_of_year.month, start_of_year.day)
        
    #start_date = '2021-03-31'

    # filter data for the specific time period
    df = df[(df.index >= start_date)]  # & (test5.index <= end_date)
   
    cat = 'POS_' + cat # e.g. POS_ASSET_CLASS, POS_SECTOR, POS_FX
    
    #cat = 'POS_ASSET_CLASS'
    #cat = 'POS_SECTOR'
    #cat = 'POS_TICKER'
    asset_columns = [col for col in df.columns if col.startswith(cat)]
    l = len(asset_columns)
    n = l+1
    
    
    # resolve the warning while creating new columns, you can ensure that df
    # is not a view but a standalone DataFrame. This can be done by making 
    # a copy of the DataFrame
    df = df.copy()

    for i in range(1, l+1):  # Adjust the range based on the number of positions
        df[f'POS_WEIGHTED_RET_{i}'] = df[f'POS_RET_{i}'] * df[f'POS_WEIGHT_{i}']

 
    # Initialize an empty DataFrame to hold aggregated returns
    #
    #  index (time) ¦ Equity  ¦ Commodity  ¦ Gold ¦ ...
    #                 --------- returns ----         
    
    
    unique_asset_classes = pd.unique(df[[f'{cat}_{i}' for i in range(1, n)]].values.ravel())
    asset_class_returns = pd.DataFrame(0, index=df.index, columns=unique_asset_classes).astype(float)
    
    # Aggregate weighted returns by asset class
    for i in range(1, l+1):
        for index, row in df.iterrows():
            #asset_class = row[f'POS_ASSET_CLASS_{i}']
            asset_class = row[f'{cat}_{i}']
            weighted_ret = row[f'POS_WEIGHTED_RET_{i}']
            asset_class_returns.at[index, asset_class] += weighted_ret
    
    
    # get cumulative returns for asset classes in df: 
    # 
    #  Equtiy      0.213
    #  Commodity   0.12 
    
    n_classes = unique_asset_classes.size

    normalized_returns = pd.DataFrame([0] *n_classes).T.astype(float)
    normalized_returns.columns = unique_asset_classes
    
    for asset_class in unique_asset_classes: 
        normalized_returns[asset_class] = (1 +  asset_class_returns[asset_class]).prod() - 1    
        print(normalized_returns )
    
    
    
    # normalize returns: 
    #------------------------------------------------------------------------------
    #cumulative_return_ptf = (1 + df.PTF_RET).prod() - 1
    #cumulative_return_ptf = (1 + df.PTF_RET).cumprod() 
        
    ret_sum = normalized_returns.sum(axis=1)
    normalized_returns = normalized_returns.loc[0]/ret_sum[0] 
    #normalized_returns = normalized_returns.loc[0]/ret_sum[0] * cumulative_return_ptf
    
    
    contribution_df = normalized_returns

      
    return contribution_df


