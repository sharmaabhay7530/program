# Problem Statement: Check prime number using function.
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# take input from the user 
N = int(input("Enter a number: "))

# Check and print result
if is_prime(N):
    print(f"{N} is a prime number.")
else:
    print(f"{N} is not a prime number.")

'''output
Enter a number: 5
5 is a prime number.'''