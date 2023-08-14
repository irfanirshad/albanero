'''
Using curl, 
'''

import subprocess
import random
from faker import Faker
from time import sleep

fake = Faker()

while True:
    name = fake.name()
    age = random.randint(10, 20)

    curl_cmd = f'curl -X POST http://localhost:5000/save_student -u mikoadmin:mikopw -H \'Content-Type: application/json\' -d \'{{ "name": "{name}", "age": {age} }}\''
    
    subprocess.call(curl_cmd, shell=True)
    sleep(5)

"""
curl -X POST \
  http://localhost:5000/save_student \
  -u mikoadmin:mikopw \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "John Doe99",
    "age": 18
}'
"""