# Problem 100: Compress a string using character counts
text = input("Enter a string: ")
compressed = ""
i = 0
while i < len(text):
    count = 1
    while i + 1 < len(text) and text[i] == text[i+1]:
        count += 1
        i += 1
    compressed += text[i] + str(count)
    i += 1
print("Compressed string:", compressed)

'''output
Enter a string: hello
Compressed string: h1e1l2o1'''