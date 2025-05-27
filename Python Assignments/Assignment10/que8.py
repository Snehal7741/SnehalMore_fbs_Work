
# 8. Create a duplicate of an existing list

l1 = [100,77,45,25,98,43,77,45,67,98,34]

d_list = []
i = 0
while i < len(l1):
    d_list += [l1[i]]
    i =i+ 1
print("Duplicated List is :", d_list)

