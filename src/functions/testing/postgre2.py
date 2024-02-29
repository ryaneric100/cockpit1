# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:26:33 2024

@author: DCHELD
"""

import psycopg2
from psycopg2 import OperationalError




def create_connection():
    try:
        connection = psycopg2.connect(
            host="dpg-cn2er8ol6cac739d1o7g-a.frankfurt-postgres.render.com",
            database="dufour_db",
            user="dufour_user",
            password="0vvXGsHfyzvYQLMHeMusJXkVKiMkG4AO",
            port="5432"  # Adjust if using a different port
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None

# Example usage
connection = create_connection()



#postgres://dufour_user:0vvXGsHfyzvYQLMHeMusJXkVKiMkG4AO@dpg-cn2er8ol6cac739d1o7g-a.frankfurt-postgres.render.com/dufour_db