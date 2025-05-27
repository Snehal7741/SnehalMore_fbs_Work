
#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
  
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("Invalid triangle! The given sides do not form a valid triangle.")
''''
Enter first side: 34
Enter second side: 56
Enter third side: 23
The triangle is Scalene.

'''