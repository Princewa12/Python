# WAP to enter 3 movies name and store into a list and display the list.

movies = []

movie1 = input("Enter movie1 name: ")
movies.append(movie1)
movie2 = input("Enter movie2 name: ")
movies.append(movie2)
movie3 = input("Enter movie3 name: ")
movies.append(movie3)
print("Movies are: ", movies)

# OR

movie1 = input("Enter movie1 name: ")
movie2 = input("Enter movie2 name: ")
movie3 = input("Enter movie3 name: ")
movies = [movie1, movie2, movie3]
print("Movies are: ", movies)

# WAP to check if a list contains a palindrome of elements or not.
list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]

copy_list1 = list1.copy()
copy_list2 = list2.copy()
copy_list1.reverse()
copy_list2.reverse()

if list1 == copy_list1:
    print("List1 is palindrome")
else:
    print("List1 is not palindrome")

if list2 == copy_list2:
    print("List2 is palindrome")
else:
    print("List2 is not palindrome")

# WAP to find the number of students with a grade A in following tuple.
students_grade = ("A", "B", "A", "C", "D", "A", "B", "A", "C", "A")
print("Number of students with grade A: ", students_grade.count("A"))

# store the above values in a list and sort the list from A to D.
students_grade_list = list(students_grade)
students_grade_list.sort()
print("Sorted list: ", students_grade_list)


