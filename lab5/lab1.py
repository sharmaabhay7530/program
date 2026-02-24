# Question-1 write a program in python to create a list of 20 number and ask the user to input any no. and delte these no. from your list from its all occurances expect 1st occurance
# create empty list
numbers = []
print("Enter 20 numbers:")
# taking 20 numbers from user
for i in range(20):
    while True:
        try:
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")
print("\nOriginal List:")
print(numbers)

# ask user for number to modify
try:
    target = int(input("\nEnter a number to delete its extra occurrences: "))
except ValueError:
    print("Invalid input! Program exiting.")
    exit()

if target in numbers:
    first_found = False
    updated_list = []

    for item in numbers:
        if item == target:
            if not first_found:
                updated_list.append(item)   # keep first occurrence
                first_found = True
            # skip other occurrences
        else:
            updated_list.append(item)

    print("\nUpdated List:")
    print(updated_list)

else:
    print("Number not found in the list.")

    