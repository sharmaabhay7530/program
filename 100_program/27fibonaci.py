# Problem Statement: Generate Fibonacci series using while loop.

# taking number form the user

N = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1
count = 0

while count < N:
    print(a, end=" ")
    a, b = b, a + b  # Update the next term
    count += 1