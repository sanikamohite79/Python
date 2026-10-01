#from abc import ABC, abstractmethod

class Policy:

    def __init__(self, policy_number, customer_name):
        self.policy_number = policy_number
        self.customer_name = customer_name

    def calculate_premium(self):
        print("Calculating premium")

    def display_policy(self):
        print("Policy Number:", self.policy_number)
        print("Customer Name:", self.customer_name)