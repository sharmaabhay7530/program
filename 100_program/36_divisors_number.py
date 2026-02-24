# Problem Statement: Print all divisors of a number.
# take input from the user 
N = int(input("Enter a number: "))

# Loop from 1 to N and check for divisors
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=" ")


'''output
Enter a number: 6
1 2 3 6 '''