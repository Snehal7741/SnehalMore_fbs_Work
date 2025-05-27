#Write a program to calculate area of circle     

# type1  - function w/o par w/o return
import math
def calculate_area():
    r= 7  # Example radius
    area = math.pi * r * r  
    print("The area of the circle is:", area)

calculate_area()

#type2 function w/o par  w return
def calculate_area():
    r = 5
    area = math.pi * r * r  
    return area  
res = calculate_area()
print("The area of the circle is:", res)


#type3 function w par  w/o return
def calculate_area(r):
    area = math.pi * r * r
    print("The area of the circle is:", area)
calculate_area(8)


#type4  w par  - w return
def calculate_area(r):
    area=math.pi * r* r
    return area 
res = calculate_area(7)

print("The area of the circle is:", res)