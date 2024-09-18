CREATE DATABASE IF NOT EXISTS banking;
USE banking;

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20),
    balance DECIMAL(10,2)
);

INSERT INTO accounts (account_number, balance) VALUES ('12345', 1000.00);
