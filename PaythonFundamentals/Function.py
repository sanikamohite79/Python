#A function is a reusable block of code that performs a specific task.

def greet():
    print("Hello")
greet()

#Function with Parameter---

def Welcome(name):
    print("Welcome" , name)
Welcome("Sanika")
Welcome("Roshan")

#Multiple Parameters--
def student(name, course):
    print(name, "is learning" , course)
student("Rahul" , "python")

#return--
def add(a, b):
    return a + b
result = add(20 ,30)
print(result)

#Local Veriable-A variable created inside a function is normally a local variable.
def demo():
    message="Hello"
    print(message)
demo()  

#Global variable--A variable created outside a function is a global variable.
collage = "Transflower"

def display():
    print(collage)
display()    

#Positional Argument---Arguments are matched according to their position.
def multiply(a, b):
    print(a * b)

multiply(5, 4)

#Keyword Argument--We specify the parameter name.
def employee(name, department):
    print(name, department)

employee(department="HR", name="Ravi")

#Default Argument--A parameter can have a default value.
def greet(name="Pramav"):
    print("Welcome", name)

greet()
greet("Anita")