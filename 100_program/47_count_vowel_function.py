# Problem Statement: Count vowels using function.

def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
    return count

# Read input
text = input("Enter a string: ")

# Call function and print result
print(f"Number of vowels in the string: {count_vowels(text)}")

'''output
Enter a string: krihshna
Number of vowels in the string: 2'''