from flask import Flask, render_template, request
from jinja2 import TemplateNotFound
import os

# Set template_folder to the local `templates` directory inside the Flask folder
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

@app.route('/')
def home():
    return "Welcome to the home page"

@app.route('/first/<int:num>')
def first(num):
    return f"It's the first page\nMy marks are: {num}"

@app.route('/form', methods=['GET', 'POST'])
def get_form():
    if request.method == 'POST':
        name = request.form.get('name', 'N/A')
        age = request.form.get('age', 'N/A')
        weight = request.form.get('weight', 'N/A')
        return f"Name: {name}, Age: {age}, Weight: {weight}"

    try:
        return render_template('form.html')
    except TemplateNotFound:
        return "Form template 'form.html' not found. Create 'templates/form.html'.", 404

if __name__ == "__main__":
    app.run()