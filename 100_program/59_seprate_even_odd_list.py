# Problem 59: Separate even and odd numbers from list
numbers = list(map(int, input("Enter list elements separated by space: ").split()))
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

'''output
Enter list elements separated by space: 22 33 55  77 55 
Even numbers: [22]
Odd numbers: [33, 55, 77, 55]'''