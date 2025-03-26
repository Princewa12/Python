# WAP to find sum of n natural numbers
# using for loop
n = int(input("Enter the number:"))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum is ", sum)

# by using while loop
n = int(input("Enter the number:"))
sum = 0
i = 1
while i <= n:
   sum += i
   i += 1
print("Sum is ", sum)



# WAP to get factorial of number n.
n = int(input("Enter the number :"))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    i += 1
print("Factorial is", factorial)