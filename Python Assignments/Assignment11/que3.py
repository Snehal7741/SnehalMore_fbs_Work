#3.Python Program to Sort the List According to the Second Element in a Sublist.

sublist = [[1, 3], [4, 2], [6, 5], [7, 1]]

for i in range(len(sublist)):
    for j in range(len(sublist) - i - 1):
        if sublist[j][1] > sublist[j + 1][1]:
            sublist[j], sublist[j + 1] = sublist[j + 1], sublist[j]

print("Sorted List:", sublist)

#Sorted List: [[7, 1], [4, 2], [1, 3], [6, 5]]