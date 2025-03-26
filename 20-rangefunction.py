# range function
# range(start, stop, step)  # start is optional, stop is mandatory, step is optional
# range start from 0 by default and step size is 1
# example: range(5)  # 0, 1, 2, 3, 4

seq = range(1, 10)
for i in seq:
    print(i)  

# another way
for i in range(1,10):
    print(i)

# WAP to write even numbers between 0 to 50
for i in range(2, 50, 2):
    print(i)

# WAP to print 1 to 100
for i in range(1,101):
    print(i)

# WAP to print 100 to 1
for i in range(100, 0, -1):
    print(i)

# WAP for multiplication table of a number

x = int(input("Enter a number:"))
for i in range(1,11):
    print(x, "X", i, "=", x*i)

# pass statement
# pass is a null statement that does nothhing. It is used as placeholder for future code. 

for i in range(5):
    if i == 3:
        pass
    else:
        print("Code executed for ", i)
    i += 1
