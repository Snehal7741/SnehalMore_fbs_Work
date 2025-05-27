# wap to check if the given number is in the list or not and count how many time it comes

l1 = [100,77,45,25,98,43,77,45,67,98,34]
ele = int(input("Enter the number to search: "))
count = 0 

for num in l1:
    if num == ele:
        count += 1
if ele in l1 :
    print("Number is present:",ele)
    print("The number is present",count,"times in list")
else:
    print("The number is not in list:")