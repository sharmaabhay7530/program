# Problem 77: Count character frequency using dictionary
text = input("Enter a string: ")
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequency:")
for key, value in freq.items():
    print(f"{key}: {value}")

'''output
Enter a string: krishna
Character frequency:
k: 1
r: 1
i: 1
s: 1
h: 1
n: 1
a: 1'''