# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:11:07 2023

@author: DCHELD
"""
import pandas as pd
import numpy as np


def get_historical_allocations_from_df(df, cat):
    
    cat = 'POS_' + cat # e.g. POS_ASSET_CLASS, POS_SECTOR, POS_FX
    
    asset_columns = [col for col in df.columns if col.startswith(cat)]
    df_asset_class = df[asset_columns]

    weight_columns = [col for col in df.columns if col.startswith('POS_WEIGHT')]
    df_weights = df[weight_columns] 


    # convert the dataframe df_asset_class that loos like that:
    # -----------------------------------------------------------------------------
    #
    # TIME - POS_ASSET_CLASS_1 - POS_ASSET_CLASS_2 ....
    #
    # to a new dataframe:
    #
    # TIME - Bonds - Cash - Commodities  - Equities ....
    #
    # where the weights forthe asset classes are aggregated.    
            
    # 1) get unique values of asset classes (sectors whatever)      
    # unique() can just be applied to one column of a dataframe - therefore one 
    # has to convert the dataframe first into an array (using np) to get the 
    # unique values of all columns    
    flattened_array = df_asset_class.values.ravel('K')
    unique_values = np.unique(flattened_array)

    # 2) now create a new dataframe with the unique values as the new columns
    # and take over the index for the time series
    # new_df = pd.DataFrame(columns=unique_values)
    df_converted = pd.DataFrame(index=df_asset_class.index, columns=unique_values)


    # 3) sum over the rows to get the aggregated weights
    for col in df_converted.columns:
        
        print(col)

        df_asset_class == col # select class 
        df_bool = df_asset_class == col # all entries with this asset class
        
        # to apply the booleans to the df_weights dataframe the name of the 
        # columns need to be the same so that .where() can be apllied
        df_weights.columns = df_asset_class.columns
        df_weights_select = df_weights.where(df_bool)
        
        # sum alonh rows, set axis = 1 for that
        df_sum = df_weights_select.sum(axis=1)
        
        # fill in the aggragted weight values into the empty dataframe
        df_converted[col] = df_sum
      
   
    return df_converted
