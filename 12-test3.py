# WAP to grade student marks based on the following criteria:
# 1. If marks >= 90, grade is A
# 2. If marks >= 80 and < 90, grade is B
# 3. If marks >= 70 and < 80, grade is C
# 4. If marks >= 60 and < 70, grade is D
# 5. If marks < 60, grade is F fail.

marks = int(input("Enter student marks: "))

if marks>=90:
    print("Grade is A")
elif marks>=80 and marks<90:
    print("Grade is B")
elif marks>=70 and marks<80:
    print("Grade is C")
elif marks>=60 and marks<70:
    print("Grade is D")
else:
    print("Grade is F (student is fail)")

# WAP to check if a number is positive, negative or zero.
number = int(input("Enter a number: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")


# WAP to check if a person can drive based on age 18 and above, but also if age is 80 and above, then person cannot drive.
age = int(input("Enter person's age: "))
if age >= 18: # also can be written as if age >= 18 and age < 80:
    print("Person can drive")
    if age >= 80:
        print("Person cannot drive")
else:
    print("Person cannot drive")

# WAP to check if a number is even or odd, but also if number is divisible by 3, then print "divisible by 3".
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Number is even")
    if number % 3 == 0:
        print("Number is divisible by 3")
else:
    print("Number is odd")
    if number % 3 == 0:
        print("Number is divisible by 3")

# WAP to find the largest number among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c: # also b>=c 
    print("b is the largest number")
else:
    print("c is the largest number")

# WAP to check is a number is a multiple of 5 and 7.
number = int(input("Enter a number: "))
if number % 5 == 0 and number % 7 == 0:
    print("Number is a multiple of 5 and 7")
elif number % 5 == 0:
    print("Number is a multiple of 5")
elif number % 7 == 0:
    print("Number is a multiple of 7")
else:
    print("Number is not a multiple of 5 and 7")