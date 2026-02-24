# Problem Statement: Calculate BMI category.

# taking weight from the user 
weight = float(input("Enter weight in kg: "))

# taking height form the user
height = float(input("Enter height in meters: "))

# calculating BMI

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))

'''output
Enter weight in kg: 79
Enter height in meters: 123
BMI: 0.01'''