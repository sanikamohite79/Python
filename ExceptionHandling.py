class Policy:
    def __init__(self, policy_number, policy_type, premium):
        self.policy_number = policy_number
        self.policy_type = policy_type
        self.premium = premium

    def display(self):
        print("\n--- Policy Details ---")
        print("Policy Number:", self.policy_number)
        print("Policy Type:", self.policy_type)
        print("Premium:", self.premium)


print("Insurance Policy System")

try:
    policy_number = input("Enter policy number: ")
    policy_type = input("Enter policy type: ")

    premium = int(input("Enter premium: "))

    if premium <= 0:
        raise ValueError("Premium must be greater than 0")

except ValueError as e:
    print("Invalid input:", e)

else:
    policy = Policy(policy_number, policy_type, premium)
    policy.display()

finally:
    print("\nProgram execution completed.")