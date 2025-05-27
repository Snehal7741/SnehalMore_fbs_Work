#Write a program to find print the following Fibonacci series using functions:
  #1  2  3 5 8  n terms

#Type-1 Function (Without Parameter, Without Return)

def fibonacci_series():
    n = 10 
    a, b = 1, 2 
    print(a, b, end=" ")  

    for _ in range(n - 2): 
        c = a + b
        print(c, end=" ")
        a, b = b, c
fibonacci_series()

#Type-3 Function (With Parameter, Without Return)

def fibonacci_series(n):
    a, b = 1, 2  
    print(a, b, end=" ") 

    for _ in range(n - 2): 
        c = a + b
        print(c, end=" ")
        a, b = b, c
fibonacci_series(10)
