import pandas as pd


# Step 1: Load CSV
df = pd.read_csv("policies.csv")

print("----- ORIGINAL DATA -----")
print(df)
print()

print(df.head())



# avg_premium = df["Premium"].apply(lambda primium:primium).mean()
# print("....Average primium-------")
# print(avg_premium)
# print()

# C = df["Coverage"].apply(lambda coverage :"high"
# if coverage > 500000
# else "normal")
# print(C)

# sort_primium = df.sort_values(
#     by="Premium",
#     ascending=True
# )
# print(sort_primium)
# print()


# # # Step 7: Active Policies
# # active_policies = df[
# #     df["Status"] == "Active"
# # ]

# # print("\n----- ACTIVE POLICIES -----")
# # print(active_policies)
# #
# #print()


# active_policies = df["Status"].apply(lambda status: status == "Active")
# print(active_policies)
# print()



# result= df[
#     df["Status"].apply(lambda status : status == "Active")&
#     df["Coverage"].apply(lambda coverage: coverage >1000000)
# ]
# print(result)


# df ["Discount"] = df["Premium"].apply(lambda primium: primium * 0.85)
# print(df)


df["premium_status"] =df["Premium"].apply(lambda premium : "high" if premium >= 1000000
 else "middle" if premium <= 800000
 else "low")

print(df)

# # Step 2: High Coverage Policies
# high_coverage = df[
#     df["Coverage"].apply(
#         lambda coverage: coverage > 1000000
#     )
# ]

# print("\n----- HIGH COVERAGE POLICIES -----")
# print(high_coverage)


# # Step 3: 10% Discount
# df["DiscountedPremium"] = df["Premium"].apply(
#     lambda premium: premium * 0.90
# )

# print("\n----- AFTER 10% DISCOUNT -----")
# print(df)


# # Step 4: Premium Category
# df["PremiumCategory"] = df["Premium"].apply(
#     lambda premium:
#         "High" if premium >= 50000
#         else "Normal"
# )

# print("\n----- PREMIUM CATEGORY -----")
# print(df)


# # Step 5: Sort by Premium
# sorted_policies = df.sort_values(
#     by="Premium",
#     ascending=False
# )

# print("\n----- SORTED BY PREMIUM -----")
# print(sorted_policies)



# # Step 6: Average Premium per Product
# avg_premium = (
#     df.groupby("Product")["Premium"]
#       .apply(lambda x: x.mean())
# )

# print("\n----- AVERAGE PREMIUM -----")
# print(avg_premium)




# # Step 6: Average Coverage per Product
# avg_coverage = (
#     df.groupby("Product")["Coverage"]
#       .apply(lambda x: x.mean())
# )

# print("\n----- AVERAGE COVERAGE -----")
# print(avg_coverage)




# # Bonus 1: Active + Coverage > 20 Lakh
# result = df[
#     (df["Status"] == "Active") &
#     (df["Coverage"] > 2000000)
# ]

# print("\n----- ACTIVE + HIGH COVERAGE -----")
# print(result)


# # Bonus 2: 15% Discount
# df["SpecialPremium"] = df["Premium"].apply(
#     lambda premium: premium * 0.85
# )

# print("\n----- SPECIAL PREMIUM -----")
# print(df)


# # Bonus 3: Risk Category
# df["RiskCategory"] = df["Age"].apply(
#     lambda age:
#         "Senior" if age > 50
#         else "Middle" if age >= 35
#         else "Young"
# )

# print("\n----- RISK CATEGORY -----")
# print(df)


# # Bonus 4: Sort by Coverage
# sorted_by_coverage = df.sort_values(
#     by="Coverage",
#     ascending=False
# )

# print("\n----- SORTED BY COVERAGE -----")
# print(sorted_by_coverage)



# """import json
# with open("policies.json", "r") as file:
#     policies = json.load(file)

# new_policy = {
#     "policy_number": "POL1003",
#     "customer_name": "Amit",
#     "premium": 18000,
#     "status": "Active"
# }

# policies.append(new_policy)

# with open("policies.json", "w") as file:
#     json.dump(policies, file, indent=4) 
# """

# # def find_policy(policy_number):

# #     with open("policies.json", "r") as file:
# #         policies = json.load(file)

# #     for policy in policies:

# #         if policy["policy_number"] == policy_number:
# #             return policy

# #     return None    

# # policy = find_policy("POL1001")

# # print(policy)



# # try:

# #     with open("policie.json", "r") as file:
# #         policies = json.load(file)

# # except FileNotFoundError:

# #     print("Policy file does not exist.")
# #     policies = []

# # import json
# # try:

# #     with open("policies.json", "r") as file:
# #         policies = json.load(file)

# # except FileNotFoundError:

# #     print("Policy file not found.")
# #     policies = []
  
# # except json.JSONDecodeError:

# #     print("Policy file contains invalid JSON.")
# #     policies = []