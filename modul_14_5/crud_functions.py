import sqlite3


def initiate_db():
    connection = sqlite3.connect("yes_telegram.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')
    connection.commit()
    connection.close()


# baza = initiate_db()
# connection = sqlite3.connect("yes_telegram.db")
# cursor = connection.cursor()
# for i in range(1, 5, 1):
#     cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
#                    (f"Product{i}", f"описание{i}", str(i*100)))
# connection.commit()
# connection.close()


def get_all_products():
    connection = sqlite3.connect("yes_telegram.db")
    cursor = connection.cursor()
    result = cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    connection.close()
    return result


def add_user(username, email, age):
    connection = sqlite3.connect("yes_telegram.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f"{username}", f"{email}", f"{age}", str(1000)))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect("yes_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM Users")
    chek_user = [row[0] for row in cursor]
    chek = username in chek_user
    connection.commit()
    connection.close()
    return chek
