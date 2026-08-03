from database.connection import get_connection , close_connection

from services.customers_service import (
    add_customer,
    view_customers,
    search_customer,
    update_customer,
    delete_customer,
)
from services.accounts_service import(
        create_account,
        view_account,
        search_account,
        deposit_money,
        withdraw_money,
        transfer_money

)
from utils.helpers import (
    print_title,
)
from services.transaction_history import(
    block_account,
    close_account,
    search_transactions,
    view_transactions,

)

def test_connection():
    connection,cursor = get_connection()

    if connection:
        print("Database connected successfully")
    else:
        print("Failed")

    close_connection(connection,cursor)

 

def main():
    while True:
        print_title("Bank Management System")
        print("1. Add Customer") 
        print("2. View Customer") 
        print("3. Search Customer") 
        print("4. Update Customer") 
        print("5. Delete Customer") 
        print("6. Create Account") 
        print("7. View Account") 
        print("8. Search Account") 
        print("9. Deposit Money") 
        print("10. Withdraw money") 
        print("11. Transfer Money") 
        print("12. View Transactions") 
        print("13. Search Transactions") 
        print("14. Block Account") 
        print("15. Close Account") 
        print("16. Exit") 
        print("=" * 40)

        choice = input("Select an option : ")
        
        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            update_customer()
        elif choice == "5":
            delete_customer()
        elif choice == "6":
            create_account()
        elif choice == "7":
            view_account()
        elif choice == "8":
            search_account()
        elif choice == "9":
            deposit_money()
        elif choice == "10":
            withdraw_money()
        elif choice == "11":
            transfer_money()
        elif choice == "12":
            view_transactions()
        elif choice == "13":
            search_transactions()
        elif choice == "14":
            block_account()
        elif choice == "15":
            close_account()

        elif choice == "16":
            print("Thank you")
            break     
        else:
            print("Invalid Option")


if __name__ == "__main__":
    test_connection()
    main()    