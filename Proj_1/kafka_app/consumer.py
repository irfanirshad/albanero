from confluent_kafka import Consumer, KafkaError

bootstrap_servers = 'kafka-1:9092'


consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})

topic = 'my-topic'

consumer.subscribe([topic])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        print(msg.error())
        break

    print(f"Consumed: {msg.value().decode('utf-8')}")


'''
TODO: add a pymongo connector here (or connection pool) and use it to save to DB
'''