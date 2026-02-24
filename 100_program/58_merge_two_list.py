# Problem 58: Merge two lists and remove duplicates
list1 = input("Enter first list elements: ").split()
list2 = input("Enter second list elements: ").split()

merged = list1 + list2
unique = []
for item in merged:
    if item not in unique:
        unique.append(item)

print("Merged list without duplicates:", unique)

'''output
Enter first list elements: 21
Enter second list elements: 33
Merged list without duplicates: ['21', '33']'''