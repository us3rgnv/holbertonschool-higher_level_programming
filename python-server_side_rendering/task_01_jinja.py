#!/usr/bin/python3
"""
Basic Flask application with reusable header and footer templates
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Render the homepage with index.html"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
