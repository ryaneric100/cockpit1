# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:11:07 2023

@author: DCHELD
"""

# from functions.sql.get_main_portfolio_df import  get_main_portfolio_df
# from functions.get_seasonal_table_from_df import  get_seasonal_table_from_df
# from functions.get_stats_table_from_df import  get_stats_table_from_df
# from functions.get_current_allocation_from_df import  get_current_allocation_from_df
# from functions.get_positions_from_df import get_positions_from_df


from functions.sql.get_main_portfolio_df import  get_main_portfolio_df
from functions.get_seasonal_table_from_df import  get_seasonal_table_from_df
from functions.get_stats_table_from_df import  get_stats_table_from_df
from functions.get_current_allocation_from_df import  get_current_allocation_from_df
from functions.get_positions_from_df import get_positions_from_df
from functions.get_historical_allocations_from_df import  get_historical_allocations_from_df
from functions.get_trades_from_df import  get_trades_from_df
from functions.get_contributions_from_df import  get_contributions_from_df

from functions.calculate_return_since_entry import  calculate_return_since_entry
from functions.calculate_current_positions_return import  calculate_current_positions_return

# testing 
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import datetime as dt
from datetime import date



df = get_main_portfolio_df('dc_protect')
df_seasonal = get_seasonal_table_from_df(df,2020)
df_stats = get_stats_table_from_df(df)
df_alloc = get_current_allocation_from_df(df,'ASSET_CLASS')
df_positions = get_positions_from_df(df)
df_alloc_historical = get_historical_allocations_from_df(df,'ASSET_CLASS')
df_trades = get_trades_from_df(df)
#df_contribution = get_contributions_from_df(df,'ASSET_CLASS')
df_contribution = get_contributions_from_df(df,'TICKER','1M')


df = get_main_portfolio_df('dc_ai_ptf')

return_since_recent_entry, entry_dates = calculate_current_positions_return(df)






df_prices = df['PTF_VAMI']











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







df_alloc = get_current_allocation_from_df(df,'FX')

df_alloc_hist = get_historical_allocations_from_df(df,'SECTOR')






























colors = ['blue', '#FF5733', 'rgb(0,255,0)', 'rgba(255,0,255,0.5)']


fig = px.bar(x=df_contribution.values, y=df_contribution.index, orientation='h', color=df_contribution.index)
fig.show()


fig = px.bar(x=df_contribution.values, y=df_contribution.index, orientation='h', color=df_contribution.index, color_discrete_map=dict(zip(df_contribution.index, colors)))
fig.show()



end_date = date.today()







































# Calculate the contribution of each asset class and currency
# Assuming you have daily returns for each position in columns like 'POS_RET_1', 'POS_RET_2', etc.
# and weights in columns like 'POS_WEIGHT_1', 'POS_WEIGHT_2', etc.
# Calculate weighted returns for each position

#cat = 'POS_' + cat # e.g. POS_ASSET_CLASS, POS_SECTOR, POS_FX
cat = 'POS_ASSET_CLASS'
asset_columns = [col for col in df.columns if col.startswith(cat)]
l = len(asset_columns)


for i in range(1, l+1):  # Adjust the range based on the number of positions
    df[f'POS_WEIGHTED_RET_{i}'] = df[f'POS_RET_{i}'] * df[f'POS_WEIGHT_{i}']


# asset_columns = [col for col in df.columns if col.startswith(cat)]
# df_asset_class = df[asset_columns]

# weighted_ret_columns = [col for col in df.columns if col.startswith('POS_WEIGHTED_RET')]
# df_weighted_ret = df[weighted_ret_columns] 



start_date = '2021-01-01'
end_date = '2021-03-31'

# Filter data for the specific time period
df = df[(df.index >= start_date)]  # & (test5.index <= end_date)
# df_weighted_ret = df_weighted_ret[(df_weighted_ret.index >= start_date)]  # & (test5.index <= end_date)
# df_asset_class = df_asset_class[(df_asset_class.index >= start_date)]  # & (test5.index <= end_date)   



# flattened_array = df_asset_class.values.ravel('K')
# unique_values = np.unique(flattened_array)





# get equity returns for all positions: 
#------------------------------------------------------------------------------

# for asset_class in unique_values: 

#     df_bools = (df_asset_class == 'Equity').astype(bool)
#     #df_bools = (df_asset_class == asset_class).astype(bool)
    
#     #df_bools = (df_asset_class == 'CASH').astype(bool)
    
#     # the approach with mask did not work - tried out everything...! 
#     #df_bools = df_asset_class == 'Equity'
#     #df_weighted_ret = df_weighted_ret.mask(df_bools, other = 110)
    
#     # workaround:
#     df_bools = df_bools.mask(df_bools==True,1).astype(float)
#     df_bools = df_bools.mask(df_bools==False,0).astype(float)
    
#     df_weighted_ret_copy = df_weighted_ret.copy()
    
#     for i in range(1, l+1):  # Adjust the range based on the number of positions
#         df_weighted_ret_copy[f'POS_WEIGHTED_RET_{i}'] = df_weighted_ret_copy[f'POS_WEIGHTED_RET_{i}'] * df_bools[f'POS_ASSET_CLASS_{i}']
    
#     # sum over positions: 
#     sum_weighted_ret = df_weighted_ret_copy.sum(axis = 1)
    
#     # Calculate cumulative return
#     cumulative_return = (1 + sum_weighted_ret).prod() - 1
    
#     print(cumulative_return)
    

# # Calculate cumulative return ptf
# cumulative_return_ptf = (1 + df.PTF_RET).prod() - 1


#------------------------------------------------------------------------------
# Assuming df is your original DataFrame
# Initialize an empty DataFrame to hold aggregated returns
unique_asset_classes = pd.unique(df[[f'POS_ASSET_CLASS_{i}' for i in range(1, 6)]].values.ravel())
asset_class_returns = pd.DataFrame(0, index=df.index, columns=unique_asset_classes).astype(float)

# Aggregate weighted returns by asset class
for i in range(1, l+1):
    for index, row in df.iterrows():
        asset_class = row[f'POS_ASSET_CLASS_{i}']
        weighted_ret = row[f'POS_WEIGHTED_RET_{i}']
        asset_class_returns.at[index, asset_class] += weighted_ret

# Now, asset_class_returns has the daily aggregated returns for each asset class
# Calculate cumulative return
#cumulative_return = (1 + asset_class_returns.Equity).prod() - 1
#cumulative_return = (1 + asset_class_returns.Bonds).prod() - 1


# get cumulative returns for asset classes: 
normalized_returns = pd.DataFrame([0] * 6).T.astype(float)
normalized_returns.columns = unique_asset_classes

for asset_class in unique_asset_classes: 
    normalized_returns[asset_class] = (1 +  asset_class_returns[asset_class]).prod() - 1    
    print(normalized_returns )



# normalize returns: 
#------------------------------------------------------------------------------
cumulative_return_ptf = (1 + df.PTF_RET).prod() - 1
#cumulative_return_ptf = (1 + df.PTF_RET).cumprod() 


ret_sum = normalized_returns.sum(axis=1)
normalized_returns = normalized_returns.loc[0]/ret_sum[0] 
#normalized_returns = normalized_returns.loc[0]/ret_sum[0] * cumulative_return_ptf





























# test for trades out of df: 
#------------------------------------------------------------------------------

# Example DataFrame (replace with your data)
# data = {
#     'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
#     'Stock_A': [10, 10, 15, 15, 20],
#     'Stock_B': [5, 10, 10, 5, 5]
# }
# df = pd.DataFrame(data).set_index('Date')

# # Calculate the differences (trades)



# # Function to detect changes
# def detect_changes(series):
#     return series != series.shift(1)

# # Apply the function to the DataFrame
# changes = df_positions.apply(detect_changes)

# # Filter to get only the rows where changes occurred
# changes_df = df_positions[changes]

# # Drop rows with no changes (all NaNs)
# changes_df = changes_df.dropna(how='all')

# print(changes_df)



position_columns = [col for col in df.columns if col.startswith('POS_TICKER')]
df_positions = df[position_columns]



# Function to compare rows and find entered/exited positions
def find_changes(row, prev_row):
    entered = row[row != prev_row].dropna()
    exited = prev_row[prev_row != row].dropna()
    return entered, exited

# List to store changes
changes = []

# Iterate through DataFrame
for i in range(1, len(df_positions)):
    entered, exited = find_changes(df_positions.iloc[i], df_positions.iloc[i-1])
    if entered.any() or exited.any():  # Check if there is any change
        changes.append({'Date': df_positions.index[i], 'Entered': entered.to_dict(), 'Exited': exited.to_dict()})

# Create a DataFrame of changes
changes_df = pd.DataFrame(changes).set_index('Date')

print(changes_df)




# # Prepare a list to hold the reshaped data
# reshaped_data = []

# # Iterate over the rows in changes_df
# for date, row in changes_df.iterrows():
#     # Process entered positions
#     for position in row['Entered']:
#         reshaped_data.append({'Date': date, 'Name of Position': position, 'Type of Trade': 'Enter'})

#     # Process exited positions
#     for position in row['Exited']:
#         reshaped_data.append({'Date': date, 'Name of Position': position, 'Type of Trade': 'Exit'})

# # Create a new DataFrame from the reshaped data
# trades_df = pd.DataFrame(reshaped_data)

# print(trades_df)




# Prepare a list to hold the reshaped data
reshaped_data = []

# Iterate over the rows in changes_df
for date, row in changes_df.iterrows():
    # Process entered positions
    for position, name in row['Entered'].items():
        reshaped_data.append({'Date': date, 'Name of Position': name, 'Type of Trade': 'Enter'})

    # Process exited positions
    for position, name in row['Exited'].items():
        reshaped_data.append({'Date': date, 'Name of Position': name, 'Type of Trade': 'Exit'})

# Create a new DataFrame from the reshaped data
trades_df = pd.DataFrame(reshaped_data)

print(trades_df)












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
                'Date': current_row.name,
                'Name of Position': current_row[position],
                'Type of Trade': 'Enter'
            })
        
        # Exit
        if previous_row[position] != current_row[position] and pd.notna(previous_row[position]):
            all_trades.append({
                'Date': current_row.name,
                'Name of Position': previous_row[position],
                'Type of Trade': 'Exit'
            })

# Create a DataFrame from the list of trades
trades_df = pd.DataFrame(all_trades)

print(trades_df)











# test historical allocations: 
#------------------------------------------------------------------------------
asset_columns = [col for col in df.columns if col.startswith('POS_ASSET_CLASS')]
df_asset_class = df[asset_columns]

weight_columns = [col for col in df.columns if col.startswith('POS_WEIGHT')]
df_weights = df[weight_columns] 

# create dataframe with actual position allocation: 
actual_weights = df_weights.iloc[-1]
actual_asset_classes = df_asset_class.iloc[-1]

# drop the indices first to create one dataframe: 
actual_weights = actual_weights.reset_index(drop=True)
actual_asset_classes = actual_asset_classes.reset_index(drop=True)

df_alloc = pd.DataFrame({'ASSET_CLASS': actual_asset_classes, 'WEIGHTS': actual_weights})
# note: as_index = FALSE - otherwise group col gets index, not ideal to generate pie chart out of df
df_alloc = df_alloc.groupby('ASSET_CLASS', as_index=False).sum() 


    

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




# {'POS_WEIGHT_1','POS_WEIGHT_2'}
fig = px.area(df_converted, x=df_weights.index, y=df_converted.columns, 
              title='Area Chart for')
fig.update_yaxes(range=[0, 1])  # Set the range for y-axis
fig.show()









line_color_dict = {
    'Bonds': '#1f77b4',
    'CASH': '#ff7f0e',
    'Commodity': '#ff7f0e',
    'Equity': '#8c564b',
    'Real_Estate': '#9467bd'
    }

# Create a figure
fig = go.Figure()

# Loop through each column (except for the x-axis column)
for col in df_converted.columns:  # Assuming the first column is for the x-axis
    fig.add_trace(
        go.Scatter(
            y=df_converted[col],
            x=df_converted.index,
            fill='tonexty',
            # Customize your trace here (e.g., name, mode, line properties)
            name=col,
            stackgroup='one',
            line=dict(width=0,color=line_color_dict.get(col, None)),
            #mode = 'none'
        )
    )

# Customize the layout
fig.update_layout(
    title="Dynamic Area Chart",
    xaxis_title="X Axis",
    yaxis_title="Y Axis",
    yaxis_range=(0, 1)
)

# Show the plot
fig.show()





# string test 

cat = 'FX'

cat = 'POS_' + cat








# test position tables: 
#------------------------------------------------------------------------------

# position_columns = [col for col in df.columns if col.startswith('POS_TICKER')]
# df_positions = df[position_columns]

# weight_columns = [col for col in df.columns if col.startswith('POS_WEIGHT')]
# df_weights = df[weight_columns] 

# asset_columns = [col for col in df.columns if col.startswith('POS_ASSET_CLASS')]
# df_asset_class = df[asset_columns]


# # create dataframe with actual position allocation: 
# actual_weights = df_weights.iloc[-1]
# actual_positions = df_positions.iloc[-1]
# actual_asset_classes = df_asset_class.iloc[-1]
 

# # drop the indices first to create one dataframe: 
# actual_weights = actual_weights.reset_index(drop=True)
# actual_positions = actual_positions.reset_index(drop=True)
# actual_asset_classes = actual_asset_classes.reset_index(drop=True)

# test = actual_asset_classes.copy()
# test[:] = 'LYTNOW.SW'


# df_positions = pd.DataFrame({'POSITIONS': actual_positions, 'WEIGHTS': actual_weights,'ASSET_CLASS': actual_asset_classes,'TICKER': test})
# # note: as_index = FALSE - otherwise group col gets index, not ideal to generate pie chart out of df
# # df_positions  = df_alloc.groupby('POSITIONS', as_index=False).sum() 



    #df = get_data()
    
    # Filter DataFrame based on selected category
    #filtered_df = df[df['Category'] == selected_category]



