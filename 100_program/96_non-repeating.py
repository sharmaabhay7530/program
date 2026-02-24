# Problem 96: Find first non-repeating character in string
text = input("Enter a string: ")
first = None
for char in text:
    if text.count(char) == 1:
        first = char
        break
print("First non-repeating character:", first)

'''output
Enter a string: krishna
First non-repeating character: k'''