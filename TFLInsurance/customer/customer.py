class Customer:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print("Customer Name:", self.name)
        print("Email:", self.email)