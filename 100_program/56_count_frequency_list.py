# Problem 56: Count frequency of elements in list
# Read input list
numbers = input("Enter list elements separated by space: ").split()
# Count frequency
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency of elements:")
for key, value in freq.items():
    print(f"{key}: {value}")

'''output
Enter list elements separated by space: 222 44 22 66 21 77 
Frequency of elements:
222: 1
44: 1
22: 1
66: 1
21: 1
77: 1
PS C:\anudeep.foundation> '''