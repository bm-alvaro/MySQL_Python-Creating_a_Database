import random
from datetime import datetime, timedelta
import pandas as pd

# Global constants
NUM_ENTRIES_SALES = 600
NUM_ENTRIES_INVENTORY = 20
NUM_ENTRIES_CUSTOMER = 600

PRODUCT_IDS = list(range(1, NUM_ENTRIES_INVENTORY + 1))
CUSTOMER_IDS = list(range(1, NUM_ENTRIES_CUSTOMER + 1))


# sales data generation

DATE_START = datetime(2019, 1, 1)
DATE_END = datetime(2024, 1, 1)
QUANTITY = range(1, 99)
TOTAL_AMOUNT = range(1, 9999)

sales_data = []

def generate_data_sales():
    for i in range(NUM_ENTRIES_SALES):
        sales_data.append({
            'product_id': random.choice(PRODUCT_IDS),
            'customer_id': random.choice(CUSTOMER_IDS),
            'date': DATE_START + timedelta(days=random.randint(0, (DATE_END - DATE_START).days)),
            'quantity': random.choice(QUANTITY),
            'total_amount': random.choice(TOTAL_AMOUNT),
            'discount': random.randint(1, 20) * 5,
        })

generate_data_sales()

df_sales = pd.DataFrame(sales_data)
df_sales.to_csv('data/sales_data.csv', index=False)


# inventory data generation

PRODUCT_NAMES = ['product_' + str(i) for i in range(1, NUM_ENTRIES_INVENTORY + 1)]
CATEGORY = ['category_' + str(i) for i in range(1, 6)]
STOCK_LEVEL = range(1, 101)
REORDER_LEVEL = range(1, 81)
SUPPLIER_ID = range(1, 11)

inventory_data = []

def generate_data_inventory():
    for i in range(NUM_ENTRIES_INVENTORY):
        inventory_data.append({
            'product_id': PRODUCT_IDS[i],
            'product_name': PRODUCT_NAMES[i],
            'category': random.choice(CATEGORY),
            'stock_level': random.choice(STOCK_LEVEL),
            'reorder_level': random.choice(REORDER_LEVEL),
            'supplier_id': random.choice(SUPPLIER_ID),
        })

generate_data_inventory()

df_inventory = pd.DataFrame(inventory_data)
df_inventory.to_csv('data/inventory_data.csv', index=False)


# customer data generation

CUSTOMER_NAME = ['name_' + str(i) for i in range(1, NUM_ENTRIES_CUSTOMER + 1)]
CUSTOMER_EMAIL = ['email_' + str(i) + '@gmail.com' for i in range(1, NUM_ENTRIES_CUSTOMER + 1)]
CUSTOMER_PHONE = ['+91-9' + str(random.randint(100000000, 999999999)) for i in range(1, NUM_ENTRIES_CUSTOMER + 1)]  
CUSTOMER_ADDRESS = ['address_' + str(i) for i in range(1, NUM_ENTRIES_CUSTOMER + 1)]

customer_data = []

def generate_data_customer():
    for i in range(NUM_ENTRIES_CUSTOMER):
        customer_data.append({
            'customer_id': CUSTOMER_IDS[i],
            'customer_name': CUSTOMER_NAME[i],
            'customer_email': CUSTOMER_EMAIL[i],
            'customer_phone': CUSTOMER_PHONE[i],
            'customer_address': CUSTOMER_ADDRESS[i]
        })

generate_data_customer()

df_customer = pd.DataFrame(customer_data)
df_customer.to_csv('data/customer_data.csv', index=False)

# supplier data generation

NUM_ENTRIES = 10
SUPPLIER_NAME = ['supplier_' + str(i) for i in range(1, 11)]
SUPPLIER_EMAIL = ['email_' + str(i) + '@gmail.com' for i in range(1, 11)]

supplier_data = []

def generate_data_supplier():
    for i in range(NUM_ENTRIES):
        supplier_data.append({
            'supplier_id': i+1,
            'supplier_name': SUPPLIER_NAME[i],
            'supplier_email': SUPPLIER_EMAIL[i],
        })

generate_data_supplier()

df_supplier = pd.DataFrame(supplier_data)
df_supplier.to_csv('data/supplier_data.csv', index=False)