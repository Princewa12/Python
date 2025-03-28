# class & object in python
# class is a blueprint for creating objects. 
# creating a class

class Car:
    color = "Blue"

# Ojects in the class (Instance)

car1 = Car()
print(car1.color)
    
car2 = Car()
print(car2.color)

# __init__ (constructor) function
# All classes have a function called __init__(), which is always executed when the object is being initiated. 


class Student:
    # default constructors
    def __init__(self):
        pass
    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students in DB") #optional

s1 = Student("Prince", 98) # called atributes
print(s1.name, s1.marks)
s2 = Student("Kumar", 97)
print(s2.name, s2.marks)


#static method
# Methods that don't use the self parameters (work at class level)


# decorators: allow us to wrap annother function in order to extrend the behaviour of the wrapped function,
# without permanently modifying it. 
# @staticmethod

# WAP with creating Account class with 2 attr account number and balance,
# create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.account = acc
        self.balance = bal

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited" )
        print("Remaining balance in your account is ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Remaining balance in your account is ", self.balance)

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 564151)
acc1.debit(1000)
acc1.credit(2000)
acc1.credit(100000)