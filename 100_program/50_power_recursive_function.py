# Problem Statement: Calculate power using recursive function.

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Read base and exponent
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

# Call function and print result
print(f"{base} raised to the power {exp} is {power(base, exp)}")

'''output
Enter base: 4
Enter exponent: 2
4 raised to the power 2 is 16'''