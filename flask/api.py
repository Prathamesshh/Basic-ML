## working with API 'S -- Json
from flask import Flask, jsonify, request

app = Flask(__name__)

## initial data in my to do list
todos = [
    {'id': 1, 'task': 'Buy groceries', 'done': False},
    {'id': 2, 'task': 'Walk the dog', 'done': False},
    {'id': 3, 'task': 'Read a book', 'done': False}
]

@app.route('/')
def home():
    return "Welcome to the To-Do List APP"

## Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True)

