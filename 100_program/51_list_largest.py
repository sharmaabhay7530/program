# Problem Statement: Find largest element in a list.

# Read input as space-separated numbers
numbers_input = input("Enter elements of the list separated by space: ")

# Convert input to a list of integers manually
numbers = []
for num in numbers_input.split():
    numbers.append(int(num))

# Initialize largest with the first element
largest = numbers[0]

# Loop through the list to find the largest element
for num in numbers:
    if num > largest:
        largest = num

# Print the largest element
print("The largest element in the list is:", largest)

'''output
Enter elements of the list separated by space: 12 21 42 54
The largest element in the list is: 54'''