class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, A):
        return Money(self.amount + A.amount)

    def __sub__(self, B):    
         return Money(self.amount - B.amount)


# Create objects
m1 = Money(100)
m2 = Money(200)

# Add two Money objects
m3 = m1 + m2
m4 = m1 - m2

# Display result
print(f"{m1.amount}+{m2.amount}={m3.amount}")
print(f"{m1.amount}-{m2.amount}={m4.amount}")
print(m4.amount)