# Problem 83: Check whether key exists in dictionary
d = {'a': 1, 'b': 2, 'c': 3}
key_to_check = input("Enter key to check: ")

if key_to_check in d:
    print(f"Key '{key_to_check}' exists in dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in dictionary.")

'''output
Enter key to check: 1
Key '1' does not exist in dictionary.'''