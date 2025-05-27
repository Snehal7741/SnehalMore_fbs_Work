
#type4  w par  - w return

import math

# Function to find sum of natural numbers
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Function to find sum of factorials
def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += math.factorial(i)
    return total

# Function to find sum of powers
def sum_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = 5
natural_sum = sum_natural_numbers(n)
factorial_sum = sum_factorials(n)
power_sum = sum_powers(n)

print("Sum of natural numbers:", natural_sum)
print("Sum of factorials:", factorial_sum)
print("Sum of powers:", power_sum)
