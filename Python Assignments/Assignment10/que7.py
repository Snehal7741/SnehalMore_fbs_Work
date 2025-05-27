# 7. Create a new list with cubes of each number in the list

l1 = [12,7,9,3,8]

cube_li= []
i = 0
while i < len(l1):
    cube_li += [l1[i] * l1[i] * l1[i]]
    i =i + 1
print("Cub of each number in List :", cube_li)

#Cub of each number in List : [1728, 343, 729, 27, 512]