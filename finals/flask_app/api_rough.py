from flask import Flask, request, jsonify
from pymongo import MongoClient
from pydantic import ValidationError
from models import User  # Assuming your Pydantic models are defined in a 'models.py' module

app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

@app.route("/save_data", methods=["POST"])
def save_data():
    try:
        data = request.json
        validated_data = User.parse_obj(data)
        document = validated_data.dict()  # Convert Pydantic model to dictionary
        collection.insert_one(document)
        return jsonify({"message": "Data saved successfully"}), 201
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

@app.route("/get_all_data", methods=["GET"])
def get_all_data():
    try:
        all_data = list(collection.find({}))
        return jsonify(all_data), 200
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=True)


