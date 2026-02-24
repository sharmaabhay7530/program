# Problem Statement: Check whether a number is divisible by both 3 and 5.

# taking input from the user 
num = int(input("Enter a number: "))

# check condition 
if num % 3 == 0:
    print(num, "is divisible by 3")
elif num % 5 == 0:
    print(num, "is divisible by  5")
else:
    print(num, "is not divisible by both 3 and 5")

'''output
Enter a number: 3
3 is divisible by 3
'''