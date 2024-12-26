import sqlite3
'''
Этот модуль содержит функции для работы с базой данных
Подключаем базу данных  data/data.db
'''
connection = sqlite3.connect("data/data.db")
cursor = connection.cursor()


def initiate_db():
    """
    Функция initiate_db() проверяет етьли таблица Result_Test в базе данных, если нет таблицы создает её с полями id,
    name_test, memory, time и очищаем её если там есть данные.

    :param: Данные не получает
    :return: Ни чего не возвращает
    """
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Result_Test(
    id INTEGER PRIMARY KEY,
    name_test TEXT NOT NULL,
    memory FLOAT NOT NULL,
    time FLOAT NOT NULL
    )
    ''')

    cursor.execute('DELETE FROM Result_Test')
    connection.commit()


def create_data(name_test, memory, time):
    """
    Данная функция добавляет данные в таблицу Result_Test
    :param name_test:
    :param memory:
    :param time:
    :return:
    """

    cursor.execute("INSERT INTO Result_Test (name_test, memory, time) VALUES (?, ?, ?)",
                   (name_test, memory, time))
    connection.commit()


def get_all_data():
    """
    Данная функция извлекает данные из таблицы Result_Test и возвращает их для дальнейшей обработки в модуле resultat.py
    :return: all_data
    """
    all_data = cursor.execute(f"SELECT * FROM Result_Test").fetchall()
    connection.commit()
    connection.close()
    return all_data
