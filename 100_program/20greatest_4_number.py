# Problem Statement: Find the greatest of four numbers.

# taking number from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

# using function 
greatest = max(num1, num2, num3, num4)

print("The greatest number is:", greatest)

'''output
Enter first number: 5
Enter second number: 7
Enter third number: 4
Enter fourth number: 8
The greatest number is: 8.0'''