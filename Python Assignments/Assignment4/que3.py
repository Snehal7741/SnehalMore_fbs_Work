#sum of series

n = int(input("Enter a number: "))

sum_n = 0  # Initialize sum

for i in range(1, n + 1):  
    sum_n += i  # Add each number to sum

print(f"Sum of first {n}  numbers is {sum_n}")
