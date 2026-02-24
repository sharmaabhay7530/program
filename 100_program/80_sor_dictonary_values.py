# Problem 80: Sort dictionary by values
d = {}
n = int(input("Enter number of dictionary items: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

# Sort by values
sorted_items = sorted(d.items(), key=lambda item: item[1])
sorted_dict = {k: v for k, v in sorted_items}
print("Dictionary sorted by values:", sorted_dict)

'''output
Enter number of dictionary items: 1
Enter key: krishna
Enter value: 2
Dictionary sorted by values: {'krishna': '2'}'''