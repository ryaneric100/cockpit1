# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:11:07 2023

@author: DCHELD
"""
import pandas as pd
from functions.calculate_current_positions_return import  calculate_current_positions_return



def get_positions_from_df(df):
 
   position_columns = [col for col in df.columns if col.startswith('POS_TICKER')]
   df_positions = df[position_columns]

   weight_columns = [col for col in df.columns if col.startswith('POS_WEIGHT')]
   df_weights = df[weight_columns] 

   asset_columns = [col for col in df.columns if col.startswith('POS_ASSET_CLASS')]
   df_asset_class = df[asset_columns]

   isin_columns = [col for col in df.columns if col.startswith('POS_ISIN')]
   df_isin = df[isin_columns]

   etf_columns = [col for col in df.columns if col.startswith('POS_ETF')]
   df_etf = df[etf_columns]
   
   name_columns = [col for col in df.columns if col.startswith('POS_NAME')]
   df_name = df[name_columns]


   # create dataframe with actual position allocation: 
   actual_weights = df_weights.iloc[-1]
   actual_positions = df_positions.iloc[-1]
   actual_asset_classes = df_asset_class.iloc[-1]
   actual_isin = df_isin.iloc[-1] 
   actual_etf = df_etf.iloc[-1] 
   actual_name = df_name.iloc[-1] 

   # drop the indices first to create one dataframe: 
   actual_weights = actual_weights.reset_index(drop=True)
   actual_positions = actual_positions.reset_index(drop=True)
   actual_asset_classes = actual_asset_classes.reset_index(drop=True)
   actual_isin = actual_isin.reset_index(drop=True)
   actual_etf = actual_etf.reset_index(drop=True)
   actual_name = actual_name.reset_index(drop=True)
   

   df_positions = pd.DataFrame({'POSITIONS': actual_positions, 'WEIGHTS': actual_weights,'NAME': actual_name,
                                'ASSET_CLASS': actual_asset_classes,'TICKER': actual_etf,'ISIN': actual_isin})


   # get return since buy for the positions:   
   dict_ret, entry_dates = calculate_current_positions_return(df)       
   returns_series = pd.Series(dict_ret)
   returns_dates = pd.Series(entry_dates )
   df_positions['RETURN_BUY'] = df_positions['POSITIONS'].map(returns_series)
   df_positions['DATE_BUY'] = df_positions['POSITIONS'].map(returns_dates)
   df_positions['DATE_BUY'] = pd.to_datetime(df_positions['DATE_BUY']).dt.strftime('%Y-%m-%d') 
   


   #df_positions = pd.DataFrame({'POSITIONS': actual_positions, 'WEIGHTS': actual_weights,'ASSET_CLASS': actual_asset_classes})
   
   # note: as_index = FALSE - otherwise group col gets index, not ideal to generate pie chart out of df
   # df_positions  = df_alloc.groupby('POSITIONS', as_index=False).sum() 
      
   
   return df_positions
