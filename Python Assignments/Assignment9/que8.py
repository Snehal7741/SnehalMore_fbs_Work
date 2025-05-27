# 8. Check if a number is prime using recursion
def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

print(17, "is prime" if is_prime(17) else "is not prime")

#17 is prime