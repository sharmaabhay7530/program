# Problem Statement: Find the largest of three numbers.

# Read three numbers from user
a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

# Compare to find the largest
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


'''output 
enter first number4
enter second number67
enter third number23
67'''