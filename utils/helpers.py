
def print_separator():
    print("\n" + "=" * 40)


def print_title(title):
    print("\n" + "=" *40 )
    print(title)
    print("=" * 40)

def print_success(message):
    print("\n" + "-" * 40)
    print(f"Success: {message}")
    print("-" * 40)

def print_error(message):
    print("\n" + "-" * 40)
    print(f"Error: {message}")
    print("-" * 40)


def search_customer_menu():
    print_separator()
    print_title("Search Customer")
    print("\n Search customer by : ")
    print("1. Customer ID")
    print("2. First Name")
    print("3. Last Name")
    print("4. Email")
    print("5. Phone")
    print("6. Address")
    print("7. Back to Main Menu")

    return input("\nEnter your choice (1-7): ").strip()

    