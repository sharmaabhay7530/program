# Problem Statement: Find factorial using while loop.


#  taking input from the user 
num = int(input("Enter a number: "))
factorial = 1
i = 1

# using loop for it 
while i <= num:
    factorial *= i  
    i += 1


#  display the factorial 

print("Factorial of", num, "is:", factorial)

'''output
Enter a number: 5
Factorial of 5 is: 120
'''