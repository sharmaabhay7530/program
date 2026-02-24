# Problem 78: Merge two dictionaries manually
dict1 = {}
dict2 = {}

# Input first dictionary
n1 = int(input("Enter number of items in first dictionary: "))
for _ in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

# Input second dictionary
n2 = int(input("Enter number of items in second dictionary: "))
for _ in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

# Merge manually
merged_dict = dict1.copy()
for key, value in dict2.items():
    merged_dict[key] = value

print("Merged dictionary:", merged_dict)

'''output
Enter number of items in first dictionary: 1
Enter key: a
Enter value: 2
Enter number of items in second dictionary: s'''