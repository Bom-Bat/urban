from threading import Thread, Lock
from time import sleep
from random import randint


class Bank(Thread):
    def __init__(self):
        self.balance = int(500)
        self.lock = Lock()
        super().__init__()

    def deposit(self):
        for i in range(100):
            if 500 <= self.balance and self.lock == self.lock.locked():
                self.lock.release()
            pop = randint(50, 500)
            self.balance = self.balance + pop
            print(f'Пополнение: {pop}. Баланс: {self.balance}')
            sleep(0.001)
            if i == 99 and self.lock == self.lock.locked():
                self.lock.release()
        return self

    def take(self):
        for i in range(100):
            snt = randint(50, 500)
            print(f'Запрос на снятие {snt}')
            if snt <= self.balance:
                self.balance = self.balance - snt
                print(f'Снятие: {snt}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                sleep(0.01)
                if i < 99:
                    self.lock.release()
        return self


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')