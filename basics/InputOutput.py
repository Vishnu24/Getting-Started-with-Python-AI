# Printing on Console

"""
The actual syntax of the print() function is
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
objects : is the value(s) to be printed.
sep separator is used between the values. It defaults into a space character.
After all values are printed, end is printed. It defaults into a new line.
The file is the object where the values are printed and its default value is sys.stdout (screen).
"""

print(1,2,3,4)
print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
# Hello John, Goodmorning

# Operators

# Identity operators
"""is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory.
 Two variables that are equal does not imply that they are identical."""
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

# Membership operators
"""in and not in are the membership operators in Python. 
They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
In a dictionary we can only test for presence of key, not the value.
"""

x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)