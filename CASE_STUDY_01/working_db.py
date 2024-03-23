import sqlite3
import os, csv
db_file = "work_db.db"
sales_csv = 'CS1/sales.csv'
menu_csv = 'CS1/menu.csv'
members_csv = 'CS1/members.csv'


def main():

    db_objs_creation(db_file)


def db_objs_creation(db_file):
    print('--DB objects creation start program')
    drop_sqlite_database(db_file)
    create_sqlite_database(db_file)
    create_menu_table(db_file)
    create_members_table(db_file)
    create_sales_table(db_file)
    load_sales_from_csv(db_file, sales_csv)
    load_menu_from_csv(db_file, menu_csv)
    load_members_from_csv(db_file, members_csv)
    read_data(db_file)


# creates database
def create_sqlite_database(db_file):
    conn = sqlite3.connect(db_file)
    conn.close()
    print(f"SQLite database created at {db_file}")


# drops database
def drop_sqlite_database(db_file):
    try:
        os.remove(db_file)
        print(f"SQLite database '{db_file}' dropped successfully.")
    except FileNotFoundError:
        print(f"SQLite database '{db_file}' not found.")


# create table
def create_menu_table(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS menu
                    (product_id INTEGER PRIMARY KEY,
                    product_name TEXT NOT NULL,
                    price REAL NOT NULL)''')

    conn.commit()
    conn.close()
    print("Menu table created successfully.")


def create_members_table(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS members
                    (customer_id TEXT PRIMARY KEY,
                    join_date TEXT NOT NULL)''')

    conn.commit()
    conn.close()
    print("Members table created successfully.")


def create_sales_table(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                    (customer_id TEXT,
                    order_date TEXT NOT NULL,
                    product_id INTEGER,
                    FOREIGN KEY(customer_id) REFERENCES members(customer_id),
                    FOREIGN KEY(product_id) REFERENCES menu(product_id))''')

    conn.commit()
    conn.close()
    print("Sales table created successfully.")


def load_sales_from_csv(db_file, csv_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            cursor.execute('''
                INSERT INTO sales (customer_id, order_date, product_id)
                VALUES (?, ?, ?)
            ''', (row[0], row[1], int(row[2])))

    conn.commit()
    conn.close()
    print(f"Data from {csv_file} loaded into the sales table.")

def load_menu_from_csv(db_file, csv_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            cursor.execute('''
                INSERT INTO menu (product_id, product_name, price)
                VALUES (?, ?, ?)
            ''', (int(row[0]), row[1], float(row[2])))

    conn.commit()
    conn.close()
    print(f"Data from {csv_file} loaded into the menu table.")


def load_members_from_csv(db_file, csv_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            cursor.execute('''
                INSERT INTO members (customer_id, join_date)
                VALUES (?, ?)
            ''', (row[0], row[1]))

    conn.commit()
    conn.close()
    print(f"Data from {csv_file} loaded into the members table.")


def select_all_from_table(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Select all rows from the specified table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    conn.close()
    return rows


def read_data(db_file):
    # Select all rows from the menu table
    menu_rows = select_all_from_table(db_file, "menu")
    print("Menu Table:")
    for row in menu_rows:
        print(row)

    # Select all rows from the members table
    members_rows = select_all_from_table(db_file, "members")
    print("\nMembers Table:")
    for row in members_rows:
        print(row)

    # Select all rows from the sales table
    sales_rows = select_all_from_table(db_file, "sales")
    print("\nSales Table:")
    for row in sales_rows:
        print(row)

# Usage
main()