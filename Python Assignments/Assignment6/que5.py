#Pattern (e): Pyramid Pattern

n = 5  # Height of pyramid
for i in range(n):
    print("  " * (n - i - 1), end="  ")
    print("* " * (2*i + 1))

'''
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

'''