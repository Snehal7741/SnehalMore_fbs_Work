#write a program to find sum of digits of a number.

#type 1 function w/o par w/o return
def sum_of_digits():
    num = 12345 
    total = 0
    
    while num > 0:
        total += num % 10  
        num //= 10  

    print("Sum of digits:", total)

sum_of_digits()


#Type-2: Without Parameter, With Return
def sum_of_digits():
    num = 12345
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total 
result = sum_of_digits()
print("Sum of digits:", result)


#Type-3: With Parameter, Without Return
def sum_of_digits(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    print("Sum of digits:", total)
sum_of_digits(12345)



#Type-4: With Parameter, With Return
def sum_of_digits(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total  

result = sum_of_digits(12345)
print("Sum of digits:", result)
