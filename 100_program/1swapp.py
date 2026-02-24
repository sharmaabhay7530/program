# Problem Statement: Swap two numbers without using a third variable.
# take input from the user 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping
a = a + b
b = a - b
a = a - b

# printing the values 
print("After swapping:")
print("First number:", a)
print("Second number:", b)



# output
 '''Enter first number: 10
Enter second number: 20
After swapping:
First number: 20
Second number: 10'''
