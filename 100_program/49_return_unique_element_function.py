# Problem Statement: Return unique elements from a list using function.

def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Read input as space-separated numbers and convert to list of integers
numbers = list(map(int, input("Enter elements of the list separated by space: ").split()))

# Call function and print result
print("Unique elements in the list:", unique_elements(numbers))

'''output
Enter elements of the list separated by space: 34
Unique elements in the list: [34]'''