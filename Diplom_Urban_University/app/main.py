from methods import *
from data import data_start
from resultat import plot_statistic
from database import initiate_db

"""Главный модуль программы. Запуск Shift+F10"""

''' Активируем базу данных статистики data/data.db'''

initiate_db()

'''Готовим наборы данных для построения Графиков'''

(lstX, lstX1, lstX2, lstX4, lstX5, lstY, lstY1, lstY2,
 lstY3, lstY4, lstY5, lstZ, lstZ5, data, data0, data1, data2,
 data3, data4, data5, data6, dataX, dataY) = data_start()

'''Вызов функций Matplotlib для создания графиков
 Первая функция без графика для загрузки библиотеки в память'''

plot_0(0, 0, title='Загрузка Matplotlib')
plot_1(lstX, lstY, title='Разброс Matplotlib')
plot_2(lstX, lstY, title='График Matplotlib')
plot_3(lstX, lstY1, title='Гистограмма Matplotlib')
plot_4(data, title='Ящики Matplotlib')
plot_5(lstX1, title='Круговая диаграмма Matplotlib')
plot_6(lstX2, lstY2, title='График функции Matplotlib')
plot_7(lstX2, lstY2, lstY3, title='График двух функций Matplotlib')
plot_8(lstX4, lstY4, title='Двумерная гистограмма Matplotlib')
plot_9(lstX, lstY, lstZ, title='Разброс 3D Matplotlib')
plot_10(lstX5, lstY5, lstZ5, title='Каркасная поверхность Matplotlib')
plot_11(lstX5, lstY5, lstZ5, title='Просто красота от Matplotlib')


'''Вызов функций Seaborn для создания графиков
Первая функция без графика для загрузки библиотеки в память'''

sea_plot_0(data0, title='Загрузка Seaborn')
sea_plot_1(data1, title='Разброс Seaborn')
sea_plot_2(data1, title='График Seaborn')
sea_plot_3(data1, title='Гистограмма Seaborn')
sea_plot_4(dataX, dataY, title='Ящики Seaborn')
sea_plot_5(data2, title='Круговая диаграмма Seaborn')
sea_plot_6(data3, title='График функции Seaborn')
sea_plot_7(data3, data4, title='График двух функций Seaborn')
sea_plot_8(data5, title='Двумерная гистограмма Seaborn')
sea_plot_9(lstX, lstY, lstZ, title='Разброс 3D Seaborn')
sea_plot_10(lstX5, lstY5, lstZ5, title='Каркасная поверхность Seaborn')
sea_plot_11(lstX5, lstY5, lstZ5, title='Просто красота от Seaborn')


'''Вызов функций Plotly для создания графиков
Первая функция без графика для загрузки библиотеки в память'''

plot_plot_0(data0, title='Загрузка Plotly')
plot_plot_1(data1, title='Разброс Plotly')
plot_plot_2(data1, title='График Plotly')
plot_plot_3(lstX, title='Гистограмма Plotly')
plot_plot_4(dataX, dataY, title='Ящики Plotly')
plot_plot_5(data2, title='Круговая диаграмма Plotly')
plot_plot_6(data3, title='График функции Plotly')
plot_plot_7(data3, data4, title='График двух функций Plotly')
plot_plot_8(data5, title='Двумерная гистограмма Plotly')
plot_plot_9(data6, title='Разброс 3D Plotly')
plot_plot_10(lstX5, lstY5, lstZ5, title='Каркасная поверхность Plotly')
plot_plot_11(lstX5, lstY5, lstZ5, title='Просто красота от Plotly')


'''Извлекаем собраную статистику и строим график'''

plot_statistic()

'''Выводим в консоль финальную надпись'''

print(f'\nРабота программы сравнения Matplotlib, Seaborn, Plotly завершина!!!')