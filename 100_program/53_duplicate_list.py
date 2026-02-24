# Problem Statement: Remove duplicate elements from list.
# Input numbers as space-separated string
numbers = input("Enter numbers separated by space: ").split()

# Convert each element to integer manually
numbers = [int(num) for num in numbers]

# Remove duplicates while preserving order
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)

'''output
Enter numbers separated by space:
 23 43 66 22
List after removing duplicates: [23, 43, 66, 22]'''