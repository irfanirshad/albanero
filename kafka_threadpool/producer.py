"""the input should be in camelcase format, and the code should convert it to snake_case format for validation using
Pydantic. If the validation passes, the code should convert the input back to camelcase and
send it to a consumer.
"""


from confluent_kafka import Producer
from faker import Faker
import json

bootstrap_servers = 'kafka-1:9092'

producer = Producer({'bootstrap.servers': bootstrap_servers})

topic = 'my-topic1'

# for i in range(10):
#     value = f"Message {i}"
#     producer.produce(topic, value.encode('utf-8'))
#     producer.flush().


#     print(f"Produced: {value}")


fake = Faker()

fake_data_list = []

for _ in range(200):
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

# value = json.dumps(fake_data)
# producer.produce(topic, value.encode('utf-8'))
# producer.flush()

# print(f"Produced: {value}")

for fake_data in fake_data_list:
    value = json.dumps(fake_data)
    producer.produce(topic, value.encode('utf-8'))
    producer.flush()

    print(f"Produced: {value}")
