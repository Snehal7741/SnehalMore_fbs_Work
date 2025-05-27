#Write a program find reverse of a number

#Type-1: Without Parameter, Without Return
def reverse_number():
    num = 12345
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10  
        num //= 10  

    print("Reversed number:", rev)
reverse_number()


#Type-2: Without Parameter, With Return
def reverse_number():
    num = 12345  
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
        return rev  
result = reverse_number()
print("Reversed number:", result)


#Type-3: With Parameter, Without Return
def reverse_number(num):
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    print("Reversed number:", rev)
reverse_number(12345)


#Type-4: With Parameter, With Return
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    return rev  
result = reverse_number(12345)
print("Reversed number:", result)
