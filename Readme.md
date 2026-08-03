# Bank Management System

## Overview

The Bank Management System is a console-based Python application that allows users to manage customers, bank accounts, and financial transactions using a MySQL database.

This project demonstrates CRUD operations, database connectivity, input validation, modular programming, and transaction management.

---

## Features

### Customer Management

* Add Customer
* View Customers
* Search Customer
* Update Customer
* Delete Customer

### Account Management

* Create Account
* View Accounts
* Search Account
* Deposit Money
* Withdraw Money
* Transfer Money
* Block Account
* Close Account

### Transaction Management

* View Transaction History
* Search Transactions

---

## Technologies Used

* Python 3
* MySQL
* mysql-connector-python
* Git & GitHub

---

## Project Structure

```
Bank_Management_System/
│
├── database/
│   └── connection.py
│
├── services/
│   ├── customers_service.py
│   ├── accounts_service.py
│   └── transaction_history.py
│
├── utils/
│   ├── validators.py
│   └── helpers.py
│
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Database Tables

* customers
* accounts
* transactions

---

## How to Run

1. Clone the repository.

2. Install dependencies.

3. Create the MySQL database.

4. Update the database credentials in `config.py`.

5. Run the application.

```
python main.py
```

---

## Learning Outcomes

This project helped me practice:

* Python Programming
* Functions
* Modular Programming
* Exception Handling
* Input Validation
* MySQL CRUD Operations
* SQL Joins
* Database Transactions
* Git & GitHub

---

## Future Improvements

* Flask Web Application
* User Authentication
* Password Encryption
* REST API
* Account Statements (PDF)
* Logging
* Unit Testing

---

## Author

Mehul Ladwa
