# Python

+ [Check Python Version](#check-python-version)
+ [Virtual Environments](#virtual-environments)
+ [Executing Python Code](#executing-python-code)
+ [Comments](#comments)
+ [Variables](#variables)
+ [String](#string)
+ [Functions](#functions)
    + [Return](#return)
+ [Conditional](#conditional)
+ [Loops](#loops)
    + [For Loop](#for-loop)
+ [List](#list)
+ [Dictionary](#dictionary)
+ [Classes](#classes)
+ [Import](#import)

## Check Python Version
To check the version of `Python` installed, open the terminal:

```shell
$ python3 --version
```

The `PIP` (package installer for `Python`) version can also be checked:

```shell
$ pip3 --version
```

## Virtual Environments
Virtual Environments are used to manage the dependencies for a project in development and production. This allows us to use different versions of Python for different projects. Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not impact another project. In Python versions 3.3 and 3.4, `pyenv` was used to create virtual environments. Since Python version 3.6, this has now been replaced by `venv`. The documentation for `venv` can be found [here](https://docs.python.org/3/library/venv.html#module-venv).

Python comes bundled with the `venv` module to create virtual environments.

```shell
# How to setup on macOS:
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv

# How to setup on Windows:
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

Before working on a project, activate the environment. Your shell prompt will change to show the name of the activated environment:

```shell
# macOS
$ . .venv/bin/activate

# Windows
> .venv\Scripts\activate
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

## String
We can use an `f string` to allow values to be placed inside of a string.

```python
name = "Dan"

print(f"Hello {name}")
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

Default parameter values:

```python
def my_function(firstName="Dan"):
    print("Hello " + firstName)

# Call the function, this will use the default parameter value
my_function()
```

### Return
Return values are what a function sends back after it's done executing. It allows a function to produce a result that can be used later. 

```python
def add(x, y):
    return x + y

# Call the function
result = add(10, 15)
# Output the value
print(result)
```

Common uses include returning booleans, for checks, and returning complex objects.

```python
def is_even(n):
    return n % 2 == 0
```

```python
def build_user(name, age):
    return {"name": name, "age": age}
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

## Loops

### For Loop
A for loop is used to iterate over a sequence. The basic syntax of a loop:

```python
for item in items:
    # Do something with item
```

As an example:

```python
fruits = ["Apple", "Banana", "Pear"]

for fruit in fruits:
    print(fruit)
```

We can use the built-in `range()` function to loop over a range of numbers. A `range(5)` would loop over numbers from `0` to `4` (not including `5`). This is used to generate a sequence of numbers.

```python
for i in range(5):
    print(i)
```

A loop can be used on a string:

```python
for letter in "hello":
    print(letter)
```

Using `enumerate()` if we neeed the index and value:

```python
colors = ["Red", "Green", "Blue"]:

for index, color in enumerate(colors):
    print(index, color)
```

## List
A list is an ordered collection of items. Any type of item can be stored in a list. Lists are defined using square brackets. The first item always starts at the index of `0`.

```python
fruits = ["Apple", "Banana", "Pear"]
print(fruits[0])
```

Common operators:

```python
# Add an item to the list
fruits.append("Orange")

# Remove an item from the list
fruits.remove("Orange")

# Change/Edit an item
fruits[1] = "Blueberry"

# Loop through a list
for fruit in fruits:
    print(fruit)
```

## Dictionary
A Dictionary is an unordered collection, similar to an object, of items in key-value pairs. Each value is accessed using its key. A Dictionary is defined using curly braces.

```python
person = {"name": "Dan", "age": 30, "city": "London"}
print(person["name"])
```

Common operators:

```python
# Add or change a key-value pair
person["job"] = "Engineer"

# Remove a key-value pair
del person["age"]

# Loop through the dictionary
for key, value in person.items():
    print(f"{key}: {value}")
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

## Import
We can import code from there sources:

+ Built-in modules like: `math`, `os` and `random`.
+ Standard Library (this comes with Python)
+ Third-party packages/libraries usually installed using `pip`.

```shell
$ pip install package
```

```python
import package
```

An `import` statement allows us to reuse code from other files or libraries. There are built-in modules, third-party libraries, or our own custom code. The following example is a basic import used to import the entire `math` module:

```python
import math

print(math.sqrt(16))        # Use module_name.function() to access
```

To import everything (not recommended as can cause namespace conflicts and pulls eveything into the namespace itself):

```python
from math import *

print(sin(pi / 2))
```

We can import specific functions:

```python
from math import sqrt, pi

print(sqrt(16))
```

An alias can be used:

```python
import numpy as np

print(np.array([1, 2, 3]))
```
