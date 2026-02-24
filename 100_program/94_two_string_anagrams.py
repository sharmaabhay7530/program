# Problem 94: Check whether two strings are anagrams
str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Strings are anagrams.")
else:
    print("Strings are not anagrams.")

'''output
Enter first string: krishna
Enter second string: verma
Strings are not anagrams.'''