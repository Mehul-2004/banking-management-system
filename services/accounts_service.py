from database.connection import get_connection,close_connection
from services.customers_service import display_customer ,get_customer
import mysql.connector
from utils.validators import (
    get_valid_amount,
    get_non_empty_string,
)

def get_account(cursor,account_number):
    """
    Fetch a single account using its account number.
    """

    query = """
        Select
            accounts.account_id,
            accounts.account_number,
            customers.first_name,
            customers.last_name,
            accounts.account_type,
            accounts.balance,
            accounts.status
        from accounts
        inner join customers
        on accounts.customer_id = customers.customer_id
        where accounts.account_number = %s
            """

    cursor.execute(query,(account_number,))
    return cursor.fetchone()

def create_account():

    connection = None
    cursor = None

    try:
        connection,cursor = get_connection()
    
        if connection is None:
            print("No database is connected")
            return

        customer_id = int(input("Enter Customer id : "))
        customer = get_customer(cursor,customer_id)

        if customer :
            display_customer(customer)

        else:
            print("No customer found")
            return
        
        print("Choose Account Type")
        print("\n" + "=" * 40)
        print("1. Savings")
        print("2. Current")

        acc = input("Account Type (S/C) : ")

        if acc.upper() == "S":
            account_type = "Savings"
        elif acc.upper() == "C":
            account_type = "Current"

        else:
            print("Invalid Account type")
            return
        
        account_number = generate_account_number(cursor)
        query = """
            Insert into accounts(
            customer_id,
            account_number,
            account_type)
            values(%s,%s,%s)"""

        values = (
            customer_id,
            account_number,
            account_type
        )

        cursor.execute(query,values)

        connection.commit()

        print("\n" + "=" * 40)
        print("Account Created Successfully")
        print("=" * 40)
        print(f"Customer ID    : {customer_id}")
        print(f"Account Number : {account_number}")
        print(f"Account Type   : {account_type}")
        print(f"Balance        : 0.00")
        print(f"Status         : Active")
        print("=" * 40)

    except mysql.connector.Error as e:
        print(f"Error : {e}")

    finally:
        close_connection(connection,cursor)

def generate_account_number(cursor):

    query = "select max(account_number) from accounts"

    cursor.execute(query,)

    account = cursor.fetchone()

    if account[0] is None:
        account_number = 1000000001
    else:
        account_number = account[0] + 1 
    return account_number


def view_account():

    connection = None
    cursor = None

    try:
        connection,cursor = get_connection()

        if connection is None:
            print("No Database Connected ")
            return
        
        query = """
            Select 
                accounts.account_number,
                customers.first_name,
                customers.last_name,
                accounts.account_type,
                accounts.balance,
                accounts.status
            from accounts
            inner join customers on 
            accounts.customer_id = customers.customer_id;
                """
        
        cursor.execute(query,)

        accounts = cursor.fetchall()

        for account in accounts:
            display_account(account)

    except mysql.connector.Error as e:
        print(f"Error : {e}")
    
    finally:
        close_connection(connection,cursor)

def display_account(account):
    print("\n" + "=" * 40)
    print(f"Account Number : {account[1]}")
    print(f"Customer Name  : {account[2]} {account[3]}")
    print(f"Account Type   : {account[4]}")
    print(f"Balance        : {account[5]}")
    print(f"Status         : {account[6]}")


def search_account():
    connection = None
    cursor = None

    try:
        connection,cursor = get_connection()

        if connection is None:
            print("No database connected")
            return
        
        account_number = int(input("Enter Account Number : "))

        # query = """
        #     Select 
        #         accounts.account_number,
        #         customers.first_name,
        #         customers.last_name,
        #         accounts.account_type,
        #         accounts.balance,
        #         accounts.status
        #     from accounts
        #     inner join customers on 
        #     accounts.customer_id = customers.customer_id
        #     where accounts.account_number = %s;
        #         """
        
        # cursor.execute(query,(account_number,))

        # account = cursor.fetchone()
        account = get_account(cursor,account_number)

        if account:
            display_account(account)
        else:
            print("Account Not Found")
            return
        
    except mysql.connector.Error as e :
        print(f"Error : {e}")
    
    finally:
        close_connection(connection,cursor)

def deposit_money():

    connection = None
    cursor = None

    try:
        connection , cursor = get_connection()

        if connection is None:
            print("No Database Connected")
            return
        
        account_number = int(input("Enter Account Number : "))

        account = get_account(cursor,account_number)

        if account :
            display_account(account)
        
        else:
            print("Account Not Found")
            return
        
        dep_amt = get_valid_amount("Enter amount to Deposit : ")

        if dep_amt <= 0:
            print("Deposit amount must be greater than 0")
            return
        
        query = """
            update accounts
            set balance = balance + %s
            where account_number = %s"""
        
        cursor.execute(query,(dep_amt,account_number))
        
        query = """
            Insert into transactions(
                account_id,
                transaction_type,
                amount,
                description
                )
                values(%s,%s,%s,%s)"""
        
        values = (
            account[0],
            "Deposit",
            dep_amt,
            "Cash Deposit"
        )

        cursor.execute(query,values)

        connection.commit()
        print("\n" + "=" * 40)
        print("Deposit Successful")
        print(f"Account Number : {account_number}")
        print(f"Amount Deposited : ₹{dep_amt:.2f}")
        print("=" * 40)

    except mysql.connector.Error as e:
        print(f"Error : {e}")
    
    finally:
        close_connection(connection,cursor)

def withdraw_money():

    connection = None
    cursor = None

    try:
        connection , cursor = get_connection()

        if connection is None:
            print("No Database Connected")
            return
        
        account_number = int(input("Enter Account Number : "))

        account = get_account(cursor,account_number)

        if account :
            display_account(account)
        
        else:
            print("Account Not Found")
            return
        
        wid_amt = get_valid_amount("Enter amount to withdraw : ")

        balance = account[5]
        if wid_amt <= 0 :
            print("Withdrawal amount must be greater than 0")
            return
        
        elif wid_amt > balance:
            print("Withdraw amount must be greater than 0")
            return
        
        status = account[6]

        if status != "Active":
            print("This account is not active")
            return 
        
        query = """
            update accounts
            set balance = balance - %s
            where account_number = %s"""
        
        cursor.execute(query,(wid_amt,account_number))

        query = """
            Insert into transactions(
                account_id,
                transaction_type,
                amount,
                description
                )
                values(%s,%s,%s,%s)"""
        
        values = (
            account[0],
            "Withdraw",
            wid_amt,
            "Cash Withdrawn"
        )

        cursor.execute(query,values)

        connection.commit()
        print("\n" + "=" * 40)
        print("Withdrawn Successful")
        print(f"Account Number : {account_number}")
        print(f"Amount Withdrawn : ₹{wid_amt:.2f}")
        print("=" * 40)

    except mysql.connector.Error as e:
        print(f"Error : {e}")
    
    finally:
        close_connection(connection,cursor)


def transfer_money():

    connection = None
    cursor = None

    try:
        connection,cursor = get_connection()

        if connection is None:
            print("No database is connected")
            return

        #sender
        sender_acc_num = int(input("Enter Sender Account Number : "))

        sender = get_account(cursor,sender_acc_num)

        if sender:
            display_account(sender)
        else:
            print("Sender account not found")
            return
        #receiver
        receiver_acc_num = int(input("Enter Receivers Account Number : "))

        receiver = get_account(cursor,receiver_acc_num)

        if receiver:
            display_account(receiver)
        else:
            print("Receiver account not found")
            return

        if sender_acc_num == receiver_acc_num:
            print("Sender and receiver account cannot be the same.")
            return
        
        #amount
        transfer_amount = get_valid_amount("Enter the amount to transfer : ")

        if transfer_amount <= 0:
            print("Transfer amount must be greater than 0.")
            return

        if transfer_amount > sender[5]:
            print("Insufficient Balance")
            return
        
        #validate
        query = """
            update accounts
            set balance = balance - %s
            where account_number = %s
            """
        cursor.execute(query,(transfer_amount,sender_acc_num,))

        #update Receiver
        
        query = """
            update accounts
            set balance = balance + %s
            where account_number = %s
            """
        cursor.execute(query,(transfer_amount,receiver_acc_num,))

        #insert transaction
        query = """
            insert into transactions(
                account_id,
                transaction_type,
                amount,
                description
                )
            values(%s,%s,%s,%s)"""

        values = (
            sender[0],
            "Transfer",
            transfer_amount,
            f"Transferred to {receiver_acc_num}"
        )
        cursor.execute(query,values)

        query = """
            insert into transactions(
                account_id,
                transaction_type,
                amount,
                description
                )
            values(%s,%s,%s,%s)"""

        values = (
            receiver[0],
            "Transfer",
            transfer_amount,
            f"Received from {sender_acc_num}"
        )
        cursor.execute(query,values)
        
        #commit
        connection.commit()
        print("\n" + "=" * 40)
        print("Transfer Successful")
        print(f"From    :{sender_acc_num}")
        print(f"To      :{receiver_acc_num}")
        print(f"Amount  :{transfer_amount:.2f}")
        print( "=" * 40)
    except mysql.connector.Error as e:
        print(f"Error : {e}")

    finally:
        close_connection(connection,cursor)