# Problem 86: Reverse a string without slicing
text = input("Enter a string: ")
reversed_text = ""
for i in range(len(text)-1, -1, -1):
    reversed_text += text[i]
print("Reversed string:", reversed_text)
'''output
Enter a string: krishna
Reversed string: anhsirk'''