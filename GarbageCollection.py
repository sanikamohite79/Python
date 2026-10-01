import sys
import gc

class InsurancePolicy:
    
    def __init__(self, policy_id,customer,coverage):
        self.policy_id = policy_id
        self.customer = customer
        self.coverage = coverage


    def display(self):
        print("policy ID:", self.policy_id)
        print("Customer:", self.customer)
        print("Coverage:", self.coverage)
     
#Create object
policy = InsurancePolicy("POL1001", "Sanu", 100000)
policy.display()

# Create another reference to the same object
another_policy = policy
print("policy object:", policy)
print("Another refrance:", another_policy)

print()

# Both variables point to the SAME object then ewe use "is"
print(policy is another_policy)
print()

#Refrance_count
print("Reference count:", sys.getrefcount(policy))

#delete refrance
del policy
print(another_policy.policy_id)

#print("Reference count:", sys.getrefcount(another_policy))

del another_policy
#print("Reference count:", sys.getrefcount(another_policy))

collected = gc.collect()
print("Objects collected:", collected)





#---------Circular Reference----
# import gc


# class Customer:
#     pass


# class InsurancePolicy:
#     pass


# customer = Customer()
# policy = InsurancePolicy()

# customer.policy = policy
# policy.customer = customer

# del customer
# del policy

# print("Running garbage collection...")

# collected = gc.collect()

# print("Objects collected:", collected)

# print("GC Threshold:")
# print(gc.get_threshold())

# print("\nGC Count:")
# print(gc.get_count())