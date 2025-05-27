# 4. Reverse the list

l1 = [100,77,45,25,98,43]
reversed_li = []
i = len(l1) - 1
while i >= 0:
    reversed_li+= [l1[i]]
    i =i-1
print("Reversed List:", reversed_li)

#Reversed List: [43, 98, 25, 45, 77, 100]