from student import Student
from teacher import Teacher

class School_Admin:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def add_student(self, student: Student):
        self.students[student.roll_no] = student
        print(self.students)

    def add_teacher(self, teacher: Teacher):
        self.teachers[teacher.employee_id] = teacher

    def delete_teacher(self, employee_id):
        return self.teachers.pop(employee_id, None)
    
    def delete_student(self, roll_no):
        return self.students.pop(roll_no, None)
    
    def get_all_students(self):
        return list(self.students.values())
    
    def get_all_teachers(self):
        return list(self.teachers.values())