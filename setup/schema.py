import sqlite3

connection = sqlite3.connect('master.db',check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(
                username text,
                password text
                );"""
        )



connection.commit()
cursor.close()
connection.close()
