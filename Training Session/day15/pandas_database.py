import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Training Session\SQL_Learning\Chinook_Sqlite.sqlite")

with sqlite3.connect(db_path) as connection:
    # Select 10 customer data
    query = """
    SELECT * FROM Customer LIMIT 10
    """

    customer_data = pd.read_sql_query(query, connection)

    # Group by BillingCountry
    query = """
    SELECT BillingCountry, SUM(Total) as Total FROM Invoice
    GROUP BY BillingCountry
    """

    total = pd.read_sql_query(query, connection)

    # Same as above but using pandas
    query = """
        SELECT *
        FROM Invoice
        """
    new_total = pd.read_sql_query(query, connection)

    new_total = new_total.groupby("BillingCountry")["Total"].sum().reset_index()

    # Writing to sql
    new_total.to_sql("GroupByCountry", connection, if_exists="replace", index=False)

    query = """
            SELECT *
            FROM GroupByCountry
            """
    data = pd.read_sql_query(query, connection)
print(data)
