import sqlite3
from pathlib import Path

# Path for better cross-platform compatibility
db_path = Path(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Training Session\SQL_Learning\Chinook_Sqlite.sqlite")

# Auto closing
with sqlite3.connect(db_path) as connection:
    cursor = connection.cursor()

    # Get table headers
    cursor.execute("SELECT * FROM Album LIMIT 10")
    headers = [description[0] for description in cursor.description]
    print(headers)

    # Fetching all data
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

for table in tables:
    print(table)
