# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:41:30 2024

@author: DCHELD
"""


import pandas as pd
from sqlalchemy import create_engine

import plotly.express as px

# Format: postgresql://user:password@host:port/database
database_url = "postgresql://dufour_user:0vvXGsHfyzvYQLMHeMusJXkVKiMkG4AO@dpg-cn2er8ol6cac739d1o7g-a.frankfurt-postgres.render.com/dufour_db"
engine = create_engine(database_url)

# had to adjust the url
#postgres://dufour_user:0vvXGs .....
#
# to postgresql://dufour_user:0vvXGsH .....



# Sample data
data = {
    'Name': ['John Doe', 'Jane Doe', 'Mike Smith'],
    'Age': [28, 34, 23],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print("df before")
print(df)



df.to_sql('table_name', engine, index=False, if_exists='replace')  # 'replace' or 'append'



# Using a SQL query
df = pd.read_sql("SELECT * FROM table_name", engine)

# Or to read the entire table
df = pd.read_sql_table('table_name', engine)

print("df read out")
print(df)


# Or to read the entire table
df2 = pd.read_sql_table('dc_rs_short_ptf', engine)
df2 = df2.sort_values(by=['time'])

print("people read out")
print(df2)


fig = px.line(df2, x='time', y='ptf_vami', title='Value Over Time', markers=True)
fig.show()



