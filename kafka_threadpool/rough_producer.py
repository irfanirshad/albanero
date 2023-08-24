from confluent_kafka import Producer
from faker import Faker
import json
import time
import threading

bootstrap_servers = 'kafka-1:9092'

producer = Producer({'bootstrap.servers': bootstrap_servers})

topic = 'my-topic1'

fake = Faker()

fake_data_list = []

for _ in range(100):  # Increase the number of messages to be produced
    fake_data = {
        "personalDetails": {
            "name": fake.name(),
            "id": fake.random_int(min=1, max=100),
            "phone": fake.random_int(min=1000000000, max=9999999999)
        },
        "address": {
            "id": fake.random_int(min=1, max=100),
            "addressLine1": fake.street_address(),
            "pincode": fake.random_int(min=100000, max=999999),
            "city": fake.city(),
            "state": fake.random_element(elements=["UP", "DLH", "BLR", "WB"])
        }
    }
    fake_data_list.append(fake_data)

def produce_messages():
    for fake_data in fake_data_list:
        value = json.dumps(fake_data)
        producer.produce(topic, value.encode('utf-8'))
        producer.flush()
        print(f"Produced: {value}")

# Use multiple threads to simulate faster message production
threads = []
for _ in range(4):  # Increase the number of threads for faster simulation
    thread = threading.Thread(target=produce_messages)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All messages produced.")
