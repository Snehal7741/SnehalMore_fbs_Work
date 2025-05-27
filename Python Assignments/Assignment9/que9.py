# 9. Power function using recursion (m^n)
def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

print("n1^n2 =", power(2, 5))

#n1^n2 = 32