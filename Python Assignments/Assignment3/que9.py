#Input 5 subject marks from user and display grade(eg.First class,Second class ..)


sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100  


if percentage >= 70:
    grade = "First Class"
elif percentage >= 60:
    grade = "Second Class"
elif percentage >= 40:
    grade = "Pass Class"
else:
    grade = "Fail"

print("\nTotal Marks is :", total_marks)
print(f"Percentage is : {percentage:.2f} %")
print(" Grade is:", grade)


''''
Enter marks for Subject 1: 90
Enter marks for Subject 2: 98
Enter marks for Subject 3: 89
Enter marks for Subject 4: 78
Enter marks for Subject 5: 97

Total Marks is : 452.0
Percentage is : 90.40 %
 Grade is: First Class
'''