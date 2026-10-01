class Premium:

    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        tax = self.amount * 0.18
        return self.amount + tax

    def display(self):
        print("Premium:", self.amount)
        print("Total with Tax:", self.calculate_total())