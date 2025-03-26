a = 2 #integer
b = 3.4 #float
print( a+b)
print(type(a)) #type of a
print(type(b)) # type of b

name = "John Doe" #string
acount_balance = 1023039.23 #float
Interest_rate = 12.1 #float
Profit = acount_balance * Interest_rate / 100
print(Profit)

print(type(acount_balance)) #type of acount_balance

account_type = "Savings" #string
print(type(account_type))

is_customer_alive = True #boolean
print(type(is_customer_alive)) #type of is_customer_alive
print( name , "is a customer and his account balance is", acount_balance ,".", "He has earned a profit of", Profit) #concatenation

# String Manipulation
name = "John Doe"
print(name)
print(name[0])
print(name[1:3])
print(name[3:])
print(name[:3])
print(name * 2)
print(name + " is a customer")
# String Formatting
name = "John Doe"
age = 30
print("My name is", name, "and I am", age, "years old.")
# Output: My name is John Doe and I am 30 years old.
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is John Doe and I am 30 years old.