# Problem Statement: Find sum of digits using function.
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Add last digit
        n = n // 10      # Remove last digit
    return total

# take input from the user as a number
N = int(input("Enter a number: "))

# Call function and print result
print(f"The sum of digits of {N} is {sum_of_digits(N)}")