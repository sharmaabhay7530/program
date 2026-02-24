# Problem Statement: Find GCD using function.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Read two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call function and print result
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")

'''output
Enter first number: 1
Enter second number: 3
The GCD of 1 and 3 is 1'''