import math

class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides, filled=False):
        self.__sides = list(sides)
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_types and valid_values

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            print('Ошибка: количество сторон не совпадает')

class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], radius: int, filled=False):
        super().__init__(color, 2 * math.pi * radius)
        self.radius = radius

    def get_square(self):
        return math.pi * self.radius ** 2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side: int, filled=False):
        cube_sides = [side] * 12
        super().__init__(color, *cube_sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())




