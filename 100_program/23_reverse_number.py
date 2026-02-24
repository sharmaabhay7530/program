# Problem Statement: Reverse a number using while loop.

#  taking number from the user 
num = int(input("Enter a number: "))
original_num = num  
reversed_num = 0

# using while loop
while num > 0:
    digit = num % 10            
    reversed_num = reversed_num * 10 + digit  
    num = num // 10  

# display the reverse order

print("Reversed number of", original_num, "is:", reversed_num)

'''output
Enter a number: 5432
Reversed number of 5432 is: 2345'''