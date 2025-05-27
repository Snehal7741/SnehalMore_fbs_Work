# 5.Recursive function to find factorial of a number
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    return n * factorial(n - 1)  


num = 5 
print("Factorial of", num, "is", factorial(num))

#Factorial of 5 is 120