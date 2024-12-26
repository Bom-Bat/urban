import matplotlib.pyplot as plt
from app.decorators import statik_sb

'''В этом модуле собраны функции для построения графиков при помощи библиотеки Matplotlib, все функции принимают данные
расчитанные в модуле data.py, полученные из модуля main.py и выводят на экран построенне графики. Все фнкции обернуты 
декоратором для сбора статистичиских данных потерь памяти и времени при работе функций.

:param: *args, title: Получаемые данные
:return: График полученных данных'''


def plot_0(*args, title):
    @statik_sb
    def plot(x1, y1, title1):
        plt.figure(figsize=(5, 5))
        plt.scatter(x1, y1)
        plt.title(f'{title1}')
        plt.xlabel('X')
        plt.ylabel('Y')
    plot(*args, title=title)
    plt.show()


def plot_1(*args, title):
    @statik_sb
    def plot(x1, y1, title1):
        plt.figure(figsize=(5, 5))
        plt.scatter(x1, y1)
        plt.title(f'{title1}')
        plt.xlabel('X')
        plt.ylabel('Y')
    plot(*args, title=title)
    plt.show()


def plot_2(*args, title):
    @statik_sb
    def plot(x1, y1, title1):
        plt.figure(figsize=(5, 5))
        plt.plot(x1, y1)
        plt.title(f'{title1}')
        plt.xlabel('X')
        plt.ylabel('Y')
    plot(*args, title=title)
    plt.show()


def plot_3(*args, title):
    @statik_sb
    def plot(x1, y1, title1):
        plt.figure(figsize=(5, 5))
        plt.bar(x1, y1)
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def plot_4(*args, title):
    @statik_sb
    def plot(x1, title1):
        plt.figure(figsize=(5, 5))
        plt.boxplot(x1)
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def plot_5(*args, title):
    @statik_sb
    def plot(x1, title1):
        plt.figure(figsize=(5, 5))
        plt.pie(x1,  radius=1, center=(4, 4))
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def plot_6(*args, title):
    @statik_sb
    def plot(x1, y1,  title1):
        plt.figure(figsize=(10, 5))
        plt.plot(x1, y1)
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def plot_7(*args, title):
    @statik_sb
    def plot(x1, y1, y2,  title1):
        plt.figure(figsize=(10, 5))
        plt.plot(x1, y1)
        plt.plot(x1, y2)
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def plot_8(*args, title):
    @statik_sb
    def plot(x1, y1,  title1):
        plt.figure(figsize=(10, 5))
        plt.hexbin(x1, y1, gridsize=80)
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def plot_9(*args, title):
    @statik_sb
    def plot(x1, y1, z1, title1):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(x1, y1, z1)
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def plot_10(*args, title):
    @statik_sb
    def plot(x1, y1, z1, title1):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot_wireframe(x1, y1, z1)
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def plot_11(*args, title):
    @statik_sb
    def plot(x1, y1, z1, title1):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x1, y1, z1, cmap='winter')
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()