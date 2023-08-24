from confluent_kafka import Consumer, KafkaError
import concurrent.futures
import typing
import json

import threading
import time

from termcolor import colored

# from ascii_arts import kafka_kitty



ACTIVE_THREAD_COUNT = 0


executor = concurrent.futures.ThreadPoolExecutor(max_workers=16)



# Define the semaphore and timer
max_thread_count = 16
thread_count_semaphore = threading.Semaphore(max_thread_count)
pause_interval = 2  # seconds



def message_handler(message):
    global ACTIVE_THREAD_COUNT
    with thread_count_semaphore:
        # Your message processing logic here
        try:
            ACTIVE_THREAD_COUNT += 1
            print(f"Active threads: {ACTIVE_THREAD_COUNT} ")
            current_thread = threading.current_thread()
            print(colored(f"Thread {current_thread.name} \n (ID: {current_thread.ident}) \n is processing message: {message.decode('utf-8')} \n", 'light_yellow', attrs=[]))
            time.sleep(0.5)  # Simulating processing time
        finally:
            # Decrease the active thread count when finished
            ACTIVE_THREAD_COUNT -= 1

def consumer_start():
    '''
    Control flow goes like this:
        1. While true loop, we keep polling/consuming messages and using threadpools, we assign messages to threads to do post_processing.
        2. Once we hit the limit, we call consumer.pause() where we're essentially waiting for our threads to come back up ...
        3. When condition 'MTC75' is hit, consumer enters a paused state until it's 'cured'. 
        4. Keyboard Interrupt will handle shutting down in a graceful manner where we wait for all our exectutor to shutdown ...
    '''
    bootstrap_servers = "kafka-1:9092"
    topic = "my-topic1"
    
    consumer = Consumer({
        "bootstrap.servers": bootstrap_servers,
        "group.id": "my-group",
        "auto.offset.reset": "earliest",
    })
    
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
                print("Record submitted for processing")
            except Exception as e:
                print(f"An Error has occurred: {e} . \n Please try again.")
            else:
                # print("Everything working good")
                pass
            finally:
                print("Consumed && Moving onto next record \n")

            # What is thread_count_semaphore._value?
            # Tells us if all threads are currently occupied .
            '''
             ._value is the number of permits available for acquiring the semaphore meaning the number of free threads in the 'ThreadPoolExecutor'.
            So, if thread_count_semaphore._value == 0, it means there are no free threads available for running tasks and you have reached the max
            capacity of thread pool.'''

            if thread_count_semaphore._value == 0: 
                print(colored(f"Pausing due to thread count or high active threads. Pausing for {pause_interval} seconds...", 'blue', attrs=["bold","blink"]))
                consumer.pause(consumer.assignment())  # Pause the consumer 
                while ACTIVE_THREAD_COUNT <= max_thread_count * 0.5:
                    time.sleep(1)  #check every 2 secs 
                consumer.resume(consumer.assignment())   # Resume the consumer 
                print(colored("All threads are now free. Resuming consumer. WE'RE BACK IN THE GAME", 'light_cyan', attrs=["bold","underline"]))
                continue
    except KeyboardInterrupt:
        pass
    finally:
        print(colored("Waiting for the executor to shut down all threads.....", 'red', attrs=["bold"]))
        executor.shutdown(wait=True)
        consumer.close()



def consumer_main(INPUT_THREAD):
    '''
    1. Initialize the number of threads you want to run
    2. Call consumer_start() and stay indefintely until KeyboardInterrupt.
    # TODO: 
    '''
    pass

