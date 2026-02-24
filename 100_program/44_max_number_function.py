# Problem Statement: Find maximum of three numbers using function.

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# take three input from the user 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Call the function and print result
print(f"The maximum number is {maximum(num1, num2, num3)}")

'''output
Enter first number: 1
Enter second number: 2
Enter third number: 3
The maximum number is 3.0'''