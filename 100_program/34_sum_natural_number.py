# Problem Statement: Find sum of first N natural numbers.

# take input number by the user 
N = int(input("Enter N: "))

# Initialize sum
total = 0

# Calculate sum using for loop
for i in range(1, N + 1):
    total += i

# Print the result
print(total)

'''output
Enter N: 5 
15'''