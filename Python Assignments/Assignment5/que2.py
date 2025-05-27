#accept the number of students and their marks in 5 subjects,
 #then calculate and display each student's percentage along with the class average.

num_students = int(input("Enter the number of students: "))

total_percentage = 0  

for i in range(1, num_students + 1):
    print(f"\nEnter marks for Student {i}:")
    total_marks = 0
    
    for j in range(1, 6):  
        marks = float(input(f"Enter marks for subject {j}: "))
        total_marks += marks
    
    percentage = (total_marks / 500) * 100  
    total_percentage += percentage
    
    print(f"Student {i} Percentage: {percentage:.2f}%")

average_percentage = total_percentage / num_students
print(f"\nClass Average Percentage: {average_percentage:.2f}%")
