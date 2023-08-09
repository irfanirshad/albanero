'''Minimal API with 
'''
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message=f"Todo {todo_id} doesn't exist")

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        # lol, taken directly from docs..is there not a better way
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1   
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
    
    
    '''Tested it using INSOMNIA:
    Note: In-memory storage(Data structure running on RAM)....
    
    
    GET the list
    1) $ curl http://localhost:5000/todos
{"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}
    
    2) GET a single task
    curl http://localhost:5000/todos/todo3
{"task": "profit!"}
    
    
    3) DELETE a task
    curl http://localhost:5000/todos/todo2 -X DELETE -v
    
    4) ADD a new task 
    curl http://localhost:5000/todos -d "task=something new" -X POST -v

    5) Update a new task
    curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v
    '''