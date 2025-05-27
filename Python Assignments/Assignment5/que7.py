#1! + 2! + 3! + 4! + ... + n!
#N + N² + N³ + N⁴ + ... + N^N
#Sum of a geometric series from 1 to n where the common ratio is 2
#S = a + a2/2 + a3/3 + ... + a10/10
#x - x(2/3) + x(3/5) - x(4/7) + ... to n terms

import math


n = int(input("Enter the value of n: "))
N = int(input("Enter the value of N: "))
a = int(input("Enter the first term (a): "))
x = float(input("Enter the value of x: "))

# 1. Factorial Series: 1! + 2! + 3! + ... + n!
fact_sum = 0
for i in range(1, n + 1):
    fact_sum += math.factorial(i)
print("Sum of factorial series:", fact_sum)

# 2. Exponential Series: N + N² + N³ + ... + N^N
exp_sum = 0
for i in range(1, N + 1):
    exp_sum += N ** i
print("Sum of exponential series:", exp_sum)

# 3. Geometric Series (common ratio 2): S = a + a2 + a4 + ... 
geo_sum = 0
for i in range(n):
    geo_sum += a * (2 ** i)
print("Sum of geometric series:", geo_sum)

# 4. Fraction Series: S = a + a2/2 + a3/3 + ... + a10/10
frac_sum = 0
for i in range(1, 11):
    frac_sum += (a * i) / i
print("Sum of fraction series:", frac_sum)

# 5. Alternating Series: x - x(2/3) + x(3/5) - x(4/7) + ... up to n terms
alt_sum = 0
sign = 1
for i in range(1, n + 1):
    alt_sum += sign * x * (i / (2 * i - 1))
    sign *= -1
print("Sum of alternating series:", alt_sum)
