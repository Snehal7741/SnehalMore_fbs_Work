# 4. Sum of n numbers using recursion
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print("Sum of first 5 numbers:", sum_n(5))

#Sum of first 5 numbers: 15