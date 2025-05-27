#Write a program to create three lists of numbers, their squares and cubes

numbers = [5,8,4,9,10]  
squares = []  
cubes = []    


for num in numbers:
    squares.append(num * num )  
    cubes.append(num * num * num)    

print("Numbers: ", numbers)
print("Squares: ", squares)
print("Cubes  : ", cubes)

#Numbers:  [5, 8, 4, 9, 10]
#Squares:  [25, 64, 16, 81, 100]
#Cubes  :  [125, 512, 64, 729, 1000]S