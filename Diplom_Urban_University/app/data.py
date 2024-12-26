import numpy as np
import pandas as pd

'''
В этом модуле содержится функция для расчетов данных при помощи библиотек Numpy и Pandas, данные передаются набором  
в модуль main.py для дальнейшей передачи в тестовые модули

:param: Данные функция не получает
:return: Набор списков данных для построения графиков
'''


def data_start():

    """
    Готовим наборы данных для построения Графиков
    Первый набор данных - для показательной реализации библиотек.
    """

    lstX = np.random.randint(-100, 100, 20)
    lstY = np.random.randint(-100, 100, 20)

    '''
    Набор данных для - Гистограмма
    '''
    lstY1 = np.random.randint(0, 20, 20)

    '''
    Набор данных для Диограмма Ящики
    '''

    data = [lstX, lstY]

    '''
    Набор данных для - Круговая Диограмма
    '''

    lstX1 = np.random.randint(0, 3, 10)

    '''
    Набор данных для - График Фукнции
    '''

    lstX2 = np.arange(0, 15, 0.05)
    lstY2 = np.sin(lstX2)

    '''
    Набор данных для - График Двух Фукнций
    '''

    lstY3 = np.cos(lstX2)

    '''
    Набор данных для - Двумерная Гистограмма
    '''

    lstX4 = np.random.randn(5000)
    lstY4 = 1.2 * lstX4 + np.random.randn(5000) / 3

    '''
    Дополнительный набор данных для - Разброс 3D
    '''

    lstZ = np.random.randint(-100, 100, 20)

    '''
    Набор данных для - Каркасная поверхность
    '''

    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:30j]
    lstX5 = np.cos(u) * np.sin(v)
    lstY5 = np.sin(u) * np.sin(v)
    lstZ5 = np.cos(v)

    '''
    Преобразуем данные для работы Seaborn из списков в DataFrame
    Данные для загрузки Seaborn
    '''

    dataF0 = [[0, 0], [0, 0]]
    data0 = pd.DataFrame(dataF0, columns=['X', 'Y'])

    '''
    Данные для - Разброс Seaborn
    '''

    dataF1 = [list(x) for x in zip(lstX, lstY)]
    data1 = pd.DataFrame(dataF1, columns=['X', 'Y'])

    '''
    Данные для - Ящики Seaborn
    '''

    dataX = pd.DataFrame(lstX, columns=['X'])
    dataY = pd.DataFrame(lstY, columns=['Y'])

    '''
    Набор данных для - Круговая Диограмма
    '''

    data2 = lstX1

    '''
    Набор данных для - График Фукнции
    '''

    dataF3 = [list(x) for x in zip(lstX2, lstY2)]
    data3 = pd.DataFrame(dataF3, columns=['X', 'Y'])

    '''
    Набор данных для - График Двух Фукнций
    '''

    dataF4 = [list(x) for x in zip(lstX2, lstY3)]
    data4 = pd.DataFrame(dataF4, columns=['X', 'Y'])

    '''
    Набор данных для - Двумерная гистограмма
    '''

    dataF5 = [list(x) for x in zip(lstX4, lstY4)]
    data5 = pd.DataFrame(dataF5, columns=['X', 'Y'])

    '''
    Набор данных для - Разброс 3D
    '''

    dataF6 = [list(x) for x in zip(lstX, lstY, lstZ)]
    data6 = pd.DataFrame(dataF6, columns=['X', 'Y', 'Z'])

    '''
    Возвращаем расчитанные данные для дальнейшей передачи в тестовые модули
    '''

    return [lstX, lstX1, lstX2, lstX4, lstX5, lstY, lstY1, lstY2, lstY3, lstY4, lstY5, lstZ, lstZ5, data, data0, data1,
            data2, data3, data4, data5, data6, dataX, dataY]