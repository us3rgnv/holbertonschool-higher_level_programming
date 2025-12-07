#!/usr/bin/python3
"""
Flask application to display products from JSON or CSV
"""

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(**name**)

def read_json(file_path):
try:
with open(file_path, 'r', encoding='utf-8') as f:
data = json.load(f)
return data
except Exception:
return None

def read_csv(file_path):
try:
with open(file_path, 'r', encoding='utf-8') as f:
reader = csv.DictReader(f)
data = []
for row in reader:
# Convert id and price
row['id'] = int(row['id'])
try:
row['price'] = float(row['price'])
except Exception:
row['price'] = 0.0
data.append(row)
return data
except Exception:
return None

@app.route('/products')
def products():
source = request.args.get('source')
product_id = request.args.get('id')

```
error_msg = None
data = None

if source not in ['json', 'csv']:
    error_msg = "Wrong source"
else:
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')

    if data is None:
        error_msg = f"Could not read {source} data"
    elif product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if int(p['id']) == product_id]
            if filtered:
                data = filtered
            else:
                data = []
                error_msg = "Product not found"
        except ValueError:
            data = []
            error_msg = "Invalid id parameter"

# Return the template
return render_template('product_display.html', products=data, error=error_msg)
```

if **name** == '**main**':
app.run(debug=True, port=5000)
