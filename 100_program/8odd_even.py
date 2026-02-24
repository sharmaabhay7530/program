# Problem Statement: Check whether a number is even or odd without modulus operator.

# taking input from the user
num = int(input("Enter a number: "))
#  ceking conditon
if (num // 2) * 2 == num:
    print("Even")
else:
    print("Odd")

# ouptut ---------
# Enter a number: 3
# Odd ---------//