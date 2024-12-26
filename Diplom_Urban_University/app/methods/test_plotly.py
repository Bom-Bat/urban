import plotly.express as px
import plotly.graph_objects as go
from app.decorators import statik_sb
import pandas as pd

'''В этом модуле собраны функции для построения графиков при помощи библиотеки Plotly, все функции принимают данные
расчитанные в модуле data.py, полученные из модуля main.py и выводят на экран построенне графики. Все фнкции обернуты 
декоратором для сбора статистичиских данных потерь памяти и времени при работе функций.

:param *args, title: Получаемые данные
:return: График полученных данных'''


def plot_plot_0(*args, title):
    @statik_sb
    def plot(data, title1):
        fig = px.scatter(data, x='X', y='Y', title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_1(*args, title):
    @statik_sb
    def plot(data, title1):
        fig = px.scatter(data, x='X', y='Y', title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_2(*args, title):
    @statik_sb
    def plot(data, title1):
        fig = px.line(data, x='X', y='Y', title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_3(*args, title):
    @statik_sb
    def plot(data, title1):
        fig = go.Figure(data=[go.Bar(y=data)], layout_title_text=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_4(*args, title):
    @statik_sb
    def plot(dataX, dataY, title1):
        fig = go.Figure()
        fig.add_trace(go.Box(y=dataX['X']))
        fig.add_trace(go.Box(y=dataY['Y']))
        fig.update_layout(title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_5(*args, title):
    @statik_sb
    def plot(data2, title1):
        df = pd.DataFrame(data2, columns=['X'])
        fig = px.pie(df, values='X', title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_6(*args, title):
    @statik_sb
    def plot(data, title1):
        fig = px.line(data, x='X', y='Y', title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_7(*args, title):
    @statik_sb
    def plot(data3, data4, title1):
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=data3['Y']))
        fig.add_trace(go.Scatter(y=data4['Y']))
        fig.update_layout(title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_8(*args, title):
    @statik_sb
    def plot(data, title1):
        fig = px.density_heatmap(data, x='X', y='Y', nbinsx=150, nbinsy=150, title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_9(*args, title):
    @statik_sb
    def plot(data, title1):
        fig = px.scatter_3d(data, x='X', y='Y', z='Z', title=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_10(*args, title):
    @statik_sb
    def plot(lstX5, lstY5, lstZ5, title1):
        lines = []
        line_marker = dict(color='#0066FF', width=2)
        for i, j, k in zip(lstX5, lstY5, lstZ5):
            lines.append(go.Scatter3d(x=i, y=j, z=k, mode='lines', line=line_marker))
        fig = go.Figure(data=lines, layout_title_text=title1)
        fig.show()
    plot(*args, title=title)


def plot_plot_11(*args, title):
    @statik_sb
    def plot(lstX5, lstY5, lstZ5, title1):
        fig = go.Figure(go.Surface(x=lstX5, y=lstY5, z=lstZ5, colorscale='BuGn'))
        fig.update_layout(title_text=title1)
        fig.show()
    plot(*args, title=title)