class Vehicle:
    __COLOR_VARIANTS = ['синий', 'красный', 'зеленый', 'черный', 'белый', 'желтый']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'\033[34mМодель: \033[32m{self.__model}'

    def get_horsepower(self):
        return f'\033[34mМощность двигателя: \033[32m{self.__engine_power}'

    def get_color(self):
        return f'\033[34mЦвет: \033[32m{self.__color}'

    def print_info(self):
        a = self.get_model()
        b = self.get_horsepower()
        c = self.get_color()
        print(f'\n\t{a}\n\t{b}\n\t{c}\n\t\033[34mВладелец: \033[32m{self.owner}')

    def set_color(self, new_color):
        new_col = new_color.lower()
        if new_col in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print("\033[31m"f'\n\tНельзя изминить цвет на \033[32m"{new_color}"')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['синий', 'красный', 'зеленый', 'черный', 'белый', 'желтый']
vehicle1 = Sedan('Федот', 'Toyota Mark II', 'Синий', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('ГолУбой')
vehicle1.set_color('ЧЕрНЫй')
vehicle1.owner = 'Калян'

# Проверяем что поменялось
vehicle1.print_info()
