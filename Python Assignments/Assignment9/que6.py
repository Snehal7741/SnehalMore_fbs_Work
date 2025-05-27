# 6. Fibonacci series using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 7
fib_series = [fibonacci(i) for i in range(n)]
print("Fibonacci series:", fib_series)

#Fibonacci series: [0, 1, 1, 2, 3, 5, 8]