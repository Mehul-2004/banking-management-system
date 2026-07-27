from database.connection import get_connection,close_connection
from services.customers_service import display_customer 
import mysql.connector

def display_transaction(transaction):

    print("\n" + "=" * 40 )
    print(f"Transaction ID  : {transaction[0]}")
    print(f"Account Number  : {transaction[1]}")
    print(f"Customer Name   : {transaction[2]} {transaction[3]}")
    print(f"Type            : {transaction[4]}")
    print(f"Amount          : {transaction[5]:.2f}")
    print(f"Description     : {transaction[6]}")
    print(f"Date            : {transaction[7]}")
    print("=" * 40)

def view_transactions():

    connection = None
    cursor = None

    try:
        connection,cursor = get_connection()

        if connection is None:
            print("\n" + "=" * 40)
            print("Database Connection Failure")
            print("=" * 40)
            return

        query = """
            select
                transactions.transaction_id,
                accounts.account_number,
                customers.first_name,
                customers.last_name,
                transactions.transaction_type,
                transactions.amount,
                transactions.description,
                transactions.transaction_date
            from transactions
            inner join accounts
            on transactions.account_id = accounts.account_id
            inner join customers
            on accounts.customer_id = customers.customer_id;"""

        cursor.execute(query,)
        trans = cursor.fetchall()

        if trans :
            for transaction in trans:
                display_transaction(transaction)
        else:
            print("no transactions")
            


    except mysql.connector.Error as e :
        print(f"Error : {e}")

    finally:
        close_connection(connection,cursor)
        