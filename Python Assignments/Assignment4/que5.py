#WAP to print Fibonacci series upto n.

n = int(input("Enter the number of terms: "))

a, b = 0, 1  
count = 0  

print("Fibonacci Series:", end=" ")

while count < n:
    print(a, end=" ")
    a, b = b, a + b 
    count += 1  