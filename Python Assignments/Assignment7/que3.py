#Pattern 3: Number Triangl


n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == j or j == 1 or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

'''
1 
1 2 
1   3
1     4
1 2 3 4 5

'''