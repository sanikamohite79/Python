"""#A variable is a name used to store data.
#Python automatically understands the data type.
Name = 'Sanika'
age = 22
salary = 250000

#print() displays information on the screen.
print (type (Name),type(age))
#print(age + age)
#print(age , age)
#print(age)
print(salary)

# Put f before the string and variables inside {}====
print(f"My name is { Name} and My age is { age}")


#input() is used to take information from the user.

name = input("Enter your Name: ")
print("hello" , name)


Age=input("Enter your Age:")
print(Age)


#Arithmetic Operators

a=10
b= 20
print(a+b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


#Comparison Operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Logical Operators

#AND

age = 22
marks = 80

print(age >= 18 and marks >= 40)

#OR

age = 22
marks = 30

print(age >= 18 or marks >= 40)

#Not
is_student = True

print(not is_student)

Sum_assured=100000
rate=0.025
premium= Sum_assured * rate
premium += 2000
print("premimum: ", premium)"""
#if
Age = 22
if Age >= 18:
   print("eligible for vote.")

#If...else
marks = 65
if marks >= 40:
   print("pass")
else:
   print("Fail")  

#if...elif...else
marks=80
if marks >= 70:
   print("Distinction")
elif marks >= 60:
   print("First class")
elif marks >=40:
   print("pass")
else:
   print("fail")            



