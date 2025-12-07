#!/usr/bin/python3
"""
Flask application to display a dynamic list of items from a JSON file
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    """Render items.html with a list of items from items.json"""

    items_list = []
    json_file = os.path.join(os.path.dirname(__file__), 'items.json')

    # Check if JSON file exists
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict) and 'items' in data and isinstance(data['items'], list):
                    items_list = data['items']
        except json.JSONDecodeError:
            print("Error: items.json contains invalid JSON")
        except Exception as e:
            print(f"Error reading items.json: {e}")
    else:
        print("items.json file not found, showing empty list")

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
