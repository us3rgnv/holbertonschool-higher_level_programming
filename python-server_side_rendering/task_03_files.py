#!/usr/bin/python3
"""
Flask application to display products from JSON or CSV files
"""

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# File paths
JSON_FILE = "products.json"
CSV_FILE = "products.csv"

def read_json(file_path):
    """Read data from JSON file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv(file_path):
    """Read data from CSV file"""
    products = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id to int and price to float
                try:
                    row["id"] = int(row.get("id", 0))
                    row["price"] = float(row.get("price", 0))
                except ValueError:
                    row["id"] = 0
                    row["price"] = 0
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products

@app.route('/products')
def products():
    """Route to display products from JSON or CSV"""
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id")
    data = []
    error_msg = None

    # Determine source and read data
    if source == "json":
        data = read_json(JSON_FILE)
    elif source == "csv":
        data = read_csv(CSV_FILE)
    else:
        error_msg = "Wrong source"

    # Filter by id if provided
    if product_id and data and not error_msg:
        try:
            pid = int(product_id)
            filtered = [p for p in data if int(p.get("id", 0)) == pid]
            if filtered:
                data = filtered
            else:
                error_msg = "Product not found"
                data = []
        except ValueError:
            error_msg = "Invalid id parameter"
            data = []

    return render_template("product_display.html", products=data, error=error_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
