from student import Student
from teacher import Teacher
from db_connection import SchoolDB

class School_Admin:
    def __init__(self, school_admin_db: SchoolDB):
        self.school_admin_db = school_admin_db

    def add_student(self, student: Student):
        self.school_admin_db.insert_student(student)

    def add_teacher(self, teacher: Teacher):
        self.school_admin_db.insert_teacher(teacher)

    def delete_teacher(self, employee_id):
        return self.delete_teacher(employee_id)
    
    def delete_student(self, roll_no):
        return self.school_admin_db.delete_student_db(roll_no)
    
    def get_all_students(self):
        rows = self.school_admin_db.get_all_students()
        return [Student(r["name"], r["age"], r["address"], r["phone_number"], r["subjects"], r["roll_no"], r["class_"]) for r in rows]
    
    def get_all_teachers(self):
        return self.school_admin_db.get_all_teachers()