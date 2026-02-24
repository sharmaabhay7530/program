# Problem Statement: Generate Fibonacci series using function.

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# take input from the user as a term
N = int(input("Enter number of terms: "))

# Call function and print the series
print("Fibonacci series:")
print(*fibonacci_series(N))

'''output
Enter number of terms: 4
Fibonacci series:
0 1 1 2'''