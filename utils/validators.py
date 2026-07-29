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
                return value
            
        except ValueError as e:
            print("Please enter a valid amount")
            
# def get_valid_email():
# def get_valid_mobile():
# def get_valid_customer_id():
# def get_valid_account_number():