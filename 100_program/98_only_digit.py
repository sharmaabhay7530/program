# Problem 98: Check whether string contains only digits
text = input("Enter a string: ")
is_digit = True
for char in text:
    if not char.isdigit():
        is_digit = False
        break
print("String contains only digits." if is_digit else "String does not contain only digits.")

'''output
Enter a string: hello
String does not contain only digits.'''