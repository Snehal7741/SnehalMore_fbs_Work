# 9. Separate even and odd numbers into two lists

l1 = [100,77,45,25,98,43]
even_list = []
odd_list = []
i = 0
while i < len(l1):
    if l1[i] % 2 == 0:
        even_list += [l1[i]]
    else:
        odd_list += [l1[i]]
    i += 1
print("Even List:", even_list)
print("Odd List:", odd_list)

#Even List: [100, 98]
#Odd List: [77, 45, 25, 43]S