#Write a program to check if entered number is a palindrome or 

#Type-1: Without Parameter, Without Return

def check_palindrome():
    num = 12321  
    original = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10 
        num //= 10  
    if original == rev:
        print(original, "is a palindrome")
    else:
        print(original, "is not a palindrome")

check_palindrome()

#Type-2: Without Parameter, With Return
def check_palindrome():
    num = 12321  
    original = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    return original == rev  

result = check_palindrome()
print("Is palindrome:", result)

#Type-3: With Parameter, Without Return
def check_palindrome(num):
    original = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    if original == rev:
        print(original, "is a palindrome")
    else:
        print(original, "is not a palindrome")
check_palindrome(12321)

#Type-4: With Parameter, With Return
def check_palindrome(num):
    original = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    return original == rev  
num = 12321
result = check_palindrome(num)
print(num, "is a palindrome" if result else "is not a palindrome")