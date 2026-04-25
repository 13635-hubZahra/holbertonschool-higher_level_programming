#!/usr/bin/python3
from flask import Flask, request, render_template
import json
import csv
import os

app = Flask(__name__)

def read_json_file(file_path):
    """Reads JSON data, handling both flat lists and 'items' dictionaries."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Returns data if it's a list, otherwise looks for 'items' key
            return data if isinstance(data, list) else data.get("items", [])
    except (json.JSONDecodeError, IOError) as e:
        print(f"JSON Error: {e}")
        return []

def read_csv_file(file_path):
    """Reads CSV data and converts numeric strings to proper types."""
    products = []
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Type conversion for consistency with JSON data
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
    except (ValueError, KeyError, IOError) as e:
        print(f"CSV Error: {e}")
    return products

@app.route("/products")
def show_products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    
    products = []
    error = None

    # 1. Validate Source and Load Data
    if source == "json":
        products = read_json_file("products.json")
    elif source == "csv":
        products = read_csv_file("products.csv")
    else:
        error = "Wrong source"

    # 2. Filter by ID if requested (only if no source error occurred)
    if not error and product_id:
        try:
            p_id = int(product_id)
            products = [p for p in products if p.get("id") == p_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid id"

    return render_template(
        "product_display.html",
        products=products,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
