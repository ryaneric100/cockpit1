# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:41:00 2024

@author: DCHELD
"""



import pandas as pd

def calculate_return_since_entry(df):
    # Create a dictionary to store the return since entry for each ticker
    return_since_entry = {}

    # Iterate through each ticker
    for i in range(1, 6):
        pos_column = f'POS_TICKER_{i}'
        ret_column = f'POS_RET_{i}'

        # Drop rows where the position is NaN
        valid_entries = df[pos_column].dropna()

        # Identify when a new ticker enters the portfolio
        ticker_changes = valid_entries[valid_entries != valid_entries.shift()]

        # For each entry, calculate the cumulative return
        for date, ticker in ticker_changes.iteritems():
            # Select the return data from the entry date to the end
            returns = df.loc[date:, ret_column]

            # Calculate cumulative return
            cumulative_return = (returns + 1).cumprod() - 1

            # Store the final cumulative return in the dictionary
            return_since_entry[ticker] = cumulative_return.iloc[-1]

    return return_since_entry

# Example usage
# df = pd.read_csv('your_dataframe.csv')  # Load your dataframe
# returns = calculate_return_since_entry(df)
# print(returns)
