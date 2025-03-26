# WAP to show following word meanings in a python dicitonary
# table : "a piece of furniture", "list of facts and figures"
# cat : "a samall domestic animal"

dict = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small domestic animal",
}

print(dict)

# you are given a list of subject for students. Assume 1 classroom is required for each subject. How amny classromms are needed by all students? 
# "python", "java", "c", "c++", "python", "java", "c"
#  "java", "c", "c++", "python", "java", "c"

subject = {
    "python", "java", "c", "c++", "python", "java", "c"
    "java", "c", "c++", "python", "java", "c"
}

print(len(subject)) # 5

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one-by-one. Use subject name as key and marks as value. 

marks = {}

x = int(input("Enter the marks of Physics:" ))
marks.update({"Physics": x})

y = int(input("Enter the marks of Chemistry:" ))
marks.update({"Chemistry": y})

z = int(input("Enter the marks of Maths: "))
marks.update({"Maths": z})

print(marks)


# Figure out a way to store 9 and 9.0 as seperate values in set.
# you may take help of built-in datatypes. 

set = {9,"9.0"}
print(set)
# with the help of tuple
set = (
    (9),
    (9.0)
)
print(set)




