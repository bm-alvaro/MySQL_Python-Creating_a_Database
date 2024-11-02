CREATE DATABASE IF NOT EXISTS `inventorydb`;

CREATE TABLE IF NOT EXISTS inventorydb.suppliers(
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(255) NOT NULL,
    supplier_email VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS inventorydb.customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_email VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(255),
    customer_address VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS inventorydb.inventory(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(255),
    stock_level INT NOT NULL,
    reorder_level INT NOT NULL,
    supplier_id INT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES inventorydb.suppliers(supplier_id)
);

CREATE TABLE IF NOT EXISTS inventorydb.sales(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    date DATE NOT NULL,
    quantity INT NOT NULL,
    total_amount INT NOT NULL,
    discount INT,
    FOREIGN KEY (product_id) REFERENCES inventorydb.inventory(product_id),
    FOREIGN KEY (customer_id) REFERENCES inventorydb.customers(customer_id)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/supplier_data.csv'
INTO TABLE inventorydb.suppliers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(supplier_id, supplier_name, supplier_email);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customer_data.csv'
INTO TABLE inventorydb.customers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(customer_id, customer_name, customer_email, customer_phone, customer_address);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/inventory_data.csv'
INTO TABLE inventorydb.inventory
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(product_id, product_name, category, stock_level, reorder_level, supplier_id);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sales_data.csv'
INTO TABLE inventorydb.sales
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(product_id, customer_id, date, quantity, total_amount, discount);

