# 3. Reverse a number using recursion
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

num = 12345
print("Reversed number:", reverse_number(num))

#Reversed number: 54321