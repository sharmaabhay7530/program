# Problem 99: Generate all substrings of a string
text = input("Enter a string: ")
substrings = []
for i in range(len(text)):
    for j in range(i+1, len(text)+1):
        substrings.append(text[i:j])
print("All substrings:", substrings)

'''output
Enter a string: hello
All substrings: ['h', 'he', 'hel', 'hell', 'hello', 'e', 'el', 'ell', 'ello', 'l', 'll', 'llo', 'l', 'lo', 'o']'''