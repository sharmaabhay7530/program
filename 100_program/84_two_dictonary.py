# Problem 84: Create dictionary from two lists
keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()

d = {}
for i in range(min(len(keys), len(values))):
    d[keys[i]] = values[i]

print("Created dictionary:", d)

'''output
Enter keys separated by space: 1
Enter values separated by space: krish
Created dictionary: {'1': 'krish'}'''