# Python can be used to perform operations on a file (read, write data)
# types of all files
# 1 - Text files: .txt, .docx, .log etc.
# 2 - Binary files: .mp4, .mov, .png, .jpeg etc. 

# Open a file
# We need to open a file before reading or writing. 
f = open("README.md", "r") #to open a file for read.

data  = f.read() #read a file and store in data variable

print(data)
print(type(data))
f.close() #close the file file

#  mode of file
#  r --> open for reading (default)
#  w --> open for writing, turncating the file first. (vanishes the existing data first)
#  x --> create a new file and open it for writing. 
#  a --> open for writing, appending to the end of the file if it exists. 
#  b --> binary mode. 
#  t --> text mode (default).
#  + --> open a disk file for updating (reading and writing)

# reading a file

f = open("README.md", "r")

data  = f.read(10) # to read 10 characters. 
print(data)

line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)

# writing a file (overwitten)
f = open("README.md", "w")

f.write("This is a new line")
f.close()

# Append a file(add to existing file)
f = open("README.md", "a")
f.write("\n This is an another new line")
f.close()

# we can use r+ for read and write, pointer will be in the begining(without truncate, but overwritten), similarly w+ and a+. 

# with syntax
with open("README.md", "r") as f:
    data = f.read()
    print(data)


# deleting a file. 
# using os module

import os
os.remove(filename)

# create a new file "practice.txt" using python. Add the following data in it. 
# Hi everyone
# We are learning File I/O
# using python
# I like programming in python
with open("practice.txt", "w") as f:
    f.write("Hi everyone \nWe are learning file I/O\n")
    f.write("using python \nIlike programming in python")

# WAF to replace Java with Python in practice.txt

with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# find "learning" in the prctice.txt
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find("learning") != -1): 
        print("Found")
    else:
        print("Not Found")

# WAF to find in which line of the file does the a (input) word occur first.
# print -1 if not found. 
text = str(input("Enter the text :"))
def check_for_word():
    data = True
    line = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.read()
            if (text in data):
                print("Text found in line ", line)
                return
            line += 1
    return "Word not found"
print(check_for_word())

# WAP from a file containing numbers sepearated by comma, print the count of even numbers. 

with open("practice.txt", "r") as f:
    data = f.read()
    num = ""
    for i in range (len(data)):
        if (data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

# here we converted txt to int numbers. 
# now we will find the numbers of even numbers. 

with open("practice.txt", "r") as f:
    data = f.read()
    num = data.split(",")
    count = 0
    for value in num:
        if (int(value) % 2 == 0):
            count += 1
print(count)





