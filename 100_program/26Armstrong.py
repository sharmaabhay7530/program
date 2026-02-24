# Problem Statement: Check whether a number is Armstrong.

# taking number from the user
num = int(input("Enter a number: "))

# convert number into string
num_str = str(num)
power = len(num_str)
sum_digits = sum(int(digit)**power for digit in num_str)

#  apply condition
if sum_digits == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

'''output
Enter a number: 21
21 is not an Armstrong number'''