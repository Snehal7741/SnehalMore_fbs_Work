#Pattern (f): Number Pyramid

n = 5  # Number of rows

for i in range(1, n + 1):
    print("  " * (n - i), end=" ")  # Print leading spaces for centering
    for j in range(1, 2 * i, ):  # Printing numbers in increasing order
        print(j, end=" ")
    print()

    '''
         1 
       1 2 3 
     1 2 3 4 5
   1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8 9

  '''