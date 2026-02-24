# Problem 92: Find longest word in a sentence
sentence = input("Enter a sentence: ").split()
longest = ""
for word in sentence:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

'''output
Enter a sentence: krishna is a boy
Longest word: krishna'''