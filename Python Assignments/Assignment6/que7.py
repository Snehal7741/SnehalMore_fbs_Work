#Pattern (g): Alphabet Pyramid
n = 5  # Number of rows

for i in range(n):
    print("  " * (n - i - 1), end=" ")  # Print leading spaces for centering
    for j in range(2*i + 1):
        print(chr(65 + j), end=" ")  # Print A, B, C, etc.
    print()


'''
         A 
       A B C 
     A B C D E
   A B C D E F G
 A B C D E F G H I

  '''