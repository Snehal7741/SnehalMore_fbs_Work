#type2 function w/o par  w return


import math

# Function to find sum of natural numbers
def sum_natural_numbers():
    n = 5  # Example value of n
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print("Sum of natural numbers:", sum_natural_numbers())

# Function to find sum of factorials
def sum_factorials():
    n = 5  # Example value of n
    total = 0
    for i in range(1, n + 1):
        total += math.factorial(i)
    return total
print("Sum of factorials:", sum_factorials())

# Function to find sum of powers
def sum_powers():
    n = 5  # Example value of n
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total
print("Sum of powers:", sum_powers())
