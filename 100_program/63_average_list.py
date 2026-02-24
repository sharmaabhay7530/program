# Problem 63: Find average of list elements
numbers = list(map(int, input("Enter list elements: ").split()))
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average of list elements:", average)

'''output
Enter list elements: 22 44 77 33 
Average of list elements: 44.0'''