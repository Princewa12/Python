# automatic type conversion
a = 2 #integer
b = 3.4 #float
sum = a+b
print(sum)
print(type(a)) #type of a
print(type(b)) # type of b
print(type(sum)) # type of sum

# error
# sum = a + name
c = "2" #string
d = 3.4 #float
sum = c+d
print(sum)
print(type(c)) #type of c
print(type(d)) # type of d
print(type(sum)) # type of sum
# TypeError: can only concatenate str (not "float") to str


# typecasting
e = float(c) #convert string to float (type conversion)
sum = e+d
print(sum)
print(type(e)) #type of e
print(type(sum)) # type of sum