# Problem Statement: Find smallest element in a list.

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = min(numbers)  # Use built-in min() function
print("Smallest element is:", smallest)

'''output
Enter numbers separated by space:
 23 21 33 44
Smallest element is: 21'''