# Simple Interest Calculator

def simple_interest(principal, rate, time):
    """
    Calculate Simple Interest
    SI = (P * R * T) / 100
    """
    return (principal * rate * time) / 100

# Taking input from user
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest per year (%): "))
t = float(input("Enter Time in years: "))

# Calculating SI
si = simple_interest(p, r, t)

# Displaying result with 2 decimal places
print(f"Simple Interest is: {si:.2f}")

