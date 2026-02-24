# Problem 67: Find minimum value in a tuple
numbers = tuple(map(int, input("Enter tuple elements: ").split()))
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print("Minimum value in tuple:", minimum)

'''output
Enter tuple elements: 4 2 6 2 7 4 8
Minimum value in tuple: 2'''