import threading
from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):

    def __init__(self, name):
        super().__init__(name=name)
        self.name = str(name)

    def run(self):
        sleep(randint(3, 10))


class Cafe(Table):
    guests = []
    tables = []

    def __init__(self, *args):
        super().__init__(self)
        self.queue = Queue()
        for i in args:
            self.tables.append(i)

    def guest_arrival(self, *args):
        for i in args:
            self.guests.append(i.name)
            self.queue.put(i.name)

        for i in range(len(self.tables)):
            name = self.queue.get()
            for table in self.tables:
                if table.guest is None:
                    table.guest = name
                    print(f'{table.guest} сел(-а) за стол номер {table.number}')
                    Guest(name=name).start()
                    break
                else:
                    continue

        for i in range(self.queue.qsize()):
            name = self.queue.get()
            print(f'{name} в очереди')
            self.queue.put(name)

    def discuss_guests(self):
        t = threading.enumerate()
        while threading.active_count() > 1 or not self.queue.empty():
            for j in t[1::]:
                for i in t[1::]:
                    if not i.is_alive():
                        for table in self.tables:
                            if table.guest == i.name:
                                print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                                table.guest = None
                                print(f'Стол номер {table.number} свободен')
                                if not self.queue.empty():
                                    name = self.queue.get()
                                    table.guest = name
                                    Guest(name=name).start()
                                    print(f'{name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                                else:
                                    table.guest = None
                                break
                t = threading.enumerate()
                j.join()
        print(f'\033[35m\nВсе гости ушли можно отдыхать!!!')


tables = [Table(number) for number in range(1, 6)]
guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Victoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()