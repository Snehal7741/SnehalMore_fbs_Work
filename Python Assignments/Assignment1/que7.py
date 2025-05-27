# WAP TO FIND ROOTS OF QUADRATIC EQUATION


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Compute discriminant
D = b * b - 4 * a * c

# Find roots
if D >= 0:
    root1 = (-b + D ** 0.5) / (2 * a)
    root2 = (-b - D ** 0.5) / (2 * a)
    print("Roots:", root1, "and", root2)
else:
    print("No real roots")

"""
Enter a: 1
Enter b: -5
Enter c: 6
Roots: 3.0 and 2.0

"""