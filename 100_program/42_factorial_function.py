# Problem Statement: Find factorial using function.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# take input from the user as a number
N = int(input("Enter a number: "))

# Call the function and print result
print(f"The factorial of {N} is {factorial(N)}")

'''output
Enter a number: 5
The factorial of 5 is 120'''