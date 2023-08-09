# Flask Readme

GET, POST, PUT, DELETE APIs
Headers, Query Params, Body Params


-x-x-x-x-x-


## Query Parameters
Lets say you recieve an query on the 'search' endpoint 
https://localhost:8080/api/v1/search?name=Irfan

which performs a simple check whether the name exists or not

1. In this case 
@app.route('/search', method='GET')
def search():



### Request Parameters


-x-x-x-x-
1. Extracting parameters from headers:

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HeaderParameterResource(Resource):
    def get(self):
        user_agent = request.headers.get('User-Agent')
        return {'user_agent': user_agent}

api.add_resource(HeaderParameterResource, '/header-example')

if __name__ == '__main__':
    app.run()


###

2. Extracting from query parameters


from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class QueryParameterResource(Resource):
    def get(self):
        args = request.args
        name = args.get('name')
        age = args.get('age')
        return {'name': name, 'age': age}

api.add_resource(QueryParameterResource, '/query-example')

if __name__ == '__main__':
    app.run()


3. request Body parameters  

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class BodyParameterResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        return {'username': username, 'password': password}

api.add_resource(BodyParameterResource, '/body-example')

if __name__ == '__main__':
    app.run()







### Folder Structure

myapi/
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        util.py     

#### lets create a simple todo app


### My folder structure for a Todo App

todo_app/
│
├── app/
│   ├── __init__.py
│   ├── resources/
│   │   ├── __init__.py
│   │   ├── todo_resource.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── todo.py
│
├── run.py


### todo.py in MODELS folder

class Todo:
    def __init__(self, todo_id, title, description):
        self.id = todo_id
        self.title = title
        self.description = description

### todo_resource.py in resources folder

from flask_restful import Resource, reqparse
from app.models.todo import Todo

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

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        args = parser.parse_args()

        todo_id = len(todos) + 1
        new_todo = Todo(todo_id, args['title'], args['description'])
        todos[todo_id] = new_todo
        return {'message': 'Todo created successfully', 'todo': new_todo.__dict__}

    def put(self, todo_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        args = parser.parse_args()

        if todo_id in todos:
            updated_todo = Todo(todo_id, args['title'], args['description'])
            todos[todo_id] = updated_todo
            return {'message': 'Todo updated successfully', 'todo': updated_todo.__dict__}
        else:
            return {'error': 'Todo not found'}, 404

    def delete(self, todo_id):
        if todo_id in todos:
            deleted_todo = todos.pop(todo_id)
            return {'message': 'Todo deleted successfully', 'todo': deleted_todo.__dict__}
        else:
            return {'error': 'Todo not found'}, 404

### __init__.py inside the resources folder:

from .todo_resource import TodoResource

### __init__.py inside the todo folder
from .todo import Todo

### __init__.py inside app 

```
from flask import Flask
from flask_restful import Api
from app.resources.todo_resource import TodoResource

app = Flask(__name__)
api = Api(app)

# Add routes here
api.add_resource(TodoResource, '/todos', '/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run()
```
### root.py in root folder

from app import app

if __name__ == '__main__':
    app.run(debug=True)


localhost:5000/todos