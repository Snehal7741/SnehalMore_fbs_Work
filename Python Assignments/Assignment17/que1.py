class Student:
    def __init__(self, student_id, name, age, percentage):
        """Parameterized constructor for Student."""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage
    
    def display(self):
        """Displays Student information."""
        print("--- Student Details ---")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Percentage: {self.percentage:.2f}%")
    
    def accept(self):
        """Accepts Student information from the user."""
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))
    
    def calculate_rank(self):
        """Calculates the rank based on percentage (simple example)."""
        if self.percentage >= 90:
            return "A"
        elif self.percentage >= 80:
            return "B"
        elif self.percentage >= 70:
            return "C"
        else:
            return "D"
    
    def __str__(self):
        """Overrides the string representation of the Student object."""
        return f"Student(ID={self.student_id}, Name={self.name}, Age={self.age}, Percentage={self.percentage:.2f})"


class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        """Parameterized constructor for EnggStudent."""
        super().__init__(student_id, name, age, percentage)  # Call Student's constructor
        self.branch = branch
        self.internal_marks = internal_marks
    
    def display(self):
        """Displays EnggStudent information (overrides Student's display)."""
        super().display()  # Call Student's display method
        print(f"Branch: {self.branch}")
        print(f"Internal Marks: {self.internal_marks}")
    
    def accept(self):
        """Accepts EnggStudent information from the user (overrides Student's accept)."""
        super().accept()  # Call Student's accept method
        self.branch = input("Enter Branch: ")
        self.internal_marks = float(input("Enter Internal Marks: "))
    
    def calculate_rank(self):
        """Calculates rank for EnggStudent (overrides Student's calculate_rank).
        This is a placeholder - you might have a different ranking logic.
        """
        total_marks = self.percentage + self.internal_marks
        if total_marks >= 190:  # Assuming max is 200
            return "A+"
        elif total_marks >= 170:
            return "A"
        elif total_marks >= 150:
            return "B"
        else:
            return "C"
    
    def __str__(self):
        """Overrides the string representation for EnggStudent."""
        return f"EnggStudent(ID={self.student_id}, Name={self.name}, Age={self.age}, Percentage={self.percentage:.2f}, Branch={self.branch}, InternalMarks={self.internal_marks})"


class MedicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, marks_of_internship):
        """Parameterized constructor for MedicalStudent."""
        super().__init__(student_id, name, age, percentage)  
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship
    
    def display(self):
        """Displays MedicalStudent information (overrides Student's display)."""
        super().display()  # Call Student's display method
        print(f"Specialization: {self.specialization}")
        print(f"Marks of Internship: {self.marks_of_internship}")
    
    def accept(self):
        """Accepts MedicalStudent information from the user (overrides Student's accept)."""
        super().accept()  # Call Student's accept method
        self.specialization = input("Enter Specialization: ")
        self.marks_of_internship = float(input("Enter Marks of Internship: "))
    
    def calculate_rank(self):
        """Calculates rank for MedicalStudent (overrides Student's calculate_rank).
        This is a placeholder - you might have a different ranking logic.
        """
        total_marks = self.percentage + (self.marks_of_internship / 10)  # Adjust internship marks
        if total_marks >= 100:
            return "Distinction"
        elif total_marks >= 80:
            return "First Class"
        elif total_marks >= 60:
            return "Second Class"
        else:
            return "Pass"
    
    def __str__(self):
        """Overrides the string representation for MedicalStudent."""
        return f"MedicalStudent(ID={self.student_id}, Name={self.name}, Age={self.age}, Percentage={self.percentage:.2f}, Specialization={self.specialization}, InternshipMarks={self.marks_of_internship})"


class College:
    def __init__(self, num_students):
        """Parameterized constructor for College."""
        self.students = []  # Initialize an empty list to hold students
        self.max_students = num_students  # Maximum number of students the college can hold
    
    def add_student(self, student):
        """Adds a student to the college."""
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"{student.name} added to the college.")
        else:
            print("College is full. Cannot add more students.")
    
    def get_student(self, student_id):
        """Retrieves a student by their ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None  # Student not found
    
    def remove_student(self, student_id):
        """Removes a student by their ID."""
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                removed_student = self.students.pop(i)
                print(f"{removed_student.name} removed from the college.")
                return
        print(f"Student with ID {student_id} not found.")
    
    def __str__(self):
        """Overrides the string representation of the College object."""
        return f"College with {len(self.students)} students (Max: {self.max_students})"


if __name__ == "__main__":
    college = College(5)  

    engg_student1 = EnggStudent("E101", "Snehal", 20, 85.5, "Computer Science", 92.0)
    medical_student1 = MedicalStudent("M201", "Prtiksha", 21, 78.0, "Data Science", 880)

    college.add_student(engg_student1)
    college.add_student(medical_student1)

    print(college)

    engg_student1.display()
    print(f"Rank: {engg_student1.calculate_rank()}")

    medical_student1.display()
    print(f"Rank: {medical_student1.calculate_rank()}")

    found_student = college.get_student("E101")
    if found_student:
        print("Found student:", found_student)

    college.remove_student("M201")
    college.remove_student("M300") 

    print(college)