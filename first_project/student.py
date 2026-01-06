from user import User

class Student(User):
    def __init__(self, name, age, address, phone_number, subjects, roll_no, class_):
        super().__init__(name, age, address, phone_number, subjects)
        self.class_ = class_
        self.roll_no = roll_no

    def get_roll_no(self):
        return self.roll_no

    def write_exam(self):
        print("Write the exam...")

    def __str__(self):
        return f"""
        Name:           {self.name},\n
        Age:            {self.age},\n
        Address:        {self.address},\n
        Phone Number:   {self.phone_number},\n
        Subjects:       {self.subjects},\n
        Roll No:        {self.roll_no},\n
        Class:          {self.class_}
        """