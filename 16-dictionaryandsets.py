# # Dictionaries are used to store data values in key:value pairs.
# # A dictionary is a collection which is unordered, changeable and indexed. 
# # In Python dictionaries are written with curly brackets, and they have keys and values.

# dict = {
#     "name": "Prince",
#     "age": 28,
#     "city": "Bengaluru",
#     "is_adult": True,
#     "is_student": False,
#     "Marks": [80, 90, 95],
# }

# print(dict)

# print(dict["name"])
# print(dict["Marks"])

# dict["name"] = "Prince Kumar"
# print(dict)

# dict["surmane"] = "Srivastava" # Adding new key value pair
# print(dict)

# dict.pop("surmane") # Removing key value pair
# print(dict)

# Nested Dictionary
myfamily = {
    "me": {
        "name": "Prince",
        "age": 28
    },
    "wife": {
        "name": "xyz",
        "age": 24
    },
    "child": {
        "name": "ZZZZ",
        "age": 20
    }
}

print(myfamily)
print(myfamily["wife"]["name"])

# Dictionary Methods
print(myfamily.keys())
print(myfamily.values())
print(myfamily.items())
print(len(list(myfamily.keys())))
print(myfamily.get("me"))
print(myfamily.items())

# Adding Items
myfamily["mother"] = {
    "name": "ABC",
    "age": 50
}
print(myfamily)

# Another way to add items
myfamily.update({"father": {
    "name": "DEF",
    "age": 55
}}) 
print(myfamily)

# Removing Items
myfamily.pop("child")
print(myfamily)

# Copy a Dictionary
myfamily2 = myfamily.copy()
print(myfamily2)



# Sets
# A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets.
# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.


