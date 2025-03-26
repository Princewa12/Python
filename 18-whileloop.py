# while loop in python
# while loop is used to iterate over a block of code as long as the test expression is true.
# while loop is used when the number of iteration is not known in advance.
# iterration is the variable that is used to iterate over the block of code.
# While condition:

count = 1
while count <=5:
    print(count)
    count += 1
print(count)

# WAP to print the numbers from 10 to 1 using while loop.
count = 10
while count >= 1:
    print(count)
    count -= 1

# WAP to print the numbers from 1 to 10 using while loop.
count = 1
while count <= 10:
    print(count)
    count += 1

# print a multiplication table of a number n using while loop.
n = int(input("Enter the number:"))
i = 1
while i <= 10:
    print(n, "X", i, "=", n*i)
    i += 1

# WAP to print the elements of below list using while loop.
# list = [1,4,9,16,25,36,49,64,81,100]

i = 1
while i <= 10:
    print(i*i)
    i += 1

# another way (traversing the list)
list = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(list):
    print(list[index])
    index += 1


# WAP to find the maximum number from a list of numbers using while loop.


list = [1,4,90,16,205,316,490,64,81,100]
i = 0
largest_number = 0
while i < len(list):
    if list[i] > largest_number:
        largest_number = list[i]
    i += 1
print("Largest number is:", largest_number)

# Break statement in while loop
# The break statement is used to terminate the loop prematurely.

# WAP to print the numbers from 1 to 10 using while loop. If the number is 5, then break the loop.
count = 1
while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1
print("Loop is terminated")

# Continue statement in while loop
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only.

# WAP to print the numbers from 1 to 10 using while loop. If the number is 5, then skip the number.
count = 1
while count <= 10:
    if count == 5:
        count += 1
        continue
    print(count)
    count += 1
print("Loop is terminated")

# WAP to print odd numbers from 1 to 10 using while loop.
count = 1
while count <= 10:
    if count % 2 == 0:
        count += 1
        continue
    print(count)
    count += 1

# WAP to print even numbers from 1 to 10 using while loop.
count = 1
while count <= 10: 
    if count % 2 != 0:
        count += 1
        continue
    print(count)
    count += 1

# Else statement in while loop
# The else statement is used to run a block of code when the entire loop has been executed.

# WAP to print the numbers from 1 to 10 using while loop. If the number is 5, then break the loop.
count = 1
while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1
