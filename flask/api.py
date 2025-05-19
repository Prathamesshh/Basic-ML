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


## Get a single todo by id
@app.route('/todos/<int:todo_id>',methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({'error': 'Todo not found'}), 404

  
## post :create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({'error': 'Bad Request'})
    new_todo = {
        'id': todos[-1]['id'] +1,
        'name': request.json['task'],
        'done': False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

## put : update a todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    todo['name'] = request.json.get('task', todo['name'])
    todo['done'] = request.json.get('done', todo['done'])
    return jsonify(todo)

if __name__ == '__main__':
    app.run(debug=True)

