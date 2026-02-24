# take input as a string 
text = input("Enter a string: ")

# Initialize vowel count
count = 0

# Loop through each character
for char in text:
    if char.lower() in 'aeiou':
        count += 1

# Print the result
print(count)

'''ouptut
Enter a string: krishna verma
4'''