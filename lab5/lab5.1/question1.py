# 1. Student Marks Analyzer 
# You are given a list of student marks. 
# • Remove invalid marks (less than 0 or greater than 100) 
# • Calculate average 
# • Find topper(s) 
# • Display grades based on average.  


marks = [95, 85, 120, -5, 76, 88, 100, 67]

# Remove invalid marks
marks = [m for m in marks if 0 <= m <= 100]

# Average
average = sum(marks)/len(marks)

# Find topper(s)
topper = [m for m in marks if m == max(marks)]

# Display grade based on average
if average >= 90:
    grade = 'A+'
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade = 'C'
else:
    grade = 'D'

print("Valid Marks:", marks)
print("Average:", average)
print("Topper(s):", topper)
print("Grade:", grade)

# //ouptut-------
# Average: 85.16666666666667
# Topper(s): [100]
# Grade: A ---------//



