class Claim:

    def __init__(self, claim_id, policy_number, amount):
        self.claim_id = claim_id
        self.policy_number = policy_number
        self.amount = amount

    def display(self):
        print("Claim ID:", self.claim_id)
        print("Policy Number:", self.policy_number)
        print("Claim Amount:", self.amount)

    def process_claim(self):
        print("Claim processed successfully.")