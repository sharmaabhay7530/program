# creating list of numbers

numbers = [45, 47, 89, 34, 56]

# display the list
print("----")
print("Numbers are:", numbers)

# display data without square brackets
print("----")
print("Numbers are:")
print(*numbers)

# display elements by using for loop
print("--------")
print("Numbers are:")
for num in numbers:
    print(num)

length = len(numbers)
print("Number of elements in list:", length)

print("Numbers in reverse order:")
for index in range(length - 1, -1, -1):
    print(numbers[index], end=",")

# find sum of all numbers in list
print("\n-------")
total = 0
for i in numbers:
    total = total + i

print("Sum of all numbers in the list:", total)

# finding greatest number in list
print("--------")
maximum = numbers[0]

for index in range(1, length):
    if maximum < numbers[index]:
        maximum = numbers[index]

print("Maximum number in the list is:", maximum)
