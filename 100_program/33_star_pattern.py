# Problem Statement: Print star pattern using for loop.

# Read number of rows
N = int(input("Enter number of rows: "))

# Print the star pattern
for i in range(1, N + 1):
    print("*" * i)

'''output
*
**
***
****
*****'''