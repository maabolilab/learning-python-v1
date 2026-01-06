class User:
    def __init__(self, name, age, address, phone_number, subjects):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.subjects = subjects

    def __str__(self):
        return f"""
        Name:           {self.name},\n
        Age:            {self.age},\n
        Address:        {self.address},\n
        Phone Number:   {self.phone_number},\n
        Subjects:       {self.subjects}
        """
