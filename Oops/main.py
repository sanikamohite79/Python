from customer.customer import Customer

from policy.life_policy import LifePolicy
from policy.health_policy import HealthPolicy
from policy.motor_policy import MotorPolicy

from claim.claim import Claim

from Employee.agent import Agent
from Employee.claim_officer import ClaimOfficer


print("===== TFL INSURANCE SYSTEM =====")


# =====================================
# CUSTOMER
# =====================================

print("\n--- CUSTOMER ---")

customer1 = Customer(101, "Rahul")

customer1.display()


# =====================================
# POLICIES
# =====================================

print("\n--- POLICIES ---")

life_policy = LifePolicy(
    "POL1001",
    "Rahul"
)

health_policy = HealthPolicy(
    "POL1002",
    "Sneha"
)

motor_policy = MotorPolicy(
    "POL1003",
    "Amit"
)


life_policy.display_policy()
print("Premium:", life_policy.calculate_premium())

print()

health_policy.display_policy()
print("Premium:", health_policy.calculate_premium())

print()

motor_policy.display_policy()
print("Premium:", motor_policy.calculate_premium())


# =====================================
# POLYMORPHISM
# =====================================

print("\n--- POLYMORPHISM ---")

policies = [
    life_policy,
    health_policy,
    motor_policy
]

for policy in policies:

    print(
        policy.policy_number,
        "Premium:",
        policy.calculate_premium()
    )


# =====================================
# CLAIM
# =====================================

print("\n--- CLAIM ---")

claim1 = Claim("CLM1001", 50000)

claim1.display()

print("\nUpdating claim amount...")

claim1.update_amount(60000)

print("\nApproving claim...")

claim1.approve()

claim1.display()


# =====================================
# EMPLOYEE / INHERITANCE
# =====================================

print("\n--- EMPLOYEE ---")

agent1 = Agent(201, "Priya")

agent1.display_employee()
agent1.sell_policy()

print()

claim_officer1 = ClaimOfficer(202, "Amit")

claim_officer1.display_employee()
claim_officer1.process_claim()