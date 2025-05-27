#Python Program to Put Even and Odd elements of a List into two Different


lst = [23,68,90,34,65,89]

even_num = []
odd_num = []

for num in lst:
    if num % 2 == 0:
        even_num.append(num)  
    else:
        odd_num.append(num)   
print("Even numbers list :", even_num)
print("Odd numbers list:", odd_num)

#Even numbers list : [68, 90, 34]
#Odd numbers list: [23, 65, 89]