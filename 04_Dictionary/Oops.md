# Oops in Python

## What is OOP
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data in the form of fields (often known as attributes or properties) and code, in the form of procedures (often known as methods).

## Pillars of OOP
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

### Class
A class is a blueprint for creating objects.
```python
class Dog:
    pass
```

### Object
An object is an instance of a class.
```python
dog = Dog()
```

### Attributes
Attributes are variables that belong to a class or an object.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog("Buddy", 3)
print(dog.name)  # Output: Buddy
```

### Methods
Methods are functions that belong to a class or an object.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

dog = Dog("Buddy", 3)
dog.bark()  # Output: Woof!
```

### Self
The self keyword is used to refer to the current object.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog("Buddy", 3)
print(dog.name)  # Output: Buddy
```

### Inheritance
Inheritance is a mechanism by which one class can inherit the attributes and methods of another class.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")
```

#### Types of Inheritance

##### Single Inheritance
A class can inherit from a single parent class.
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")
```


##### Multiple Inheritance
A class can inherit from multiple parent classes.
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal, Cat):
    def speak(self):
        print("Woof!")
```

##### Multilevel Inheritance
A class can inherit from a class that has inherited from another class.
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Dog):
    def speak(self):
        print("Meow!")
```

##### Hierarchical Inheritance
A class can be inherited by multiple classes.
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")
```

##### Hybrid Inheritance

Hierarchical + Multiple = Hybrid Inheritance
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class DogCat(Dog, Cat):
    def speak(self):
        print("Woof!")
```

### Polymorphism
Polymorphism is the ability of an object to take on many forms.
```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")
```