# Problem 81: Find key with maximum value
d = {}
n = int(input("Enter number of items in dictionary: "))
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

max_key = None
max_value = float('-inf')
for key, value in d.items():
    if value > max_value:
        max_value = value
        max_key = key

print(f"Key with maximum value: {max_key} ({max_value})")

'''output
Enter number of items in dictionary: 2
Enter key: 1
Enter value: krishna'''