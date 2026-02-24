# take input from the user
angle1 = int(input("enter first angle: "))
angle2 = int(input("enter second angle: "))
angle3 = int(input("enter third angle: "))
if((angle1+angle2+angle3)==180):
    print("the three angle can form a triangle")
else:
    print("the three angle is not forma triangle") 




# for 3 angle and type of angle


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


################# for side 



# Take input from user
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

# Check if valid sides
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Invalid sides. Sides must be greater than 0.")
elif (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("These sides can form a triangle.")
    
    # Check triangle type
    if side1 == side2 == side3:
        print("It is an Equilateral Triangle.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("It is an Isosceles Triangle.")
    else:
        print("It is a Scalene Triangle.")
else:
    print("These sides cannot form a triangle.")
