#WAP to  check if given number is strong or not

num = int(input("Enter a number: "))
 
sum = 0  

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

while num > 0:
    digit = num % 10  
    sum += factorial(digit)  
    num //= 10  


if sum == num:
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is NOT a Strong Number.")
