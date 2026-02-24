# Problem Statement: Count digits in a number.

# taking number from the user
num = input("Enter a number: ")

# Remove negative sign if present
num = num.lstrip('-')

count = len(num)
print("Number of digits:", count)

'''output
Enter a number: 24
Number of digits: 2'''