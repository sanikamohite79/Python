policies = [
    {"policy_id": "POL1001","customer": "Ravi","premium": 25000,"coverage": 10000000},
    { "policy_id": "POL1002","customer": "Amit","premium": 40000,"coverage": 20000},
    { "policy_id": "POL1003","customer": "Sneha","premium": 15000,"coverage": 5000},
    { "policy_id": "POL1004","customer": "Priya","premium": 60000,"coverage": 30000}
]

print()

discounted = list(
    map(
        lambda p: {
            **p,
            "discounted_premium": p["premium"] * 0.90
        },
        policies
    )
)

print(discounted)

print()


high_coverage = list(
    filter(
        lambda p: p["coverage"] > 1000000,
        policies
    )
)

print(high_coverage)


print()

sorted_policies = sorted(
    policies,
    key=lambda p: p["premium"],
    reverse=False
    #used True and False function for chaking decending and assending
)

print(sorted_policies)