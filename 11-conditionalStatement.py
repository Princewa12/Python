# if-else syntax
a = 5
b = 3
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


# if-elif-else syntax
a = 5
b = 5
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")

# Nested if-else syntax 
a = 5
b = 5
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
    if a % 2 == 0:
        print("a is even")
    else:
        print("a is odd")