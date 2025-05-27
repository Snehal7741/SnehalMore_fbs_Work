#Q6.SWAP to remove duplicte values from list

l1 = [100,77,45,25,98,43,77,45,67,98,34]

print(l1)

l1 =list(set(l1))
print(l1)

#[100, 77, 45, 25, 98, 43, 77, 45, 67, 98, 34]
#[98, 67, 100, 34, 43, 45, 77, 25]