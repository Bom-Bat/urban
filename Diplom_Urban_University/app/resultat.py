import plotly.graph_objects as go
from plotly.subplots import make_subplots
from database import get_all_data

'''
В данном модуле содержатся функция для обработки данных полученых из базы данных data/data.db и построения графика 
сравнения занимаемой памяти и времени работы функций отбражения графиков тестируемыми библиотеками Matplotlib, Seaborn, 
Plotly  
'''


def plot_statistic():
    """
    Данная фнкция извлекает данные из базы данных и строит финальный график при помощи библиотеки Seaborn
    """
    '''Выборка данных для построения итогового графика'''

    x = ['Разброс', 'График', 'Гистограмма', 'Ящики', 'Круговая диограмма', 'График функци', 'График двух функций',
         'Двумерная гистограмма', 'Разброс 3D', 'Каркасная поверхность', 'Просто красота']
    data_all = list(get_all_data())
    zag_mat_m = data_all[0][2]
    zag_mat_t = data_all[0][3]
    mat = data_all[1:12]
    mat_m = [m[2] for m in mat]
    mat_t = [t[3] for t in mat]
    zag_sea_m = data_all[12][2]
    zag_sea_t = data_all[12][3]
    sea = data_all[13:24]
    sea_m = [m[2] for m in sea]
    sea_t = [t[3] for t in sea]
    zag_plot_m = data_all[24][2]
    zag_plot_t = data_all[24][3]
    plot = data_all[25::]
    plot_m = [m[2] for m in plot]
    plot_t = [t[3] for t in plot]

    '''Построение итогового графика'''

    fig = make_subplots(rows=2, cols=1, shared_xaxes=False,
                        vertical_spacing=0.03,
                        specs=[[{"type": "scatter"}], [{"type": "scatter"}]])
    fig.add_trace(go.Scatter(x=x, y=mat_m, name='Расход памяти Matplotlib'), 1, 1)
    fig.add_trace(go.Scatter(x=x, y=sea_m, name='Расход памяти Seaborn'), 1, 1)
    fig.add_trace(go.Scatter(x=x, y=plot_m, name='Расход памяти Plotly'), 1, 1)
    fig.add_trace(go.Scatter(x=x, y=mat_t, name='Расход времени Matplotlib'), 2, 1)
    fig.add_trace(go.Scatter(x=x, y=sea_t, name='Расход времени Seaborn'), 2, 1)
    fig.add_trace(go.Scatter(x=x, y=plot_t, name='Расход времени Plotly'), 2, 1)
    fig.update_layout(legend_orientation="h",
                      legend=dict(x=.5, xanchor="center"),
                      hovermode="x",
                      margin=dict(l=0, r=0, t=25, b=0))
    fig.update_layout(title=f'Итоговый график расхода памяти и времени на построение графиков. '
                            f'Загрузка: Matplotlib - память {zag_mat_m:.2f}, время {zag_mat_t:.4f}/ Seaborn - память '
                            f'{zag_sea_m:.2f}, время {zag_sea_t:.4f}/ Plotly - память {zag_plot_m:.2f}, время '
                            f'{zag_plot_t:.4f}')
    fig.update_yaxes(title='Изменение памяти', col=1, row=1)
    fig.update_yaxes(title='Изменение времени', col=1, row=2)
    fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
    fig.show()
