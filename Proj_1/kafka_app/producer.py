"""the input should be in camelcase format, and the code should convert it to snake_case format for validation using
Pydantic. If the validation passes, the code should convert the input back to camelcase and
send it to a consumer.
"""

from confluent_kafka import Producer

bootstrap_servers = 'kafka-1:9092'

producer = Producer({'bootstrap.servers': bootstrap_servers})

topic = 'my-topic'

for i in range(10):
    value = f"Message {i}"
    producer.produce(topic, value.encode('utf-8'))
    producer.flush()

    print(f"Produced: {value}")





'''
Over here we'll feed it fake data using Faker Module and we'll have a list of 
valid data which will pass validation and a another list which wont and we 
Eg:
    correct_data = 

'''

'''
TODO:# The comment is describing a task to be performed. It suggests that the input should be in
# camelcase format, and the code should convert it to snake_case format for validation using
# Pydantic. If the validation passes, the code should convert the input back to camelcase and
# send it to a consumer.
get in camelcase input and perform pydantic validation(convert to snake_case i guess? and then perform pydantic validation ) and if it passes
then convert it back to camelcase and then send it to consumer 

'''