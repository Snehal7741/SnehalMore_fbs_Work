
# 10. Write a Program to Print the List After Removing Even Numbers

l1 = [12, 9, 4, 15, 11, 18, 21, 6, 27]

oddL1= []
for num in l1:
    if num % 2 != 0:  
        oddL1.append(num)


print("Original List:", l1)
print("list Without even numbers:", oddL1)

'''
Original List: [12, 9, 4, 15, 11, 18, 21, 6, 27]
list Without even numbers: [9, 15, 11, 21, 27]'

'''