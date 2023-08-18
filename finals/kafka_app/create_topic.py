from confluent_kafka.admin import AdminClient, NewTopic

# Kafka broker configuration
bootstrap_servers = 'localhost:9092'  # Since you're running Kafka in Docker

# Create an AdminClient instance
admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

# Define the topic configuration
new_topic = NewTopic('my-topic', num_partitions=1, replication_factor=1)

# Create the topic
admin_client.create_topics([new_topic])

print("Topic 'my-topic' created.")

