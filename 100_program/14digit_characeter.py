# Problem Statement: Check whether a character is digit or alphabet.

# taking input from the user
char = input("Enter a single character: ")

# condition

if char.isdigit():
    print(char, "is a Digit")
elif char.isalpha():
    print(char, "is an Alphabet")
else:
    print(char, "is neither a Digit nor an Alphabet")


'''output
Enter a single character: a
a is an Alphabet'''