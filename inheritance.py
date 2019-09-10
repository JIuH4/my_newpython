class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):
    def __init__(self, name, job_title):
        super(Employee, self).__init__(name)
        self.job_title = job_title

    def is_employee(self):
        return True

    def do_work(self):
        return f"{self.job_title} do work"


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square:
    def __init__(self, height):
        self.height = height

    def perimeter(self):
        return self.height * 4


class RightPyramid(Triangle, Square):
    def __init__(self, base, slain_height):
        # super().__init__()
        self.height = base

        self.base = base
        self.slain_height = slain_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slain_height + base_area


pyramid = RightPyramid(4, 5)
print(pyramid.area())
print(RightPyramid.__mro__)
