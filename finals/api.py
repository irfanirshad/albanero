from flask import Flask, request, jsonify
from confluent_kafka import Consumer
from kafka_app.consumer import consumer_start
from pymongo import MongoClient
from pydantic import ValidationError
import threading
from flask_app.models import (
    User,
)  # Assuming your Pydantic models are defined in a 'models.py' module
import json
from bson import json_util

app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]  # Replace 'test_db' with your database name
collection = db["users"]  # Replace 'users' with your collection name


@app.route("/save_data", methods=["POST"])
def save_data():
    try:
        data = request.json
        # validation_data = data.get()
        validated_data = User.model_validate(data)

        document = validated_data.model_dump()  # Convert Pydantic model to dictionary
        collection.insert_one(document)
        return (
            jsonify(
                {
                    "Your input JSON has been successfully validated ... Here's a copy of it": document
                }
            ),
            201,
        )
    except ValidationError as e:
        return (
            jsonify(
                {"An Error occured while validating the data. Please try again": str(e)}
            ),
            400,
        )
    except Exception as e:
        return jsonify({"An error occurred": str(e)}), 500


@app.route("/save_data1", methods=["POST"])
def save_data_new():
    try:
        # Parse JSON data into a Pydantic model
        user = User.model_validate_json(request.data)
        data = user.model_dump()
        # Save the user to the database, etc.
        collection.insert_one(data)

        # Return a JSON response with the user data
        return (
            jsonify(
                {
                    "Your input JSON has been successfully validated ... Here's a copy of it": user.model_dump()
                }
            ),
            201,
        )

    except ValidationError as e:
        # If the JSON data doesn't match the Pydantic model, return a 400 Bad Request response
        return jsonify({"error": str(e)}), 400


@app.route("/get_all_data", methods=["GET"])
def get_all_data():
    try:
        all_data = list(collection.find({}))
        data = json_util.dumps(all_data)
        data1 = json.loads(data)
        return data1, 200
        # return jsonify({"The dacollection is" : all_data}), 200 # bson not compatible with jsonify
    except Exception as e:
        return jsonify({"An error occurred": e}), 500


if __name__ == "__main__":

    kafka_thread = threading.Thread(target=consumer_start)
    kafka_thread.start() 

    app.run(debug=True,port =8000 )

