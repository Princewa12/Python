# list in python
marks = [94.3, 83.4, 78.2, 88.5, 97.2]
print(marks)
print(marks[0])
print(marks[4])
print(type(marks))
print(len(marks))

marks[2] = 90.5 # Update the value of 3rd element
print(marks)

# list slicing
print(marks[1:4])
print(marks[:3])

# list methods
marks.append(99.5)
print(marks)
marks.insert(2, 85.5)
print(marks)
marks.remove(90.5)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)

# list comprehension
squares = [i**2 for i in range(1, 11)]
print(squares)

# list of even numbers
even = [i for i in range(1, 11) if i%2 == 0]
print(even)