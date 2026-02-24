# Problem Statement: Calculate power without using exponent operator.

# take base and exponent from the user
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

# Initialize result
result = 1

# Multiply base exp times
for i in range(exp):
    result *= base

# Print the result
print(result)

'''output
Enter base: 3
Enter exponent: 2
9'''