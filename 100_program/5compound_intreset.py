# Problem Statement: Calculate compound interest.

# take input from the user 
P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate (in %): "))
T = float(input("Enter time in years: "))

# Calculate compound amount
A = P * (1 + R/100)**T

# Calculate compound interest
CI = A - P

# Print the compound interest
print("Compound Interest:", CI)


# //output
# Enter principal amount: 1000
# Enter annual interest rate (in %): 1.2
# Enter time in years: 2
# Compound Interest: 24.144000000000005 -----------//