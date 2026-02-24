# Problem 79: Sort dictionary by keys
d = {}
n = int(input("Enter number of dictionary items: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

# Sort by keys
sorted_keys = sorted(d.keys())
sorted_dict = {key: d[key] for key in sorted_keys}
print("Dictionary sorted by keys:", sorted_dict)

'''output
Enter number of dictionary items: 1
Enter key: krishna
Enter value: 2
Dictionary sorted by keys: {'krishna': '2'}'''