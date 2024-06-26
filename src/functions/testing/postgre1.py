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




import psycopg2

def update_table():
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(
            dbname="dufour_db",
            user="dufour_user",
            password="0vvXGsHfyzvYQLMHeMusJXkVKiMkG4AO",
            host="dpg-cn2er8ol6cac739d1o7g-a.frankfurt-postgres.render.com",
            port="5432"
        )
        
        

        # Open a cursor to perform database operations
        cur = conn.cursor()
        
        # The SQL UPDATE query. Be sure to adjust table_name, column_to_update, new_value,
        # condition_column, and condition_value to fit your needs.
        query = """
        UPDATE overview_table_cockpit_dash
        SET ytd = %s
        WHERE url = %s;
        """
        
        # The data tuple to pass to the query parameters
        data = (24424, "/dc_rs_short_ptf")
        
        # Execute the query
        cur.execute(query, data)
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and the connection
        cur.close()
        conn.close()
        
        print("Update successful")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
update_table()





