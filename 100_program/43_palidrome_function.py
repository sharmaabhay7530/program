# Problem Statement: Check palindrome string using function.

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if string is equal to its reverse
    return s == s[::-1]

# Read input
text = input("Enter a string: ")

# Call function and print result
if is_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')

'''output
Enter a string: krishna verma
"krishna verma" is not a palindrome.'''