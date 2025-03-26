# Test-1: make a calculator to take 2 integer inputs and perform addition, subtraction, multiplication and division on them. The output should be in the following format

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

addition = first + second
subtraction = first - second
multiplication = first * second
division = first / second

# output
print("Addition of", first, "and", second, "is", addition)
print("Subtraction of", first, "and", second, "is", subtraction)
print("Multiplication of", first, "and", second, "is", multiplication)
print("Division of", first, "and", second, "is", division)


# WAP to input side of a square and print its area.

side = int(input("Enter side of square:"))
area = side * side # also can be written as side ** 2
print("Area of square is", area)

# WAP to input 2 float numbers and print their average

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
average = (first_number + second_number) / 2
print("Average of", first_number, "and", second_number, "is", average)

# WAP to input 2 numbers and swap them. (write using both normal logic with temp variable and also the pythonic way).
# Normal logic with temp variable
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
temp = first_num
first_num = second_num
second_num = temp
print("First number after swapping is", first_num)
print("Second number after swapping is", second_num)

# Pythonic way
first_numb = int(input("Enter first number: "))
second_numb = int(input("Enter second number: "))
first_numb, second_numb = second_numb, first_numb
print("First number after swapping is", first_numb)
print("Second number after swapping is", second_numb)

# WAP to input 2 int numbers x and y and print True if x is greater than y, False otherwise.
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print(x > y)