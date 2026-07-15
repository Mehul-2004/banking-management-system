from database.connection import get_connection , close_connection
from services.customers_service import (
    add_customer)

def test_connection():
    connection,cursor = get_connection()

    if connection:
        print("Database connected successfully")
    else:
        print("Failed")

    close_connection(connection,cursor)

if __name__ == "__main__":
    test_connection()

add_customer()    