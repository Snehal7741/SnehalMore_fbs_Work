def palindrome_generator():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1


print("First 10 palindrome numbers:")
gen = palindrome_generator()
for _ in range(10):
    print(next(gen), end=' ')
print("\n")
