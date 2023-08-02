# Control Flow
### url: https://docs.python.org/3.7/tutorial/controlflow.html


## Control Flow

### if statements

If looping over a list that you wish to mutate then , use a copy then

```
for word in words[:]:
    if len(word) > 4:
        words.insert(0, word)
```

### break, continue 

## Functions

### Default Argument Values
```
i = 5
def f(arg=i):
    print(arg) 
i = 7
f() 
'''
Calling this function will print out 5.
This is because the default values are evaluated at the point of function definition in the defining scope.
'''
```

'''
The default value is only evaluated once. However, if the default is a mutable object such as a list, dict or class instances, then the default will be shared between subsequent calls and will accumulate.
```
def f(arg, L = []):
    L.append(arg)
    return L
f(1)
f(2)
f(3)
```
This will print out:
    [1]
    [1,2]
    [1,2,3]


If you don't wish to the mutable object to be shared , then simply assign a default value of None to it.

```
def f(arg, L=None):
    if L == None:
        L = []
    else:
        L.append(arg)
    return L
```
'''

### Keyword Args

Functions can also called using Keyword arguments of the form kwarg=value 

```
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

'''
accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be called in any of the following ways:
'''
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

The below calls are invalid though...
```
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```

'''

'''
Notice the difference when we have *args and **kwargs in a function ; with **kwargs, we can use dictionary containing all 
keywords arguments.
YOu now have the option to combine this with *args 
```
def shop_roleplay(name, *args, **kwargs):
    print(f"Customer: Do you have any kind of {name} in stock today?")
    print(f"ShopKeeper: No Sir, We're sorry . WE do not have any kind of {name} with us right now.")
    print(f"Customer: I really need a {name} right now. Please consider making one for me this moment.")
    print(f"But sir \n ")
    for arg in args:
        print(arg)
    print("I'm not the only one who says so .... Take a look at the other shopkeeper who claim the same as me!")
    for kw in kwarg:
        print(kw, : , kwargs[kw])
```


It could be called like this:

```

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```
'''


### Unpacking Argument Lists
The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the * operator to unpack the arguments out of a list or tuple:

```
list(range(3,6))

-> [3,4,5]

# here range() needs a start and stop to call it 
# what the docs guide is conveying is that we can unpack the start and stop from our *args and pass it into the range() function to use it

args = [3,6]
list(range(*args))
```

Same can be used with **kwargs
Here we are passing an initialized dictionary inside of a function (assuming same number of arguments) and then using the **  operator to unpack it .

```
def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

O/P = This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```


### Lambda Expressions

Small anonymous functions can be created with the lambda keyword.

THis example uses a lambda expression to return a function . 
```
def make_decrement(n):
    return lambda x: x - n

f = make_decrement(42)

f(0) # 42
f(2) # 40
```

'''
The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:

pairs = [(1, 'one'), (2, 'two'), (5, 'five')]
pairs.sort(key=lambda pair: pair[1])
pairs
'''

### Documentation Strings

def documented_function(*args, **kwargs):
    """ Well 


### Function Annotations:


