# Problem 57: Reverse a list without reverse() method
numbers = input("Enter list elements separated by space: ").split()
reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])
print("Reversed list:", reversed_list)

'''output
Enter list elements separated by space: 22 44 66 77 44 88  
Reversed list: ['88', '44', '77', '66', '44', '22']'''