from flask import Flask
from flask_restful import Api
from app.resources.todo_resource import TodoResource


app = Flask(__name__)
api = Api(app)

# Import and add routes here
api.add_resource(TodoResource, '/todos', '/todos/<int:todo_id>')
