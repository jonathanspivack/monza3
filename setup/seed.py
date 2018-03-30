import sqlite3


def register(username,password):
    print('in here')
    connection = sqlite3.connect('master.db',check_same_thread=False)
    cursor = connection.cursor()
    query = "INSERT INTO users(username,password) VALUES(?,?)"
    cursor.execute(query,(username,password))
    connection.commit()
    connection.close()




register("mellon@gmail.com","123")
