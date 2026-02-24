# Problem Statement: Find sum of even numbers up to N.

# takong number from the user
N = int(input("Enter a number N: "))
sum_even = 0


for i in range(2, N+1, 2):  
    sum_even += i

print("Sum of even numbers up to", N, "is:", sum_even)

'''output
Enter a number N: 4
Sum of even numbers up to 4 is: 6'''