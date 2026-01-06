from student import Student
from teacher import Teacher
from school_admin import School_Admin

def display_menu():
    print("-"*60)
    print("Press 1 to add Student")
    print("Press 2 to add Teacher")
    print("Press 3 to delete Student")
    print("Press 4 to delete Teacher")
    print("Press 5 to get all list of Students")
    print("Press 6 to get all list of teachers")
    print("Press any other key to quit.")
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

admin = School_Admin()

while True:
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
            5
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

        case "5":
            for stundent in admin.get_all_students():
                print(student)

        case "6":
            for teacher in admin.get_all_teachers():
                print(teacher)
        case _:
            print("Exit")
            break