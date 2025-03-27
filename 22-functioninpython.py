# function in python is block of statement that perform a specific task. 
# inputs are called parameters.

#function definition
def calc_sum(a, b): #parameters 
    return a + b 

sum = calc_sum(2, 5) #function call; argument
print( sum)

# to print hello
def print_hello():
    print("Hello")

print_hello()

# pre-defined functions
# print()
# range()
# len()
# type()

# user defined function
# assigning a default value to parameter, which is used when no argument is passed. 
def calc(a, b=3): #default value can be passed in last parameters only. 
    print(a * b)
    return a * b
calc(4)


# WAF to print the length of a list. 
numbers = [12, 13, 11, 12, 14, 15, 13, 14]
heroes = ["shahrukh", "salman", "hritik", "abhishek", "amir", "akshay"]

def length(list):
    print(len(list))
    return list
length(numbers)
length(heroes)

# WAF to print elements of a list in a single line. 
numbers = [12, 13, 11, 12, 14, 15, 13, 14]
heroes = ["shahrukh", "salman", "hritik", "abhishek", "amir", "akshay"]

def list_el(list):
   for item in list:
      print(item, end=" ")

list_el(numbers)
list_el(heroes)


# WAF to find a factorial of n.
num = int(input("Enter the number :"))

def cal_fact(num):
   fact = 1
   for i in range(1, num+1):
      fact *= i
   print(fact)
    
cal_fact(num)
   

# WAF to convert USD to INR.
INR = float(input("Enter the INR amaount :"))
def USD():
    print("USD is :", INR * 84.5)
    return INR * 84.5
USD()

# WAF to identify number is odd or even. 

num = float(input("Enter the number :"))

def number(num):
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
number(num)


# Recursion
# when a function call itself repeatedly. 

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

show(6)

# WAP to find factorial of n numbers.

n = int(input("Enter the number :"))

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
print(fact(n))
    

# WA recursive function to find sum of na natural numbers. 

n = int(input("Enter the number: "))

def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
print(sum(n))


# WA a recursive function to print all elements in a list.

fruits = ["Apple", "Banana", "Guava", "Orange", "Mango"]

def item(list, idx = 0):
    if (idx == len(list)):
        return
    print(list[idx])
    item(list, idx+1)

item(fruits)

