# Problem Statement: Check whether a number lies within a given range.


num = float(input("Enter the number: "))
lower = float(input("Enter the lower bound of the range: "))
upper = float(input("Enter the upper bound of the range: "))

if lower <= num <= upper:
    print(num, "lies within the range", lower, "to", upper)
else:
    print(num, "does not lie within the range", lower, "to", upper)



'''output
Enter the number: 15
Enter the lower bound of the range: 10
Enter the upper bound of the range: 20
15.0 lies within the range 10.0 to 20.0'''