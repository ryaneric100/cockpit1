# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:11:07 2023

@author: DCHELD
"""
import pandas as pd



def get_current_allocation_from_df(df,cat):
 
    cat = 'POS_' + cat # e.g. POS_ASSET_CLASS, POS_SECTOR, POS_FX   
    
    asset_columns = [col for col in df.columns if col.startswith(cat)]
    df_asset_class = df[asset_columns]

    weight_columns = [col for col in df.columns if col.startswith('POS_WEIGHT')]
    df_weights = df[weight_columns] 

    # create dataframe with actual position allocation: 
    actual_weights = df_weights.iloc[-1]
    actual_asset_classes = df_asset_class.iloc[-1]

    # drop the indices first to create one dataframe: 
    actual_weights = actual_weights.reset_index(drop=True)
    actual_asset_classes = actual_asset_classes.reset_index(drop=True)
    
    
    # define colors here: 
    # color_dict = {
    #     'CASH':'#bcbcbc',
    #     'Equity':'#2986cc',
    #     'Gold': '#ffd966',
    #     'Bonds': '#6aa84f',
    #     'Commodity':'#bf9000'
        
    #     }
    
    
    # for key, value in asset_colors.items():  #accessing keys
    #     print(key,end=',')
    #     print(value,end=',')
        
       

    df_alloc = pd.DataFrame({'ASSET_CLASS': actual_asset_classes, 'WEIGHTS': actual_weights})
    # note: as_index = FALSE - otherwise group col gets index, not ideal to generate pie chart out of df
    df_alloc = df_alloc.groupby('ASSET_CLASS', as_index=False).sum() 
      
   
    # df_alloc['COLOR'] = df_alloc['ASSET_CLASS'].map(color_dict)
   
    
    return df_alloc
