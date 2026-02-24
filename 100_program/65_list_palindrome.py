# Problem 65: Check whether list is palindrome
numbers = input("Enter list elements: ").split()
is_palindrome = True
for i in range(len(numbers)//2):
    if numbers[i] != numbers[-(i+1)]:
        is_palindrome = False
        break
print("List is palindrome." if is_palindrome else "List is not palindrome.")

'''output
Enter list elements: 2 44 77 22 88 
List is not palindrome.'''