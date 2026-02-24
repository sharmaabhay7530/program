# Problem Statement: Assign grades based on marks.

# taking  input from the user
marks = float(input("Enter marks out of 100: "))

# check condition
if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"

# dispaly 
print("Grade:", grade)

''' output
Enter marks out of 100 : 100
Grade: A
'''