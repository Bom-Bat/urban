from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        j = 1
        ost = 100
        while ost > 0:
            ost = ost - self.power
            if ost < self.power:
                self.power = ost
            print(f'{self.name} сражается {j} день..., осталось {ost} воинов.')
            sleep(1)
            j += 1
        return print(f'{self.name} одержал победу спустя {j -1} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')