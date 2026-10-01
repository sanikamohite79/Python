
#This demonstrates Inheritance.
from Employee.Employee import Employee


class Agent(Employee):

    def sell_policy(self):
        print(self.name, "is selling insurance policy")