class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def Show(self):
        print(self) 

    
    def __str__(self):
         return f"BankAccount({self.name}, Balance: ${self.balance})"  

    def deposit(self, amount):
        self.balance += amount
        print(f"deposite ${amount}. New balance:${self.balance}")  

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdrew ${amount}. new balance: ${self.balance}")
        else:
            print("Insufficient balance!")  



    def __repr__(self):
        return( f"BankAccount(name={self.name!r}, "
            f"balance={self.balance!r})")          


B1=BankAccount("Sanika",25000) 
print(B1.name)
print(B1.balance)
B1.deposit(500)
B1.withdraw(200)

print(repr(B1))
print(B1)




