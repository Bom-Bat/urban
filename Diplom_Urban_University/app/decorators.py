from database import create_data
from memory_profiler import memory_usage
from timeit import default_timer

'''
В этом модуле содержится функция декоратор для сбора статистики затраченных памяти и времени на отрисовку
'''


def statik_sb(func):
    """
    Функция декоратор
    :param: func: Получает функцию
    """
    def static(*args, title):
        """
        Функция сбора данных о работе фнкций отображающих графики и передающих их в базу данных. Запускает функцию
         графика, собирает данные, запускает функцию create_data для занесения их базу данных
        :param args: Получаемые данные
        :param title: Получаемые данные
        :return:
        """
        title = title
        memory_1 = memory_usage()
        start_time = default_timer()
        func(*args, title)
        finish_time = default_timer()
        memory_2 = memory_usage()
        memory = memory_2[0] - memory_1[0]
        time = finish_time - start_time
        create_data(title, memory, time)
    return static