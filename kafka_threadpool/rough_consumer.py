from confluent_kafka import Consumer, KafkaError
import concurrent.futures
import typing
import json

# max_thread_count = 16
# thread_count_semaphore = concurrent.futures.ThreadPoolExecutor(max_workers=max_thread_count)
executor = concurrent.futures.ThreadPoolExecutor(max_workers=16)


def message_handler(message):
    # Your message processing logic here
    # processed_message = process_message(message)
    # store_message(processed_message)
    print("in message HANDLER \n")
    pass


def consumer_start():
    bootstrap_servers = "kafka-1:9092"
    topic = "my-topic1"
    consumer = Consumer(
    {
        "bootstrap.servers": bootstrap_servers,
        "group.id": "my-group",
        "auto.offset.reset": "earliest",
    }
)
    
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

            value = msg.value().decode("utf-8")
            print(f"Consumed: {value}")

            try:
                executor.submit(message_handler, msg.value())
                # message_data = json.loads(value)
                # collection.insert_one(message_data)
                print("Record successfully saved to MongoDB")
            except json.JSONDecodeError:
                print("Invalid JSON. Please try again.")
            else:
                print("Everything working good")

    except KeyboardInterrupt:
        pass  # if catches it will move on to finally block ... a little graceful exit

    finally:
        consumer.close()


def process_message(message):
    # Your message processing logic
    with open('kafka_db.txt', 'a') as f:
        data = jsonify(message)
        print(f.write(data))


def store_message(processed_message):
    # Your message storing logic
    pass

def consumer_start1():
    consumer_start()
