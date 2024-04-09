import sqlite3

con = sqlite3.connect("firstDB.db")
cursor = con.cursor()

def createTable():
        # Создание таблицы
        # Создание таблицы "people"
        cursor.execute('''CREATE TABLE IF NOT EXISTS people (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            age INTEGER,
                            salary INTEGER
                        )''')
        con.commit()
        # добавляем строку в таблицу people
        data = [("Ладюша", 18, 400), ("Дилярушка", 17, 500), ("Лейладжон", 14, 500), ("Аделинаджон", 16, 1000),
                ("Элинушка", 19, 500), ("Анюша", 15, 1000), ("Эльзахон", 17, 2000), ("Амалишка", 18, 1700),
                ("Сонюша", 16, 2540), ("Каринушка", 16, 1890), ("Луизахон", 18, 2570), ("Настюша (Шеф)", 14, 1698),
                ("Иделиябону", 19, 2578)]
        cursor.executemany("INSERT INTO people (name, age, salary) VALUES (?, ?, ?)", data)
        # выполняем транзакцию
        con.commit()


