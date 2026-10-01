class Customer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


customer1 = Customer("Ravi")

customer2 = customer1

#print(customer1)
#print(customer2)

#customer1 = None
customer2 = None

print(customer1)
