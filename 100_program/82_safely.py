# Problem 82: Safely remove a key from dictionary
d = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = input("Enter key to remove: ")

if key_to_remove in d:
    del d[key_to_remove]
    print(f"Key '{key_to_remove}' removed. Updated dictionary: {d}")
else:
    print(f"Key '{key_to_remove}' not found. Dictionary unchanged: {d}")

'''output
Enter key to remove: a
Key 'a' removed. Updated dictionary: {'b': 2, 'c': 3}'''