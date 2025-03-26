# concatination of strings
str1 = "Hello"
str2 = "World"
str3 = str1 + " " + str2
print(str3)

# repetition of strings
str4 = "Hello "
str5 = str4 * 3
print(str5)


# length of a string (number of characters in a string)
str6 = "Hello World"
print(len(str6))

# indexing of strings ()
str7 = "Hello World"
print(str7[0]) # prints H


# slicing of strings (extracting a part of a string)
str8 = "Hello World"
print(str8[0:5]) # prints Hello, also print(str8[:5])
print(str8[6:]) # prints World, also print(str8[6:11])


# check if a string is present in another string
str9 = "Hello World"
print("Hello" in str9) # prints True

# check if a string is not present in another string
str10 = "Hello World"
print("Hello" not in str10) # prints False

