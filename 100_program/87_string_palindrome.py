# Problem 87: Check whether string is palindrome

text = input("Enter a string: ").replace(" ", "").lower()
is_palindrome = True
for i in range(len(text)//2):
    if text[i] != text[-(i+1)]:
        is_palindrome = False
        break
print("Palindrome." if is_palindrome else "Not palindrome.")

'''output
Enter a string: krishna
Not palindrome.'''