# Problem Statement: Accept numbers until 0 is entered and print sum.


total = 0

# apply condition for repeating task
while True:
    # taking number from the user
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num

# display 
print("Sum of entered numbers is:", total)


'''output
Enter a number (0 to stop): 5
Enter a number (0 to stop): 10
Enter a number (0 to stop): 3
Enter a number (0 to stop): 0
Sum of entered numbers is: 18'''