# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:51:44 2024

@author: DCHELD
"""

import pandas as pd

def calculate_current_positions_return(df):
    return_since_recent_entry = {}
    entry_dates = {}

    # Identify all position and return columns
    pos_columns = [col for col in df.columns if col.startswith('POS_TICKER_')]
    ret_columns = [col for col in df.columns if col.startswith('POS_RET_')]

    # Ensure there's a corresponding return column for each position column
    assert len(pos_columns) == len(ret_columns), "The number of position and return columns does not match."

    # Identify current positions
    current_positions = df.iloc[-1][pos_columns]

    # Iterate through each current ticker
    for pos_column, ret_column in zip(pos_columns, ret_columns):
        current_ticker = current_positions[pos_column]

        if pd.notna(current_ticker):
            # Find the rows where this ticker was present and where it was absent
            ticker_present = df[pos_column] == current_ticker
            ticker_absent = df[pos_column] != current_ticker

            # Find the first occurrence of the ticker after its last absence
            last_absence = ticker_absent[::-1].idxmax()  # Searching backwards
            first_appearance_after_absence = ticker_present.loc[last_absence:].idxmax()
            
            # very cautious handling here - assuming there could be a gap after last absence to 
            # first appearance - normally just one day difference

            # Calculate cumulative return since the first appearance after the last absence
            returns_since_entry = df.loc[first_appearance_after_absence:, ret_column]
            cumulative_return = (returns_since_entry + 1).cumprod().iloc[-1] - 1

            # Store the cumulative return and the entry date
            return_since_recent_entry[current_ticker] = cumulative_return
            entry_dates[current_ticker] = first_appearance_after_absence

    return return_since_recent_entry, entry_dates


