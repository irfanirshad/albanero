"""
This script contains a Python application that consumes messages from a Kafka topic
using a KafkaConsumer, processes them, and saves them to a MySQL database using SQLAlchemy.
"""
from kafka.consumer import KafkaConsumer
from json import loads
import json
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import threading
from models.Student import Student


engine = create_engine('mysql+mysqlconnector://newuser1@localhost/miko_students')
Base = declarative_base()
Base.metadata.create_all(engine)  # error fixed 
Session = sessionmaker(bind=engine)
session = Session()

def consume_save():
    """Consume messages from Kafka and save them to the database"""
    consumer = KafkaConsumer('mikostudents', 
                            bootstrap_servers=['localhost:9092'], 
                            api_version=(0, 10),
                            auto_offset_reset='earliest',
                            enable_auto_commit=True,
                            group_id='my-group'
                            #,consumer_timeout_ms=1000
                            )
    
    """The updated_at field will be automatically updated to the current UTC time when the object
      is committed to the database due to the onupdate parameter set in the updated_at field 
      definition in the Student model class."""
    # for message in consumer:
    #     message_data = json.loads(message.value)
    #     print(message_data)
    #     student_obj = Student(name=message_data['name'], age=message_data['age'], created_at=datetime.utcnow())
    #     session.commit()
    #     print("Message added to database:", student_obj)

    for message in consumer:
        message_data = json.loads(message.value)
        print(message_data)
        student_obj = Student(name=message_data['name'], age=message_data['age'], created_at=datetime.utcnow())
        try:
            session.add(student_obj)
            session.commit()
            print("Message added to database:" , student_obj)
        except Exception as e:
            print("Error committing object to database:", e)

def background_consuming():
    """Start a background thread to consume messages from Kafka and save them to the database"""
    t = threading.Thread(target=consume_save)
    t.daemon = True
    t.start()


if __name__ == '__main__':
    background_consuming()
    while True:
        pass
