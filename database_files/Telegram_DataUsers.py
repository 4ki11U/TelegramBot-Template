import sqlite3

connect_to_db = sqlite3.connect(r'my_tested_database.db')


def create_table_telegram_data():
    """Проверяем, есть ли таблица telegram_data. Если отсутствуем - создаём"""
    try:
        with connect_to_db:
            cursor_obj = connect_to_db.cursor()
            cursor_obj.execute(
                """CREATE TABLE IF NOT EXISTS telegram_data (id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INT NOT NULL,
                telegram_name TEXT,
                telegram_username TEXT, 
                telegram_surname TEXT,
                connected_date TEXT)""")
            connect_to_db.commit()
    except sqlite3.Error as e:
        print("Error SQLite3 : ", e)


def select_from_db(telegram_id):
    """Делаем SELECT с таблицы telegram_data в поисках наличия пользователя в  нашей БД"""
    try:
        with connect_to_db:
            cursor_obj = connect_to_db.cursor()
            result = cursor_obj.execute("""SELECT * FROM telegram_data WHERE telegram_id = '{}' """.format(telegram_id))
            return result.fetchone()
    except sqlite3.Error as e:
        print("Error SQLite3 : ", e)


def insert_into_db(telegram_id, telegram_name, telegram_username, telegram_surname, datetime):
    """Делаем INSERT в Таблицу Telegram Users внося данные об пользователе"""
    try:
        with connect_to_db:
            cursor_obj = connect_to_db.cursor()
            cursor_obj.execute(
                """INSERT INTO telegram_data (telegram_id,
                telegram_name,
                telegram_username,
                telegram_surname,
                connected_date) VALUES (?,?,?,?,?)""",
                (telegram_id, telegram_name, telegram_username, telegram_surname, datetime,))
            connect_to_db.commit()
    except sqlite3.Error as e:
        print("Error SQLite3 : ", e)
