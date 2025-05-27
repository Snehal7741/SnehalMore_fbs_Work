
# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

lst = [10, 20, 4, 45, 99]
n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print("Second Largest Number:", lst[-2])

#Second Largest Number: 45