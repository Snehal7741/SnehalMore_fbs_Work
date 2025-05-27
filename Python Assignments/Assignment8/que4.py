
#type 1 function w/o par w/o return

def add_odd():
    
    n = int(input("Enter a number: "))  
    sum=0
    for i in range (1,n+1):
        if i%2 != 0:
            sum = sum+i
    print("sum of odd num is: " ,sum)

add_odd()

#type2 function w/o par  w return
def add_odd():
    n = int(input("Enter a number: "))  
    sum=0
    for i in range (1,n+1):
        if i%2 != 0:
            sum = sum+i
    return sum
res = add_odd()
print("sum of odd num is: " ,res)

#type3 function w par  w/o return
 
def add_odd(n):
    
    sum=0
    for i in range (1,n+1):
        if i%2 != 0:
            sum = sum+i
    print("sum of odd num is: " ,sum)
n = int(input("Enter a number: ")) 
add_odd(n) 

#type4  w par  - w return
def add_odd(n):
    sum = 0  
    for i in range(1, n +1):
        if i % 2 != 0:  
            sum += i
    return sum

num = int(input("Enter a number: "))  
result = add_odd(num)  
print("Sum of odd numbers is:", result)  



