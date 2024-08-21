class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.point = 0
        if self.step == 0:
            raise StepValueError(print('Шаг не может быть равен 0'))
        if self.start > self.stop and self.step > 0:
            self.step = -self.step

    def __iter__(self):
        self.point = self.start - self.step
        if (self.start - self.stop) % self.step:
            if self.start < self.stop:
                self.stop = self.start + ((self.stop - self.start) // self.step) * self.step
            else:
                self.stop = self.start - ((self.start - self.stop) // self.step) * self.step - self.step
        return self

    def __next__(self):
        if self.point != self.stop:
            self.point += self.step
            return self.point
        else:
            raise StopIteration


try:
    iter1 = Iterator(100, 200, 0)

    for i in iter1:
        print(i, end=' ')

except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()