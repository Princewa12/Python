# for loop in python
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Syntax:
# for element in sequence:
#     body of for
# Here, element is the variable that takes the value of the item inside the sequence on each iteration.

numb = [1, 2, 3, 4, 5]
for i in numb:
    print(i)

veggies = ['potato', 'tomato', 'onion', 'carrot']
for veg in veggies:
    print(veg)

tup = (1, 2, 3, 4, 5, 4, 3, 6, 5)
for i in tup:
    print(i)

# Iterating over a string
str = "Hello word"
for char in str:
    print(char)

# Iterating over a dictionary
dict = {'name': 'Prince', 'age': 28, 'job': 'Developer'}
for i in dict:
    print(i)

# Iterating over a dictionary using items() method
dict = {'name': 'Prince', 'age': 28, 'job': 'Developer'}
for key, value in dict.items():
    print(key, value)

# Iterating over a dictionary using values() method
dict = {'name': 'Prince', 'age': 28, 'job': 'Developer'}
for val in dict.values():
    print(val)

# WAP to print the sum of all the numbers in a list
list = [1, 2, 3, 4, 5]
sum = 0
for i in list:
    sum += i
print(sum)

# WAP to print the product of all the numbers in a list
list = [1, 2, 3, 4, 5]
prod = 1
for i in list:
    prod *= i
print(prod)

# WAP to search for a number x in this tuple using for loop.
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 5)
x = 5
index = 0
for i in tup:
    if i == x:
        print("Number found", index )
        # break # to stop the loop
    index += 1
        
