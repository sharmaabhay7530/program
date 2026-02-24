# Problem Statement: Generate Fibonacci series using for loop.

# take input from the user 
N = int(input("Enter number of terms: "))

# First two terms
a, b = 0, 1

# Print the series
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b

'''output
Enter number of terms: 23
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711'''