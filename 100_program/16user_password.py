# Problem Statement: Validate username and password.

#  taking username from the user
username = input("Enter username: ")
# taking password from the user 
password = input("Enter password: ")

# Validate username
if len(username) < 5 or not username.isalnum():
    print("Invalid username. Must be at least 5 characters long and contain only letters and digits.")
else:
    # Validate password
    if len(password) < 8:
        print("Invalid password. Must be at least 8 characters long.")
    elif not any(char.isalpha() for char in password):
        print("Invalid password. Must contain at least one letter.")
    elif not any(char.isdigit() for char in password):
        print("Invalid password. Must contain at least one digit.")
    else:
        print("Username and Password are valid.")


'''output
Enter username: krishna verma
Enter password: Krishn@2004
Invalid username. Must be at least 5 characters long and contain only letters and digits.'''