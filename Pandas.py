import pandas as pd

data = {
    "PolicyID": ["POL1001","POL1002","POL1003","POL1004","POL1005" ],
    "Customer": ["Ravi","Amit","Sneha","Priya","Rahul"],
    "Product": ["Life Protection", "Child Future", "Life Protection", "Retirement","Child Future"],
    "Premium": [25000,40000,15000,60000,30000],
    "Coverage": [100,2000,500,3000000,1500000],
    "Status": ["Active", "Active", "Inactive", "Active", "Active"]
}

df = pd.DataFrame(data)
print(df)
print()

high_coverage = df[
    df["Coverage"].apply(
        lambda coverage: coverage > 10000
    )
]

print(high_coverage)
print()


df["DiscountedPremium"] = df["Premium"].apply(
    lambda premium: premium * 0.90
)

print(df)
print()



sorted_df = df.sort_values(
    by="Premium",
    key=lambda column: column,
    ascending=False
)

print(sorted_df)
print()



avg_premium = (
    df.groupby("Product")["Premium"]
      .apply(lambda x: x.mean())
)

print(avg_premium)
print()

avg_coverage = (
    df.groupby("Product")["Coverage"]
      .apply(lambda x: x.mean())
)

print(avg_coverage)
print()


