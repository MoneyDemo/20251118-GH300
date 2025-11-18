"""
Flask TODO Application with In-Memory Database
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database - simple list to store TODO items
todos = []


class Todo:
    """Todo item model"""
    def __init__(self, title, description=""):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert Todo object to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }


# Web Routes
@app.route('/')
def index():
    """Main page - display all todos"""
    return render_template('index.html', todos=todos)


# API Routes
@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Get all todos"""
    return jsonify([todo.to_dict() for todo in todos])


@app.route('/api/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    todo = Todo(
        title=data['title'],
        description=data.get('description', '')
    )
    todos.append(todo)
    return jsonify(todo.to_dict()), 201


@app.route('/api/todos/<todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a specific todo by id"""
    todo = next((t for t in todos if t.id == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo.to_dict())


@app.route('/api/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo"""
    todo = next((t for t in todos if t.id == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    data = request.get_json()
    if 'title' in data:
        todo.title = data['title']
    if 'description' in data:
        todo.description = data['description']
    if 'completed' in data:
        todo.completed = data['completed']
    
    return jsonify(todo.to_dict())


@app.route('/api/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    global todos
    todo = next((t for t in todos if t.id == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    todos = [t for t in todos if t.id != todo_id]
    return jsonify({'message': 'Todo deleted successfully'})


@app.route('/api/todos/<todo_id>/toggle', methods=['POST'])
def toggle_todo(todo_id):
    """Toggle todo completion status"""
    todo = next((t for t in todos if t.id == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    todo.completed = not todo.completed
    return jsonify(todo.to_dict())


if __name__ == '__main__':
    # Add some sample data
    sample_todos = [
        Todo("Buy groceries", "Milk, eggs, bread"),
        Todo("Complete project", "Finish the TODO app"),
        Todo("Exercise", "30 minutes of cardio")
    ]
    todos.extend(sample_todos)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
