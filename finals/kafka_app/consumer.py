from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient
import json

bootstrap_servers = 'kafka-1:9092'

client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]  # Replace 'test_db' with your database name
collection = db["users"]  # Replace 'users' with your collection name

consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})

topic = 'my-topic'

consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            print(msg.error())
            break

        value = msg.value().decode('utf-8')
        print(f"Consumed: {value}")

        try:
            message_data = json.loads(value)
            collection.insert_one(message_data)
            print("Record successfully saved to MongoDB")
        except json.JSONDecodeError:
            print("Invalid JSON. Please try again.")
        else:
            print("")

except KeyboardInterrupt:
    pass # if catches it will move on to finally block ... a little graceful exit

finally:
    consumer.close()


'''
TODO: add a pymongo connector here (or connection pool) and use it to save to DB
'''