# MTC75 - Maximum Thread Control 75 App

This is a sample demo of a kafka-producer-consumer where upon reaching 100% of usage of specified  

## Executor, Max_thread_count , Thread_count_semaphore
  All of these components are needed and serve distinct purposes in managing your threaded processing. Let me explain each of them:
k
    ACTIVE_THREAD_COUNT: This is a variable that presumably tracks the number of threads currently active and processing messages. You can use this to keep a count of how many threads are busy at any given time.

    executor: This is an instance of concurrent.futures.ThreadPoolExecutor, which is responsible for managing the threads that will process your messages concurrently. You submit tasks (in the form of functions) to this executor, and it handles the distribution of these tasks to the available threads.

    thread_count_semaphore: This is a semaphore from the threading module. It's used to control access to a shared resource (in this case, the available threads) to prevent overloading the system. You can think of it as a counter that tracks how many threads are available for executing tasks. When it's zero, it means all threads are busy.

    The semaphore helps you avoid overloading your system with too many threads. When a thread is finished with its work, it releases the semaphore, making it available for another thread to use. The semaphore is initially set to the maximum number of threads you want to allow (max_thread_count in your case).

    pause_interval: This is the time interval for which your consumer will pause if all threads are busy. This allows your system to "catch its breath" if it's overwhelmed with processing.

 All these components are important and serve different purposes. The executor and thread_count_semaphore are not directly dependent on each other, but they work together to manage and control the number of active threads processing messages concurrently. The ACTIVE_THREAD_COUNT seems to be used to track the number of active threads, which can be helpful for monitoring purposes but may not be necessary if you have other ways to check thread availability.


 # How to run this?

Open up 2 terminals . Create the topic using the  ```create topic.py``` script. Then, Install the packages. 
```python3 pip3 install confluent_kafka, faker, termcolor. ``` 

*No virutal env created here..*

1. ```bash python3 MTC75_consumer.py```
Make sure to keep this screen around. There'll be a lot happening on this screen.

<br/>
Now on the 2nd terminal screen...
<br/>

2. ```bash python3 producer.py ```
This will start producing tons of messages/records onto the topic.  


**Play & TWEAK around with the 
1. time.sleep() 
2. producer script upping and lowering the number of messages it can send 
3. Increase and decrease the ```max_thread_count``` **CAUTION: DO THIS AT YOUR OWN RISK. KEEP WATCHING SYSTEM MONITOR**  