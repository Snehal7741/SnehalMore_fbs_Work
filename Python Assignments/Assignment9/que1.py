# 1. Sum of the series: 1! + 2! + 3! + ... + n!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_of_series(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_of_series(n - 1)

n = 5  
print("Sum of series:", sum_of_series(n))

#Sum of series: 153