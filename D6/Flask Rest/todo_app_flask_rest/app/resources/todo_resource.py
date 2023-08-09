'''
TodoResource

'''

from flask_restful import Resource, reqparse
from app.models.todo import Todo


# In-memory database
todos = {}


class TodoResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=False)
        args = parser.parse_args()

        if args['title']:
            filtered_todos = [todo for todo in todos.values() if args['title'].lower() in todo.title.lower()]
            return {'todos': [todo.__dict__ for todo in filtered_todos]}
        else:
            return {'todos': [todo.__dict__ for todo in todos.values()]}

    def post(self):  # sourcery skip: class-extract-method
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        args = parser.parse_args()

        todo_id = len(todos) + 1
        new_todo = Todo(todo_id, args['title'], args['description']) # type: ignore
        todos[todo_id] = new_todo
        return {'message': 'Todo created successfully', 'todo': new_todo.__dict__}

    def put(self, todo_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        args = parser.parse_args()

        if todo_id in todos:
            updated_todo = Todo(todo_id, args['title'], args['description'])  # type: ignore
            todos[todo_id] = updated_todo
            return {'message': 'Todo updated successfully', 'todo': updated_todo.__dict__}
        else:
            return {'error': 'Todo not found'}, 404

    def delete(self, todo_id):
        if todo_id not in todos:
            return {'error': 'Todo not found'}, 404
        deleted_todo = todos.pop(todo_id)
        return {'message': 'Todo deleted successfully', 'todo': deleted_todo.__dict__}
        
    
    
'''        if todo_id in todos:
            deleted_todo = todos.pop(todo_id)
            return {'message': 'Todo deleted successfully', 'todo': deleted_todo.__dict__}
        else:
            return {'error': 'Todo not found'}, 404'''