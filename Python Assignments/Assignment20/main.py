
# main.py

from symarks import SYMARKS
from tymarks import TYMARKS

class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self):
        total_marks = (self.sy_marks.comp_total +
                       self.ty_marks.theory)

        if total_marks >= 70:
            return "A"
        elif total_marks >= 60:
            return "B"
        elif total_marks >= 50:
            return "C"
        elif total_marks >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display_result(self):
        print(f"\n--- Student Result ---")
        print(f"Roll No     : {self.roll_no}")
        print(f"Name        : {self.name}")
        print(f"SY Comp     : {self.sy_marks.comp_total}")
        print(f"SY Maths    : {self.sy_marks.maths_total}")
        print(f"SY Elec     : {self.sy_marks.electronics_total}")
        print(f"TY Theory   : {self.ty_marks.theory}")
        print(f"TY Practical: {self.ty_marks.practical}")
        print(f"Grade       : {self.calculate_grade()}")


# Test
sy = SYMARKS(comp_total=35, maths_total=40, electronics_total=45)
ty = TYMARKS(theory=40, practical=30)

student = Student(roll_no=101, name="Snehal More", sy_marks=sy, ty_marks=ty)
student.display_result()
