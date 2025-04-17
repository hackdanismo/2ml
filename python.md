# Python

+ [Check Python Version](#check-python-version)
+ [Virtual Environments](#virtual-environments)
+ [Executing Python Code](#executing-python-code)
+ [Comments](#comments)
+ [Variables](#variables)
+ [Data Types](#data-types)
+ [String](#string)
+ [Functions](#functions)
    + [Return](#return)
    + [Lambda](#lambda)
    + [Args](#args)
+ [Conditional](#conditional)
    + [Ternary](#ternary)
+ [Loops](#loops)
    + [For Loop](#for-loop)
    + [While Loop](#while-loop)
+ [List](#list)
+ [Tuple](#tuple)
+ [Dictionary](#dictionary)
+ [Classes](#classes)
+ [Read & Write](#read-and-write)
+ [Import](#import)
    + [Requirements](#requirements)
+ [Try/Catch](#try-catch)
+ [Flask](#flask)
+ [Projects](#projects)
    + [Get Data from an API](#get-data-from-an-api)

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

This will create a `.venv` folder inside of your project. Any Python files (`.py`) should be outside this `.venv` folder.

Before working on a project, activate the environment. Your shell prompt will change to show the name of the activated environment:

```shell
# macOS
$ . .venv/bin/activate

# Windows
> .venv\Scripts\activate
```

We can now install packages using `pip`. When a package is installed, it is added to the `.venv/lib` folder inside the project. In the following example, `Flask` will be installed.

```shell
$ pip3 install Flask
```

The version can then be checked.

```shell
$ flask --version
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

It's recommended to separate words for variables and functions with underscores.

```python
first_name = "Dan"
```

## Data Types
Here are a list of `data types` in Python:

+ `String` - "Hello"
+ `Integer` (whole numbers) - 12345
+ `Large Integer` - 342,654,896
+ `Float` - (numbers with decimal places - floating point number) - 1.2 
+ `Boolean` - True/False

## String
We can use an `f string` to allow values to be placed inside of a string.

```python
name = "Dan"

print(f"Hello {name}")
```

To return the first letter of a string, in this example the value returned would be `"H"`:

```python
print("Hello"[0])
```

The `len()` function can be used to return the number of characters in a string:

```python
print(len("Hello"))
```

Convert a number to a string using the `str()` function and convert it to a float using the `float()` function:

```python
x = str(12345)
print(x)

y = float(12345)
print(y)
```

We cannot concatenate (join) strings and integers together initially. To check the `type`:

```python
x = str(12345)

# This will return <class 'str'> as the number is a string
print(type(x))
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

### Lambda
A `lambda` function in Python is an anonymous (unnamed) function defined with a lambda keyword. It is typically used for short, throwaway functions. Often we don't need to then use a return statement. The syntax:

```python
lambda arguments: expression
```

An example:

```python
add = lambda x, y: x + y
print(add(3, 5))

# This is the same as:
def add(x, y):
    return x + y
```

We don't use lambda functions if the function has more than one expression and if readability is more important than being concise.

### Args
In Python, `*args` is used to allow a function to accept a number of arguments when we don't know beforehand how many arguments will be passed into the function. All arguments that are passed into `*args` are returned as a tuple. This doesn't have to be named `*args`, it can be named whatever we prefer, but `*args` is usually the standard naming convention.

```python
def my_function(*args):
    # Code within the function
```

An example:

```python
def greet_all(*args):
    for name in args:
        print(f"Hello, {name}")

# Call the function and pass multiple arguments
greet_all("Dan", "Pearl", "Sammy")
```

It is often used alongside `**kwargs`, which captures keyword arguments as a dictionary.

```python
def show_info(*args, **kwargs):
    print("Positional arguments (args):")
    for arg in args:
        print(f"- {arg}")

    print("\nKeyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

# Call the function and pass multiple arguments
show_info("apple", "banana", color="red", size="large")
```

+ `"apple"` and `"banana"` are collected into `args` as a `tuple`.
+ `color="red"` and `size="large"` are collected into `kwargs` as a `dictionary`.

This pattern is super useful when you want your functions to be flexible and handle all kinds of input.

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

### Ternary
A `ternary` (inline) conditional can be used in-place of a traditional `if/else` statement.

```python
# Example
status = "ok" if 200 <= code < 300 else "error"

age = 18
adult = "You are an adult." if age >= 18 else "You are not yet an adult."
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

### While Loop
A while loop is used to repeat a block of code as long as a certain condition is true.

```python
while condition:
    # Code to run
```

An example that starts printing the count at `1`, adds 1 to the count and repeats the count until it no longer is less or equal to `5`:

```python
count = 1

while count <= 5:
    print("Count is: ", count)
    count += 1
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

## Tuple
A tuple is similar to a list, but it is immutable, meaning it cannot be modified or changed (no adding/removing or changing of items). It is ordered and items inside a tuple can be accessed using an index. Duplicates are allowed, so a tuple can contain repeated values.

A tuple is generally quicker than a list and uses less memory. This is useful for constant data that will not change. 

```python
my_tuple(1, "Hello", 3.14)

# This will print "Hello"
print(my_tuple[1])
```

We can use a tuple to return multiple items from a function.

```python
def get_user():
    return("Dan", 30)

# This is a tuple
name, age = get_user()

print(name)
print(age)
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

## Read and Write
To write to a file in Python:

```python
# This will create a new file or overwrite and existing one
with open("example.txt", "w") as file:
    file.write("Hello, World\n")
    file.write("This is a new line.\n")

# This will append to the file, will not overwrite
with open("example.txt", "a") as file:
    file.write("Adding more content to the end of the file.\n")
```

To read a file:

```python
# Read the entire file as a string
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Read the file line by line
with open("example.txt", "r") as file:
    for line in file:
        # strip() removes the new line characters from the file content
        print(line.strip())
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

### Requirements
If we have a `requirements.txt` file in our project folder, we can install the packages/modules/libraries needed using `pip`. The `requirements.txt` file may look like this:

```
flask==2.3.3
requests>=2.25.0
pandas
numpy<2.0
```

To install, we run:

```shell
$ pip3 install -r requirements.txt
```

## Try Catch
In Python, `try/catch` blocks are used to handle exceptions (errors) gracefully. This is so a program doesn't crash when something goes wrong.

```python
try:
    # Code that might raise an error/exception
except SomeException as e:
    # Code that runs when an error/exception occurs
```

## Flask
We are using `Flask` to create a simple route. This is in a file named `app.py`.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

To run:

```python
$ python3 app.py
```

This will run a development server at `http://127.0.0.1:5000` which can be opened in a browser window/tab.

## Projects

### Get Data from an API
The following Python script can be used to return `JSON` data from an `API`. This uses the `requests` package that will need to be installed.

```shell
$ pip install requests
```

The Python code is as follows:

```python
# Import the package/module needed. This is importing the requests package
import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Make a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Print the first three items
    print(data[:3])
else:
    print(f"Failed to retrieve data: {response.status_code}")
```
