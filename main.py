from database.connection import get_connection , close_connection
from services.customers_service import (
    add_customers,
    view_customers,
    search_customer,
    update_customer)

def test_connection():
    connection,cursor = get_connection()

    if connection:
        print("Database connected successfully")
    else:
        print("Failed")

    close_connection(connection,cursor)

 

def main():
    while True:
        print("\n" + "=" * 40)
        print("Bank Management system")
        print("=" * 40)
        print("1. Add Customer") 
        print("2. View Customer") 
        print("3. Search Customer") 
        print("4. Update Customer") 
        print("5. Delete Customer") 
        print("6. Exit") 
        print("=" * 40)

        choice = input("Select an option : ")
        
        if choice == "1":
            add_customers()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            update_customer()
        elif choice == "6":
            print("Thank you")
            break     
        else:
            print("Invalid Option")


if __name__ == "__main__":
    test_connection()
    main()    