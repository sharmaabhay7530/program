# Problem 64: Replace negative numbers with zero
numbers = list(map(int, input("Enter list elements: ").split()))
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print("Modified list:", numbers)



'''output
Enter list elements: 22 44 66 88 
Modified list: [22, 44, 66, 88]'''