class Car:
    number_of_weels = 4

    @classmethod
    def count_axis_number(cls):
        return cls.number_of_weels / 2

    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f"{self.name} is driving")


car = Car("Lada")
print(car.count_axis_number())


class Plane:
    engines_count = 2

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_wings_number():
        return 2

    def vzlet(self):
        print("poleteli")

    def posadka(self):
        print("posadka")


plane = Plane("Plane")
print(plane.name, Plane.engines_count, Plane.get_wings_number())
plane.vzlet()
plane.posadka()
