import sqlite3
from sqlite3 import Error

conn = ""
try:
    conn = sqlite3.connect("PersonasBD")
    print(sqlite3.version)
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()
