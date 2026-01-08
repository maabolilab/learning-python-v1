from student import Student
from teacher import Teacher
from school_admin_db import School_Admin
import os
from db_connection import SchoolDB

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("-"*60)
    print("Press 1 to add Student")
    print("Press 2 to add Teacher")
    print("Press 3 to delete Student")
    print("Press 4 to delete Teacher")
    print("Press 5 to get all list of Students")
    print("Press 6 to get all list of teachers")
    print("Press 'q or quit or exit' to stop the application")
    print("-"*60)

def get_user_details():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    address = input("Enter address: ")
    phone_number = input("Enter Phone Number: ")
    subjects = input("Enter Subjects: ")

    return {
        "name": name,
        "age": age,
        "address": address,
        "phone_number": phone_number,
        "subjects": subjects
    }

school_admin_db = SchoolDB("school_admin_db")
admin = School_Admin(school_admin_db)

while True:
    clear_screen()
    display_menu()
    value = input("Enter your value: ")
    match value:
        case "1":
            print("Enter Students Details: ")
            user_details = get_user_details()
            roll_no = input("Enter Roll No: ")
            class_ = input("Enter Your Class: ")
            student = Student(
                user_details['name'], user_details['age'], user_details['address'],
                user_details['phone_number'], user_details['subjects'], roll_no, class_
            )
            admin.add_student(student)
            print(student)
        case "2":
            print("Enter Teacher Details: ")
            user_details = get_user_details()
            employee_id = input("Enter Employee Id: ")
            classes = input("Enter Your Classes: ")
            teacher = Teacher(
                user_details['name'], user_details['age'], user_details['address'],
                user_details['phone_number'], user_details['subjects'], employee_id, classes
            )
            admin.add_teacher(teacher)

        case "3":
            roll_no = input("For delete the student enter roll no: ")
            admin.delete_student(roll_no)

        case "4":
            employee_id = input("For delete the teacher enter employee no: ")
            admin.delete_teacher(employee_id)
            
        case "5":
            for student in admin.get_all_students():
                print(student)
            input("Press Enter to continue....")
        case "6":
            for teacher in admin.get_all_teachers():
                print(teacher)
            input("Press Enter to continue....")

        case "q" | "quit" | "exit":
            print("Exit")
            break
        case _:
            print("Unrecognized options. Please try again...")