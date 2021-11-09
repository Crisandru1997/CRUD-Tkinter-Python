import sqlite3
from sqlite3 import Error

def conexion():
    conn = ""
    try:
        conn = sqlite3.connect("PersonasBD")
        cursor = conn.cursor()
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        return conn
