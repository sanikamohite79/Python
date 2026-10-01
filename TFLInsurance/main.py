from customer.customer import Customer
from policy.policy import Policy
from premium.premium import Premium
from claim.claim import Claim


# Customer
customer = Customer(
    "Sanika",
    "sanika@gmail.com"
)

# Policy
policy = Policy(
    "POL1001",
    "Life Insurance"
)

# Premium
premium = Premium(25000)


#Claim
# Claim
claim = Claim(
    "CLM001",
    "POL1001",
    10000
)


print("----- CUSTOMER -----")
customer.display()

print("\n----- POLICY -----")
policy.display()

print("\n----- PREMIUM -----")
premium.display()


print("\n----- CLAIM -----")
claim.display()
claim.process_claim()
