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
def add_customer():
    connection = None
    cursor = None
    try:
        #connect to database
        connection , cursor = get_connection()

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
    

# def view_customer():
# def search_customer():
# def update_customer():
# def delete_customer():
