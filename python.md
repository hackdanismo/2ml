# Python

+ [Check Python Version](#check-python-version)
+ [Executing Python Code](#executing-python-code)
+ [Variables](#variables)
+ [Functions](#functions)
+ [Array](#array)

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
