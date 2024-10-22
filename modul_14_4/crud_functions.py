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


