#WAP to print all even numbers until n.
n = int(input("Enter a number: "))

print("Even numbers up to", n, "are:")
for i in range(1, n + 1):  # Loop from 1 to n
    if i % 2 == 0:  # Check if the number is even
        print(i, end=" ")

'''
Enter a number: 50
Even numbers up to 50 are:'
2 4 6 8 10 12 14 16 18 20 '
22 24 26 28 30 32 34 36'
38 40 42 44 46 48 50 '
'''