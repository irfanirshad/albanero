## Lists


### List 
```
fruits = ['apple', 'banana', 'orange', 'pear', 'kiwi', 'banana', 'apple']

1. fruits.count('apple') #2
2. fruits.index('banana') #1   #returns the first index of found banana
3. fruits.index('banana', 1 ) #5 # find the index of next banana starting from index 1
4. fruits.reverse()
5. fruits.sort() # sorts it
6. fruits.pop() # pops last element
```

### Lists as Stacks

```
stack = [3,4,5]
stack.append(6) # [3,4,5,6]
stack.pop() # [3,4,5]

```


###  Lists as Queues

```
from collections import deque

queue = deque(['Eric, 'Irfan', 'Sagar'])
queue.append("Terry")
queue.append("Graham")

queue.appendleft("Zoo)
queue.popleft() #Sagar
queue #(['Zoo', 'Eric, 'Irfan'])
```

### List Comprehensions
```
squares = []
for x in range(10):
    squares.append(x**2)

Above 3 lines is equivalent to below line 

squares = [x**2 for x in range(10)]
```

Tuples in list comprehension must be paranthesized

```
t = [(x, x+1) for x in range(10)]
```

Flattening a lst using list
```
vec = [[1,2,3]. [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
```
would print out 
[1,2,3,4,5,6,7,8,9]

List comprehesions can contain complex expressions and nested functions:
```
from math import pi 
[str(round(pi,i) for i in range(1,6))]
```


### Nested list 
Consider a 3x4 matrix implemented as 3 lists of length 4

```matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns:


[[row[i] for row in matrix] for i in range(4)]

```

which is equivalent to 

```transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed```


IRL you should use built-in functions to complex flow statements . 

```
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list(zip(*matrix))
```


### del statement

Its different from pop() as del does not return a value..

It can also be used to remove slices from a list

del a[2:4]


### Sets

Sets is an unordered collection with no duplicate items.
Basic uses of sets include:
    - Membership testing
    - Eliminating duplicate entries
    - Support mathematical operations like union, intersection, difference, symmetric difference

To create an empty set use set() and not {}..
Can create an initiliazed set with {} like

```
basket = {'apple' , 'banana' , 'orange'}
flag = 'apple' in basket # Fast membership testing


# set operation on unique from two words
a = set('abracadabra')

# unique letters in a
print(a) # {'a', 'r', 'b', 'c', 'd'}

b = set('alacazam')

# letters in a but not in b
print(a - b) # {'r', 'd', 'b'}

# letters in a or b or both
print(a | b)

# letters strictly in a and b
print(a & b)

# letters in a or b but not both
print(a ^ b) # {'r', 'd', 'b', 'm', 'z', 'l'}
```






### Dictionaries

Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.

```
tel = {'Irfan' : 123, 'Sagar' : 999}

```



### Looping techniques


Enumerate
```
for idx, num in enumerate(nums):
    print(idx, num)
```


Zip
```
for elem1, elem2 in zip(list1, list2):
    print(elem1, elem2)
```

To loop over a sequence in sorted order, use sorted() functions which returns a new sorted list while leaving source unaltered.
```
basket = ['mango', 'apple', 'grape','jackfruit']
for fruit in sorted(basket):
    print(fruit)
```

It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.





### More on Conditions

Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.
```
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null # Trondheim
```


Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other Boolean expression) may be negated with not. These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C. As always, parentheses can be used to express the desired composition.

```
COnsider this...

A and not B or C 

1. (A and (not B)) or C
2. (A and (not B or C)) ? 

Is the 2nd one correct as well? 

```


Note that in Python, unlike C, assignment cannot occur inside expressions. C programmers may grumble about this, but it avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.


### COmparison of Sequence and other Types


Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted.

If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively.

// So matlab if they're 


```
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

```

Note that comparing objects of different types with < or > is legal provided that the objects have appropriate comparison methods. For example, mixed numeric types are compared according to their numeric value, so 0 equals 0.0, etc. Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.