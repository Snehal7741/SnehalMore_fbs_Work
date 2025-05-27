# q1. Write a program to calculate area of rectangle

# #type 1 function w/o par w/o return
def calculate_area():
    length = 10  
    width = 5   
    area = length * width
    print("The area of the rectangle is:", area)

calculate_area()

#type 2 function w/o par  w return

def calculate_area():
    length = 10  
    width = 5   
    return length * width   

area = calculate_area()

print("The area of the rectangle is:", area)



#type3 function w par  w/o return

def calculate_area(length, width):
    area = length * width
    print("The area of the rectangle is:", area)

calculate_area(10, 5)


#type4  w par  - w return
def calculate_area(length, width):
    return length * width  

area = calculate_area(10, 5)

print("The area of the rectangle is:", area)