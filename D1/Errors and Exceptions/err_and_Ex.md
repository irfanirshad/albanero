## Errors and Exceptions
aTLEAST 2 DISTINGUISHABLE KINDS OF ERRORS:
    - Syntax Errors
    - Exceptions

### Syntax Errors

eg: Indentation Error(invalid syntax)


### Exceptions

Even if a statement or expression is syntactically correct, it may cause
an error when an attempt is made to execute it. 
Errors detected during execution are called esceptions and are not unconditionally fatal. 

Most exceptions are not handled by programs, however and result in error messages as shown here...

```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```

The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers.


Built-in Exceptions lists the built-in exceptions and their meanings.



### Handling Exceptions

```
while True:
    try:
        x = int(input("Please enter a number"))
        break
    except ValueError:
        print("OOps! Try again")
```

try statements works as follows:
    - First, the try clause is executed.
    - If no exception occurs, the except clause is skipped and execution  of try statement is finished..
    - If an exception occurs during try clause, rest code is skipped...Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.
    - If an execution occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is unhandled exception and execution stops with a message as shown above..


// Nested tries?

```
while True:
    y = 2
    try:
        x = int(input("Please enter a number \n"))
        if x == y:
            print("Correct")
            break
        else:
            print("Oops! not correct gues...Try again...")
    except:
        print("oops WRONG NUMBER ... try again")






while True:
    y = 2
    try:
        x = int(input("Please enter a number: "))
        if x == y:
            print("Correct!")
            break
        else:
            print("Oops! Try again?")
    except ValueError:
        print("Oops! That was not a valid number. Try again...")




//spot the bad code?


while True:
    y = 2
    try:
        x = int(input("Please enter a number \n"))
        break
    except:
        print("oops. Not valid number..try again")


```



A try statement may have more than one except clause for different exceptions..

```
... except (Runtime, TypeError, NameError)
        pass
```


