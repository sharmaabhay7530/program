# Problem Statement: Find GCD using while loop.

# taking two input from the user 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Euclidean algorithm
while b != 0:
    a, b = b, a % b

print("GCD is:", a)

'''output
Enter first number: 48
Enter second number: 18
GCD is: 6'''