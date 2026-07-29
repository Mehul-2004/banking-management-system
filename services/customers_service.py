from database.connection import get_connection,close_connection
import mysql.connector
from utils.validators import (
    get_non_empty_string,
    get_valid_email,
    get_valid_customer_id,
    get_valid_mobile
)

def get_customer_input():
    first_name = get_non_empty_string("Enter First Name ")
    last_name = get_non_empty_string("Enter customers last name : ")
    gender = input("Enter gender : ")       
    date_of_birth = input("Enter date of birth (YYYY-MM-DD) : ")
    mobile = get_valid_mobile("Enter mobile number : ")
    email = get_valid_email("Enter email id : ")
    address = get_non_empty_string("Enter address : ")

    return{
        "first_name" :first_name,
        "last_name" :last_name,
        "gender" :gender,
        "date_of_birth" :date_of_birth,
        "mobile" :mobile,
        "email" :email,
        "address" :address,
    }


def get_customer(cursor,customer_id):
        """
        Fetch a single customer using customer_id.
        """
        query = "Select * from customers where customer_id = %s"
        
        cursor.execute(query,(customer_id,))
        return cursor.fetchone()

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
        
        customer_id = get_valid_customer_id("Enter the customer id : ")
        
        # query = "Select * from customers where customer_id = %s"
        
        # cursor.execute(query,(customer_id,))
        customer = get_customer(cursor,customer_id)
        
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
        
        customer_id  = get_valid_customer_id("Enter customer_id : ")

        customer = get_customer(cursor,customer_id)

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
        
        customer_id = get_valid_customer_id("Enter Customer ID : ")

        customer = get_customer(cursor,customer_id)

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

