# Problem 95: Remove duplicate characters from string
text = input("Enter a string: ")
unique_chars = ""
for char in text:
    if char not in unique_chars:
        unique_chars += char
print("String after removing duplicates:", unique_chars)

'''output
Enter a string: krishna 
String after removing duplicates: krishna '''