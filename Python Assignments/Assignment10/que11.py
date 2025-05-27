#write a program to print all numbers which are divisible by m and n in the list

lst = [45,90,34,67,85,20,35,100]

m = int(input("Enter the first divisor (m): "))
n = int(input("Enter the second divisor (n): "))

print("Numbers divisible by", m, "and", n, "are:")

for num in lst:
    if num % m == 0 and num % n == 0:
        print(num, end=" ")
