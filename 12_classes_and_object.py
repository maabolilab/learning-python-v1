class Human:
    def __init__(self, human_name, human_age):
        self.name = human_name
        self.age = human_age

    def sleep(self):
        print(f"{self.name} Sleeping...")

    def eat(self):
        print(f"{self.name} Eating....")

harmeet = Human("Harmeet", "32")
print(harmeet.name)
print(harmeet.age)
harmeet.sleep()

class MotorCycle:
    def __init__(self, name, company, make, model, oil):
        self.m_name = name
        self.m_company = company
        self.m_make = make
        self.m_model = model
        self.m_oil = oil

    def start(self):
        print(f"{self.m_name} starts")

    def accelrate(self):
        print(f"{self.m_name} with {self.m_make} and {self.m_model} accelrate upto 200km/h")

    def service(self):
        print(f"{self.m_name} using {self.m_oil}")

bullet = MotorCycle("Bullet", "Enfield", 2024, "Electric", "Castrol")
suplender = MotorCycle("Splender", "Hero", 2025, "Petrol", "Engine Oil")

bullet.start()
suplender.start()
