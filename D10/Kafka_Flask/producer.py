"""
This script contains a Flask application that sends messages to a Kafka topic
using a KafkaProducer.
"""
from kafka.producer import KafkaProducer
import json 
from datetime import datetime
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.Student import Student
import logging



# create a Flask app and an HTTP basic authentication object
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.logger.setLevel(logging.DEBUG)
auth = HTTPBasicAuth()
users = {
    "mikoadmin": "mikopw"
}

# set up database connection
engine = create_engine('mysql+mysqlconnector://newuser1@localhost/miko_students')
Base = declarative_base()
Base.metadata.create_all(engine)  # error fixed 
Session = sessionmaker(bind=engine)
session = Session()



# create a KafkaProducer object
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                         api_version=(0, 10, 1)
)


# initialize a global variable to track the time of the last request
last_request_time = datetime.now()


# define a route for sending messages to Kafka
@app.route('/save_student', methods=['POST'])
def send_message():
    """Added a rate limiter set for 1 request/minute. Returns a 429 if invalid."""
    # use the global variable for the last request time
    global last_request_time

    # get the current time and calculate the time difference since the last request
    current_time = datetime.now()
    time_diff = (current_time - last_request_time).total_seconds()
    """
    1) ratelimiter condition for each request - 60secs
    2) 3 requests/minute
    {req1 ::: 4:11pm}, {req2 ::: 4:11pm}, {req3 ::: 4:11pm}

    dry-run:::
    OK      -> {req1 ::: 4:11pm}, {req2 ::: 4:11pm}, {req3 ::: 4:11pm}, 
    NOT OK  -> {req4 ::: 4:11pm}



    4:30pm => translated to a dictionary represented as {minute:counter} K-V pair 
    inital state -> {11:3} 

    after {req1 ::: 4:11pm}, {req2 ::: 4:11pm}, {req3 ::: 4:11pm} this happens. 
    
    current state -> {11:0} 

    pseudocode:
        - when request comes in , do a dictionary lookup of the minute . 
        - if it doesn't exist, create one and initialize it with value 3. || {11:3}
        - if it does exist, then decrement the count
        
        - if the counter_limiter has exceeded the limit, then return invalid 429 response 



    {count: minute}
    
    SCENARIO1: (not thinking about individual users. only thinking from api-server POV)
        - maintain a global api_rate_limiter_counter = 3 
        - count = 0

        requirements ::
            - 3 requests count per 60 secs. 

    """

    # if the time difference is less than 60 seconds, return an 429 error response else pass
    if time_diff < 2 : # change number to play with the last request time
        return 'Too many requests. Try again later.', 429 
    else:
        # update the last request time to the current time
        last_request_time = current_time
        name = request.json['name']
        age = request.json['age']
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # send the message to the 'mikostudents' Kafka topic and return success response
        producer.send('mikostudents', {'name': name, 'age': age, 'timestamp': timestamp})
        return 'Message sent to Kafka topic'

# define a route for getting information about a single student
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        return jsonify(student.to_dict())
    else:
        return "Student not found", 404
    
# define a route for getting information about all students
@app.route('/students', methods=['GET'])
def get_all_students():
    students = session.query(Student).all()
    student_list = [student.to_dict() for student in students]
    return jsonify(student_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
