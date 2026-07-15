DROP DATABASE IF EXISTS bank_management_system;

CREATE DATABASE bank_management_system;

USE bank_management_system;

CREATE TABLE customers(
    customer_id int auto_increment PRIMARY KEY,
    first_name varchar(50),
    last_name varchar(50),
    gender enum("Male","Female","Other") not null,
    date_of_birth date,
    mobile varchar(30) unique not null,
    email varchar(20) unique,
    address text,
    created_at timestamp default current_timestamp
);

CREATE TABLE accounts(
    account_id int auto_increment PRIMARY KEY,
    customer_id int not null,
    account_number bigint unique not null,
    account_type enum("Savings","Current"),
    balance decimal(12,2) default 0.00,
    status enum("Active","Blocked","Closed") default "Active",
    created_at timestamp default current_timestamp,
    foreign key(customer_id) references customers(customer_id)    
);

CREATE TABLE transactions(
    transaction_id int auto_increment PRIMARY KEY,
    account_id int not null,
    transaction_type enum("Deposit","Withdraw","Transfer"),
    amount decimal(12,2) default 0.00,
    description varchar(999),
    transaction_date timestamp default current_timestamp,
    foreign key(account_id) references accounts(account_id)    

);