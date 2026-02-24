# Problem 91: Convert string to title case manually
text = input("Enter a string: ").split()
title_case = ""
for word in text:
    if word:
        title_case += word[0].upper() + word[1:].lower() + " "
print("Title cased string:", title_case.strip())

'''output
Enter a string: krishna
Title cased string: Krishna'''