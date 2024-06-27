# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:11:07 2023

@author: DCHELD
"""
import pandas as pd



def get_trades_from_df(df):
    
    position_columns = [col for col in df.columns if col.startswith('POS_TICKER')]
    df_positions = df[position_columns]
    
    # List to store all trades
    all_trades = []
    
    # Iterate through DataFrame
    for i in range(1, len(df_positions)):
        current_row = df_positions.iloc[i]
        previous_row = df_positions.iloc[i-1]
    
        # Check for entries and exits
        for position in current_row.index:
            # Entry
            if current_row[position] != previous_row[position]:
                all_trades.append({
                    'Date': current_row.name.strftime('%Y-%m-%d') ,
                    'Name of Position': current_row[position],
                    'Type of Trade': 'Enter'
                })
            
            # Exit
            if previous_row[position] != current_row[position] and pd.notna(previous_row[position]):
                all_trades.append({
                    'Date': current_row.name.strftime('%Y-%m-%d') ,
                    'Name of Position': previous_row[position],
                    'Type of Trade': 'Exit'
                })
    
    # Create a DataFrame from the list of trades
    trades_df = pd.DataFrame(all_trades)
      
    return trades_df


