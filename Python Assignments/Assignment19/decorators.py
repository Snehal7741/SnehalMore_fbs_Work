def memoize(func):
    cache = {}
    def wrapper(arg):
        if arg in cache:
            print(f"Fetching from cache for: {arg}")
            return cache[arg]
        print(f"Calculating result for: {arg}")
        result = func(arg)
        cache[arg] = result
        return result
    return wrapper

# Example usage: Fibonacci with memoization
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test the memoized Fibonacci function
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")
