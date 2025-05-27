#Write a program to find maximum and minimum element in a list.

l1 = [100,77,45,25,98,43]

maximum = l1[0]
minimum = l1[0]

for num in l1:
    if num > maximum:
        maximum = num  
    if num < minimum:
        minimum = num  
print("Maximum element:", maximum)
print("Minimum element:", minimum)

#Maximum element: 100
#Minimum element: 25