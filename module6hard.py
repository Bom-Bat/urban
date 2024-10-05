class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.sides_count = len(sides)
        self.filled = True
        self.__sides = list(sides)
        self.__color = list(color)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == 3:
            return (len(new_sides) == self.sides_count and
                    all(isinstance(i, int) and i > 0 for i in new_sides)
                    or len(new_sides) == 1)
        else:
            return (len(new_sides) == self.sides_count and
                    all(isinstance(i, int) and i > 0 and i == new_sides[0] for i in new_sides)
                    or len(new_sides) == 1)

    def get_sides(self):
        return f'Стороны фигуры: {self.__sides}'

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def ust_sides(self, new_sides):
        new_sides = list(new_sides)
        if len(new_sides) == 3 and self.sides_count == 3:
            self.__sides = new_sides
        elif len(new_sides) != 1 and (len(new_sides) != self.sides_count
                                      or all(isinstance(i, int) and 0 < i for i in new_sides)):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = [new_sides[0]] * self.sides_count
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *l_stor):
        new_sides = self.ust_sides(l_stor)
        super().__init__(__color, *new_sides)
        self.__sides = new_sides
        self.__radius = int(self.__sides[0]) / (2 * 3.1415926)

    def get_square(self):
        self.__radius = self.set_sides()[0] / (2 * 3.1415926)
        return f'Площадь круга: {3.1415926 * self.__radius ** 2} Радиус: {self.__radius}'


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *l_stor):
        new_sides = self.ust_sides(l_stor)
        super().__init__(__color, *new_sides)
        self.__sides = new_sides

    def get_square(self):
        self.__sides = self.set_sides()
        s = sum(self.__sides) / 2
        return (f'Площадь треугольника: {(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))
                                         ** 0.5} с торонами: {self.__sides[0]}, {self.__sides[1]}, {self.__sides[2]}')


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *l_stor):
        new_sides = self.ust_sides(l_stor)
        super().__init__(__color, *new_sides)
        self.__sides = list(new_sides)

    def get_volume(self):
        return f'Обьем куба: {self.set_sides()[0] ** 3} со стороной: {self.set_sides()[0]}'


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(f'Цвет линии фигуры (R, G, B):{circle1.get_color()}')
cube1.set_color(300, 70, 15) # Не изменится
print(f'Цвет линии фигуры (R, G, B):{cube1.get_color()}')


# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(f'Периметр фигуры: {len(circle1)}')

# Проверка площади круга и радиуса:
print(circle1.get_square())

# Проверка объёма (куба) и стороны:
print(cube1.get_volume())
"""
triangle1 = Triangle((150, 70, 120), 8, 15, 10)

# Проверка на изменение цветов:
triangle1.set_color(300, 70, 15) # Не изменится
print(f'Цвет линии фигуры (R, G, B):{triangle1.get_color()}')

# Проверка на изменение сторон:
print(triangle1.get_sides())
triangle1.set_sides(9, 12, 7) # Изменится
print(triangle1.get_sides())

# Проверка площади треугольника и сторон:
print(triangle1.get_square())
"""