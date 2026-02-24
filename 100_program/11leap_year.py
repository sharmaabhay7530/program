# Problem Statement: Check whether a given year is a leap year.


# taking input from the user
year = int(input("Enter a year: "))
 
#  check condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# output-------
# Enter a year: 2025
# 2025 is not a Leap Year  --------//