from confluent_kafka import Consumer
from rough_2_consumer import consumer_start
from pymongo import MongoClient
from pydantic import ValidationError
import threading
import json
from bson import json_util
from ascii_arts import ASCII_ART
import time
from termcolor import colored

# Configure MongoDB connection
# client = MongoClient("mongodb://localhost:27017/")
# db = client["test_db"]  # Replace 'test_db' with your database name
# collection = db["users"]  # Replace 'users' with your collection name



if __name__ == "__main__":
    # cool ascii art
    print(colored(f"{ASCII_ART} ", 'magenta', attrs=["bold"]))
    print(colored(f"Maximum Thread Control 75 \n \n ", "magenta", attrs=["bold"]))
    # INPUT_THREAD = input(colored(f"Enter", "magenta", attrs=["bold"]))
    time.sleep(1)
    consumer_start()
    # consumer_main(INPUT_THREAD) # pass ni user ipnut 


