#pattern g

n = 5  # Number of rows

for i in range(1, n + 1):
    
    print("  " * (n - i), end=" ")

    
    for j in range(1, i + 1):
        print(j, end=" ")

   
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  


"""         
         1 
       1 2 1 
     1 2 3 2 1
   1 2 3 4 3 2 1
 1 2 3 4 5 4 3 2 1
 
"""