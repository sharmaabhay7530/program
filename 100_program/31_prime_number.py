# Problem Statement: Print all prime numbers between 1 and N.

N = int(input("Enter N: "))

# Loop through numbers from 2 to N
for num in range(2, N + 1):
    is_prime = True
    # Check divisibility from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


'''output
Enter N: 54
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 '''