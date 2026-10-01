class Policy:

    def __init__(self, policy_number, policy_type):
        self.policy_number = policy_number
        self.policy_type = policy_type

    def display(self):
        print("Policy Number:", self.policy_number)
        print("Policy Type:", self.policy_type)