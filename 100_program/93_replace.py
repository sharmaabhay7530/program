# Problem 93: Replace all vowels with '*'
text = input("Enter a string: ")
result = ""
for char in text:
    if char.lower() in 'aeiou':
        result += '*'
    else:
        result += char
print("Modified string:", result)
'''output
Enter a string: divyanshu
Modified string: d*vy*nsh*'''