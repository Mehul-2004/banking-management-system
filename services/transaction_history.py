from database.connection import get_connection,close_connection
from services.accounts_service import display_account,display_account
import mysql.connector
from utils.validators import(
    get_valid_amount,
    get_non_empty_string,
)

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

def search_transactions():
    connection = None
    cursor = None

    try:
        connection,cursor = get_connection()

        if connection is None:
            print("No database is Connected")
            return

        acc_num = int(input("Enter Account Number : "))

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
                on accounts.customer_id = customers.customer_id
                where accounts.account_number = %s    """

        cursor.execute(query,(acc_num,))
        transactions = cursor.fetchall()

        if transactions :
            for transaction in transactions:
                display_transaction(transaction)

        else:
            print("No transaction found")


    except mysql.connector.Error as e:
        print(f"Database Error : {e}")

    finally:
        close_connection(connection,cursor)

def block_account():
    connection = None
    cursor = None

    try:
        connection,cursor = get_connection()

        if connection is None:
            print("No database is connected")
            return

        account_number = int(input("Enter account number : "))

        account = display_account(cursor,account_number)

        if account is None:
            print("Account not found")
            return

        else:
            display_account(account)

        if account[6] == "Blocked":
            print("Account is already blocked")
            return

        confirm = input("Block this account (Y/N) : ")

        if confirm.upper() != "Y":
            print("Operation Cancelled")
            return

        query = """
                update accounts
                set status = 'Blocked'
                where account_number = %s
                """
        cursor.execute(query,(account_number,))

        connection.commit()

        print("\n" + "=" * 40)
        print("Account Blocked Successfully")
        print("=" * 40)

    except mysql.connector.Error as e:
        print(f"Dataase Error : {e}")

    finally:
        close_connection(connection,cursor)

def close_account():
    connection = None
    cursor = None

    try :
        connection,cursor = get_connection()

        if connection is None:
            print("No database connected")
            return
        account_number = int(input("Enter account number : "))

        account = display_account(cursor,account_number)

        if account is None:
            print("No account found")
            return
        else:
            display_account(account)

        if account[6] == 'Closed':
            print("Account is already Closed")
            return

        if account[5] > 0:
            print("Account cannot be closed while balance is greater than 0")
            return

        confirm = input("Close this account(Y/N) : ")

        if confirm.upper() != 'Y':
            print("Operation Cancelled")
            return

        query = """
            update accounts
            set status = 'Closed'
            where account_number = %s
            """
        cursor.execute(query,(account_number,))
        connection.commit()

        print("\n" + "=" * 40)
        print("Account Closed Successfully")
        print("=" * 40)

    except mysql.connector.Error as e:
        print(f"Database Error : {e}")

    finally:
        close_connection(connection,cursor)