# Problem 61: Rotate a list by K positions
numbers = input("Enter list elements: ").split()
K = int(input("Enter number of positions to rotate: "))

rotated = numbers[K:] + numbers[:K]
print("Rotated list:", rotated)

'''output
Enter list elements: 22 55 33 77 11
Enter number of positions to rotate: 22
Rotated list: ['22', '55', '33', '77', '11']'''