# Python Functions

""" We can provide a default value to an argument by using the assignment operator (=). Here is an example."""

def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)
   print("Hello "+ name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")

# Python Arbitrary Arguments

"""Sometimes, we do not know in advance the number of arguments that will 
    be passed into a function.Python allows us to handle this kind of situation through 
    function calls with arbitrary number of arguments.
    In the function definition we use an asterisk (*) before 
    the parameter name to denote this kind of argument. Here is an example.
"""

def greet(*names):
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")

# lambda functions
"""
    In Python, anonymous function is a function that is defined without a name.
    Lambda functions can have any number of arguments but only one expression.
     The expression is evaluated and returned. 
    Lambda functions can be used wherever function objects are required.
    Generaly Use with filter() and map() functions
"""

double = lambda x: x * 2
print(double(5))

# filter function
# The filter() function in Python takes in a function and a list as arguments.

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)

# map Function
# The map() function in Python takes in a function and a list.

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
