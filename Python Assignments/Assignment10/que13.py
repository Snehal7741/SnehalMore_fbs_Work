#rite a program to print list after removing even numbers.


l1 = [100,77,45,25,98,43]

odd_numbers = []

for num in l1:
    if num % 2 != 0: 
        odd_numbers.append(num)

print("List after removing even numbers:", odd_numbers)

#List after removing even numbers: [77, 45, 25, 43]