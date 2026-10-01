"""class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Customer:", self.name)
        print("Age:", self.age)


# Create object
customer1 = Customer("Sanika", 22)

# Call method
customer1.display() """


"""
class Policy:

    def __init__(self, policy_number, policy_type, premium):
        self.policy_number = policy_number
        self.policy_type = policy_type
        self.premium = premium

    def display(self):
        print("Policy Number:", self.policy_number)
        print("Policy Type:", self.policy_type)
        print("Premium:", self.premium)


# Create object
policy1 = Policy("POL1001", "Life", 25000)

# Call display method
policy1.display()"""

"""
#Loops
#for--
for i in range(1 ,5):
    print("Sanu")

    print()

number = int (input("Enter Number:"))
for i in range(1, 11):
    #print(number*i)    
    print(number,"x", i, "=" , number*i) 
    print()


 #While---A while loop runs while a condition is true.

count = 1

while count <= 5:
    print(count)
    count += 1"""

"""
#range--range() is used to generate a sequence of numbers.

range(stop)
range(start, stop)
range(start, stop, step)

range(5)          # 0, 1, 2, 3, 4
range(1, 5)       # 1, 2, 3, 4
range(1, 10, 2)   # 1, 3, 5, 7, 9"""

"""
#Nested Control Structures---
#A Pogram can use a loop and an if together.

for i in range(1,6):
    if i % 2 == 0:
        print(i,"is Even")
    else:
        print(i, "is Odd")"""


"""ber Guessing Game
The main project in the file combines several concepts.
The computer generates a random number between 1 and 100. The user keeps guessing until the correct number is found."""

import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Congratulations!")
        print("Attempts:", attempts)
        break