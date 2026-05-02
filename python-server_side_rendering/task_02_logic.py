import os
import json
from flask import Flask, render_template, render_template_string
def setup_files():
    if not os.path.exists('templates'):
        os.makedirs('templates')
    items_data = {
        "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
    }
    with open('items.json', 'w') as f:
        json.dump(items_data, f, indent=4)
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Items List</title>
</head>
<body>
    <h1>Items List</h1>
    
    {% if items %}
        <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No items found</p>
    {% endif %}
</body>
</html>
"""
    with open('templates/items.html', 'w') as f:
        f.write(html_content.strip())

setup_files()

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except Exception:
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    print("Server baslayir... http://127.0.0.1:5000/items ünvanına daxil olun.")
    app.run(debug=True, port=5000)
