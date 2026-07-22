from database.connection import get_connection,close_connection
import mysql.connector

def get_customer_input():
    first_name = input("Enter customers first name : ")
    last_name = input("Enter customers last name : ")
    gender = input("Enter gender : ")       
    date_of_birth = input("Enter date of birth (YYYY-MM-DD) : ")
    mobile = input("Enter mobile number : ")
    email = input("Enter email id : ")
    address = input("Enter address : ")

    return{
        "first_name" :first_name,
        "last_name" :last_name,
        "gender" :gender,
        "date_of_birth" :date_of_birth,
        "mobile" :mobile,
        "email" :email,
        "address" :address,
    }


    
def display_customer(customer):
    print("=" * 40)
    print(f" Customer iD    : {customer[0]}")
    print(f" Name           : {customer[1]} {customer[2]}")
    print(f" Gender         : {customer[3]}")
    print(f"Date of Birth   : {customer[4]}")
    print(f" Mobile Number  : {customer[5]}")
    print(f" Email ID       : {customer[6]}")
    print(f" Address        : {customer[7]}")

def add_customers():
    connection = None
    cursor = None
    try:
        #connect to database
        connection , cursor = get_connection()

        if connection is None:
            return 
        
        # get user input
        customer = get_customer_input()

        #validate input
        query = """
            INSERT INTO customers(
                first_name ,
                last_name,
                gender,
                date_of_birth,
                mobile,
                email,
                address
                )
                values(%s,%s,%s,%s,%s,%s,%s)
                """
        values=(
            customer["first_name"],
            customer["last_name"],
            customer["gender"],
            customer["date_of_birth"],
            customer["mobile"],
            customer["email"],
            customer["address"],
        )
        # insert into database
        cursor.execute(query,values)

        # commit
        connection.commit()
        print("Customer Added Successfully ")
        
        # close connection
    except mysql.connector.Error as e:
        print(f"Database Error : {e}")

    finally:
        close_connection(connection,cursor)
    

def view_customers():
    connection = None
    cursor = None
    try:
        connection,cursor = get_connection()

        if connection is None:
            return
        
        query = "Select * from customers"

        cursor.execute(query,)

        customers = cursor.fetchall()

        if not customers:
            print("No customers found")
            return
        
        for customer in customers:
            display_customer(customer)


    except mysql.connector.Error as e:
        print(f"Database Error : {e}")

    finally:
        close_connection(connection,cursor)

def search_customer():
    connection = None
    cursor = None

    try :
        connection,cursor = get_connection()

        if connection is None:
            print("Database Connection failed")
            return
        
        customer_id = int(input("Enter the customer id : "))
        
        query = "Select * from customers where customer_id = %s"
        
        cursor.execute(query,(customer_id,))
        
        customer = cursor.fetchone()
        
        if  customer :
           display_customer(customer)
        
        else:
            print("No customer Found")

    except mysql.connector.Error as e:
        print(f"Database Error : {e}")
    
    finally:
        close_connection(connection,cursor)
        

def update_customer():
    connection = None
    cursor = None

    try :
        connection , cursor = get_connection()

        if connection is None:
            print("Database Connection failed")
            return
        
        customer_id  = int(input("Enter customer_id : "))

        query = "select * from customers where customer_id = %s"
        
        cursor.execute(query,(customer_id,))
        
        customer = cursor.fetchone()

        if customer :
            display_customer(customer)
        else:
            print("Customer not found")
            return
        
        print("\nWhat do you want to update?")
        print("1. First Name")
        print("2. Last Name")
        print("3. Gender")
        print("4. Date of Birth")
        print("5. Mobile Number")
        print("6. Email")
        print("7. Address")
        print("8. Cancel")

        choice = input("Enter your choice: ")
        update_fields = {
            "1" : "first_name",
            "2" : "last_name",
            "3" : "gender",
            "4" : "date_of_birth",
            "5" : "mobile",
            "6" : "email",
            "7" : "address",
        }
        if choice == "8":
            print("Update Cancelled")
            return

        if choice not in update_fields:
            print("Invalid Choice")
            return
       
        field = update_fields[choice]
        
        new_value = input(f"Enter new {field.replace('_',' ')} : ")

        query = f"""
        update customers set {field} = %s 
        where customer_id = %s """

        cursor.execute(query,(new_value,customer_id))
        connection.commit()
        print("Customer Updated Successfully")

    except mysql.connector.Error as e:
        print(f"Error : {e}")
    
    finally :
        close_connection(connection,cursor)

    

def delete_customer():

    connection = None
    cursor = None

    try:

        connection,cursor = get_connection()

        if connection is None:
            print("Failed to connect database")
            return
        
        customer_id = int(input("Enter Customer ID : "))

        query = "Select * from customers where customer_id = %s"

        cursor.execute(query,(customer_id,))

        customer = cursor.fetchone()
        if customer:
            display_customer(customer)

        else:
            print("no customer found")
            return
        
        cnf = input("Do you confirm want to delete this data (Y/N) ? ")

        if cnf.upper() != "Y":
            print("Deletion Cancelled")
            return

        # else:
        #     print("Proceed")

        query = "Delete from customers where customer_id = %s"

        cursor.execute(query,(customer_id,))
        
        connection.commit()
        print("Successfully deleted ")

    except mysql.connector.Error as e:
        print(f"Error : {e}")

    finally:
        close_connection(connection,cursor)

def create_account():

    connection = None
    cursor = None

    try:
        connection,cursor = get_connection()
    
        if connection is None:
            print("No database is connected")
            return

        customer_id = int(input("Enter Customer id : "))

        query = "select * from customers where customer_id = %s"
        cursor.execute(query,(customer_id,))

        customer = cursor.fetchone()
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
    print(f"Account ID     : {account[0]}")
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
        
        acc_number = int(input("Enter Account Number : "))

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
            accounts.customer_id = customers.customer_id
            where accounts.account_number = %s;
                """
        
        cursor.execute(query,(acc_number,))

        account = cursor.fetchone()

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
            inner join customers on 
            accounts.customer_id = customers.customer_id
            where accounts.account_number = %s;
                """
        
        cursor.execute(query,(account_number,))
        account = cursor.fetchone()

        if account :
            display_account(account)
        
        else:
            print("Account Not Found")
            return
        dep_amt = float(input("Enter amount to Deposit : "))

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
