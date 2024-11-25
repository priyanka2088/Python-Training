import sqlite3
from pathlib import Path

db_path = Path(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Training Session\SQL_Learning\Chinook_Sqlite.sqlite")

new_customer = (123, "Ken", "Adams", "UST", "ken.adams@ust", "USA")

try:
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        # Create
        cursor.execute(
            """
            INSERT INTO Customer(CustomerId, FirstName, LastName, Company, Email, Country)
            VALUES(?, ?, ?, ?, ?, ?)
            """, new_customer
        )
        print("New customer added.")

        # Update
        new_email = "ken.adams@tcs"
        new_company = "tcs"
        customer_id = 123

        cursor.execute(
            """
            UPDATE Customer
            SET Email = ?, Company = ?
            WHERE CustomerId = ?
            """, (new_email, new_company, customer_id)
        )
        print("Data updated.")

        # Delete
        cursor.execute(
            """
            DELETE FROM Customer
            WHERE CustomerId = 123
            """
        )
        print("Data deleted.")

        # Read
        cursor.execute(
            """
            SELECT * FROM Customer
            WHERE CustomerId = 123
            """
        )
        customer = cursor.fetchall()
        for row in customer:
            print(row)

except sqlite3.Error as e:
    print("Error!")
