# Write a program to remove all occurrences of a given element in the list.

l1 = [10, 20, 30, 10, 40, 10, 50]

print("Original List:", l1)

remove = int(input("Enter the element to remove: "))

new_list = []

for item in l1:
    if item != remove:
        new_list.append(item)

print("List after removing", remove, ":", new_list)

#Original List: [10, 20, 30, 10, 40, 10, 50]
#Enter the element to remove: 10
#List after removing 10 : [20, 30, 40, 50]