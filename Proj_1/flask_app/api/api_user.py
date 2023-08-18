"""
Exposing our API endpoints which will inturn call our services ...
"""

import json 
from datetime import datetime
from flask import Flask, request, jsonify   
import pymongo
# from flask_app.models.User import User
import logging
#xxx-xxx-xxx-xxx-xxx---IMPORTS---xxx-xxx-xxx-xxx
from flask_app.models.user import User




# create a Flask app and an HTTP basic authentication object
app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False

# not used==ing logger here. 
app.logger.setLevel(logging.DEBUG)


# set up database connection or a mongoDB (pymongo) connection pool 


# define a route for sending messages to Kafka
@app.route('/save_user', methods=['POST'])
def save_user():
    """Save a single user or list of user.
    i'll be getting a camelcase JSON here ...using pydantic i need to convert it to snake to perform validation
    If its all good then , i convert it back to camelCase and save it to my DB
    """
    data = request.json
    query = data.get('data') # camel Case when coming in and going out
    
    if not query: 
        return jsonify({"Error": "Invalid request"}), 400
    
    result =  add_user()
    return jsonify(result)



# define a route for getting information about all students
@app.route('/users', methods=['GET'])
def get_all_users():
    '''Use my mongoDB connection and retrieve all the data in my collection'''
    pass




if __name__ == '__main__':
    app.run(debug=True, port=5000)


