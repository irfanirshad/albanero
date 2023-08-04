### Getters and Setters...
Does one use getters and setters like in Java,C++ or use Python way of instance.variable (direct access) ?


### Class objects

### Method Objects

### Instance Objects  


### Multiple Inheritance 

Python solved diamond problem . Supports multiple base classes

```
class A:
    def do():
        print("DO A")

class B(A):
    def do():
        print("DO B")

class C(B):
    def do():
        print("DO C")

class D(A,B,C):
    pass
```

Look more into super()