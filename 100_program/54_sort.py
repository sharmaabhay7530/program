# Problem Statement: Sort a list without using sort method.

# Read input as space-separated numbers
numbers_input = input("Enter elements of the list separated by space: ")

# Convert input to a list of integers
numbers = []
for num in numbers_input.split():
    numbers.append(int(num))

# Create a new sorted list
sorted_list = []
while numbers:
    # Find the minimum element
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    # Append the minimum to the sorted list and remove it from original
    sorted_list.append(min_value)
    numbers.remove(min_value)

# Print the sorted list
print("Sorted list:", sorted_list)

'''output
Enter elements of the list separated by space: 32 43 22 11 55 
Sorted list: [11, 22, 32, 43, 55]'''