from confluent_kafka import Consumer
from MTC75_consumer import consumer_start
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
    # INPUT_THREAD = input(colored(f"Enter the number of threads do you wish to play with ? ", "magenta", attrs=["bold"]))
    time.sleep(1)
    consumer_start()
    # consumer_main(INPUT_THREAD) # pass ni user ipnut 




'''
Questions to think about ....( or maybe my inner paranoia speaking here..)
(Either way , they are) A list of QUESTIONS THAT I DON'T KNOW THE ANSWER TO ....
(but glad that my subconscious mind has thrown me these thoughts to ponder about...)



1. What happens when my KAFKA TOPIC is FULL... //kafka heap problems when scaling up -> deep dive 
    i) increase my RAM ? [read that kafka 6GB heap equals to 30-32GB... bookmarked some links on chrome/ff on this..]
2. Multiple consumer thread workers / processes? //kafka architecture OPEN_ENDED questions
    i) Architectures of this? Is it like multiple worker threads per partition 
    (acc to confluent page . LINK: https://www.confluent.io/blog/kafka-consumer-multi-threaded-messaging/ )
3. More on what breaks KAFKA topics? Where is it not used for? //DONT USE KAFKA if you're intentions are _____ 
    i) Other than real-time-chat apps(in a pub-sub context), where else is it not suitable? (use redis instead. )
    ii) Other than latency stuff, where else does kafka not perform well compared to other solutions.... 
    (FIND kafka DONT-DO's )

GL.HF.
'''