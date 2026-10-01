class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display(self):
        print("Customer ID:", self.customer_id)
        print("Customer Name:", self.name)