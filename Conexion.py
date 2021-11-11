import sqlite3
from sqlite3 import Error
from tkinter import messagebox

def conexion():
    conn = ""
    try:
        conn = sqlite3.connect("PersonasBD")
        cursor = conn.cursor()
        messagebox.showinfo(title="Conexion exitosa", message="Se ha conectado exitosamente a la base de datos", icon="info")
    except Error as e:
        print(e)
    finally:
        return conn
