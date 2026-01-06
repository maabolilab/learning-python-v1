from user import User

class Teacher(User):
    def __init__(self, name, age, address, phone_number, subjects, employee_id, classes):
        super().__init__(name, age, address, phone_number, subjects)
        self.classes = classes
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id

    def prepare_exam(self):
        print("Prepare the exam...")