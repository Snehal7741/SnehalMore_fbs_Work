#2. Python Program to Merge Two Lists and Sort it

list1 = [15, 45, 5, 25]
list2 = [10, 35, 20, 30]

# Merging lists
merged_list = list1 + list2

for i in range (0,len(merged_list)):
    for j in range (i+1 , len(merged_list)):
        if merged_list[j]< merged_list[i]:
           merged_list[i], merged_list[j] = merged_list[j], merged_list[i]


print("Sorted list is: ",merged_list)

#Sorted list is:  [5, 10, 15, 20, 25, 30, 35, 45]
