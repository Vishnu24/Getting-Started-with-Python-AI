
# Flow Control

""" The if elif else statement is used in Python for decision making
"""

# In this program, we input a number
# check if the number is positive or
# negative or zero and display
# an appropriate message
# This time we use nested if

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# range() function
"""We can generate a sequence of numbers using range() function. 
range(10) will generate numbers from 0 to 9 (10 numbers).
We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.
"""

# Output: range(0, 10)
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))

"""
We can use the range() function in for loops to iterate through a sequence of numbers. 
It can be combined with the len() function to iterate though a sequence using indexing. Here is an example.
"""

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])

"""
A for loop can have an optional else block as well.
 The else part is executed if the items in the sequence used in for loop exhausts.
"""

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

# While Loop with else
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1

else:
    print("Inside else")

# Python paas statement
"""
In Python programming, pass is a null statement. 
The difference between a comment and pass statement in Python is that,
 while the interpreter ignores a comment entirely, pass is not ignored.
However, nothing happens when pass is executed. It results into no operation (NOP).
"""

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
print("Pass Completed")