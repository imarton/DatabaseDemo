import sqlite3
from sqlite3 import Error

def create_connection(filename):
    connection = None
    try:
        connection = sqlite3.connect(filename)
        # print(f"Connection to '{filename}' SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def isUserExists(username:str)->bool:
    '''A függvény igazat ad vissza, ha a paraméterben megadott felhasználónév már létezik'''

    #kapcsolódás az adatbázishoz
    conn = create_connection("mydatabase.db")


    sql = f"SELECT * FROM users t WHERE t.name = '{username}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    conn.close()

    if len(row) == 0 :
        return False
    else:
        return True


def addUser(name, pwd)->str:
    conn = create_connection("mydatabase.db")
    sql = f"INSERT INTO users (name, age) VALUES('{name}', 22)"
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        msg = "Regisztráció sikeres!"
    except Error as e:
        msg = "Jaj valami hiba történt: " + str(e)

    conn.close()
    return msg



if __name__ == "__main__":
    print("Ha új vagy kérlek regisztrálj")

    name = input("Add meg a felhasználó nevet:")
    pwd = input("Add meg a jelszavad:")

    user_exists = isUserExists(name)

    if user_exists :
        print(f"A(z) '{name}' felhasználónév már foglalt")
    else:
        msg = addUser(name, pwd)
        print(msg)

    # conn = create_connection("mydatabase.db")
    #
    # cursor = conn.cursor()
    #
    # # Tábla létrehozása
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS users (
    #         id INTEGER PRIMARY KEY,
    #         name TEXT,
    #         age INTEGER
    #     )
    # ''')
    #
    # # Adatok beszúrása
    # # cursor.execute("INSERT INTO users (name, age) VALUES ('John Doe', 30)")
    # # conn.commit()
    #
    # # Adatok lekérdezése
    # cursor.execute("SELECT * FROM users")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    #
    # conn.close()