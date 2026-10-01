class Claim:

    def __init__(self, claim_id, amount):
        self.claim_id = claim_id
        self.__amount = amount  # make private __
        self.status = "Submitted"

    def get_amount(self):
        return self.__amount

    def update_amount(self, amount):
        if amount > 0:
            self.__amount = amount
            print("Claim amount updated")
        else:
            print("Invalid amount")

    def approve(self):
        self.status = "Approved"
        print("Claim approved")

    def reject(self):
        self.status = "Rejected"
        print("Claim rejected")

    def display(self):
        print("Claim ID:", self.claim_id)
        print("Claim Amount:", self.__amount)
        print("Claim Status:", self.status)