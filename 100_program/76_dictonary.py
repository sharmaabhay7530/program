# Problem 76: Create student marks dictionary and find topper
# Read number of students
n = int(input("Enter number of students: "))
students = {}

# Input student marks
for _ in range(n):
    name = input("Enter student name: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# Find topper
topper = max(students, key=students.get)
print(f"The topper is {topper} with marks {students[topper]}")


'''output
Enter number of students: 1
Enter student name: krishna
Enter marks of krishna: 33
The topper is krishna with marks 33.0'''