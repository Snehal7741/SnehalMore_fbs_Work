
# 3. Find the second largest element in the list

l1 = [100,77,45,25,98,43]

largest = l1[0]
second = 0
i = 0
while i < len(l1):
    if l1[i] > largest:
        second = largest
        largest = l1[i]
    elif l1[i] > second and l1[i] != largest:
        second = l1[i]
    i = i+1
print("Second Largest:", second)

#Second Largest: 98