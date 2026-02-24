# Problem Statement: Check whether a character is vowel or consonant.

# taking input from the user
char = input("Enter a single character: ").lower()  # Convert to lowercase

#  condition
if char in 'aeiou':
    print(char, "is a Vowel")
else:
    print(char, "is a Consonant")

'''output
Enter a single character: a
a is a Vowel'''