# Problem 89: Find frequency of each character in string
text = input("Enter a string: ")
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Character frequency:", freq)
'''output
Enter a string: rajesh
Character frequency: {'r': 1, 'a': 1, 'j': 1, 'e': 1, 's': 1, 'h': 1}'''