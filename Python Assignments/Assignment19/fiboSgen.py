def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Example usage:
print("Fibonacci numbers up to 100:")
for num in fibonacci_generator(100):
    print(num, end=' ')
print()
