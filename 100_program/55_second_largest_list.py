# Problem Statement: Find second largest number in list.
# Input numbers as space-separated string
numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]

# Remove duplicates to handle cases where largest number repeats
numbers = list(set(numbers))

if len(numbers) < 2:
    print("There is no second largest number")
else:
    numbers.sort()  # Sort in ascending order
    print("Second largest number is:", numbers[-2])

'''output
Enter numbers separated by space:
 54 33 77 22 88 
Second largest number is: 77'''