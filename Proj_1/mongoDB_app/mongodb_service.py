'''
There's a COMMON save method here that is used by both 
consumer-save and @app.route('/api-save') methods....
'''
from pymongo import MongoClient
from pymongo.collection import Collection

from flask_app.models.user import User

class DB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['mydatabase']
        self.users_collection: Collection = self.db['users']
        return self

    def get_all_users(self):
        users = self.users_collection.find()
        return [User(**user) for user in users]

    def common_save_method(self, user: User):
        user_dict = user.model_dump()
        self.users_collection.insert_one(user_dict)

# Create an instance of the DB class
db = DB()

