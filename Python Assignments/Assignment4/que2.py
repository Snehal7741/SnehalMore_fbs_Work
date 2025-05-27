#WAP to print all odd numbers until n.

n = int(input("Enter a number: "))

print("Odd  numbers up to", n, "are:")
for i in range(1, n + 1):  # Loop from 1 to n
    if i % 2 != 0:  # Check if the number is even
        print(i, end=" ")

'''
Enter a number: 50
Odd  numbers up to 50 are:
1 3 5 7 9 11 13 15 17 19
 21 23 25 27 29 31 33 35 
 37 39 41 43 45 47 49 
 

'''