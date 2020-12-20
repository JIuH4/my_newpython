class ColorSetMixin:

    def color_set(self, color):
        self.color = color


class Plane(ColorSetMixin):
    def __init__(self, name, engines_count=2, wings_num=2, ):
        self.engines_count = engines_count
        self.wings_num = wings_num
        self.name = name

    def down(self):
        raise NotImplementedError

    def up(self):
        raise NotImplementedError


class CivilPlane(Plane):
    def __init__(self, name, passengers_count, light=False, music=False):
        self.music = music
        self.light = light

        self.passengers_count = passengers_count
        super().__init__(name)

    def up(self):
        return "up"

    def down(self):
        return "down"

    def enable_music(self):
        self.music = not self.music
        return f"music on {self.music}"

    def toggle_light(self):
        self.light = not self.light
        return f"light on {self.light}"


class WarPlane(Plane):
    def __init__(self, name, bombs_number, ):
        self.catapult_not_launched = True
        self.bombs_number = bombs_number
        super().__init__(name)

    def up(self):
        return "up"

    def down(self):
        return "down"

    def drop_bomb(self):
        if self.bombs_number > 0:
            self.bombs_number -= 1
        return f"bomb ostalos {self.bombs_number}"

    def catapult(self):
        if self.catapult_not_launched:
            self.catapult_not_launched = False
            return "catapult launch"
        else:
            return "catapult alredy launched"


plane2 = CivilPlane("Civil", 6)
plane2.color_set("blue")
plane3 = WarPlane("War", 5)
plane3.color_set("red")

print(plane2.color)
print(plane2.passengers_count)
print(plane2.up())
print(plane2.down())
print(plane2.enable_music())
print(plane2.enable_music())
print(plane2.enable_music())
print(plane2.toggle_light())
print(plane2.toggle_light())
print(plane2.toggle_light())

print(plane3.color)
print(plane3.bombs_number)
print(plane3.up())
print(plane3.down())
print(plane3.drop_bomb())
print(plane3.drop_bomb())
print(plane3.drop_bomb())
print(plane3.drop_bomb())
print(plane3.drop_bomb())
print(plane3.drop_bomb())
print(plane3.drop_bomb())
print(plane3.drop_bomb())
print(plane3.drop_bomb())
print(plane3.catapult())
print(plane3.catapult())
