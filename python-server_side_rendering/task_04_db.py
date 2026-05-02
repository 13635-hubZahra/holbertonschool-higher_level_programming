import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()

def create_test_files():
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    products_json = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
        {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
    ]
    with open('products.json', 'w') as f:
        json.dump(products_json, f)

    with open('products.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "category", "price"])
        writer.writeheader()
        writer.writerows(products_json)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    products = []
    error = None

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except Exception:
            error = "JSON file error."

    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products.append(row)
        except Exception:
            error = "CSV file error."

    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row  
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()
            products = [dict(row) for row in rows]
            conn.close()
        except sqlite3.Error as e:
            error = f"Database error: {e}"

    else:
        if source:
            error = "Wrong source"
        else:
            error = "Please provide a source (json, csv, or sql)."

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    init_db()
    create_test_files() 
    app.run(debug=True, port=5000)
