# Problem 69: Count occurrence of element in tuple
numbers = tuple(input("Enter tuple elements separated by space: ").split())
element = input("Enter element to count: ")
count = 0
for item in numbers:
    if item == element:
        count += 1
print(f"'{element}' occurs {count} times in tuple.")

'''output
Enter tuple elements separated by space: 3 54 26
 2 54
Enter element to count: 2
'2' occurs 1 times in tuple.'''