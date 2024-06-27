# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:41:30 2024

@author: DCHELD
"""



import psycopg2

def update_value_postgre(value,row,col):
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
        # query = """
        # UPDATE overview_table_cockpit_dash
        # SET ytd = %s
        # WHERE url = %s;
        # """
        
        query = """
        UPDATE overview_table_cockpit_dash
        SET {col} = %s
        WHERE url = %s;
        """
        
        query = query.format(col="ytd")
        
        
        # The data tuple to pass to the query parameters
        data = (value, row)
        
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



update_value_postgre(1000, "/dc_rs_short_ptf","ytd")
 



