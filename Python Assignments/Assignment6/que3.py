#Pattern (c): Pascal's Triangle

n = 4  # Number of rows

for i in range(n):
    print("  " * (n - i), end=" ")  
    num = 1
    for j in range(i + 1):
        print(num, end="   ")  
        num = num * (i - j) // (j + 1)  
    print()


'''
                1  
              1   1  
            1   2   1
          1   3   3   1
            
  '''