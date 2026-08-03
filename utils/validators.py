def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print(f"{value} cannot be empty")
        else: 
            return value


def get_valid_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be greater than 0.")
                continue

            return value
            
        except ValueError as e:
            print("Please enter a valid amount")

def get_valid_customer_id(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Id  must be greater than 0.")
                continue

            return value
            
            
        except ValueError as e:
            print("Please enter a valid Id")


def get_valid_email(prompt):
    while True:
        value = input(prompt).strip()
        if "@" not in value or "." not in value:
            print("Please enter a valid Email ID.")
            continue

        return value


def get_valid_mobile(prompt):
    while True:
        value = input(prompt).strip()

        if not value.isdigit():
            print("Please enter digits only")
            continue

        if len(value) != 10:
            print("Mobile number must contain exactly 10 digits.")
            continue

        return value

def get_valid_account_number(prompt):
    while True:
        value = input(prompt).strip()

        if not value.isdigit():
            print("Please enter digits only.")
            continue

        if len(value) != 10:
            print("Account number must contain exactly 10 digits.")
            continue

        return int(value)