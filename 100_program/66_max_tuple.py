# Problem 66: Find maximum value in a tuple
numbers = tuple(map(int, input("Enter tuple elements: ").split()))
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum value in tuple:", maximum)

'''output
Enter tuple elements: 54 32 66 2 4 7 
Maximum value in tuple: 66'''