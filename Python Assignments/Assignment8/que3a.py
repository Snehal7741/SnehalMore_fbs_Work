 #write a program to find the sum of the following series using functions:
#Given series:
#1.Sum of natural numbers:
   #1+2+3+4+⋯+n

#2 Sum of factorials:
   #1!+2!+3!+4!+⋯+n!

#3 Sum of powers:
    #1^1+2^2+3^3+......+n^n

import math

#Type1= function w/o par w/o return

# Function to find sum of natural numbers
def sum_natural_numbers():
    n = 5  # Example value of n
    total = sum(range(1, n + 1))
    print("Sum of natural numbers:", total)

sum_natural_numbers()

# Function to find sum of factorials
def sum_factorials():
    n = 5  # Example value of n
    total = sum(math.factorial(i) for i in range(1, n + 1))
    print("Sum of factorials:", total)
sum_factorials()

# Function to find sum of powers
def sum_powers():
    n = 5  # Example value of n
    total = sum(i ** i for i in range(1, n + 1))
    print("Sum of powers:", total)
sum_powers()
