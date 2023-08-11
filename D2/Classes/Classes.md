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

Look more into super() trickery 



### Dunder dicts

__dict__ for post mortem accessing ... True immutability not available?


### Slots performance

Around 20% Performance increase using slots .however you gain this at a cost of losing some inbuilt properties/features that python provides like instance dictionary, multiple inheritance problems, dynamic-attribute adding flexibility etc...


### Class methods vs static methods


class methods -(self, cls ) instance 


#### Static methods
   1. Code organization: Sometimes, you have a method that is related to the class, but it doesn't require access to the class or instance-specific state. In such cases, staticmethod provides a cleaner way to organize the code within the class, keeping it logically related to the class without implying a strong dependency on the class itself.

   2.  Improving readability and reducing ambiguity: When you see a staticmethod, you know that the method is not bound to the class or instance and doesn't depend on the class-level state. This can help make the code clearer and reduce confusion for other developers working on the codebase.

   3.  Subclassing: If a method in a base class is static, it is easier to override the method in a subclass without worrying about the cls parameter. This can be useful when you have a utility method related to the class, and you want to provide a different implementation for a subclass without changing the method signature.


### Class methods

1. Alternative Constructors: classmethods are often used to provide alternative constructors for a class. These constructors allow creating instances of the class using different input formats or initializing the object using different parameters. It's useful when you want to provide more flexibility to users while creating objects of the class.

2. Factory Methods: classmethods can also be used to create instances of subclasses or provide objects from a factory class. A factory method encapsulates object creation logic, allowing you to decouple object creation from the client code.

3. Inheriting Class-Level Behavior: When you have a class hierarchy, classmethods can be useful in inheriting class-level behavior. Subclasses can override class methods and provide their own implementation, tailoring the behavior to their specific needs.

```
class Animal:
    legs = 4

    @classmethod
    def show_legs(cls):
        print(f"{cls.__name__} has {cls.legs} legs.")

class Dog(Animal):
    legs = 2  # Overriding class variable

    @classmethod
    def bark(cls):
        print("Woof! Woof!")

# Using class methods
Animal.show_legs()  # Output: Animal has 4 legs.
Dog.show_legs()  # Output: Dog has 4 legs.
Dog.bark()  # Output: Woof! Woof!

```

