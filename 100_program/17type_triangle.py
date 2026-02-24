# Problem Statement: Determine the type of triangle.

# Take input from user
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

# Check if valid triangle
if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
    print("Invalid angles. Angles must be greater than 0.")
elif angle1 + angle2 + angle3 != 180:
    print("These angles cannot form a triangle.")
else:
    print("These angles can form a triangle.")
    
    # Check triangle type
    if angle1 == angle2 == angle3:
        print("It is an Equilateral Triangle.")
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        print("It is an Isosceles Triangle.")
    else:
        print("It is a Scalene Triangle.")


'''output
Enter first angle: 80
Enter second angle: 10
Enter third angle: 90
These angles can form a triangle.
It is a Scalene Triangle.'''