# Data Generation and Database Setup

This project generates synthetic data for sales, inventory, customers, and suppliers, and loads it into a MySQL database.

## Project Structure

- **`data/`**: 
- **`scripts/`**: 

## Prerequisites

- Python 3.x
- Pandas library
- MySQL Server

## Setup

1. **Install Python dependencies:**

    ```sh
    pip install pandas
    ```

2. **Generate Data:**

    Run the `data_generation.py` script to generate CSV files in the `data` directory.

    ```sh
    python scripts/data_generation.py
    ```

3. **Setup MySQL Database:**

    - Create a database named `inventorydb` in your MySQL server.
    - Update the file paths in `scripts/create_database.sql` to match your MySQL server's `LOAD DATA INFILE` path.
    - Execute the SQL script to create tables and load data:

    ```sh
    mysql -u [username] -p inventorydb < scripts/create_database.sql
    ```

## Data Generation Details

### Sales Data

- **Number of Entries:** 600
- **Fields:**
  - `product_id`: Randomly chosen from product IDs
  - `customer_id`: Randomly chosen from customer IDs
  - `date`: Random date between 2019-01-01 and 2024-01-01
  - `quantity`: Random value between 1 and 98
  - `total_amount`: Random value between 1 and 9998
  - `discount`: Random value between 5 and 100 (multiples of 5)

### Inventory Data

- **Number of Entries:** 20
- **Fields:**
  - `product_id`: Sequential from 1 to 20
  - `product_name`: `product_1` to `product_20`
  - `category`: Randomly chosen from 5 categories
  - `stock_level`: Random value between 1 and 100
  - `reorder_level`: Random value between 1 and 80
  - `supplier_id`: Randomly chosen from 1 to 10

### Customer Data

- **Number of Entries:** 600
- **Fields:**
  - `customer_id`: Sequential from 1 to 600
  - `customer_name`: `name_1` to `name_600`
  - `customer_email`: `email_1@gmail.com` to `email_600@gmail.com`
  - `customer_phone`: Randomly generated phone numbers
  - `customer_address`: `address_1` to `address_600`

### Supplier Data

- **Number of Entries:** 10
- **Fields:**
  - `supplier_id`: Sequential from 1 to 10
  - `supplier_name`: `supplier_1` to `supplier_10`
  - `supplier_email`: `email_1@gmail.com` to `email_10@gmail.com`

## License

This project is licensed under the MIT License.