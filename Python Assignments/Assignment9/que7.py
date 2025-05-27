## 7. Sum of digits using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print("Sum of digits:", sum_of_digits(1234))

#Sum of digits: 10