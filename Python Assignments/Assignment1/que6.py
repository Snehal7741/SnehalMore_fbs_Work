#python program to to take 2 angle from user as input and find find third angle of triangle

A = float(input("Enter the first angle: "))
B = float(input("Enter the second angle: "))


C = 180 - (A + B)


print(f"The third angle of the triangle is: {C}°")

"""
output:
Enter the first angle: 70
Enter the second angle: 80
The third angle of the triangle is: 30.0°S

"""