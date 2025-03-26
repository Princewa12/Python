# A built-in data type in Python is the tuple. A tuple is a sequence of immutable Python objects. 
# Tuples are sequences, just like lists. 
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

tup = (2, 3, 1, 4, 1)
print(tup)
print(type(tup))
# tup[2] = 5 # This will give an error because tuple is immutable
print(tup[2])


# Tuple with mixed datatypes
tup1 = (1, "Hello", 3.4)
print(tup1)

