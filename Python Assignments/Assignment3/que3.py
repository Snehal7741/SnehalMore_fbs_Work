#Write a program to input angles of a triangle and check whether triangle is valid or not


a1 = float(input("Enter first angle: "))
a2 = float(input("Enter second angle: "))
a3 = float(input("Enter third angle: "))

sum = a1 +a2 +a3

if  (sum) == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")


''''
Enter first angle: 45
Enter second angle: 20
Enter third angle: 125
The triangle is not valid.
'''
