
#type3 function w par  w/o return
import math

# Function to find sum of natural numbers
def sum_natural_numbers(n):
    total = sum(range(1, n + 1))
    print("Sum of natural numbers:", total)
    

# Function to find sum of factorials
def sum_factorials(n):
    total = sum(math.factorial(i) for i in range(1, n + 1))
    print("Sum of factorials:", total)
 
# Function to find sum of powers
def sum_powers(n):
    total = sum(i ** i for i in range(1, n + 1))
    print("Sum of powers:", total)

n = 5
sum_powers(n)
sum_natural_numbers(n)
sum_factorials(n)
