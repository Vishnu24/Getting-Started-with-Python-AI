# Python Numbers
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

# Python Lists

""" List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. 
All the items in a list do not need to be of the same type.
Lists are mutable, meaning, value of elements of a list can be altered.

We can add one item to a list using append() method or add several items using extend() method.
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list

Built In function in List
all()	Return True if all elements of the list are true (or if the list is empty).
any()	Return True if any element of the list is true. If the list is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	Return the length (the number of items) in the list.
list()	Convert an iterable (tuple, string, set, dictionary) to a list.
max()	Return the largest item in the list.
min()	Return the smallest item in the list
sorted()	Return a new sorted list (does not sort the list itself).
sum()	Return the sum of all elements in the list.

"""

a = [5,10,15,20,25,30,35,40,50]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

# append and extend method
a.append(6)
a.extend([11,22])

# Delete 1 to 4 itesm
del a[1:4]
# delet complete List
#def a
# Python Tuples


"""Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. 
Tuples once created cannot be modified.
Tuples are used to write-protect data and are usually faster than list as it cannot change dynamically.
count(x)	Return the number of items that is equal to x
index(x)	Return index of first item that is equal to x

Built in functions
all()	Return True if all elements of the tuple are true (or if the tuple is empty).
any()	Return True if any element of the tuple is true. If the tuple is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
len()	Return the length (the number of items) in the tuple.
max()	Return the largest item in the tuple.
min()	Return the smallest item in the tuple
sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
sum()	Retrun the sum of all elements in the tuple.
tuple()	Convert an iterable (list, string, set, dictionary) to a tuple.
"""

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
#t[0] = 10

# Python Strings
"""Python Strings
String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. 
Like list and tuple, slicing operator [ ] can be used with string. Strings are immutable.
Multi-line strings can be denoted using triple quotes, ''' or """
s = "This is a string"
print (s)
s = '''a multiline'''
print (s)
s = 'Hello world!'
# s[4] = 'o'
print("s[4] = ", s[4])
# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
#s[5] ='d'

#Python Set
"""Set is an unordered collection of unique items. 
Set is defined by values separated by comma inside braces { }. 
Items in a set are not ordered.Since, set are unordered collection, indexing has no meaning. 
Hence the slicing operator [] does not work.

A particular item can be removed from set using methods, discard() and remove().

The only difference between the two is that, while using discard() if the item does not exist in the set, 
it remains unchanged. But remove() will raise an error in such condition.


Similarly, we can remove and return an item using the pop() method.

Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.

We can also remove all items from a set using clear().

add()	Add an element to a set
clear()	Remove all elements form a set
copy()	Return a shallow copy of a set
difference()	Return the difference of two or more sets as a new set
difference_update()	Remove all elements of another set from this set
discard()	Remove an element from set if it is a member. (Do nothing if the element is not in set)
intersection()	Return the intersection of two sets as a new set
intersection_update()	Update the set with the intersection of itself and another
isdisjoint()	Return True if two sets have a null intersection
issubset()	Return True if another set contains this set
issuperset()	Return True if this set contains another set
pop()	Remove and return an arbitary set element. Raise KeyError if the set is empty
remove()	Remove an element from a set. If the element is not a member, raise a KeyError
symmetric_difference()	Return the symmetric difference of two sets as a new set
symmetric_difference_update()	Update a set with the symmetric difference of itself and another
union()	Return the union of sets in a new set
update()	Update a set with the union of itself and others
"""

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)
# data type of variable a
print(type(a))

my_set = {5,2,3,1,4}
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
# Output: random element
my_set.pop()
print(my_set)

# clear my_set
#Output: set()
my_set.clear()
print(my_set)


# Python frozenSet
"""
Python Frozenset
Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. 
While tuples are immutable lists, frozensets are immutable sets.
"""
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print (A)
print (B)
# Python Dictionary
"""
Dictionary is an unordered collection of key-value pairs.

It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. 
We must know the key to retrieve the value.
In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. 
Key and value can be of any type.

We can remove a particular item in a dictionary by using the method pop(). This method removes as item with the provided key and returns the value.

The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. All the items can be removed at once using the clear() method.

We can also use the del keyword to remove individual items or the entire dictionary itself.

clear()	Remove all items form the dictionary.
copy()	Return a shallow copy of the dictionary.
fromkeys(seq[, v])	Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])	Return the value of key. If key doesnot exit, return d (defaults to None).
items()	Return a new view of the dictionary's items (key, value).
keys()	Return a new view of the dictionary's keys.
pop(key[,d])	Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
popitem()	Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d])	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
update([other])	Update the dictionary with the key/value pairs from other, overwriting existing keys.
values()	Return a new view of the dictionary's values

"""

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

print(d.popitem())
d.clear()
del d
# Data Type Conversion
"""We can convert between different data types by using different type conversion functions like int(), float(), str() etc.
"""
print("DATA Conversion")

print(float(5))
print(int(10.6))
print(str(25))
#List To Set
print(set([1,2,3]))
#Set To Tuple
print(tuple({5,6,7}))
# String to lIst
print(list('hello'))
