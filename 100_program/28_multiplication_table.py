# Problem Statement: Print multiplication table using while loop.

# taking number fromt the user for multiplication
num = int(input("Enter a number: "))
i = 1

# using loop for table
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

'''output
Enter a number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50'''