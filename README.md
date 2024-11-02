# Data Generation and Database Setup

In this project, I have generated synthetic data to populate a database that I have built in MySQL. My goal is to develop a small working model that demonstrates the process of database creation followed by data entry and retrieval.

In other projects, I use real data to perform sales analysis and inventory management.

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