def custom_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    if step == 0:
        raise ValueError("step argument must not be zero")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

# Example usage:
print("Custom range from 1 to 10 with step 2:")
for num in custom_range(1, 10, 2):
    print(num, end=' ')
