import sqlite3

def 01_query(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Join sales and menu tables to get the price of each product
    cursor.execute('''
        SELECT s.customer_id, SUM(m.price) AS total_amount_spent
        FROM sales s
        JOIN menu m ON s.product_id = m.product_id
        GROUP BY s.customer_id
    ''')
    rows = cursor.fetchall()

    conn.close()
    return rows

# Usage
db_file = "mydatabase.db"
customer_spending = total_amount_spent_by_customer(db_file)

print("Customer Spending:")
for row in customer_spending:
    print(f"Customer ID: {row[0]}, Total Amount Spent: ${row[1]:.2f}")
