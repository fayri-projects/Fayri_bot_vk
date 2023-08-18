import sqlite3
from vkbottle.bot import Message
#============================================================

class BotDB:
     
    def __init__(self, db_file: str):
        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()

    def start_db(self) -> None:
        """Создание системных бд"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS examples (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL UNIQUE,
                buttons INTEGER NOT NULL,
                names TEXT
            )
        ''')
         


    def safe_example(self, mes:Message, buttons:int, names:str):

        self.cursor.execute(
            f"INSERT INTO 'examples' ('user_id', 'buttons', 'names') VALUES (?, ?, ?)", (mes.from_id, buttons, names))
        return self.con.commit()

    def get_example(self, mes:Message):

        """Получение данных из бд"""
        result = self.cursor.execute(
            f"SELECT * FROM examples WHERE user_id = ?", (mes.from_id,))
        return result.fetchone()

    def del_example(self, mes:Message):

        """Удаление записи"""
        if self.get_example(mes):
            self.cursor.execute(f"DELETE from examples where user_id = {mes.from_id}")
            self.con.commit()
            return True
        else:
            return False
