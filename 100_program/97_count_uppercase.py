# Problem 97: Count uppercase and lowercase letters
text = input("Enter a string: ")
upper = 0
lower = 0
for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")

'''output
Enter a string: hello
Uppercase letters: 0, Lowercase letters: 5'''