# Python

+ [Check Python Version](#check-python-version)
+ [Executing Python Code](#executing-python-code)
+ [Comments](#comments)
+ [Variables](#variables)
+ [Functions](#functions)
+ [Array](#array)
+ [Conditional](#conditional)
+ [Classes](#classes)

## Check Python Version
To check the version of `Python` installed, open the terminal:

```shell
$ python3 --version
```

The `PIP` (package installer for `Python`) version can also be checked:

```shell
$ pip3 --version
```

## Executing Python Code
Create a `Python` file containing the source code with the file extension of `.py`. Once the file has been created, execute the code:

```shell
$ python3 filename.py
```

## Comments
Add a comment to the code using a hash (`#`):

```python
# This is a single-line code comment
```

## Variables
Variables are declared like this:

```python
x = 5
y = "Dan"

print(x)
```

## Functions
Functions are declared using the `def` keyword.

```python
def my_function():
    print("Hello, World")

# Call the function
my_function()
```

Values can be passed into the function using `parameters`.

```python
def my_function(firstName):
    print("Hello " + firstName)

# Call the function
my_function("Dan")
```

Multiple parameters:


```python
def my_function(firstName, lastName):
    print(firstName + " " + lastName)

# Call the function
my_function("Dan", "Jackson")
```

## Array
An array can be created like so:

```python
cars = ["Ford", "BMW", "Audi"]

ford = cars[0]
print(ford)

# Use the len method to get the total length of the array (number of items)
arrayLength = len(cars)
print(arrayLength)
```

## Conditional
The basic conditional syntax in Python will look like this:

```python
if condition:
    # Do this condition if true
elif another_condition:
    # Or, do this condition if the first condition is false but this one is true
else:
    # Or, do this if all conditions are false
```

An example would look like this:

```python
age = 18

# Conditional to check if age is equal or greater than the value
if age >= 18:
    print("You are an adult.")
else:
    print("You are not yet an adult.")
```

## Classes
Create a class using the `class` keyword. The name of the class should use `PascalCase` e.g. `MyClass`.

```python
class MyClass:
    # Code within the class is here
```

A `Constructor` method is then added to the class. This runs whenever we create a new `object` from the class.

```python
class MyClass:
    def __init__(self):
        # Code within the constructor method here
```

The keyword of `self` refers to the instance of the class. This is required by all method definitions. 

Default values can be defined in the `constructor` method:

```python
class MyClass:
    def __init__(self, variable_one="value", variable_two="value"):
        # Code within the constructor method here
```

We can create an `object` as an instance of the class:

```python
class MyClass:
    def __init__(self):
        # Code within the constructor method here

# Create an instance (object) of the class
obj = MyClass()
```

We can add `instance variables` inside the `constructor`. These are unique to each object (instance) created.

```python
class MyClass:
    def __init__(self):
        # Instance variables, unique to each object
        self.variable_one = value
        self.variable_two = value

# Create an instance (object) of the class
obj = MyClass()
```

`Methods` are added, which are functions inside of a class.

```python
class MyClass:
    def __init__(self):
        # Instance variables, unique to each object
        self.variable_one = value
        self.variable_two = value

    # Method of a class
    def my_method(self):
        # Code within the method of a class

# Create an instance (object) of the class
obj = MyClass()

# Calling a method inside of a class from the object (instance)
print(obj.my_method())
```

Here's a full example:

```python
class Dog:
    # Set default values for the instance variables if no values are set
    def __init__(self, name="Fido", breed="Mixed"):
        # Instance variables, unique to each object
        self.name = name
        self.breed = breed

    # Method of a class
    def bark(self):
        return f"{self.name} barks"

# Create an instance (object) of the class for each dog
my_dog = Dog("Jack", "Springer Spaniel")
new_dog = Dog("Bailey", "Cocker Spaniel")
# Use default values
other_dog = Dog()

# Calling a method inside of a class from the object (instance)
print(my_dog.bark())
print(new_dog.bark())
print(other_dog.bark())
```
