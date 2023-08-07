### urls:

1. logging flow - https://docs.python.org/3/howto/logging.html#logging-flow

### Logging 

Libraries like logstash

Plain old logging library 
ELK 


#### Logger Real Python

for example:

```import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
```


### Logger Essentials in Classes 

You should define your own logger by creating an object of the logger class

4 modules to took care of:

- Logger: This is the class whose objects will be used 
 
- LogRecord: Loggers automatically create LogRecord objects which will contain all info like
logger name, errorlog, function_name, line_number etc..  

- Handler: This handler function is responsible for sending/transporting the log to the server or in the system eg. sys.stdout or some disk location/folder etc. 
Handler is a base class for subclasses like StreamHandler, FileHandler, HttpHandler, SMTPHandler etc..


- Formatter: Where you specify the string format...  



### Logger Python Docs

Can pickle up objects before sending them over wire, say from a socketconnection....

#### logger objects..

#### lOGGING LEVELS

lOGGING levels ...Can be used with specific handlers.. 

#### Handlers

### Filters


