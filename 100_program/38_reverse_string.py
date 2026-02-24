# Problem Statement: Reverse a string using for loop.

# take input from the user as a string
text = input("Enter a string: ")

# Initialize reversed string
reversed_text = ""

# Loop through the string in reverse order
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

# Print the reversed string
print(reversed_text)

'''output
Enter a string: krishna verma
amrev anhsirk'''