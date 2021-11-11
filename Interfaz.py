from tkinter import *
import tkinter.scrolledtext as scrolledtext # Scroll para area de Comentario.
from tkinter import messagebox # Mensajes en ventana al presionar un boton.
import Conexion

raiz = Tk()
raiz.title("CRUD")
miFrame = Frame(raiz, width=800, height=800)
miFrame.pack()

# TODO: Funciones utilizadas

idCrud = BooleanVar()
nombreCrud = StringVar()
apellidoCrud = StringVar()
passwordCrud = StringVar()
comentarioCrud = StringVar()

bandera = BooleanVar()
bandera = False
conn = StringVar()

def estado():
    global bandera, conn
    if bandera:
        conn = Conexion.conexion()
        messagebox.showinfo(title="Se encuentra conectado", message="Ya se ha conectado a la BD", icon="info")
        return conn
    bandera = True

def conectar():
    if bandera:
        conn = estado()
        print("CONECTADOOOOOO")
        return conn

def insertarDatos():
    conn = conectar()
    try:
        miCursor = conn.cursor()
    except AttributeError:
        print("No se ha conectado a la BD")
    
    idCrud = idCaja.get()
    if idCrud == "":
        
        nombreCrud = nombreCaja.get()
        apellidoCrud = apellidoCaja.get()
        passwordCrud = passwordCaja.get()
        comentarioCrud = comentarioCaja.get("1.0", 'end') # Debemos agregar esos datos para obtener la info de esta caja.
        # Para verificar que el comentario no se encuentre vacio, debemos utilizar esta opcion.
        if nombreCrud == "" or apellidoCrud == "" or passwordCrud == "" or not comentarioCrud:
            messagebox.showinfo(title="Campos vacios", message="Debes rellenar todos los campos, con excepcion de la ID", icon="warning")
        else:
            miCursor.execute("INSERT INTO PERSONA VALUES(NULL, ?, ?, ?, ?)", (nombreCrud, apellidoCrud, passwordCrud, comentarioCrud))
            conn.commit()
            messagebox.showinfo(title='Insercion correcta', message='Los datos han sido insertados correctamente', icon='info')
            limpiarPantalla()
            conn.close()
    else:
        print("no podemos insertar :c")

def mostrarDatos():
    conn = conectar()
    try:
        miCursor = conn.cursor()
    except AttributeError:
        messagebox.showinfo(title="No se encuentra conectado", message="No esta conectado a la BD, favor de conectarse", icon="warning")
    idCrud = idCaja.get()
    limpiarPantalla()
    try:
        miCursor.execute("SELECT * FROM PERSONA WHERE per_id = {}".format(idCrud))
        datos = miCursor.fetchall()
        if datos[0][0] != "":
            for _ , nombre, apellido, password, comentario  in datos:
                nombreCaja.insert(0, nombre)
                apellidoCaja.insert(0, apellido)
                passwordCaja.insert(0, password)
                comentarioCaja.insert("1.0",comentario)
    except:
        messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")
        limpiarPantalla()
    # finally:
        # conn.close()

def actualizarDatos():
    conn = conectar()
    miCursor = conn.cursor()
    idCrud = idCaja.get()
    if idCrud != "":
        idCrud = idCaja.get()
        nombreCrud = nombreCaja.get()
        apellidoCrud = apellidoCaja.get()
        passwordCrud = passwordCaja.get()
        comentarioCrud = comentarioCaja.get("1.0", 'end')
        miCursor.execute("SELECT per_id FROM PERSONA WHERE per_id = {}".format(idCrud))
        datos = miCursor.fetchall()
        try:
            id = datos[0][0]
            miCursor.execute("UPDATE PERSONA SET per_nombre = ?, per_apellido = ?, per_password = ?, per_comentario = ? WHERE per_id = {}".format(id), (nombreCrud, apellidoCrud, passwordCrud, comentarioCrud))
            conn.commit()
            messagebox.showinfo(title="Usuario Modificado", message="Se han modificado correctamente los datos", icon="info")
        except IndexError:
            messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")
        finally:
            mostrarDatos()
            conn.close()
    else:
        messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")

def eliminarRegistro():
    conn = conectar()
    miCursor = conn.cursor()
    idCrud = idCaja.get()
    if idCrud != "":
        miCursor.execute("SELECT per_id FROM PERSONA WHERE per_id = {}".format(idCrud))
        datos = miCursor.fetchall()
        try:
            id = datos[0][0]
            miCursor.execute("DELETE FROM PERSONA WHERE per_id = {}".format(id))
            conn.commit()
            messagebox.showinfo(title="Usuario Eliminado", message="Se ha eliminado correctamente al usuario", icon="info")
        except IndexError:
            messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")
        finally:
            limpiarPantalla()
            conn.close()
    else:
        messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")
def limpiarPantalla():
    nombreCaja.delete(0, END)
    apellidoCaja.delete(0, END)
    passwordCaja.delete(0, END)
    comentarioCaja.delete("1.0", END)

# TODO: Barra del Menu
miMenu = Menu(raiz)
raiz.config(menu=miMenu)

# Primer Menu - BBDD
archivoBBDD = Menu(miMenu, tearoff=0)
archivoBBDD.add_command(label="Conexion", command=estado)
archivoBBDD.add_command(label="Salir")

# Segundo Menu - Borrar
archivoBorrar = Menu(miMenu, tearoff=0)
archivoBorrar.add_command(label="Borrar campos", command=limpiarPantalla)

# Tercer Menu - CRUD
archivoCRUD = Menu(miMenu, tearoff=0)
archivoCRUD.add_command(label="Crear", command=insertarDatos)
archivoCRUD.add_command(label="Leer", command=mostrarDatos)
archivoCRUD.add_command(label="Actualizar", command=actualizarDatos)
archivoCRUD.add_command(label="Borrar", command=eliminarRegistro)

# Cuarto Menu - Ayuda
archivoAyuda = Menu(miMenu, tearoff=0)
archivoAyuda.add_command(label="Creador")
archivoAyuda.add_command(label="Version")

miMenu.add_cascade(label="BBDD", menu=archivoBBDD)
miMenu.add_cascade(label="Borrar", menu=archivoBorrar)
miMenu.add_cascade(label="CRUD", menu=archivoCRUD)
miMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

# TODO: Campo de ID
idLabel = Label(miFrame, text="ID")
idLabel.grid(row=0, column=0, sticky="w", pady=10)
idCaja = Entry(miFrame)
idCaja.grid(row=0, column=1, pady=10, columnspan=4)

# TODO: Campo de NOMBRE
nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=1, column=0, sticky="w", pady=10)
nombreCaja = Entry(miFrame)
nombreCaja.grid(row=1, column=1, pady=10, columnspan=4)

# TODO: Campo de APELLIDO
apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="w", pady=10)
apellidoCaja = Entry(miFrame)
apellidoCaja.grid(row=2, column=1, pady=10, columnspan=4)

# TODO: Campo de CONTRASEÑA
passwordLabel = Label(miFrame, text="Contraseña")
passwordLabel.grid(row=3, column=0, sticky="w", pady=10)
passwordCaja = Entry(miFrame, show="*")
passwordCaja.grid(row=3, column=1, pady=10, columnspan=4)

# TODO: Campo de COMENTARIO
comentarioLabel = Label(miFrame, text="Comentario")
comentarioLabel.grid(row=4, column=0, sticky="w", pady=10)
comentarioCaja = scrolledtext.ScrolledText(miFrame)
comentarioCaja.config(width=23, height=5)
comentarioCaja.grid(row=4, column=1, pady=10, columnspan=4)

# TODO: BOTONES

botonCreate = Button(miFrame, text="CREAR", padx=10, pady=10, command=insertarDatos)
botonCreate.grid(row=5, column=0, padx=0)

botonRead = Button(miFrame, text="LEER", padx=10, pady=10, command=mostrarDatos)
botonRead.grid(row=5, column=1, padx=0)

botonUpdate = Button(miFrame, text="ACTUALIZAR", padx=10, pady=10, command=actualizarDatos)
botonUpdate.grid(row=5, column=3, padx=6)

botonDelete = Button(miFrame, text="BORRAR", padx=10, pady=10, command=eliminarRegistro)
botonDelete.grid(row=5, column=4)

raiz.mainloop()