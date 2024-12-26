import seaborn as sns
import matplotlib.pyplot as plt
from app.decorators import statik_sb

'''В этом модуле собраны функции для построения графиков при помощи библиотеки Seaborn, все функции принимают данные
расчитанные в модуле data.py, полученные из модуля main.py и выводят на экран построенне графики. Все фнкции обернуты 
декоратором для сбора статистичиских данных потерь памяти и времени при работе функций.

:param *args, title: Получаемые данные
:return: График полученных данных'''


def sea_plot_0(*args, title):
    @statik_sb
    def sea_pl(data, title1):
        sns.scatterplot(data=data, x='X', y='Y')
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_1(*args, title):
    @statik_sb
    def sea_pl(data, title1):
        sns.scatterplot(data=data, x='X', y='Y')
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_2(*args, title):
    @statik_sb
    def sea_pl(data, title1):
        sns.lineplot(data=data, x='X', y='Y')
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_3(*args, title):
    @statik_sb
    def sea_pl(data, title1):
        sns.barplot(data=data, x='X', y='Y')
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_4(*args, title):
    @statik_sb
    def sea_pl(dataX, dataY, title1):
        sns.boxplot(data=dataX, y='X')
        sns.boxplot(data=dataY, y='Y')
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_5(*args, title):
    @statik_sb
    def plot(x1, title1):
        plt.figure(figsize=(5, 5))
        plt.pie(x1, radius=1, center=(4, 4))
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def sea_plot_6(*args, title):
    @statik_sb
    def sea_pl(data, title1):
        sns.lineplot(data=data, x='X', y='Y')
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_7(*args, title):
    @statik_sb
    def sea_pl(data1, data2, title1):
        sns.lineplot(data=data1, x='X', y='Y')
        sns.lineplot(data=data2, x='X', y='Y')
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_8(*args, title):
    @statik_sb
    def sea_pl(data, title1):
        sns.histplot(data=data, x='X', y='Y')
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_9(*args, title):
    @statik_sb
    def sea_pl(x1, y1, z1, title1):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(x1, y1, z1)
        plt.title(f'{title1}')
    sea_pl(*args, title=title)
    plt.show()


def sea_plot_10(*args, title):
    @statik_sb
    def plot(x1, y1, z1, title1):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot_wireframe(x1, y1, z1)
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()


def sea_plot_11(*args, title):
    @statik_sb
    def plot(x1, y1, z1, title1):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x1, y1, z1, cmap='winter')
        plt.title(f'{title1}')
    plot(*args, title=title)
    plt.show()