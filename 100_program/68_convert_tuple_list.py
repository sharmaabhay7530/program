# Problem 68: Convert tuple to list
numbers = tuple(input("Enter tuple elements separated by space: ").split())
converted_list = list(numbers)
print("Converted list:", converted_list)

'''output
Enter tuple elements separated by space: 22 55 3
2 55 2
Converted list: ['22', '55', '32', '55', '2']'''