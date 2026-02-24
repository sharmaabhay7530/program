# Problem 70: Check whether tuple elements are unique

numbers = tuple(input("Enter tuple elements separated by space: ").split())
unique = True
for i in range(len(numbers)):
    if numbers[i] in numbers[:i]:
        unique = False
        break
print("Tuple elements are unique." if unique else "Tuple elements are not unique.")

'''output
Enter tuple elements separated by space: 2 543 7
65 33 66 22
Tuple elements are unique.'''